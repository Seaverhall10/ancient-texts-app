/**
 * Ancient Texts Library — App Controller (IIFE)
 * Handles: library navigation, era navigation, chapter rendering, scroll-spy,
 *          search, bookmarks, cross-ref drawer, glossary overlay, hash routing,
 *          interlinear reading pane, multi-text support
 */
(function() {
    'use strict';

    // ── Data (injected at build time) ───────────────────────
    const MANIFEST = __MANIFEST_DATA__;
    const ERA_DATA = __ERA_DATA__;
    const GLOSSARY = __GLOSSARY_DATA__;
    const INTERLINEAR = __INTERLINEAR_DATA__;
    const INTERLINEAR_EXODUS = __INTERLINEAR_EXODUS_DATA__;
    const INTERLINEAR_LEVITICUS = __INTERLINEAR_LEVITICUS_DATA__;
    const INTERLINEAR_NUMBERS = __INTERLINEAR_NUMBERS_DATA__;
    const INTERLINEAR_DEUTERONOMY = __INTERLINEAR_DEUTERONOMY_DATA__;
    const INTERLINEAR_JOSHUA = __INTERLINEAR_JOSHUA_DATA__;
    const INTERLINEAR_JUDGES = __INTERLINEAR_JUDGES_DATA__;
    const INTERLINEAR_RUTH = __INTERLINEAR_RUTH_DATA__;
    const INTERLINEAR_1SAMUEL = __INTERLINEAR_1SAMUEL_DATA__;
    const INTERLINEAR_2SAMUEL = __INTERLINEAR_2SAMUEL_DATA__;
    const INTERLINEAR_1KINGS = __INTERLINEAR_1KINGS_DATA__;
    const INTERLINEAR_2KINGS = __INTERLINEAR_2KINGS_DATA__;
    const INTERLINEAR_PSALMS = __INTERLINEAR_PSALMS_DATA__;
    const INTERLINEAR_ISAIAH = __INTERLINEAR_ISAIAH_DATA__;
    const INTERLINEAR_DANIEL = __INTERLINEAR_DANIEL_DATA__;
    // NT Greek interlinear (27 books — MorphGNT + Strong's)
    const INTERLINEAR_NT_MATTHEW        = __INTERLINEAR_NT_MATTHEW_DATA__;
    const INTERLINEAR_NT_MARK           = __INTERLINEAR_NT_MARK_DATA__;
    const INTERLINEAR_NT_LUKE           = __INTERLINEAR_NT_LUKE_DATA__;
    const INTERLINEAR_NT_JOHN           = __INTERLINEAR_NT_JOHN_DATA__;
    const INTERLINEAR_NT_ACTS           = __INTERLINEAR_NT_ACTS_DATA__;
    const INTERLINEAR_NT_ROMANS         = __INTERLINEAR_NT_ROMANS_DATA__;
    const INTERLINEAR_NT_1CORINTHIANS   = __INTERLINEAR_NT_1CORINTHIANS_DATA__;
    const INTERLINEAR_NT_2CORINTHIANS   = __INTERLINEAR_NT_2CORINTHIANS_DATA__;
    const INTERLINEAR_NT_GALATIANS      = __INTERLINEAR_NT_GALATIANS_DATA__;
    const INTERLINEAR_NT_EPHESIANS      = __INTERLINEAR_NT_EPHESIANS_DATA__;
    const INTERLINEAR_NT_PHILIPPIANS    = __INTERLINEAR_NT_PHILIPPIANS_DATA__;
    const INTERLINEAR_NT_COLOSSIANS     = __INTERLINEAR_NT_COLOSSIANS_DATA__;
    const INTERLINEAR_NT_1THESSALONIANS = __INTERLINEAR_NT_1THESSALONIANS_DATA__;
    const INTERLINEAR_NT_2THESSALONIANS = __INTERLINEAR_NT_2THESSALONIANS_DATA__;
    const INTERLINEAR_NT_1TIMOTHY       = __INTERLINEAR_NT_1TIMOTHY_DATA__;
    const INTERLINEAR_NT_2TIMOTHY       = __INTERLINEAR_NT_2TIMOTHY_DATA__;
    const INTERLINEAR_NT_TITUS          = __INTERLINEAR_NT_TITUS_DATA__;
    const INTERLINEAR_NT_PHILEMON       = __INTERLINEAR_NT_PHILEMON_DATA__;
    const INTERLINEAR_NT_HEBREWS        = __INTERLINEAR_NT_HEBREWS_DATA__;
    const INTERLINEAR_NT_JAMES          = __INTERLINEAR_NT_JAMES_DATA__;
    const INTERLINEAR_NT_1PETER         = __INTERLINEAR_NT_1PETER_DATA__;
    const INTERLINEAR_NT_2PETER         = __INTERLINEAR_NT_2PETER_DATA__;
    const INTERLINEAR_NT_1JOHN          = __INTERLINEAR_NT_1JOHN_DATA__;
    const INTERLINEAR_NT_2JOHN          = __INTERLINEAR_NT_2JOHN_DATA__;
    const INTERLINEAR_NT_3JOHN          = __INTERLINEAR_NT_3JOHN_DATA__;
    const INTERLINEAR_NT_JUDE           = __INTERLINEAR_NT_JUDE_DATA__;
    const INTERLINEAR_NT_REVELATION     = __INTERLINEAR_NT_REVELATION_DATA__;
    // New OT Hebrew interlinear (24 books — OSHB + Strong's)
    const INTERLINEAR_JOB              = __INTERLINEAR_JOB_DATA__;
    const INTERLINEAR_PROVERBS         = __INTERLINEAR_PROVERBS_DATA__;
    const INTERLINEAR_ECCLESIASTES     = __INTERLINEAR_ECCLESIASTES_DATA__;
    const INTERLINEAR_SONGOFSOLOMON    = __INTERLINEAR_SONGOFSOLOMON_DATA__;
    const INTERLINEAR_JEREMIAH         = __INTERLINEAR_JEREMIAH_DATA__;
    const INTERLINEAR_EZEKIEL          = __INTERLINEAR_EZEKIEL_DATA__;
    const INTERLINEAR_LAMENTATIONS     = __INTERLINEAR_LAMENTATIONS_DATA__;
    const INTERLINEAR_1CHRONICLES      = __INTERLINEAR_1CHRONICLES_DATA__;
    const INTERLINEAR_2CHRONICLES      = __INTERLINEAR_2CHRONICLES_DATA__;
    const INTERLINEAR_EZRA             = __INTERLINEAR_EZRA_DATA__;
    const INTERLINEAR_NEHEMIAH         = __INTERLINEAR_NEHEMIAH_DATA__;
    const INTERLINEAR_ESTHER           = __INTERLINEAR_ESTHER_DATA__;
    const INTERLINEAR_HOSEA            = __INTERLINEAR_HOSEA_DATA__;
    const INTERLINEAR_JOEL             = __INTERLINEAR_JOEL_DATA__;
    const INTERLINEAR_AMOS             = __INTERLINEAR_AMOS_DATA__;
    const INTERLINEAR_OBADIAH          = __INTERLINEAR_OBADIAH_DATA__;
    const INTERLINEAR_JONAH            = __INTERLINEAR_JONAH_DATA__;
    const INTERLINEAR_MICAH            = __INTERLINEAR_MICAH_DATA__;
    const INTERLINEAR_NAHUM            = __INTERLINEAR_NAHUM_DATA__;
    const INTERLINEAR_HABAKKUK         = __INTERLINEAR_HABAKKUK_DATA__;
    const INTERLINEAR_ZEPHANIAH        = __INTERLINEAR_ZEPHANIAH_DATA__;
    const INTERLINEAR_HAGGAI           = __INTERLINEAR_HAGGAI_DATA__;
    const INTERLINEAR_ZECHARIAH        = __INTERLINEAR_ZECHARIAH_DATA__;
    const INTERLINEAR_MALACHI          = __INTERLINEAR_MALACHI_DATA__;
    const TEXT_INTROS = __TEXT_INTROS_DATA__;
    const PROPHECY_MATRIX = __PROPHECY_DATA__;
    const BOOK_PROPHECIES = __PROPHECY_TRACKER_DATA__;
    const CORE_BELIEFS = __CORE_BELIEFS_DATA__;
    const RESOURCES = __RESOURCES_DATA__;
    var SEARCH_QA = __SEARCH_QA_DATA__;
    var SEARCH_INDEX = __SEARCH_INDEX_DATA__;

    // ── State ───────────────────────────────────────────────
    let currentText = localStorage.getItem('atl-current-text') || null;
    let libraryMode = !currentText;
    let currentEra = null;
    let bookmarks = JSON.parse(localStorage.getItem('genesis-study-bookmarks') || '[]');
    let readChapters = JSON.parse(localStorage.getItem('atl-read-chapters') || '{}');
    let searchIndex = null;
    let readingPaneOpen = localStorage.getItem('genesis-reading-pane') !== 'false';
    let readingPaneMode = localStorage.getItem('genesis-reading-mode') || 'full';
    let currentILChapter = null;
    let currentILBook = 'genesis';
    let ilFontScale = parseFloat(localStorage.getItem('genesis-il-font-scale') || '1');
    let sourceReadingMode = false; // true when showing source passages instead of interlinear
    var singleChapterMode = false; // true on mobile — show one chapter at a time
    var currentChapterIndex = 0;   // index in flatChapters for single-chapter view
    var readingMode = localStorage.getItem('atl-reading-mode') || 'study'; // scripture | study | interlinear

    // ── User Mode & Row Visibility State ──────────────────
    var USER_MODES = {
        reader:  { translit: false, morph: false, strongs: false, gloss: false, flow: true, notes: false },
        student: { translit: true,  morph: false, strongs: false, gloss: true,  flow: true, notes: false },
        scholar: { translit: true,  morph: true,  strongs: true,  gloss: true,  flow: true, notes: false }
    };
    var userMode = localStorage.getItem('atl-user-mode') || 'scholar';
    var ilRows = JSON.parse(localStorage.getItem('atl-il-rows') || 'null') || USER_MODES[userMode];
    var highContrast = localStorage.getItem('atl-high-contrast') === 'true';

    // ── Study Notes (user pins/annotations per chapter) ──────
    var studyNotes = JSON.parse(localStorage.getItem('atl-study-notes') || '{}');

    // ── THC ↔ Library Cross-Reference Map ──────────────────
    var THC_XREFS = {
        // Library chapter ID → THC chapters that provide deep analysis
        fromLibrary: {
            'gen-1': [{id: 'hc-ch01', label: 'Ch 1: The Throne and the Court', note: 'Divine council in creation \u2014 "Let us make"'}],
            'gen-2': [{id: 'hc-ch01', label: 'Ch 1: The Throne and the Court', note: 'The heavenly court framework'}],
            'gen-3': [{id: 'hc-ch03', label: 'Ch 3: Rebellion in the Heavens', note: 'The nachash \u2014 shining divine rebel'}],
            'gen-4': [{id: 'hc-ch03', label: 'Ch 3: Rebellion in the Heavens', note: 'Post-Fall consequences'}],
            'gen-5': [{id: 'hc-ch02', label: 'Ch 2: The Sons of God', note: 'Antediluvian genealogy context'}],
            'gen-6-1-4': [
                {id: 'hc-ch02', label: 'Ch 2: The Sons of God', note: 'Full grammatical analysis of b\'nei ha\'elohim'},
                {id: 'hc-ch13', label: 'Ch 13: 1 Enoch \u2014 Book of Watchers', note: 'Second Temple expansion of Genesis 6'}
            ],
            'gen-6b': [{id: 'hc-ch02', label: 'Ch 2: The Sons of God', note: 'The Flood as divine judgment on the Watchers'}],
            'gen-7': [{id: 'hc-ch02', label: 'Ch 2: The Sons of God', note: 'Flood narrative \u2014 Watcher context'}],
            'gen-10': [{id: 'hc-ch04', label: 'Ch 4: The Deuteronomy 32 Worldview', note: 'Table of Nations \u2014 divine allotment of 70 nations'}],
            'gen-11a': [{id: 'hc-ch04', label: 'Ch 4: The Deuteronomy 32 Worldview', note: 'Babel \u2014 cosmic rebellion and divine response'}],
            '1en-1': [{id: 'hc-ch13', label: 'Ch 13: 1 Enoch \u2014 Book of Watchers', note: 'Overview and canonical relationship'}],
            '1en-6': [
                {id: 'hc-ch02', label: 'Ch 2: The Sons of God', note: 'Genesis parallel \u2014 Watchers = b\'nei ha\'elohim'},
                {id: 'hc-ch13', label: 'Ch 13: 1 Enoch \u2014 Book of Watchers', note: 'The Watchers\' descent and oath on Hermon'}
            ],
            '1en-7-8': [{id: 'hc-ch13', label: 'Ch 13: 1 Enoch \u2014 Book of Watchers', note: 'Forbidden knowledge and resulting violence'}],
            '1en-9-11': [{id: 'hc-ch13', label: 'Ch 13: 1 Enoch \u2014 Book of Watchers', note: 'The archangels\' intercession'}],
            '1en-12-16': [{id: 'hc-ch13', label: 'Ch 13: 1 Enoch \u2014 Book of Watchers', note: 'Enoch\'s mission to the imprisoned Watchers'}],
            '1en-17-19': [{id: 'hc-ch13', label: 'Ch 13: 1 Enoch \u2014 Book of Watchers', note: 'The prison of the Watchers \u2014 cosmic geography'}],
            '1en-20-25': [{id: 'hc-ch13', label: 'Ch 13: 1 Enoch \u2014 Book of Watchers', note: 'The fate of the Watchers and their offspring'}],
            '1en-26-36': [{id: 'hc-ch13', label: 'Ch 13: 1 Enoch \u2014 Book of Watchers', note: 'Enoch\'s cosmic journeys'}],
            'giants-1': [{id: 'hc-ch14', label: 'Ch 14: Book of Giants & Jubilees', note: 'Fragments expanding the Watcher tradition'}],
            'giants-2': [{id: 'hc-ch14', label: 'Ch 14: Book of Giants & Jubilees', note: 'Dreams and visions of the Nephilim'}],
            'giants-3': [{id: 'hc-ch14', label: 'Ch 14: Book of Giants & Jubilees', note: 'The Nephilim giants\' final fate'}],
            'jub-4': [{id: 'hc-ch14', label: 'Ch 14: Book of Giants & Jubilees', note: 'Jubilees\' Watchers narrative'}],
            'jub-5': [{id: 'hc-ch14', label: 'Ch 14: Book of Giants & Jubilees', note: 'Jubilees 5: judgment and imprisonment'}]
        },
        // THC chapter → library chapters for "Study in Library" links
        toLibrary: {
            'hc-ch01': [{id: 'gen-1', text: 'genesis', label: 'Genesis 1 \u2014 "Let us make"'}],
            'hc-ch02': [
                {id: 'gen-6-1-4', text: 'genesis', label: 'Genesis 6:1-4 \u2014 The Foundational Passage'},
                {id: '1en-6', text: '1enoch', label: '1 Enoch 6 \u2014 The Watchers\' Descent'}
            ],
            'hc-ch03': [{id: 'gen-3', text: 'genesis', label: 'Genesis 3 \u2014 The Fall & the Nachash'}],
            'hc-ch04': [
                {id: 'gen-10', text: 'genesis', label: 'Genesis 10 \u2014 Table of Nations'},
                {id: 'gen-11a', text: 'genesis', label: 'Genesis 11 \u2014 Tower of Babel'}
            ],
            'hc-ch13': [
                {id: '1en-1', text: '1enoch', label: '1 Enoch 1 \u2014 Introduction'},
                {id: '1en-6', text: '1enoch', label: '1 Enoch 6 \u2014 The Watchers\' Descent'},
                {id: '1en-7-8', text: '1enoch', label: '1 Enoch 7-8 \u2014 Forbidden Knowledge'},
                {id: '1en-12-16', text: '1enoch', label: '1 Enoch 12-16 \u2014 Enoch\'s Mission'}
            ],
            'hc-ch14': [
                {id: 'giants-1', text: 'giants', label: 'Book of Giants \u2014 Fragment 1'},
                {id: 'jub-5', text: 'jubilees', label: 'Jubilees 5 \u2014 Watchers & Judgment'}
            ]
        }
    };

    // ── Reverse Cross-Reference Index ──────────────────────
    // Maps chapter IDs to chapters that cite them (built at init)
    var reverseXrefIndex = {};

    function buildReverseXrefIndex() {
        MANIFEST.eras.forEach(function(era) {
            var chapters = ERA_DATA[era.id] || [];
            chapters.forEach(function(ch) {
                if (!ch.cross_refs) return;
                ch.cross_refs.forEach(function(raw) {
                    var xr = normXref(raw);
                    // Parse the xref's target book to find matching chapters
                    var parsed = parseScriptureRef(xr.ref);
                    if (!parsed) return;
                    var targetKey = parsed.textId + ':' + parsed.chapter;
                    if (!reverseXrefIndex[targetKey]) reverseXrefIndex[targetKey] = [];
                    reverseXrefIndex[targetKey].push({
                        fromChapterId: ch.id,
                        fromRef: ch.ref,
                        fromTitle: ch.title,
                        fromText: era.text,
                        note: xr.note,
                        type: xr.type
                    });
                });
            });
        });
    }

    function getReverseCitations(chapterId, textId) {
        // Find chapters that cite this chapter's scripture range
        var ch = getChapterById(chapterId);
        if (!ch || !ch.ref) return [];
        var parsed = parseScriptureRef(ch.ref);
        if (!parsed) return [];
        var key = parsed.textId + ':' + parsed.chapter;
        var refs = reverseXrefIndex[key] || [];
        // Dedupe by source chapter and exclude self
        var seen = {};
        return refs.filter(function(r) {
            if (r.fromChapterId === chapterId) return false;
            if (seen[r.fromChapterId]) return false;
            seen[r.fromChapterId] = true;
            return true;
        });
    }

    function getChapterById(chId) {
        var allEras = MANIFEST.eras;
        for (var i = 0; i < allEras.length; i++) {
            var chapters = ERA_DATA[allEras[i].id] || [];
            for (var j = 0; j < chapters.length; j++) {
                if (chapters[j].id === chId) return chapters[j];
            }
        }
        return null;
    }

    // ── Study Trails (Curated Thematic Paths) ────────────
    var STUDY_TRAILS = [
        {
            id: 'divine-council',
            name: 'Divine Council & Heavenly Court',
            icon: '\u2727',
            color: '#c9a84c',
            desc: 'The complete deep-dive study \u2014 trace how God governs through a council of divine beings, from creation through the New Testament.',
            steps: [
                { chId: 'gen-1', label: 'Genesis 1 \u2014 "Let Us Make"', why: 'The plural of divine deliberation' },
                { chId: 'gen-6-1-4', label: 'Genesis 6:1\u20134 \u2014 Sons of God', why: 'Divine beings cross the boundary' },
                { chId: 'gen-11a', label: 'Genesis 11 \u2014 Tower of Babel', why: 'God disinherits the nations' },
                { textId: 'deuteronomy', label: 'Deuteronomy 32:8\u20139 \u2014 The Worldview', why: 'Nations allotted to sons of God; Israel to YHWH' },
                { textId: 'psalms', label: 'Psalm 82 \u2014 God Judges the Gods', why: 'YHWH indicts corrupt divine rulers' },
                { textId: 'isaiah', label: 'Isaiah 6 \u2014 The Throne Room', why: 'Isaiah sees the council in session' },
                { textId: 'daniel', label: 'Daniel 7 \u2014 Son of Man', why: 'A human figure given authority over the council' },
                { textId: '1enoch', label: '1 Enoch 1\u201336 \u2014 Book of Watchers', why: 'Second Temple expansion of the council rebellion' },
                { textId: 'hebrews', label: 'Hebrews 1\u20132 \u2014 Superior to Angels', why: 'Christ\u2019s authority above the council' }
            ]
        },
        {
            id: 'messianic-thread',
            name: 'The Messianic Thread',
            icon: '\u2720',
            color: '#5a9a6a',
            desc: 'Follow the promise of the Seed from Genesis to Revelation \u2014 every major prophecy and its fulfillment.',
            steps: [
                { chId: 'gen-3', label: 'Genesis 3:15 \u2014 The Protoevangelium', why: 'First promise: the Seed will crush the serpent' },
                { chId: 'gen-12', label: 'Genesis 12 \u2014 Abrahamic Covenant', why: 'Through Abraham\u2019s seed, all nations blessed' },
                { chId: 'gen-22', label: 'Genesis 22 \u2014 The Binding of Isaac', why: 'Typological foreshadowing of the Father\u2019s sacrifice' },
                { textId: 'deuteronomy', label: 'Deuteronomy 18:15\u201319 \u2014 The Prophet', why: 'Moses promises a prophet like himself' },
                { textId: 'psalms', label: 'Psalm 22 \u2014 Crucifixion Psalm', why: 'Prophetic detail a thousand years before the cross' },
                { textId: 'isaiah', label: 'Isaiah 52\u201353 \u2014 Suffering Servant', why: 'Wounded for our transgressions' },
                { textId: 'daniel', label: 'Daniel 9 \u2014 Seventy Weeks', why: 'Prophetic timetable for Messiah\u2019s coming' },
                { textId: 'matthew', label: 'Matthew 1\u20132 \u2014 The Arrival', why: 'Born of a virgin, in Bethlehem, from David\u2019s line' },
                { textId: 'john', label: 'John 1 \u2014 The Word Made Flesh', why: 'The Logos enters creation as a man' },
                { textId: 'revelation', label: 'Revelation 19\u201322 \u2014 King of Kings', why: 'The seed\u2019s ultimate triumph' }
            ]
        },
        {
            id: 'nephilim-giants',
            name: 'Nephilim & Giants',
            icon: '\uD83D\uDC79',
            color: '#a05a54',
            desc: 'Track the giant bloodlines from Genesis 6 through the conquest of Canaan and David\u2019s final battles.',
            steps: [
                { chId: 'gen-6-1-4', label: 'Genesis 6:1\u20134 \u2014 The Origin', why: 'Sons of God + daughters of men = Nephilim' },
                { chId: 'gen-6b', label: 'Genesis 6\u20139 \u2014 The Flood', why: 'Divine judgment on the corrupted world' },
                { textId: 'numbers', label: 'Numbers 13 \u2014 Spies\u2019 Report', why: 'Anakim (Nephilim descendants) terrify the spies' },
                { textId: 'deuteronomy', label: 'Deuteronomy 2\u20133 \u2014 Og of Bashan', why: 'Last of the Rephaim \u2014 his bed was 13 feet' },
                { textId: 'joshua', label: 'Joshua 11 \u2014 Anakim Driven Out', why: 'Joshua\u2019s systematic campaign against giant clans' },
                { textId: '1samuel', label: '1 Samuel 17 \u2014 David & Goliath', why: 'Goliath of Gath \u2014 the last champion' },
                { textId: '2samuel', label: '2 Samuel 21 \u2014 Final Giant Slayers', why: 'David\u2019s mighty men finish the job' },
                { textId: '1enoch', label: '1 Enoch 7\u201310 \u2014 The Watchers\u2019 Sin', why: 'How 200 Watchers taught forbidden arts' },
                { textId: 'giants', label: 'Book of Giants \u2014 Nephilim Dreams', why: 'The giants receive visions of their doom' }
            ]
        },
        {
            id: 'covenant-arc',
            name: 'The Covenant Arc',
            icon: '\uD83D\uDCDC',
            color: '#5b8dbf',
            desc: 'Each covenant builds on the last \u2014 from Eden to the New Covenant in Christ\u2019s blood.',
            steps: [
                { chId: 'gen-1', label: 'Genesis 1\u20132 \u2014 Edenic Mandate', why: 'Dominion, commission, sacred space' },
                { chId: 'gen-8-9', label: 'Genesis 8\u20139 \u2014 Noahic Covenant', why: 'Never again \u2014 rainbow sign, creation preserved' },
                { chId: 'gen-12', label: 'Genesis 12\u201315 \u2014 Abrahamic Covenant', why: 'Land, seed, blessing \u2014 God walks between the pieces' },
                { textId: 'exodus', label: 'Exodus 19\u201324 \u2014 Mosaic Covenant', why: 'Torah given at Sinai \u2014 "a kingdom of priests"' },
                { textId: '2samuel', label: '2 Samuel 7 \u2014 Davidic Covenant', why: 'An everlasting throne \u2014 the royal seed' },
                { textId: 'jeremiah', label: 'Jeremiah 31:31\u201334 \u2014 New Covenant', why: 'Written on hearts, not stone' },
                { textId: 'matthew', label: 'Matthew 26 \u2014 "This Is My Blood"', why: 'Jesus inaugurates the New Covenant at Passover' },
                { textId: 'hebrews', label: 'Hebrews 8\u201310 \u2014 Better Covenant', why: 'Christ as mediator of the superior covenant' }
            ]
        },
        {
            id: 'adam-to-jesus',
            name: 'Adam to Jesus: The Bloodline',
            icon: '\uD83C\uDF33',
            color: '#7a5c3a',
            desc: 'Trace the genealogical line from Adam through Seth, Noah, Abraham, Judah, David, and the exile \u2014 all the way to Jesus of Nazareth.',
            steps: [
                { chId: 'gen-1', label: 'Genesis 1\u20132 \u2014 Adam Created', why: 'God creates Adam in His image \u2014 the line begins' },
                { chId: 'gen-4', label: 'Genesis 4\u20135 \u2014 Seth: The Appointed Seed', why: 'After Abel\u2019s murder, God appoints Seth \u2014 the covenant line' },
                { chId: 'gen-6b', label: 'Genesis 6\u20139 \u2014 Noah: The Line Preserved', why: 'Through the Flood, God preserves the Messianic bloodline' },
                { chId: 'gen-11a', label: 'Genesis 11 \u2014 Shem to Abram', why: 'The genealogy narrows from Shem to Terah\u2019s son Abram' },
                { chId: 'gen-12', label: 'Genesis 12\u201315 \u2014 Abraham: The Promise', why: 'Through your seed all nations will be blessed' },
                { chId: 'gen-22', label: 'Genesis 22 \u2014 Isaac: The Son of Promise', why: 'God provides a ram \u2014 the only son offered and received back' },
                { chId: 'gen-25', label: 'Genesis 25\u201328 \u2014 Jacob/Israel', why: 'The younger chosen over the elder \u2014 12 tribes spring from him' },
                { chId: 'gen-38', label: 'Genesis 38 \u2014 Judah & Tamar', why: 'The royal line passes through Judah \u2014 by a Canaanite widow\u2019s faith' },
                { textId: 'ruth', label: 'Ruth 4 \u2014 Boaz & Ruth', why: 'A Moabite woman grafted into the Messianic line \u2014 great-grandmother of David' },
                { textId: '2samuel', label: '2 Samuel 7 \u2014 David: Eternal Throne', why: 'God promises David an everlasting dynasty' },
                { textId: '1chronicles', label: '1 Chronicles 1\u20139 \u2014 The Full Genealogy', why: 'Adam to the post-exilic community \u2014 the complete record' },
                { textId: 'matthew', label: 'Matthew 1:1\u201317 \u2014 Abraham to Christ', why: 'The legal genealogy through Joseph \u2014 14+14+14 generations' },
                { textId: 'luke', label: 'Luke 3:23\u201338 \u2014 Jesus to Adam', why: 'The biological line traced back to Adam, the son of God' }
            ]
        },
        {
            id: 'cosmic-geography',
            name: 'Cosmic Geography',
            icon: '\uD83C\uDF0D',
            color: '#2d9a8f',
            desc: 'The Bible\u2019s three-tier cosmos: heaven above, earth in the middle, the underworld below \u2014 and how spiritual territory maps onto physical geography.',
            steps: [
                { chId: 'gen-1', label: 'Genesis 1 \u2014 The Three-Tier Cosmos', why: 'Waters above, firmament, waters below \u2014 the cosmic architecture' },
                { chId: 'gen-11a', label: 'Genesis 11 \u2014 Babel & Territorial Allotment', why: 'God disinherits nations, assigns them to divine beings' },
                { textId: 'deuteronomy', label: 'Deuteronomy 32:8\u20139 \u2014 Divine Allotment', why: 'Each nation under a son of God; Israel under YHWH' },
                { textId: 'psalms', label: 'Psalm 82 \u2014 God Judges the Gods', why: 'Territorial rulers judged for corrupt governance' },
                { textId: 'daniel', label: 'Daniel 10 \u2014 Prince of Persia', why: 'Angelic princes over nations \u2014 spiritual warfare behind geopolitics' },
                { textId: '1enoch', label: '1 Enoch 6\u201316 \u2014 Watchers at Hermon', why: 'Mt. Hermon as the cosmic boundary breach point' },
                { textId: 'ephesians', label: 'Ephesians 6:10\u201318 \u2014 Rulers & Powers', why: 'Spiritual forces in heavenly places \u2014 the armor of God' },
                { textId: 'revelation', label: 'Revelation 21\u201322 \u2014 Heaven & Earth Reunited', why: 'The three-tier cosmos healed \u2014 God dwells with humanity' }
            ]
        },
        {
            id: 'dead-sea-scrolls',
            name: 'The Dead Sea Scrolls',
            icon: '\uD83D\uDCDC',
            color: '#2d9a8f',
            desc: 'Trace the texts found at Qumran \u2014 from the Great Isaiah Scroll to the War Scroll, these 2,000-year-old manuscripts changed everything we know about the Bible.',
            steps: [
                { textId: 'isaiah', label: 'Isaiah \u2014 The Great Isaiah Scroll (1QIsa\u1D43)', why: 'The oldest complete biblical book \u2014 1,000 years older than any other Isaiah manuscript. Every chapter of Isaiah was found at Qumran.' },
                { textId: 'deuteronomy', label: 'Deuteronomy 32:8 \u2014 "Sons of God" Restored', why: '4QDeut confirms the DSS/LXX reading "sons of God" over the Masoretic "sons of Israel" \u2014 the divine council allotment of nations.' },
                { chId: 'hab-2', label: 'Habakkuk Pesher (1QpHab) \u2014 "The Righteous Shall Live"', why: 'Among the first 7 scrolls found in 1947. Interprets Habakkuk 2:4 as referring to those who trust the Teacher of Righteousness \u2014 the same verse Paul quotes in Romans 1:17 and Galatians 3:11.' },
                { chId: 'nah-1', label: 'Nahum Pesher (4QpNah) \u2014 The Lion of Wrath', why: 'Applies Nahum\u2019s prophecy against Nineveh to historical Seleucid figures \u2014 rare in DSS for naming real people. Shows how Qumran read prophets as speaking about their own era.' },
                { textId: 'daniel', label: 'Daniel \u2014 8 Manuscripts at Qumran', why: 'Early copies (4QDan\u1D9C ~125 BC) prove the book circulated far earlier than critics claimed.' },
                { textId: 'psalms', label: 'Psalms \u2014 The Great Psalms Scroll (11QPs\u1D43)', why: 'Different ordering + extra psalms (including Psalm 151) \u2014 shows the Psalter was still being shaped. A pesher on Psalm 37 (4QpPs\u1D43) interprets it line by line about the Yahad community.' },
                { textId: 'enoch1', label: '1 Enoch \u2014 4Q201\u2013212 (Aramaic)', why: 'More copies than some OT books \u2014 the Qumran community treated this as authoritative. The Watchers tradition shaped their entire worldview.' },
                { textId: 'jubilees', label: 'Jubilees \u2014 ~15 Copies at Qumran', why: 'More manuscripts than Deuteronomy \u2014 defined the Qumran calendar (364-day solar) and Mastema theology.' },
                { textId: 'dss_sectarian', label: 'Community Rule (1QS) \u2014 Two Spirits', why: 'The foundational theology of the Yahad: Spirit of Truth vs. Spirit of Falsehood in every person. Directly parallels 1 John 4:6 and Johannine light/darkness theology.' },
                { textId: 'dss_sectarian', label: 'War Scroll (1QM) \u2014 Sons of Light', why: 'The 40-year eschatological battle plan \u2014 Michael leads heaven\u2019s armies against Belial. Echoes Revelation 12 and Daniel 12:1.' },
                { textId: 'genesis_apocryphon', label: 'Genesis Apocryphon (1QapGen)', why: 'One of the original 7 scrolls found in Cave 1 in 1947 \u2014 Noah and Abraham speak in first person. Badly deteriorated, only partially readable.' },
                { textId: 'giants', label: 'Book of Giants \u2014 Nephilim at Qumran', why: 'Unknown until the DSS discovery \u2014 the Nephilim receive apocalyptic dreams of their coming judgment. Fills gaps in 1 Enoch\u2019s Watcher narrative.' }
            ]
        },
        {
            id: 'resurrection-trail',
            name: 'Death, Resurrection & New Creation',
            icon: '\u2600',
            color: '#7a6e8a',
            desc: 'What happens when you die? Sheol, nephesh, bodily resurrection, and the physical new creation \u2014 the Hebrew answer to the Platonic afterlife.',
            steps: [
                { textId: 'sheol_resurrection', label: 'Sheol \u2014 The Hebrew Understanding', why: 'Not hell, not heaven \u2014 the universal waiting place everyone goes to' },
                { textId: 'sheol_resurrection', label: 'Nephesh \u2014 You ARE a Soul', why: 'Genesis 2:7 says Adam BECAME a living soul. Plato said you HAVE one.' },
                { textId: 'isaiah', label: 'Isaiah 26:19 \u2014 "Your Dead Shall Live"', why: 'The first clear resurrection promise in the Hebrew Bible' },
                { textId: 'daniel', label: 'Daniel 12:2\u20133 \u2014 "Many Shall Awake"', why: 'Resurrection to life and judgment \u2014 bodily, differentiated' },
                { textId: 'sheol_resurrection', label: '1 Corinthians 15 \u2014 Paul\u2019s Resurrection Argument', why: 'Soma pneumatikon. The last enemy. "We shall be changed."' },
                { textId: 'sheol_resurrection', label: 'Purgatory Dismantled', why: 'Tetelestai + teteleioken = no further purification needed' },
                { textId: 'sheol_resurrection', label: 'The New Creation', why: 'God comes DOWN. Physical earth. Embodied life. Better than "heaven."' },
                { textId: 'revelation', label: 'Revelation 21\u201322 \u2014 All Things New', why: 'New Jerusalem descends. Tree of life reopened. "He will dwell with them."' }
            ]
        },
        {
            id: 'prophetic-matrix',
            name: 'The Prophetic Matrix',
            icon: '\uD83D\uDD2E',
            color: '#b85c3a',
            desc: 'The eight-stage prophetic sequence from the current age through Christ\u2019s return, the millennium, and the new creation \u2014 versus what you were taught.',
            steps: [
                { textId: 'prophetic_sequence', label: 'The Rapture Has a Birthday \u2014 1830', why: 'Zero attestation before Darby. The church never saw this for 1,800 years.' },
                { textId: 'prophetic_sequence', label: 'Apantesis \u2014 One Return', why: '1 Thessalonians 4:17 is a civic escort, not an extraction.' },
                { textId: 'prophetic_sequence', label: 'The Eight-Stage Sequence', why: 'Current age \u2192 Tribulation \u2192 Signs \u2192 Return \u2192 Resurrection \u2192 Millennium \u2192 Gog-Magog \u2192 New Creation' },
                { textId: 'daniel', label: 'Daniel 7 \u2014 The Son of Man', why: 'Given dominion, glory, a kingdom \u2014 all peoples serve him' },
                { textId: 'revelation', label: 'Revelation 20:1\u20136 \u2014 The Millennium', why: 'Six times "thousand years." First resurrection. Reigning with Christ.' },
                { textId: 'prophetic_sequence', label: 'Gog-Magog \u2014 POST-Millennium', why: 'Revelation 20:7\u201310 = Ezekiel 38\u201339. One event. After the thousand years.' },
                { textId: 'reward_bema', label: 'The Bema Seat \u2014 Reward, Not Punishment', why: '2 Corinthians 5:10. What you did IN THE BODY determines your authority.' },
                { textId: 'reward_bema', label: 'Reigning With Christ', why: 'Divine council positions vacated. Believers fill them. Rev 22:5 forever.' }
            ]
        }
    ];

    // ── Ancient Library (Non-Canonical Texts by Source) ──────
    var ANCIENT_LIBRARY = [
        {
            group: 'Dead Sea Scrolls',
            groupId: 'dss',
            subtitle: 'Found at Qumran (250 BC \u2013 68 AD) \u2014 over 900 manuscripts from 11 caves',
            color: '#c9a84c',
            texts: [
                { textId: 'enoch1', title: '1 Enoch', tagline: 'Quoted by Jude. The angels who fell.', catalog: '4Q201\u2013212' },
                { textId: 'jubilees', title: 'Jubilees', tagline: '~15 copies found. Genesis retold with angels.', catalog: '4Q216\u2013228' },
                { textId: 'giants', title: 'Book of Giants', tagline: 'Nephilim dreams of their doom.', catalog: '4Q530\u2013533' },
                { textId: 'genesis_apocryphon', title: 'Genesis Apocryphon', tagline: 'Noah speaks. One of the original 7 scrolls.', catalog: '1QapGen' },
                { textId: 'dss_sectarian', title: 'Community Rule', tagline: 'Two Spirits: Light vs. Darkness.', catalog: '1QS' },
                { textId: 'dss_sectarian', title: 'War Scroll', tagline: 'Sons of Light vs. Sons of Darkness.', catalog: '1QM', era: 'war_scroll' }
            ]
        },
        {
            group: 'Referenced in Scripture',
            groupId: 'referenced',
            subtitle: 'Texts the biblical authors knew and cited by name',
            color: '#5a9a6a',
            texts: [
                { textId: 'jasher', title: 'Book of Jasher', tagline: 'Joshua 10:13 \u2014 "Is this not written in the Book of Jasher?"', catalog: 'Josh 10:13; 2 Sam 1:18' }
            ]
        },
        {
            group: 'Historical Sources',
            groupId: 'historical',
            subtitle: 'First-century eyewitness accounts and church history tested against Scripture',
            color: '#5b8dbf',
            texts: [
                { textId: 'josephus', title: 'Josephus', tagline: 'Eyewitness to the Temple\u2019s destruction, AD 70.', catalog: 'Jewish War, Antiquities, Against Apion' },
                { textId: 'church_history', title: 'Church History', tagline: 'Pentecost to the Reformation \u2014 tested against Scripture as the final standard.', catalog: 'AD 30\u20131648' }
            ]
        }
    ];

    // ── Dead Sea Scrolls Attestation ────────────────────────
    // Every OT book except Esther was found at Qumran.
    // This lookup drives DSS badges on Library cards.
    var DSS_ATTESTATION = {
        // OT — All found at Qumran except Esther
        genesis: '4Q1\u20138 (~250 BC)', exodus: '4QExod (~250 BC)',
        leviticus: '4QLev, 11QLev', numbers: '4QNum (~30 BC)',
        deuteronomy: '4QDeut (33 MSS)', joshua: '4QJosh',
        judges: '4QJudg', ruth: '4QRuth',
        '1samuel': '4QSam\u1D43 (~50 BC)', '2samuel': '4QSam\u1D43',
        '1kings': '4QKgs, 5QKgs', '2kings': '4QKgs, 6QKgs',
        psalms: '11QPs\u1D43 (41+ psalms)', isaiah: '1QIsa\u1D43 (COMPLETE)',
        daniel: '1QDan, 4QDan (8 MSS)',
        job: '4QJob, 11QtgJob', proverbs: '4QProv',
        ecclesiastes: '4QQoh', songofsolomon: '4QCant, 6QCant',
        jeremiah: '4QJer (6 MSS)', ezekiel: '4QEzek',
        lamentations: '4QLam, 5QLam',
        hosea: '4QXIIa', joel: '4QXIIa', amos: '4QXIIa',
        obadiah: '4QXIIa', jonah: '4QXIIa', micah: '4QXIIa',
        nahum: '4QpNah (pesher)', habakkuk: '1QpHab (pesher)',
        zephaniah: '4QXIIa', haggai: '4QXIIa',
        zechariah: '4QXIIa', malachi: '4QXIIa',
        '1chronicles': '4QChr', '2chronicles': '4QChr',
        ezra: '4QEzra', nehemiah: '4QEzra',
        // Non-biblical texts found at Qumran
        enoch1: '4Q201\u2013212 (Aramaic)', giants: '4Q203, 4Q530\u2013533',
        jubilees: '4Q216\u2013228 (~15 MSS)', genesis_apocryphon: '1QapGen (orig. 7)',
        dss_sectarian: '1QS, 1QM, 11Q19, CD'
    };

    // ── Bible Truth Matrix Data ──────────────────────────────
    var BIBLE_TEACHES = {
        god: { label: 'Nature of God', teaching: 'One God in three Persons: Father, Son, and Holy Spirit. Eternal, omniscient, omnipotent, holy, just, and loving. Creator of all things visible and invisible.', scriptures: ['Genesis 1:1','Deuteronomy 6:4','Isaiah 45:5','Matthew 28:19','John 1:1-3','Colossians 1:16-17'] },
        jesus: { label: 'Person of Jesus Christ', teaching: 'Jesus Christ is the eternal Son of God, fully God and fully man. Born of a virgin, lived sinless, died as substitutionary atonement, rose bodily, ascended, and will return in glory.', scriptures: ['John 1:1,14','John 3:16','Philippians 2:5-11','1 Corinthians 15:3-4','Hebrews 4:15','Revelation 19:11-16'] },
        salvation: { label: 'Salvation', teaching: 'Salvation is by grace alone through faith alone in Christ alone. Not earned by works but a gift of God. Repentance and faith bring forgiveness and eternal life.', scriptures: ['Ephesians 2:8-9','Romans 3:23-24','John 14:6','Acts 4:12','Romans 10:9-10'] },
        scripture: { label: 'View of Scripture', teaching: 'The Bible (66 books) is the inspired, inerrant, and authoritative Word of God. Sufficient for faith and practice.', scriptures: ['2 Timothy 3:16-17','2 Peter 1:20-21','Psalm 119:105','Hebrews 4:12'] },
        afterlife: { label: 'Afterlife', teaching: 'Believers go to be with Christ. At the resurrection, believers to eternal life, unbelievers to judgment. Heaven and hell are real.', scriptures: ['2 Corinthians 5:8','John 14:2-3','Revelation 21:1-4','Matthew 25:46','Daniel 12:2'] },
        creation: { label: 'Creation', teaching: 'God created the heavens and the earth. Adam and Eve were specially created. Creation declares God\'s glory and power.', scriptures: ['Genesis 1:1-31','Genesis 2:7','Psalm 19:1','Romans 1:20','Colossians 1:16'] },
        angels: { label: 'Angels & Demons', teaching: 'Angels are created spiritual beings who serve God. Some fell with Satan and became demons. Believers have authority over demonic powers through Christ.', scriptures: ['Hebrews 1:14','Psalm 103:20','Revelation 12:7-9','Ephesians 6:11-12','James 4:7'] },
        nephilim: { label: 'Nephilim / Genesis 6', teaching: 'The Nephilim were offspring of the sons of God (divine/angelic beings) and human women. They were giants and mighty men. This incursion contributed to the corruption that led to the Flood.', scriptures: ['Genesis 6:1-4','Jude 1:6-7','2 Peter 2:4-5','Numbers 13:33','1 Enoch 6-16'] },
        flood: { label: 'The Flood', teaching: 'The Flood was a global judgment on human wickedness and Nephilim corruption. Noah and his family (8 people) were saved on the Ark.', scriptures: ['Genesis 6-9','2 Peter 3:5-6','Matthew 24:37-39','1 Peter 3:20','Hebrews 11:7'] },
        mary: { label: 'Mary', teaching: 'Mary was a virgin chosen by God to bear Jesus. Blessed among women but a sinner in need of salvation. Not to be worshipped or prayed to. One mediator: Christ.', scriptures: ['Luke 1:26-38','Luke 1:46-47','1 Timothy 2:5','Mark 3:31-35'] },
        baptism: { label: 'Baptism', teaching: 'An outward sign of inward grace \u2014 public declaration of faith. Symbolizes death to sin, burial with Christ, and resurrection to new life. Believer\'s baptism by immersion.', scriptures: ['Matthew 28:19','Acts 2:38','Romans 6:3-4','Colossians 2:12'] },
        communion: { label: 'Communion', teaching: 'A memorial ordinance instituted by Christ. The bread represents His body; the cup His blood shed for the new covenant. A remembrance, not a re-sacrifice.', scriptures: ['Luke 22:19-20','1 Corinthians 11:23-26','Matthew 26:26-28'] },
        holyspirit: { label: 'Holy Spirit', teaching: 'The third Person of the Trinity, fully God. Convicts of sin, regenerates, indwells, seals, gives gifts, produces fruit, and guides into truth.', scriptures: ['John 14:16-17','Acts 1:8','Romans 8:9-11','1 Corinthians 12:4-11','Galatians 5:22-23'] }
    };

    var DOCTRINE_KEYS = ['god','jesus','salvation','scripture','afterlife','creation','angels','nephilim','flood','mary','baptism','communion','holyspirit'];

    var RELIGIONS_DATA = [
        // Christian denominations
        {id:'baptist',name:'Baptist',cat:'christian',founded:'1609',adherents:'~100M',d:{god:'full',jesus:'full',salvation:'full',scripture:'full',afterlife:'full',creation:'mostly',angels:'full',nephilim:'mostly',flood:'full',mary:'full',baptism:'full',communion:'full',holyspirit:'full'}},
        {id:'catholic',name:'Roman Catholic',cat:'christian',founded:'~33 AD',adherents:'~1.4B',d:{god:'full',jesus:'full',salvation:'partial',scripture:'partial',afterlife:'mostly',creation:'mostly',angels:'full',nephilim:'partial',flood:'mostly',mary:'divergent',baptism:'partial',communion:'partial',holyspirit:'mostly'}},
        {id:'orthodox',name:'Eastern Orthodox',cat:'christian',founded:'~33 AD',adherents:'~220M',d:{god:'mostly',jesus:'full',salvation:'partial',scripture:'partial',afterlife:'mostly',creation:'mostly',angels:'full',nephilim:'partial',flood:'mostly',mary:'divergent',baptism:'partial',communion:'partial',holyspirit:'mostly'}},
        {id:'lutheran',name:'Lutheran',cat:'christian',founded:'1517',adherents:'~80M',d:{god:'full',jesus:'full',salvation:'full',scripture:'full',afterlife:'full',creation:'mostly',angels:'full',nephilim:'mostly',flood:'full',mary:'mostly',baptism:'partial',communion:'mostly',holyspirit:'full'}},
        {id:'presbyterian',name:'Presbyterian / Reformed',cat:'christian',founded:'1560s',adherents:'~75M',d:{god:'full',jesus:'full',salvation:'full',scripture:'full',afterlife:'full',creation:'mostly',angels:'full',nephilim:'mostly',flood:'full',mary:'full',baptism:'partial',communion:'mostly',holyspirit:'full'}},
        {id:'methodist',name:'Methodist',cat:'christian',founded:'1738',adherents:'~80M',d:{god:'full',jesus:'full',salvation:'mostly',scripture:'mostly',afterlife:'full',creation:'mostly',angels:'full',nephilim:'mostly',flood:'mostly',mary:'full',baptism:'partial',communion:'mostly',holyspirit:'full'}},
        {id:'pentecostal',name:'Pentecostal',cat:'christian',founded:'1901',adherents:'~280M',d:{god:'mostly',jesus:'full',salvation:'mostly',scripture:'mostly',afterlife:'full',creation:'full',angels:'full',nephilim:'full',flood:'full',mary:'full',baptism:'full',communion:'full',holyspirit:'full'}},
        {id:'sda',name:'Seventh-day Adventist',cat:'christian',founded:'1863',adherents:'~22M',d:{god:'full',jesus:'mostly',salvation:'partial',scripture:'partial',afterlife:'partial',creation:'full',angels:'full',nephilim:'partial',flood:'full',mary:'full',baptism:'full',communion:'mostly',holyspirit:'full'}},
        {id:'anglican',name:'Anglican / Episcopalian',cat:'christian',founded:'1534',adherents:'~85M',d:{god:'full',jesus:'full',salvation:'mostly',scripture:'mostly',afterlife:'mostly',creation:'mostly',angels:'full',nephilim:'mostly',flood:'mostly',mary:'mostly',baptism:'partial',communion:'mostly',holyspirit:'full'}},
        {id:'assemblies',name:'Assemblies of God',cat:'christian',founded:'1914',adherents:'~70M',d:{god:'full',jesus:'full',salvation:'mostly',scripture:'full',afterlife:'full',creation:'full',angels:'full',nephilim:'full',flood:'full',mary:'full',baptism:'full',communion:'full',holyspirit:'full'}},
        {id:'churchofchrist',name:'Church of Christ',cat:'christian',founded:'1800s',adherents:'~3M',d:{god:'full',jesus:'full',salvation:'partial',scripture:'full',afterlife:'full',creation:'full',angels:'full',nephilim:'mostly',flood:'full',mary:'full',baptism:'partial',communion:'mostly',holyspirit:'mostly'}},
        {id:'nondenominational',name:'Non-Denominational Evangelical',cat:'christian',founded:'20th c.',adherents:'~20M',d:{god:'full',jesus:'full',salvation:'full',scripture:'full',afterlife:'full',creation:'mostly',angels:'full',nephilim:'mostly',flood:'full',mary:'full',baptism:'full',communion:'full',holyspirit:'full'}},
        {id:'reformed_baptist',name:'Reformed Baptist',cat:'christian',founded:'1630s',adherents:'~5M',d:{god:'full',jesus:'full',salvation:'full',scripture:'full',afterlife:'full',creation:'full',angels:'full',nephilim:'mostly',flood:'full',mary:'full',baptism:'full',communion:'mostly',holyspirit:'full'}},
        // World religions
        {id:'islam',name:'Islam',cat:'world',founded:'622 AD',adherents:'~2B',d:{god:'partial',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'partial',creation:'mostly',angels:'partial',nephilim:'divergent',flood:'mostly',mary:'partial',baptism:'divergent',communion:'divergent',holyspirit:'divergent'}},
        {id:'judaism',name:'Judaism (Rabbinic)',cat:'world',founded:'~6th c. BC',adherents:'~15M',d:{god:'partial',jesus:'divergent',salvation:'divergent',scripture:'partial',afterlife:'partial',creation:'mostly',angels:'mostly',nephilim:'mostly',flood:'full',mary:'divergent',baptism:'partial',communion:'divergent',holyspirit:'partial'}},
        {id:'hinduism',name:'Hinduism',cat:'world',founded:'~1500+ BC',adherents:'~1.2B',d:{god:'divergent',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'divergent',creation:'divergent',angels:'partial',nephilim:'divergent',flood:'parallel',mary:'divergent',baptism:'divergent',communion:'divergent',holyspirit:'divergent'}},
        {id:'buddhism',name:'Buddhism',cat:'world',founded:'~500 BC',adherents:'~500M',d:{god:'divergent',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'divergent',creation:'divergent',angels:'partial',nephilim:'divergent',flood:'divergent',mary:'divergent',baptism:'divergent',communion:'divergent',holyspirit:'divergent'}},
        {id:'mormonism',name:'Mormonism (LDS)',cat:'world',founded:'1830',adherents:'~17M',d:{god:'divergent',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'divergent',creation:'partial',angels:'partial',nephilim:'divergent',flood:'full',mary:'partial',baptism:'partial',communion:'mostly',holyspirit:'partial'}},
        {id:'jw',name:"Jehovah's Witnesses",cat:'world',founded:'1870s',adherents:'~8.7M',d:{god:'divergent',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'divergent',creation:'partial',angels:'partial',nephilim:'full',flood:'full',mary:'full',baptism:'mostly',communion:'divergent',holyspirit:'divergent'}},
        {id:'sikhism',name:'Sikhism',cat:'world',founded:'1469',adherents:'~30M',d:{god:'partial',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'divergent',creation:'partial',angels:'partial',nephilim:'divergent',flood:'divergent',mary:'divergent',baptism:'divergent',communion:'divergent',holyspirit:'divergent'}},
        {id:'bahai',name:"Baha'i Faith",cat:'world',founded:'1863',adherents:'~8M',d:{god:'partial',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'divergent',creation:'partial',angels:'divergent',nephilim:'divergent',flood:'divergent',mary:'partial',baptism:'divergent',communion:'divergent',holyspirit:'divergent'}},
        {id:'new_age',name:'New Age',cat:'world',founded:'1960s',adherents:'Millions',d:{god:'divergent',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'divergent',creation:'divergent',angels:'partial',nephilim:'divergent',flood:'divergent',mary:'divergent',baptism:'divergent',communion:'divergent',holyspirit:'divergent'}},
        {id:'scientology',name:'Scientology',cat:'world',founded:'1954',adherents:'~20-50K',d:{god:'divergent',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'divergent',creation:'divergent',angels:'divergent',nephilim:'divergent',flood:'divergent',mary:'divergent',baptism:'divergent',communion:'divergent',holyspirit:'divergent'}},
        {id:'nation_of_islam',name:'Nation of Islam',cat:'world',founded:'1930',adherents:'~50K',d:{god:'divergent',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'divergent',creation:'divergent',angels:'divergent',nephilim:'divergent',flood:'divergent',mary:'divergent',baptism:'divergent',communion:'divergent',holyspirit:'divergent'}},
        {id:'christian_science',name:'Christian Science',cat:'world',founded:'1879',adherents:'~100K',d:{god:'divergent',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'divergent',creation:'divergent',angels:'divergent',nephilim:'divergent',flood:'divergent',mary:'partial',baptism:'divergent',communion:'divergent',holyspirit:'divergent'}},
        {id:'unitarian',name:'Unitarian Universalism',cat:'world',founded:'1961',adherents:'~200K',d:{god:'divergent',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'divergent',creation:'divergent',angels:'divergent',nephilim:'divergent',flood:'divergent',mary:'divergent',baptism:'divergent',communion:'divergent',holyspirit:'divergent'}},
        {id:'taoism',name:'Taoism',cat:'world',founded:'~4th c. BC',adherents:'~20M',d:{god:'divergent',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'divergent',creation:'divergent',angels:'divergent',nephilim:'divergent',flood:'parallel',mary:'divergent',baptism:'divergent',communion:'divergent',holyspirit:'divergent'}},
        {id:'shinto',name:'Shinto',cat:'world',founded:'Prehistoric',adherents:'~80M',d:{god:'divergent',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'divergent',creation:'divergent',angels:'divergent',nephilim:'divergent',flood:'divergent',mary:'divergent',baptism:'divergent',communion:'divergent',holyspirit:'divergent'}},
        {id:'rastafari',name:'Rastafari',cat:'world',founded:'1930s',adherents:'~1M',d:{god:'divergent',jesus:'divergent',salvation:'divergent',scripture:'partial',afterlife:'divergent',creation:'partial',angels:'partial',nephilim:'divergent',flood:'mostly',mary:'divergent',baptism:'divergent',communion:'divergent',holyspirit:'partial'}},
        {id:'black_hebrew_israelites',name:'Black Hebrew Israelites',cat:'world',founded:'Late 1800s',adherents:'~200K',d:{god:'partial',jesus:'partial',salvation:'partial',scripture:'partial',afterlife:'partial',creation:'full',angels:'full',nephilim:'full',flood:'full',mary:'mostly',baptism:'mostly',communion:'partial',holyspirit:'partial'}},
        // Esoteric
        {id:'freemasonry',name:'Freemasonry',cat:'esoteric',founded:'1717',adherents:'~2-6M',d:{god:'divergent',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'divergent',creation:'partial',angels:'divergent',nephilim:'divergent',flood:'partial',mary:'divergent',baptism:'divergent',communion:'divergent',holyspirit:'divergent'}},
        {id:'gnosticism',name:'Gnosticism',cat:'esoteric',founded:'1st-2nd c.',adherents:'~100K',d:{god:'divergent',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'divergent',creation:'divergent',angels:'partial',nephilim:'partial',flood:'divergent',mary:'divergent',baptism:'divergent',communion:'divergent',holyspirit:'divergent'}},
        {id:'kabbalah',name:'Kabbalah',cat:'esoteric',founded:'12th c.',adherents:'~3M',d:{god:'partial',jesus:'divergent',salvation:'divergent',scripture:'partial',afterlife:'partial',creation:'partial',angels:'mostly',nephilim:'mostly',flood:'partial',mary:'divergent',baptism:'partial',communion:'partial',holyspirit:'partial'}},
        {id:'satanism',name:'Satanism (LaVeyan)',cat:'esoteric',founded:'1966',adherents:'~20-100K',d:{god:'divergent',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'divergent',creation:'divergent',angels:'divergent',nephilim:'divergent',flood:'divergent',mary:'divergent',baptism:'divergent',communion:'divergent',holyspirit:'divergent'}},
        {id:'hermeticism',name:'Hermeticism',cat:'esoteric',founded:'~2nd c. AD',adherents:'~100K',d:{god:'partial',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'divergent',creation:'divergent',angels:'partial',nephilim:'divergent',flood:'divergent',mary:'divergent',baptism:'divergent',communion:'divergent',holyspirit:'divergent'}},
        {id:'rosicrucianism',name:'Rosicrucianism',cat:'esoteric',founded:'1614',adherents:'~250K',d:{god:'divergent',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'divergent',creation:'divergent',angels:'partial',nephilim:'partial',flood:'partial',mary:'divergent',baptism:'divergent',communion:'divergent',holyspirit:'divergent'}},
        {id:'theosophy',name:'Theosophy',cat:'esoteric',founded:'1875',adherents:'~50K',d:{god:'divergent',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'divergent',creation:'divergent',angels:'partial',nephilim:'partial',flood:'partial',mary:'divergent',baptism:'divergent',communion:'divergent',holyspirit:'divergent'}},
        // Ancient mythology
        {id:'mystery_babylon',name:'Mystery Babylon',cat:'mythology',founded:'~3000 BC',adherents:'Historical',d:{god:'divergent',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'partial',creation:'divergent',angels:'partial',nephilim:'parallel',flood:'parallel',mary:'divergent',baptism:'partial',communion:'partial',holyspirit:'divergent'}},
        {id:'greek',name:'Greek Mythology',cat:'mythology',founded:'~2000 BC',adherents:'Historical',d:{god:'divergent',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'partial',creation:'divergent',angels:'partial',nephilim:'parallel',flood:'parallel',mary:'divergent',baptism:'partial',communion:'partial',holyspirit:'divergent'}},
        {id:'norse',name:'Norse Mythology',cat:'mythology',founded:'~800 AD',adherents:'Historical',d:{god:'divergent',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'partial',creation:'divergent',angels:'partial',nephilim:'parallel',flood:'parallel',mary:'divergent',baptism:'partial',communion:'partial',holyspirit:'partial'}},
        {id:'egyptian',name:'Egyptian Religion',cat:'mythology',founded:'~3100 BC',adherents:'Historical',d:{god:'divergent',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'partial',creation:'partial',angels:'partial',nephilim:'partial',flood:'partial',mary:'divergent',baptism:'partial',communion:'partial',holyspirit:'divergent'}},
        {id:'sumerian',name:'Sumerian / Mesopotamian',cat:'mythology',founded:'~4000 BC',adherents:'Historical',d:{god:'divergent',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'partial',creation:'partial',angels:'parallel',nephilim:'parallel',flood:'parallel',mary:'divergent',baptism:'partial',communion:'partial',holyspirit:'divergent'}},
        {id:'zoroastrianism',name:'Zoroastrianism',cat:'mythology',founded:'~1500 BC',adherents:'~100-200K',d:{god:'partial',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'partial',creation:'partial',angels:'parallel',nephilim:'partial',flood:'parallel',mary:'divergent',baptism:'divergent',communion:'divergent',holyspirit:'parallel'}},
        {id:'chinese',name:'Chinese Traditional / Folk',cat:'mythology',founded:'Prehistoric',adherents:'~400M',d:{god:'partial',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'divergent',creation:'divergent',angels:'partial',nephilim:'partial',flood:'parallel',mary:'divergent',baptism:'divergent',communion:'divergent',holyspirit:'divergent'}},
        {id:'hindu_myth',name:'Hindu Mythology',cat:'mythology',founded:'~1500 BC+',adherents:'Part of Hinduism',d:{god:'divergent',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'divergent',creation:'divergent',angels:'partial',nephilim:'parallel',flood:'parallel',mary:'divergent',baptism:'partial',communion:'partial',holyspirit:'divergent'}},
        {id:'biblical_angels',name:'Biblical Angelology (Reference)',cat:'mythology',founded:'Biblical',adherents:'All Bible-believing',d:{god:'full',jesus:'full',salvation:'full',scripture:'full',afterlife:'full',creation:'full',angels:'full',nephilim:'full',flood:'full',mary:'full',baptism:'full',communion:'full',holyspirit:'full'}},
        // Native / Indigenous
        {id:'cherokee',name:'Cherokee Traditional',cat:'native',founded:'Pre-Columbian',adherents:'Cultural',d:{god:'partial',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'divergent',creation:'divergent',angels:'partial',nephilim:'parallel',flood:'parallel',mary:'divergent',baptism:'partial',communion:'partial',holyspirit:'partial'}},
        {id:'hopi',name:'Hopi Traditional',cat:'native',founded:'Pre-Columbian',adherents:'Cultural',d:{god:'partial',jesus:'partial',salvation:'divergent',scripture:'divergent',afterlife:'divergent',creation:'partial',angels:'partial',nephilim:'parallel',flood:'parallel',mary:'divergent',baptism:'partial',communion:'partial',holyspirit:'partial'}},
        {id:'lakota',name:'Lakota / Sioux',cat:'native',founded:'Pre-Columbian',adherents:'Cultural',d:{god:'partial',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'divergent',creation:'divergent',angels:'partial',nephilim:'partial',flood:'parallel',mary:'divergent',baptism:'partial',communion:'partial',holyspirit:'partial'}},
        {id:'iroquois',name:'Iroquois (Haudenosaunee)',cat:'native',founded:'Pre-Columbian',adherents:'Cultural',d:{god:'partial',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'partial',creation:'divergent',angels:'partial',nephilim:'parallel',flood:'parallel',mary:'divergent',baptism:'divergent',communion:'partial',holyspirit:'partial'}},
        {id:'algonquin',name:'Algonquin',cat:'native',founded:'Pre-Columbian',adherents:'Cultural',d:{god:'partial',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'divergent',creation:'partial',angels:'partial',nephilim:'parallel',flood:'parallel',mary:'divergent',baptism:'divergent',communion:'partial',holyspirit:'partial'}},
        {id:'lenape',name:'Lenape (Delaware)',cat:'native',founded:'Pre-Columbian',adherents:'Cultural',d:{god:'partial',jesus:'divergent',salvation:'divergent',scripture:'divergent',afterlife:'partial',creation:'divergent',angels:'partial',nephilim:'parallel',flood:'parallel',mary:'divergent',baptism:'divergent',communion:'partial',holyspirit:'partial'}}
    ];

    // Religions detail data (injected by build.py — full doctrinal position text)
    var RELIGIONS_DETAIL = __RELIGIONS_DETAIL_DATA__;

    // Standalone flow translations for texts without interlinear (1 Enoch, DSS, etc.)
    var STANDALONE_FLOW = __STANDALONE_FLOW_DATA__;
    var STANDALONE_NOTES = __STANDALONE_NOTES_DATA__;

    var ALIGNMENT_INFO = {
        full:      { label: 'Full Match',  color: '#22c55e' },
        mostly:    { label: 'Mostly Aligned', color: '#3b82f6' },
        parallel:  { label: 'Parallel Tradition', color: '#a78bfa' },
        partial:   { label: 'Partial Agreement', color: '#f59e0b' },
        divergent: { label: 'Divergent', color: '#ef4444' }
    };

    var RELIGION_CATEGORIES = {
        christian: { label: 'Christian Denominations', icon: '\u2720' },
        world:     { label: 'World Religions', icon: '\uD83C\uDF0D' },
        esoteric:  { label: 'Esoteric / Occult', icon: '\u2609' },
        mythology: { label: 'Ancient Mythology', icon: '\uD83C\uDFDB' },
        native:    { label: 'Native / Indigenous', icon: '\uD83C\uDF3F' }
    };

    // ── Biblical + World History Timeline Data ──────────────
    var TIMELINE_DATA = [
        // Primeval history
        { year: -4000, end: -4000, label: 'Creation', desc: 'God creates heavens and earth, Adam and Eve in Eden', cat: 'bible', era: 'primeval', ref: 'Genesis 1\u20132' },
        { year: -3900, end: -3900, label: 'The Fall', desc: 'Humanity\'s rebellion; the serpent\'s deception; the Protoevangelium (Gen 3:15)', cat: 'bible', era: 'primeval', ref: 'Genesis 3' },
        { year: -3500, end: -3500, label: 'Cain & Abel', desc: 'First murder; line of Cain builds civilization', cat: 'bible', era: 'primeval', ref: 'Genesis 4' },
        { year: -3300, end: -3300, label: 'Sumerians Emerge', desc: 'Earliest Sumerian city-states (Eridu, Uruk) in Mesopotamia', cat: 'world', era: 'primeval' },
        { year: -3100, end: -3100, label: 'Egypt Unified', desc: 'Upper and Lower Egypt unified under Narmer/Menes; First Dynasty', cat: 'world', era: 'primeval' },
        { year: -3000, end: -3000, label: 'Sons of God Descend', desc: 'Watchers descend to Mt. Hermon; take human wives; Nephilim born', cat: 'bible', era: 'primeval', ref: 'Genesis 6:1\u20134' },
        { year: -2900, end: -2900, label: 'Cuneiform Writing', desc: 'Sumerians develop cuneiform \u2014 earliest known writing system', cat: 'world', era: 'primeval' },
        { year: -2500, end: -2500, label: 'The Great Flood', desc: 'Global judgment on Nephilim corruption; Noah and 8 saved on the Ark', cat: 'bible', era: 'primeval', ref: 'Genesis 6\u20139' },
        { year: -2400, end: -2400, label: 'Tower of Babel', desc: 'Nations scattered; God disinherits nations to sons of God (Deut 32:8\u20139)', cat: 'bible', era: 'primeval', ref: 'Genesis 11' },
        { year: -2500, end: -2350, label: 'Great Pyramid', desc: 'Pyramid of Giza built during Old Kingdom Egypt', cat: 'world', era: 'primeval' },
        { year: -2350, end: -2350, label: 'Akkadian Empire', desc: 'Sargon of Akkad unifies Mesopotamia \u2014 first empire', cat: 'world', era: 'primeval' },
        // Patriarchal period
        { year: -2100, end: -2100, label: 'Ur III Period', desc: 'Third Dynasty of Ur \u2014 Sumerian renaissance; ziggurat of Ur', cat: 'world', era: 'patriarchs' },
        { year: -2000, end: -2000, label: 'Abraham Called', desc: 'God calls Abram from Ur; Abrahamic Covenant (land, seed, blessing)', cat: 'bible', era: 'patriarchs', ref: 'Genesis 12\u201315' },
        { year: -1900, end: -1900, label: 'Sodom & Gomorrah', desc: 'Divine judgment destroys the cities of the plain', cat: 'bible', era: 'patriarchs', ref: 'Genesis 18\u201319' },
        { year: -1900, end: -1900, label: 'Binding of Isaac', desc: 'Abraham\'s ultimate test of faith; ram provided; foreshadows Christ', cat: 'bible', era: 'patriarchs', ref: 'Genesis 22' },
        { year: -1850, end: -1850, label: 'Jacob & Esau', desc: 'Jacob receives the blessing; wrestles God at Peniel; becomes Israel', cat: 'bible', era: 'patriarchs', ref: 'Genesis 25\u201335' },
        { year: -1800, end: -1800, label: 'Hammurabi\'s Code', desc: 'Babylonian law code \u2014 compare with Mosaic Law parallels', cat: 'world', era: 'patriarchs' },
        { year: -1750, end: -1750, label: 'Joseph in Egypt', desc: 'Sold by brothers, rises to vizier; Israel\'s family moves to Egypt', cat: 'bible', era: 'patriarchs', ref: 'Genesis 37\u201350' },
        // Exodus & conquest
        { year: -1600, end: -1600, label: 'Hyksos Period', desc: 'Semitic Hyksos rulers in Egypt \u2014 possible context for Joseph\'s rise', cat: 'world', era: 'exodus' },
        { year: -1450, end: -1450, label: 'The Exodus', desc: 'Moses leads Israel out of Egypt; 10 plagues against Egyptian gods; Red Sea crossing', cat: 'bible', era: 'exodus', ref: 'Exodus 1\u201315' },
        { year: -1450, end: -1450, label: 'Torah Given at Sinai', desc: 'Mosaic Covenant; Ten Commandments; Tabernacle instructions', cat: 'bible', era: 'exodus', ref: 'Exodus 19\u201340' },
        { year: -1400, end: -1400, label: 'Conquest of Canaan', desc: 'Joshua leads Israel into the land; campaigns against giant clans (Anakim)', cat: 'bible', era: 'exodus', ref: 'Joshua' },
        { year: -1400, end: -1400, label: 'Amarna Letters', desc: 'Egyptian diplomatic archive \u2014 mentions \u201cHabiru\u201d (possible Hebrews)', cat: 'world', era: 'exodus' },
        { year: -1350, end: -1350, label: 'Akhenaten', desc: 'Egyptian pharaoh introduces monotheistic sun worship (Aten)', cat: 'world', era: 'exodus' },
        { year: -1200, end: -1200, label: 'Period of Judges', desc: 'Cycles of rebellion, oppression, and deliverance; Deborah, Gideon, Samson', cat: 'bible', era: 'exodus', ref: 'Judges' },
        { year: -1200, end: -1200, label: 'Bronze Age Collapse', desc: 'Sea Peoples destroy eastern Mediterranean civilizations; Hittites fall', cat: 'world', era: 'exodus' },
        { year: -1200, end: -1200, label: 'Trojan War', desc: 'Greek siege of Troy (traditional date) \u2014 Homer\'s Iliad & Odyssey', cat: 'world', era: 'exodus' },
        // United & Divided Kingdom
        { year: -1050, end: -1050, label: 'King Saul', desc: 'Israel demands a king; Saul anointed; rejects God\'s instructions', cat: 'bible', era: 'kingdom', ref: '1 Samuel 8\u201331' },
        { year: -1010, end: -1010, label: 'David\'s Reign', desc: 'Man after God\'s heart; conquers Jerusalem; Davidic Covenant \u2014 everlasting throne', cat: 'bible', era: 'kingdom', ref: '2 Samuel 7' },
        { year: -1000, end: -1000, label: 'Psalms Written', desc: 'David composes many Psalms \u2014 Ps 22 (crucifixion), Ps 82 (divine council)', cat: 'bible', era: 'kingdom', ref: 'Psalms' },
        { year: -970, end: -970, label: 'Solomon\'s Temple', desc: 'First Temple built in Jerusalem; God\'s glory fills the Holy of Holies', cat: 'bible', era: 'kingdom', ref: '1 Kings 5\u20138' },
        { year: -930, end: -930, label: 'Kingdom Divides', desc: 'Israel splits: Northern (10 tribes) and Southern Judah (2 tribes)', cat: 'bible', era: 'kingdom', ref: '1 Kings 12' },
        { year: -900, end: -900, label: 'Phoenician Expansion', desc: 'Phoenicians establish Carthage; Mediterranean trade networks', cat: 'world', era: 'kingdom' },
        { year: -850, end: -850, label: 'Elijah & Elisha', desc: 'Prophets confront Baal worship; fire from heaven on Carmel', cat: 'bible', era: 'kingdom', ref: '1 Kings 17\u2013 2 Kings 13' },
        { year: -776, end: -776, label: 'First Olympics', desc: 'First recorded Olympic Games at Olympia, Greece', cat: 'world', era: 'kingdom' },
        { year: -753, end: -753, label: 'Rome Founded', desc: 'Traditional founding of Rome by Romulus and Remus', cat: 'world', era: 'kingdom' },
        { year: -740, end: -740, label: 'Isaiah\'s Ministry', desc: 'Isaiah sees God\'s throne (ch 6); prophesies virgin birth (7:14), Suffering Servant (52\u201353)', cat: 'bible', era: 'kingdom', ref: 'Isaiah' },
        { year: -722, end: -722, label: 'Northern Kingdom Falls', desc: 'Assyria conquers Israel; 10 tribes scattered \u2014 lost tribes', cat: 'bible', era: 'kingdom', ref: '2 Kings 17' },
        { year: -700, end: -700, label: 'Assyrian Empire', desc: 'Sennacherib, Ashurbanipal; massive library at Nineveh with flood tablets', cat: 'world', era: 'kingdom' },
        // Exile & Return
        { year: -605, end: -605, label: 'Babylonian Captivity Begins', desc: 'Nebuchadnezzar takes first captives including Daniel', cat: 'bible', era: 'exile', ref: 'Daniel 1' },
        { year: -586, end: -586, label: 'Temple Destroyed', desc: 'Babylon destroys Solomon\'s Temple; Jerusalem burned; Judah exiled', cat: 'bible', era: 'exile', ref: '2 Kings 25' },
        { year: -563, end: -563, label: 'Buddha Born', desc: 'Siddhartha Gautama born in Nepal; founds Buddhism', cat: 'world', era: 'exile' },
        { year: -550, end: -550, label: 'Cyrus the Great', desc: 'Persian Empire rises; conquers Babylon; fulfills Isaiah 45 prophecy', cat: 'world', era: 'exile' },
        { year: -539, end: -539, label: 'Fall of Babylon', desc: 'Writing on the wall (Daniel 5); Cyrus takes Babylon in one night', cat: 'bible', era: 'exile', ref: 'Daniel 5' },
        { year: -538, end: -538, label: 'Decree of Cyrus', desc: 'Jews allowed to return; rebuilding begins \u2014 fulfills Jeremiah 29:10', cat: 'bible', era: 'exile', ref: 'Ezra 1' },
        { year: -516, end: -516, label: 'Second Temple Built', desc: 'Zerubbabel completes the Second Temple \u2014 modest compared to Solomon\'s', cat: 'bible', era: 'exile', ref: 'Ezra 6' },
        { year: -509, end: -509, label: 'Roman Republic', desc: 'Rome overthrows monarchy; establishes the Republic', cat: 'world', era: 'exile' },
        { year: -500, end: -500, label: 'Confucius', desc: 'Chinese philosopher teaches ethics, order, and filial piety', cat: 'world', era: 'exile' },
        { year: -480, end: -480, label: 'Esther & Purim', desc: 'Jewish queen saves her people in Persia from Haman\'s plot', cat: 'bible', era: 'exile', ref: 'Esther' },
        { year: -458, end: -458, label: 'Ezra\'s Return', desc: 'Ezra brings Torah reform; reinstates covenant faithfulness', cat: 'bible', era: 'exile', ref: 'Ezra 7\u201310' },
        { year: -445, end: -445, label: 'Nehemiah Rebuilds Walls', desc: 'Jerusalem\'s walls rebuilt in 52 days despite opposition', cat: 'bible', era: 'exile', ref: 'Nehemiah' },
        // Intertestamental / Second Temple
        { year: -430, end: -430, label: 'Malachi \u2014 OT Closes', desc: 'Last OT prophet; 400 years of prophetic silence begin', cat: 'bible', era: 'secondtemple', ref: 'Malachi' },
        { year: -336, end: -323, label: 'Alexander the Great', desc: 'Conquers Persian Empire; Hellenization of the Near East', cat: 'world', era: 'secondtemple' },
        { year: -300, end: -200, label: '1 Enoch Composed', desc: 'Book of Watchers (1\u201336) and Book of Parables; expands Genesis 6 and divine council theology', cat: 'bible', era: 'secondtemple', ref: '1 Enoch' },
        { year: -250, end: -250, label: 'Septuagint (LXX)', desc: 'Hebrew Bible translated into Greek in Alexandria; basis for NT quotations', cat: 'world', era: 'secondtemple' },
        { year: -200, end: -100, label: 'Jubilees Composed', desc: 'Retells Genesis\u2013Exodus with 50-year jubilee calendar; Watchers narrative', cat: 'bible', era: 'secondtemple', ref: 'Jubilees' },
        { year: -167, end: -167, label: 'Maccabean Revolt', desc: 'Antiochus IV desecrates Temple; Judas Maccabeus leads revolt \u2014 Hanukkah', cat: 'bible', era: 'secondtemple', ref: '1 Maccabees' },
        { year: -150, end: -70, label: 'Dead Sea Scrolls Written', desc: 'Qumran community preserves biblical manuscripts + sectarian texts', cat: 'world', era: 'secondtemple' },
        { year: -63, end: -63, label: 'Rome Conquers Jerusalem', desc: 'Pompey enters Holy of Holies; Judea becomes Roman territory', cat: 'world', era: 'secondtemple' },
        { year: -44, end: -44, label: 'Julius Caesar Assassinated', desc: 'End of Roman Republic era; rise of the Empire', cat: 'world', era: 'secondtemple' },
        { year: -37, end: -4, label: 'Herod the Great', desc: 'Herod rules Judea; massive Temple renovation; massacre of innocents', cat: 'world', era: 'secondtemple' },
        // New Testament
        { year: -5, end: -5, label: 'Jesus Born', desc: 'The Word becomes flesh in Bethlehem \u2014 God enters creation as a man', cat: 'bible', era: 'nt', ref: 'Matthew 1\u20132; Luke 1\u20132' },
        { year: 27, end: 27, label: 'Jesus\u2019 Baptism', desc: 'John baptizes Jesus; Spirit descends; Father speaks \u2014 Trinity revealed', cat: 'bible', era: 'nt', ref: 'Matthew 3' },
        { year: 30, end: 30, label: 'Crucifixion & Resurrection', desc: 'Jesus dies on Passover, rises on the third day \u2014 the hinge of all history', cat: 'bible', era: 'nt', ref: 'Matthew 26\u201328' },
        { year: 30, end: 30, label: 'Pentecost', desc: 'Holy Spirit poured out; the Church is born; 3,000 saved in one day', cat: 'bible', era: 'nt', ref: 'Acts 2' },
        { year: 34, end: 34, label: 'Paul\'s Conversion', desc: 'Persecutor becomes apostle on the Damascus Road', cat: 'bible', era: 'nt', ref: 'Acts 9' },
        { year: 44, end: 44, label: 'James Martyred', desc: 'First apostle killed; Herod Agrippa executes James son of Zebedee', cat: 'bible', era: 'nt', ref: 'Acts 12' },
        { year: 49, end: 49, label: 'Jerusalem Council', desc: 'Gentiles don\'t need circumcision \u2014 faith in Christ is sufficient', cat: 'bible', era: 'nt', ref: 'Acts 15' },
        { year: 50, end: 65, label: 'Paul\'s Letters', desc: 'Romans, Corinthians, Galatians, Ephesians, Philippians \u2014 theology of the Church', cat: 'bible', era: 'nt', ref: 'Pauline Epistles' },
        { year: 64, end: 64, label: 'Nero\'s Persecution', desc: 'Rome burns; Nero blames Christians; first imperial persecution', cat: 'world', era: 'nt' },
        { year: 70, end: 70, label: 'Temple Destroyed (AD 70)', desc: 'Rome destroys Herod\'s Temple; Jesus\u2019 prophecy fulfilled (Matthew 24)', cat: 'bible', era: 'nt', ref: 'Matthew 24; Luke 21' },
        { year: 73, end: 73, label: 'Masada Falls', desc: 'Last Jewish fortress falls to Rome; mass suicide of defenders', cat: 'world', era: 'nt' },
        { year: 90, end: 95, label: 'Revelation Written', desc: 'John receives the Apocalypse on Patmos \u2014 cosmic war, final victory', cat: 'bible', era: 'nt', ref: 'Revelation' },
        // Post-biblical
        { year: 100, end: 200, label: 'Church Fathers', desc: 'Polycarp, Ignatius, Clement, Justin Martyr defend and define the faith', cat: 'world', era: 'postbiblical' },
        { year: 313, end: 313, label: 'Edict of Milan', desc: 'Constantine legalizes Christianity; end of Roman persecution', cat: 'world', era: 'postbiblical' },
        { year: 325, end: 325, label: 'Council of Nicaea', desc: 'Nicene Creed affirms Christ\'s full deity against Arianism', cat: 'world', era: 'postbiblical' },
        { year: 382, end: 382, label: 'Biblical Canon Affirmed', desc: 'Councils of Rome, Hippo, Carthage affirm the 27 NT books', cat: 'world', era: 'postbiblical' },
        { year: 410, end: 410, label: 'Rome Falls', desc: 'Visigoths sack Rome; Augustine writes City of God', cat: 'world', era: 'postbiblical' },
        { year: 622, end: 622, label: 'Islam Founded', desc: 'Muhammad\'s Hijra to Medina; beginning of the Islamic calendar', cat: 'world', era: 'postbiblical' },
        { year: 1054, end: 1054, label: 'Great Schism', desc: 'East-West split: Roman Catholic and Eastern Orthodox churches separate', cat: 'world', era: 'postbiblical' },
        { year: 1517, end: 1517, label: 'Protestant Reformation', desc: 'Martin Luther\'s 95 Theses; sola scriptura, sola fide', cat: 'world', era: 'postbiblical' },
        { year: 1611, end: 1611, label: 'King James Bible', desc: 'KJV published \u2014 becomes the most influential English translation', cat: 'world', era: 'postbiblical' },
        { year: 1947, end: 1947, label: 'Dead Sea Scrolls Found', desc: 'Bedouin shepherds discover scrolls at Qumran \u2014 validates OT text', cat: 'world', era: 'postbiblical' },
        { year: 1948, end: 1948, label: 'Israel Reborn', desc: 'Modern State of Israel declared \u2014 2,500-year prophetic fulfillment', cat: 'world', era: 'postbiblical' }
    ];

    var TIMELINE_ERAS = {
        primeval:     { label: 'Primeval History', color: '#8b5cf6', range: [-4000, -2200] },
        patriarchs:   { label: 'Patriarchs', color: '#c9a84c', range: [-2200, -1600] },
        exodus:       { label: 'Exodus & Conquest', color: '#ef4444', range: [-1600, -1050] },
        kingdom:      { label: 'Kingdom Era', color: '#3b82f6', range: [-1050, -605] },
        exile:        { label: 'Exile & Return', color: '#f59e0b', range: [-605, -430] },
        secondtemple: { label: 'Second Temple', color: '#a78bfa', range: [-430, -5] },
        nt:           { label: 'New Testament', color: '#22c55e', range: [-5, 100] },
        postbiblical: { label: 'Post-Biblical', color: '#6b7280', range: [100, 2000] }
    };

    // ── Helpers ────────────────────────────────────────────
    var categories = MANIFEST.categories || [];
    var texts = MANIFEST.texts || [];

    function getTextDef(textId) {
        return texts.find(function(t) { return t.id === textId; });
    }

    function getCategoryDef(catId) {
        return categories.find(function(c) { return c.id === catId; });
    }

    function getTextEras(textId) {
        return MANIFEST.eras.filter(function(e) { return e.text === textId; });
    }

    function getTextInterlinear(textId) {
        // OT Hebrew (15 books)
        if (textId === 'genesis') return INTERLINEAR;
        if (textId === 'exodus') return INTERLINEAR_EXODUS;
        if (textId === 'leviticus') return INTERLINEAR_LEVITICUS;
        if (textId === 'numbers') return INTERLINEAR_NUMBERS;
        if (textId === 'deuteronomy') return INTERLINEAR_DEUTERONOMY;
        if (textId === 'joshua') return INTERLINEAR_JOSHUA;
        if (textId === 'judges') return INTERLINEAR_JUDGES;
        if (textId === 'ruth') return INTERLINEAR_RUTH;
        if (textId === '1samuel') return INTERLINEAR_1SAMUEL;
        if (textId === '2samuel') return INTERLINEAR_2SAMUEL;
        if (textId === '1kings') return INTERLINEAR_1KINGS;
        if (textId === '2kings') return INTERLINEAR_2KINGS;
        if (textId === 'psalms') return INTERLINEAR_PSALMS;
        if (textId === 'isaiah') return INTERLINEAR_ISAIAH;
        if (textId === 'daniel') return INTERLINEAR_DANIEL;
        // OT Hebrew (24 new books)
        if (textId === 'job') return INTERLINEAR_JOB;
        if (textId === 'proverbs') return INTERLINEAR_PROVERBS;
        if (textId === 'ecclesiastes') return INTERLINEAR_ECCLESIASTES;
        if (textId === 'songofsolomon') return INTERLINEAR_SONGOFSOLOMON;
        if (textId === 'jeremiah') return INTERLINEAR_JEREMIAH;
        if (textId === 'ezekiel') return INTERLINEAR_EZEKIEL;
        if (textId === 'lamentations') return INTERLINEAR_LAMENTATIONS;
        if (textId === '1chronicles') return INTERLINEAR_1CHRONICLES;
        if (textId === '2chronicles') return INTERLINEAR_2CHRONICLES;
        if (textId === 'ezra') return INTERLINEAR_EZRA;
        if (textId === 'nehemiah') return INTERLINEAR_NEHEMIAH;
        if (textId === 'esther') return INTERLINEAR_ESTHER;
        if (textId === 'hosea') return INTERLINEAR_HOSEA;
        if (textId === 'joel') return INTERLINEAR_JOEL;
        if (textId === 'amos') return INTERLINEAR_AMOS;
        if (textId === 'obadiah') return INTERLINEAR_OBADIAH;
        if (textId === 'jonah') return INTERLINEAR_JONAH;
        if (textId === 'micah') return INTERLINEAR_MICAH;
        if (textId === 'nahum') return INTERLINEAR_NAHUM;
        if (textId === 'habakkuk') return INTERLINEAR_HABAKKUK;
        if (textId === 'zephaniah') return INTERLINEAR_ZEPHANIAH;
        if (textId === 'haggai') return INTERLINEAR_HAGGAI;
        if (textId === 'zechariah') return INTERLINEAR_ZECHARIAH;
        if (textId === 'malachi') return INTERLINEAR_MALACHI;
        // NT Greek (27 books)
        if (textId === 'matthew')        return INTERLINEAR_NT_MATTHEW;
        if (textId === 'mark')           return INTERLINEAR_NT_MARK;
        if (textId === 'luke')           return INTERLINEAR_NT_LUKE;
        if (textId === 'john')           return INTERLINEAR_NT_JOHN;
        if (textId === 'acts')           return INTERLINEAR_NT_ACTS;
        if (textId === 'romans')         return INTERLINEAR_NT_ROMANS;
        if (textId === '1corinthians')   return INTERLINEAR_NT_1CORINTHIANS;
        if (textId === '2corinthians')   return INTERLINEAR_NT_2CORINTHIANS;
        if (textId === 'galatians')      return INTERLINEAR_NT_GALATIANS;
        if (textId === 'ephesians')      return INTERLINEAR_NT_EPHESIANS;
        if (textId === 'philippians')    return INTERLINEAR_NT_PHILIPPIANS;
        if (textId === 'colossians')     return INTERLINEAR_NT_COLOSSIANS;
        if (textId === '1thessalonians') return INTERLINEAR_NT_1THESSALONIANS;
        if (textId === '2thessalonians') return INTERLINEAR_NT_2THESSALONIANS;
        if (textId === '1timothy')       return INTERLINEAR_NT_1TIMOTHY;
        if (textId === '2timothy')       return INTERLINEAR_NT_2TIMOTHY;
        if (textId === 'titus')          return INTERLINEAR_NT_TITUS;
        if (textId === 'philemon')       return INTERLINEAR_NT_PHILEMON;
        if (textId === 'hebrews')        return INTERLINEAR_NT_HEBREWS;
        if (textId === 'james')          return INTERLINEAR_NT_JAMES;
        if (textId === '1peter')         return INTERLINEAR_NT_1PETER;
        if (textId === '2peter')         return INTERLINEAR_NT_2PETER;
        if (textId === '1john')          return INTERLINEAR_NT_1JOHN;
        if (textId === '2john')          return INTERLINEAR_NT_2JOHN;
        if (textId === '3john')          return INTERLINEAR_NT_3JOHN;
        if (textId === 'jude')           return INTERLINEAR_NT_JUDE;
        if (textId === 'revelation')     return INTERLINEAR_NT_REVELATION;
        return {};
    }

    // Returns true if the current text uses Greek (NT) vs Hebrew (OT)
    function isGreekText(textId) {
        var ntBooks = ['matthew','mark','luke','john','acts','romans','1corinthians',
            '2corinthians','galatians','ephesians','philippians','colossians',
            '1thessalonians','2thessalonians','1timothy','2timothy','titus','philemon',
            'hebrews','james','1peter','2peter','1john','2john','3john','jude','revelation'];
        return ntBooks.indexOf(textId) !== -1;
    }

    function getTextName(textId) {
        var t = getTextDef(textId);
        return t ? t.name : textId;
    }

    function getTextMaxChapter(textId) {
        var t = getTextDef(textId);
        return t ? (t.chapters || 0) : 0;
    }

    // Parse a scripture reference string → { textId, chapter } or null
    var BOOK_NAME_MAP = {
        'genesis':'genesis','gen':'genesis','ge':'genesis',
        'exodus':'exodus','exod':'exodus','ex':'exodus',
        'leviticus':'leviticus','lev':'leviticus',
        'numbers':'numbers','num':'numbers','nu':'numbers',
        'deuteronomy':'deuteronomy','deut':'deuteronomy','dt':'deuteronomy',
        'joshua':'joshua','josh':'joshua',
        'judges':'judges','judg':'judges','jdg':'judges',
        'ruth':'ruth','ru':'ruth',
        '1 samuel':'1samuel','1samuel':'1samuel','1 sam':'1samuel','1sam':'1samuel',
        '2 samuel':'2samuel','2samuel':'2samuel','2 sam':'2samuel','2sam':'2samuel',
        '1 kings':'1kings','1kings':'1kings','1 kgs':'1kings','1kgs':'1kings',
        '2 kings':'2kings','2kings':'2kings','2 kgs':'2kings','2kgs':'2kings',
        '1 chronicles':'1chronicles','1chronicles':'1chronicles','1 chr':'1chronicles','1chr':'1chronicles',
        '2 chronicles':'2chronicles','2chronicles':'2chronicles','2 chr':'2chronicles','2chr':'2chronicles',
        'ezra':'ezra',
        'nehemiah':'nehemiah','neh':'nehemiah',
        'esther':'esther','est':'esther','esth':'esther',
        'job':'job',
        'psalms':'psalms','psalm':'psalms','ps':'psalms','psa':'psalms',
        'proverbs':'proverbs','prov':'proverbs','pr':'proverbs',
        'ecclesiastes':'ecclesiastes','eccl':'ecclesiastes','ecc':'ecclesiastes',
        'song of solomon':'songofsolomon','song of songs':'songofsolomon','song':'songofsolomon','sos':'songofsolomon','cant':'songofsolomon',
        'isaiah':'isaiah','isa':'isaiah','is':'isaiah',
        'jeremiah':'jeremiah','jer':'jeremiah',
        'lamentations':'lamentations','lam':'lamentations',
        'ezekiel':'ezekiel','ezek':'ezekiel','eze':'ezekiel',
        'daniel':'daniel','dan':'daniel','da':'daniel',
        'hosea':'hosea','hos':'hosea',
        'joel':'joel',
        'amos':'amos','am':'amos',
        'obadiah':'obadiah','obad':'obadiah','ob':'obadiah',
        'jonah':'jonah','jon':'jonah',
        'micah':'micah','mic':'micah',
        'nahum':'nahum','nah':'nahum','na':'nahum',
        'habakkuk':'habakkuk','hab':'habakkuk',
        'zephaniah':'zephaniah','zeph':'zephaniah','zep':'zephaniah',
        'haggai':'haggai','hag':'haggai',
        'zechariah':'zechariah','zech':'zechariah','zec':'zechariah',
        'malachi':'malachi','mal':'malachi',
        'matthew':'matthew','matt':'matthew','mt':'matthew',
        'mark':'mark','mk':'mark','mr':'mark',
        'luke':'luke','lk':'luke','lu':'luke',
        'john':'john','jn':'john',
        'acts':'acts','ac':'acts',
        'romans':'romans','rom':'romans','ro':'romans',
        '1 corinthians':'1corinthians','1corinthians':'1corinthians','1 cor':'1corinthians','1cor':'1corinthians',
        '2 corinthians':'2corinthians','2corinthians':'2corinthians','2 cor':'2corinthians','2cor':'2corinthians',
        'galatians':'galatians','gal':'galatians',
        'ephesians':'ephesians','eph':'ephesians',
        'philippians':'philippians','phil':'philippians','php':'philippians',
        'colossians':'colossians','col':'colossians',
        '1 thessalonians':'1thessalonians','1thessalonians':'1thessalonians','1 thess':'1thessalonians','1thess':'1thessalonians',
        '2 thessalonians':'2thessalonians','2thessalonians':'2thessalonians','2 thess':'2thessalonians','2thess':'2thessalonians',
        '1 timothy':'1timothy','1timothy':'1timothy','1 tim':'1timothy','1tim':'1timothy',
        '2 timothy':'2timothy','2timothy':'2timothy','2 tim':'2timothy','2tim':'2timothy',
        'titus':'titus','tit':'titus',
        'philemon':'philemon','phlm':'philemon','phm':'philemon',
        'hebrews':'hebrews','heb':'hebrews',
        'james':'james','jas':'james','jam':'james',
        '1 peter':'1peter','1peter':'1peter','1 pet':'1peter','1pet':'1peter',
        '2 peter':'2peter','2peter':'2peter','2 pet':'2peter','2pet':'2peter',
        '1 john':'1john','1john':'1john','1 jn':'1john','1jn':'1john',
        '2 john':'2john','2john':'2john','2 jn':'2john','2jn':'2john',
        '3 john':'3john','3john':'3john','3 jn':'3john','3jn':'3john',
        'jude':'jude',
        'revelation':'revelation','rev':'revelation','re':'revelation'
    };

    function parseScriptureRef(refStr) {
        if (!refStr) return null;
        // Match patterns like "Genesis 1:28", "1 Samuel 3", "Psalm 82:1-8", "Song of Solomon 1:1"
        var m = refStr.match(/^(\d?\s*[A-Za-z][A-Za-z\s]+?)\s+(\d+)(?::[\d\-,\s]+)?$/);
        if (!m) return null;
        var bookName = m[1].trim().toLowerCase();
        var chapter = parseInt(m[2]);
        var textId = BOOK_NAME_MAP[bookName];
        if (!textId) return null;
        // Verify this text exists in manifest
        if (!getTextDef(textId)) return null;
        return { textId: textId, chapter: chapter };
    }

    function navigateToScriptureRef(refStr) {
        var parsed = parseScriptureRef(refStr);
        if (!parsed) return false;
        selectText(parsed.textId);
        // Navigate reading pane to the right chapter
        var il = getTextInterlinear(parsed.textId);
        if (Object.keys(il).length > 0 && parsed.chapter > 0) {
            renderInterlinear(parsed.chapter);
        }
        return true;
    }

    // Build a flat ordered list of all chapters for a text (for prev/next nav)
    function getFlatChapterList(textId) {
        var eras = getTextEras(textId);
        var list = [];
        eras.forEach(function(era) {
            var chapters = ERA_DATA[era.id] || [];
            chapters.forEach(function(ch) {
                list.push({ id: ch.id, ref: ch.ref || ch.title, title: ch.title, eraName: era.name, eraId: era.id });
            });
        });
        return list;
    }

    function getChapterPrefix(textId) {
        if (textId === 'exodus') return 'exod-';
        if (textId === 'genesis') return 'gen-';
        if (textId === 'leviticus') return 'lev-';
        if (textId === 'numbers') return 'num-';
        if (textId === 'deuteronomy') return 'deut-';
        if (textId === 'joshua') return 'josh-';
        if (textId === '1enoch') return '1en-';
        if (textId === 'jubilees') return 'jub-';
        if (textId === 'jasher') return 'jasher-';
        return textId.replace(/[^a-z0-9]/g, '') + '-';
    }

    function prefixToTextId(prefix) {
        var map = {
            gen: 'genesis', exod: 'exodus', lev: 'leviticus', num: 'numbers',
            deut: 'deuteronomy', josh: 'joshua', judg: 'judges', ruth: 'ruth',
            '1sam': '1samuel', '2sam': '2samuel', '1kgs': '1kings', '2kgs': '2kings',
            '1chr': '1chronicles', '2chr': '2chronicles', ezra: 'ezra', neh: 'nehemiah',
            esth: 'esther', job: 'job', ps: 'psalms', prov: 'proverbs',
            eccl: 'ecclesiastes', song: 'songofsolomon', isa: 'isaiah', jer: 'jeremiah',
            lam: 'lamentations', ezek: 'ezekiel', dan: 'daniel', hos: 'hosea',
            joel: 'joel', amos: 'amos', obad: 'obadiah', jonah: 'jonah',
            mic: 'micah', nah: 'nahum', hab: 'habakkuk', zeph: 'zephaniah',
            hag: 'haggai', zech: 'zechariah', mal: 'malachi',
            matt: 'matthew', mark: 'mark', luke: 'luke', john: 'john',
            acts: 'acts', rom: 'romans', '1cor': '1corinthians', '2cor': '2corinthians',
            gal: 'galatians', eph: 'ephesians', phil: 'philippians', col: 'colossians',
            '1thess': '1thessalonians', '2thess': '2thessalonians',
            '1tim': '1timothy', '2tim': '2timothy', tit: 'titus', phlm: 'philemon',
            heb: 'hebrews', jas: 'james', '1pet': '1peter', '2pet': '2peter',
            '1jn': '1john', '2jn': '2john', '3jn': '3john', jude: 'jude', rev: 'revelation'
        };
        return map[prefix] || prefix;
    }

    // ── DOM References ──────────────────────────────────────
    var mainContent = document.getElementById('mainContent');
    var sidebarNav = document.getElementById('sidebarNav');
    var searchInput = document.getElementById('searchInput');
    var searchResults = document.getElementById('searchResults');
    var xrefDrawer = document.getElementById('xrefDrawer');
    var xrefContent = document.getElementById('xrefContent');
    var glossaryOverlay = document.getElementById('glossaryOverlay');
    var glossaryList = document.getElementById('glossaryList');
    var glossarySearch = document.getElementById('glossarySearch');
    var resourcesOverlay = document.getElementById('resourcesOverlay');
    var resourcesList = document.getElementById('resourcesList');
    var resourcesSearch = document.getElementById('resourcesSearch');
    var resourcesFilters = document.getElementById('resourcesFilters');
    var activeResourceFilter = 'all';
    var bookmarksContainer = document.getElementById('bookmarksContainer');
    var sidebar = document.getElementById('sidebar');
    var sidebarToggle = document.getElementById('sidebarToggle');
    var sidebarBackdrop = document.getElementById('sidebarBackdrop');
    var readingPane = document.getElementById('readingPane');
    var readingPaneToggle = document.getElementById('readingPaneToggle');
    var readingPaneTitle = document.getElementById('readingPaneTitle');
    var readingPaneContent = document.getElementById('readingPaneContent');
    var readingPaneModeSelect = document.getElementById('readingPaneMode');
    var wordPopup = document.getElementById('wordPopup');

    // ── Initialize ──────────────────────────────────────────
    var _initDone = false;
    function init() {
        if (_initDone) return;
        _initDone = true;
        buildReverseXrefIndex();
        renderBookmarks();
        initReadingPane();
        initAccessibility();
        bindEvents();
        updateModeUI();
        initHallelujahChat();

        // Check hash — handle book landing, bible mode, or text view
        var hash = location.hash.slice(1);
        if (hash && hash !== 'library') {
            // Book landing page
            if (hash.startsWith('book/')) {
                showBookLanding(hash.slice(5));
                return;
            }
            // Bible reading mode — hash has 1-based chapter, convert to 0-based index
            if (hash.startsWith('read/')) {
                var parts = hash.split('/');
                var chNum = parseInt(parts[2]) || 1;
                showBibleMode(parts[1], chNum - 1);
                return;
            }
            var textFromHash = detectTextFromHash(hash);
            if (textFromHash) {
                selectText(textFromHash, true);
                requestAnimationFrame(function() { handleHash(); });
                return;
            }
        }

        // Always start on library landing page
        showLibrary();
    }

    function detectTextFromHash(hash) {
        if (hash.startsWith('hc-')) return 'heavenly_court';
        if (hash.startsWith('gen-') || hash.startsWith('era-creation') || hash.startsWith('era-eden') ||
            hash.startsWith('era-antediluvian') || hash.startsWith('era-flood') || hash.startsWith('era-babel') ||
            hash.startsWith('era-abraham') || hash.startsWith('era-isaac') || hash.startsWith('era-joseph')) {
            return 'genesis';
        }
        if (hash.startsWith('exod-') || hash.startsWith('era-bondage') || hash.startsWith('era-plague') ||
            hash.startsWith('era-exodus') || hash.startsWith('era-wilderness') || hash.startsWith('era-sinai') ||
            hash.startsWith('era-tabernacle') || hash.startsWith('era-golden')) {
            return 'exodus';
        }
        if (hash.startsWith('1en-')) return '1enoch';
        if (hash.startsWith('jub-')) return 'jubilees';
        if (hash.startsWith('jasher-')) return 'jasher';
        // Check era ids
        for (var i = 0; i < MANIFEST.eras.length; i++) {
            if (hash === 'era-' + MANIFEST.eras[i].id) {
                return MANIFEST.eras[i].text;
            }
        }
        return null;
    }

    // ═══════════════════════════════════════════════════════
    // LIBRARY VIEW
    // ═══════════════════════════════════════════════════════

    function showLibrary() {
        closeAllOverlays();
        libraryMode = true;
        currentText = null;
        document.body.classList.remove('text-selected', 'book-landing-view', 'bible-mode-active');
        document.body.classList.add('library-fullwidth');
        var oldBM = document.getElementById('bibleMode');
        if (oldBM) oldBM.remove();
        localStorage.removeItem('atl-current-text');
        location.hash = '';
        setReadingPane(false);
        buildLibrarySidebar();
        renderLibraryMain();
    }

    function showProphecyMatrix() {
        libraryMode = true;
        currentText = null;
        document.body.classList.remove('text-selected', 'library-fullwidth', 'book-landing-view', 'bible-mode-active');
        localStorage.removeItem('atl-current-text');
        location.hash = '#prophecy-matrix';
        setReadingPane(false);
        buildLibrarySidebar();

        var catNames = {
            'BIRTH': 'Birth &amp; Origin', 'MINISTRY': 'Life &amp; Ministry', 'PASSION': 'Suffering &amp; Death',
            'RESURRECT': 'Resurrection &amp; Ascension', 'KINGDOM': 'Reign &amp; Return', 'COVENANT': 'Covenant Promises',
            'TYPE': 'Types &amp; Shadows', 'JUDGMENT': 'Divine Judgment', 'RESTORE': 'Restoration &amp; New Creation',
            'COSMIC_CONFLICT': 'Cosmic Warfare &amp; Divine Council'
        };
        var catColors = {
            'BIRTH': '#c9a84c', 'MINISTRY': '#5b8dbf', 'PASSION': '#9a5044', 'RESURRECT': '#5a9a6a',
            'KINGDOM': '#7a5a96', 'COVENANT': '#4a8a6a', 'TYPE': '#a08046', 'JUDGMENT': '#a05a54',
            'RESTORE': '#4a8a96', 'COSMIC_CONFLICT': '#9b7ec8'
        };
        var statusLabels = {
            'FULFILLED_FIRST_COMING': 'Fulfilled', 'PARTIALLY_FULFILLED': 'Partially Fulfilled',
            'AWAITING_SECOND_COMING': 'Awaiting', 'DUAL': 'Dual Fulfillment'
        };
        var statusColors = {
            'FULFILLED_FIRST_COMING': '#5a9a6a', 'PARTIALLY_FULFILLED': '#b09050',
            'AWAITING_SECOND_COMING': '#5a7a9e', 'DUAL': '#7a5a96'
        };

        // Group by category
        var cats = {};
        var catOrder = ['BIRTH','COVENANT','TYPE','MINISTRY','PASSION','RESURRECT','KINGDOM','JUDGMENT','RESTORE','COSMIC_CONFLICT'];
        PROPHECY_MATRIX.forEach(function(p) {
            if (!cats[p.category]) cats[p.category] = [];
            cats[p.category].push(p);
        });

        // Stats
        var fulfilled = PROPHECY_MATRIX.filter(function(p) { return p.status === 'FULFILLED_FIRST_COMING'; }).length;
        var partial = PROPHECY_MATRIX.filter(function(p) { return p.status === 'PARTIALLY_FULFILLED'; }).length;
        var awaiting = PROPHECY_MATRIX.filter(function(p) { return p.status === 'AWAITING_SECOND_COMING'; }).length;

        var html = '<div class="prophecy-view">' +
            '<div class="prophecy-header">' +
            '<button class="prophecy-back" id="prophecyBack">&larr; Library</button>' +
            '<h1 class="prophecy-title">The Prophecy Matrix</h1>' +
            '<p class="prophecy-subtitle">Every major messianic prophecy, type, and shadow &mdash; traced from the Hebrew Bible to its New Testament fulfillment</p>' +
            '<div class="prophecy-stats">' +
            '<span class="prophecy-stat"><strong>' + PROPHECY_MATRIX.length + '</strong> Prophecies</span>' +
            '<span class="prophecy-stat" style="color:#5a9a6a"><strong>' + fulfilled + '</strong> Fulfilled</span>' +
            '<span class="prophecy-stat" style="color:#b09050"><strong>' + partial + '</strong> Partial</span>' +
            '<span class="prophecy-stat" style="color:#5a7a9e"><strong>' + awaiting + '</strong> Awaiting</span>' +
            '</div>' +
            '<button class="prophecy-tracker-link" id="prophecyTrackerLink">Per-Book Tracker &rarr;</button>' +
            '</div>';

        catOrder.forEach(function(catId) {
            var entries = cats[catId];
            if (!entries || entries.length === 0) return;
            var color = catColors[catId] || '#c9a84c';

            html += '<div class="prophecy-category">' +
                '<h2 class="prophecy-cat-title" style="color:' + color + '">' +
                (catNames[catId] || catId) + ' <span class="prophecy-cat-count">(' + entries.length + ')</span></h2>';

            entries.forEach(function(p) {
                var sc = statusColors[p.status] || '#9a968e';
                var sl = statusLabels[p.status] || p.status;

                html += '<div class="prophecy-entry">' +
                    '<div class="prophecy-entry-header">' +
                    '<span class="prophecy-id" style="color:' + color + '">' + p.id + '</span>' +
                    '<span class="prophecy-entry-title">' + p.title + '</span>' +
                    '<span class="prophecy-status" style="background:' + sc + '20;color:' + sc + ';border-color:' + sc + '40">' + sl + '</span>' +
                    '</div>' +
                    '<div class="prophecy-entry-body">' +
                    '<div class="prophecy-ref-row">' +
                    '<div class="prophecy-ref"><strong>OT:</strong> ' + p.ot_ref + '</div>' +
                    '<div class="prophecy-ref"><strong>NT:</strong> ' + p.nt_ref + '</div>' +
                    '</div>' +
                    '<div class="prophecy-ot-text">' + p.ot_text + '</div>';
                if (p.ot_hebrew) {
                    html += '<div class="prophecy-hebrew">' + p.ot_hebrew + '</div>';
                }
                html += '<div class="prophecy-fulfillment"><strong>Fulfillment:</strong> ' + p.fulfillment + '</div>' +
                    '</div></div>';
            });

            html += '</div>';
        });

        html += '</div>';
        mainContent.innerHTML = html;

        document.getElementById('prophecyBack').addEventListener('click', function() { showLibrary(); });

        // Link to per-book tracker
        var trackerLink = document.getElementById('prophecyTrackerLink');
        if (trackerLink) {
            trackerLink.addEventListener('click', function() { showProphecyTracker(); });
        }
    }

    // ── Per-Book Prophecy Tracker ───────────────────────────
    function showProphecyTracker(bookFilter) {
        libraryMode = true;
        currentText = null;
        document.body.classList.remove('text-selected', 'library-fullwidth', 'book-landing-view', 'bible-mode-active');
        localStorage.removeItem('atl-current-text');
        location.hash = '#prophecy-tracker';
        setReadingPane(false);
        buildLibrarySidebar();

        var books = Object.keys(BOOK_PROPHECIES);
        if (books.length === 0) {
            mainContent.innerHTML = '<div style="padding:2rem;color:var(--text-secondary)"><h2>Prophecy Tracker</h2><p>Prophecy tracker data is being compiled. Check back soon.</p></div>';
            return;
        }

        var statusIcons = {
            'FULFILLED': '\u2713', 'PARTIALLY_FULFILLED': '\u25D1', 'PENDING': '\u25CB',
            'DUAL_FULFILLMENT': '\u25C9', 'DISPUTED': '\u2047'
        };
        var statusColors = {
            'FULFILLED': '#5a9a6a', 'PARTIALLY_FULFILLED': '#b09050', 'PENDING': '#5a7a9e',
            'DUAL_FULFILLMENT': '#7a5a96', 'DISPUTED': '#a05a54'
        };
        var statusLabels = {
            'FULFILLED': 'Fulfilled', 'PARTIALLY_FULFILLED': 'Partially Fulfilled', 'PENDING': 'Pending',
            'DUAL_FULFILLMENT': 'Dual Fulfillment', 'DISPUTED': 'Disputed'
        };

        var html = '<div class="prophecy-view prophecy-tracker-view">' +
            '<div class="prophecy-header">' +
            '<button class="prophecy-back" id="trackerBack">&larr; Library</button>' +
            '<h1 class="prophecy-title">Prophecy Tracker</h1>' +
            '<p class="prophecy-subtitle">Per-book prophecy tracking with Christian and Orthodox Jewish interpretations &mdash; because understanding <em>why</em> people disagree is as important as knowing <em>what</em> they believe</p>' +
            '</div>';

        // Book selector tabs
        html += '<div class="tracker-book-tabs">';
        books.forEach(function(bookId) {
            var book = BOOK_PROPHECIES[bookId];
            var isActive = bookFilter === bookId || (!bookFilter && books.indexOf(bookId) === 0);
            html += '<button class="tracker-book-tab' + (isActive ? ' active' : '') + '" data-book="' + bookId + '">' +
                book.book_name + ' <span class="tracker-count">' + book.prophecy_count + '</span></button>';
        });
        html += '</div>';

        // Show selected book
        var activeBook = bookFilter || books[0];
        var bookData = BOOK_PROPHECIES[activeBook];
        if (bookData && bookData.prophecies) {
            html += '<div class="tracker-book-content">' +
                '<h2 class="tracker-book-title">' + bookData.book_name + ' &mdash; ' + bookData.prophecy_count + ' Prophecies</h2>';

            bookData.prophecies.forEach(function(p) {
                var cStatus = p.christian_view ? p.christian_view.status : 'PENDING';
                var jStatus = p.jewish_view ? p.jewish_view.status : 'PENDING';
                var cColor = statusColors[cStatus] || '#9a968e';
                var jColor = statusColors[jStatus] || '#9a968e';

                html += '<div class="tracker-prophecy">' +
                    '<div class="tracker-prophecy-header">' +
                    '<span class="tracker-id">' + p.id + '</span>' +
                    '<span class="tracker-ref">' + p.ref + '</span>' +
                    '<h3 class="tracker-title">' + p.title + '</h3>' +
                    '</div>';

                if (p.text_snippet) {
                    html += '<div class="tracker-snippet">&ldquo;' + p.text_snippet + '&rdquo;</div>';
                }

                html += '<div class="tracker-views">' +
                    '<div class="tracker-view tracker-christian">' +
                    '<div class="tracker-view-header">' +
                    '<span class="tracker-view-label">Christian View</span>' +
                    '<span class="tracker-status" style="color:' + cColor + '">' + (statusIcons[cStatus] || '') + ' ' + (statusLabels[cStatus] || cStatus) + '</span>' +
                    '</div>';
                if (p.christian_view) {
                    if (p.christian_view.fulfillment_ref) html += '<div class="tracker-fulfillment-ref"><strong>NT References:</strong> ' + p.christian_view.fulfillment_ref + '</div>';
                    if (p.christian_view.fulfillment_date) html += '<div class="tracker-date"><strong>Fulfilled:</strong> ' + p.christian_view.fulfillment_date + '</div>';
                    html += '<div class="tracker-explanation">' + p.christian_view.explanation + '</div>';
                }
                html += '</div>';

                html += '<div class="tracker-view tracker-jewish">' +
                    '<div class="tracker-view-header">' +
                    '<span class="tracker-view-label">Orthodox Jewish View</span>' +
                    '<span class="tracker-status" style="color:' + jColor + '">' + (statusIcons[jStatus] || '') + ' ' + (statusLabels[jStatus] || jStatus) + '</span>' +
                    '</div>';
                if (p.jewish_view) {
                    html += '<div class="tracker-explanation">' + p.jewish_view.explanation + '</div>';
                }
                html += '</div></div>';

                if (p.scholarly_notes) {
                    html += '<div class="tracker-scholarly"><strong>Scholarly Notes:</strong> ' + p.scholarly_notes + '</div>';
                }

                html += '</div>';
            });

            html += '</div>';
        }

        html += '</div>';
        mainContent.innerHTML = html;

        document.getElementById('trackerBack').addEventListener('click', function() { showLibrary(); });
        mainContent.addEventListener('click', function(e) {
            var tab = e.target.closest('.tracker-book-tab');
            if (tab) showProphecyTracker(tab.dataset.book);
        });
    }

    // ── Core Beliefs (Governance Architecture) ──────────────
    function showCoreBeliefs(topicId) {
        libraryMode = true;
        currentText = null;
        document.body.classList.remove('text-selected', 'library-fullwidth', 'book-landing-view', 'bible-mode-active');
        localStorage.removeItem('atl-current-text');
        location.hash = '#core-beliefs';
        setReadingPane(false);
        buildLibrarySidebar();

        // Handle both flat list [{id, category, ...}] and object {categories: [...]} formats
        var allTopics = [];
        if (Array.isArray(CORE_BELIEFS)) {
            allTopics = CORE_BELIEFS;
        } else if (CORE_BELIEFS.categories) {
            CORE_BELIEFS.categories.forEach(function(cat) { (cat.topics || []).forEach(function(t) { t._cat = cat.name; t._catColor = cat.color; allTopics.push(t); }); });
        }
        if (allTopics.length === 0) {
            mainContent.innerHTML = '<div style="padding:2rem;color:var(--text-secondary)"><h2>Governance Architecture</h2><p>Content is being compiled. Check back soon.</p></div>';
            return;
        }

        // Group by category
        var catOrder = [], catMap = {};
        var catColors = { 'ONTOLOGY':'#c9a84c','REBELLION':'#e05540','COVENANT':'#2ea043','ESCHATOLOGY':'#5a7a9e','SOTERIOLOGY':'#7a5a96','ECCLESIOLOGY':'#b09050','PNEUMATOLOGY':'#2d9a8f','ANTHROPOLOGY':'#d29922' };
        allTopics.forEach(function(t) {
            var ck = t.category || t._cat || 'General';
            if (!catMap[ck]) { catMap[ck] = []; catOrder.push(ck); }
            catMap[ck].push(t);
        });

        var html = '<div class="beliefs-view">' +
            '<div class="prophecy-header">' +
            '<button class="prophecy-back" id="beliefsBack">&larr; Library</button>' +
            '<h1 class="prophecy-title">' + (CORE_BELIEFS.title || 'The Governance Architecture of Scripture') + '</h1>' +
            '<p class="prophecy-subtitle">' + (CORE_BELIEFS.subtitle || 'Not systematic theology &mdash; the actual framework the biblical authors wrote within') + '</p>' +
            '</div>';

        catOrder.forEach(function(catKey, ci) {
            var catTopics = catMap[catKey];
            var color = catColors[catKey] || (catTopics[0] && catTopics[0]._catColor) || 'var(--gold)';
            var label = catKey.charAt(0).toUpperCase() + catKey.slice(1).toLowerCase();

            html += '<div class="beliefs-category">' +
                '<h2 class="beliefs-cat-title" style="border-left-color:' + color + '">' +
                '<span class="beliefs-cat-num">' + (ci + 1) + '</span>' +
                label + '</h2>';

            catTopics.forEach(function(topic) {
                var tid = topic.id || '';
                var isExpanded = tid === topicId;
                html += '<div class="beliefs-topic' + (isExpanded ? ' expanded' : '') + '" data-topic="' + tid + '">' +
                    '<div class="beliefs-topic-header" data-toggle-topic="' + tid + '">' +
                    '<span class="beliefs-topic-chevron">' + (isExpanded ? '\u25BC' : '\u25B6') + '</span>' +
                    '<span class="beliefs-topic-title">' + (topic.title || '') + '</span>' +
                    '</div>';

                html += '<div class="beliefs-topic-body" style="' + (isExpanded ? '' : 'display:none') + '">';
                if (topic.subtitle) html += '<p class="beliefs-summary" style="font-style:italic;color:var(--text-secondary)">' + topic.subtitle + '</p>';
                if (topic.council_relevance) html += '<div class="beliefs-view-box beliefs-governance"><div class="beliefs-view-label">Divine Council Relevance:</div><p>' + topic.council_relevance + '</p></div>';
                if (topic.summary) html += '<p class="beliefs-summary">' + topic.summary + '</p>';
                if (topic.systematic_view) html += '<div class="beliefs-view-box beliefs-systematic"><div class="beliefs-view-label">Systematic Theology Says:</div><p>' + topic.systematic_view + '</p></div>';
                if (topic.governance_view) html += '<div class="beliefs-view-box beliefs-governance"><div class="beliefs-view-label">The Governance Architecture Reveals:</div><p>' + topic.governance_view + '</p></div>';
                if (topic.key_texts) {
                    var kt = Array.isArray(topic.key_texts) ? topic.key_texts.join(', ') : topic.key_texts;
                    html += '<div class="beliefs-texts"><strong>Key Texts:</strong> ' + kt + '</div>';
                }
                if (topic.implications) html += '<div class="beliefs-implications"><strong>So What?</strong> ' + topic.implications + '</div>';
                html += '</div></div>';
            });

            html += '</div>';
        });

        html += '</div>';
        mainContent.innerHTML = html;

        document.getElementById('beliefsBack').addEventListener('click', function() { showLibrary(); });
        mainContent.addEventListener('click', function(e) {
            var header = e.target.closest('[data-toggle-topic]');
            if (header) {
                var topic = header.closest('.beliefs-topic');
                if (topic) {
                    var body = topic.querySelector('.beliefs-topic-body');
                    var chevron = topic.querySelector('.beliefs-topic-chevron');
                    var isOpen = body.style.display !== 'none';
                    body.style.display = isOpen ? 'none' : 'block';
                    chevron.textContent = isOpen ? '\u25B6' : '\u25BC';
                    topic.classList.toggle('expanded', !isOpen);
                }
            }
        });
    }

    function buildLibrarySidebar() {
        var html = '<div class="library-sidebar-header">' +
            '<button class="hub-back-btn" id="hubBackBtn" title="Home">' +
            '&#x2190; Home</button>' +
            '<div class="library-label">LIBRARY</div></div>';

        // Group texts by category
        categories.forEach(function(cat) {
            var catTexts = texts.filter(function(t) { return t.category === cat.id; });
            if (catTexts.length === 0) return;

            html += '<div class="library-category">' +
                '<div class="library-cat-label" style="color:' + cat.color + '">' + cat.name + '</div>';

            catTexts.forEach(function(t) {
                var eraCount = getTextEras(t.id).length;
                var hasContent = eraCount > 0;
                html += '<div class="library-text-link' + (hasContent ? '' : ' no-content') + '" data-text="' + t.id + '">' +
                    '<span class="library-dot" style="background:' + (t.color || cat.color) + '"></span>' +
                    '<span class="library-text-name">' + t.name + '</span>' +
                    (hasContent ? '' : '<span class="library-coming-soon">Soon</span>') +
                    '</div>';
            });

            html += '</div>';
        });

        // Special navigation items
        html += '<div class="library-category">' +
            '<div class="library-cat-label" style="color:var(--gold)">Tools</div>' +
            '<div class="library-text-link" data-action="prophecy-matrix">' +
            '<span class="library-dot" style="background:var(--gold)"></span>' +
            '<span class="library-text-name">Prophecy Matrix</span>' +
            '<span class="library-badge-count">' + (Array.isArray(PROPHECY_MATRIX) ? PROPHECY_MATRIX.length : '') + '</span>' +
            '</div>' +
            '<div class="library-text-link" data-action="prophecy-tracker">' +
            '<span class="library-dot" style="background:#5a7a9e"></span>' +
            '<span class="library-text-name">Prophecy Tracker</span>' +
            '<span class="library-badge-count">' + (Object.keys(BOOK_PROPHECIES).length || '') + '</span>' +
            '</div>' +
            '<div class="library-text-link" data-action="core-beliefs">' +
            '<span class="library-dot" style="background:#9b7ec8"></span>' +
            '<span class="library-text-name">Governance Architecture</span>' +
            '</div>' +
            '</div>';

        html += '<div class="library-sidebar-spacer"></div>';
        sidebarNav.innerHTML = html;
    }

    function renderStudyTrail(trailId) {
        var trail = STUDY_TRAILS.find(function(t) { return t.id === trailId; });
        if (!trail) return;

        var html = '<div class="breadcrumb-bar">' +
            '<span class="bc-link" data-action="go-library">Library</span>' +
            '<span class="bc-sep">\u203A</span>' +
            '<span class="bc-current">Study Trail: ' + trail.name + '</span></div>';

        html += '<div class="trail-detail" style="--trail-color:' + trail.color + '">' +
            '<div class="trail-detail-header">' +
            '<span class="trail-detail-icon">' + trail.icon + '</span>' +
            '<h1 class="trail-detail-title">' + trail.name + '</h1>' +
            '</div>' +
            '<p class="trail-detail-desc">' + trail.desc + '</p>' +
            '<div class="trail-steps">';

        trail.steps.forEach(function(step, i) {
            var textId = step.textId || (step.chId ? getTextForChapter(step.chId) : null);

            // Try to extract chapter number for inline scripture
            var chNum = '';
            if (step.chId) {
                var chMatch = step.chId.match(/(\d+)$/);
                if (chMatch) chNum = chMatch[1];
            } else if (step.label) {
                var lblMatch = step.label.match(/(\d+)/);
                if (lblMatch) chNum = lblMatch[1];
            }

            // Try to load inline scripture for this stop
            var scriptureHtml = '';
            if (textId && chNum) {
                var ilData = getTextInterlinear(textId);
                if (ilData && ilData[String(chNum)] && ilData[String(chNum)].verses) {
                    var verses = ilData[String(chNum)].verses;
                    scriptureHtml = '<div class="trail-stop-scripture">';
                    verses.forEach(function(v) {
                        var text = v.flow || '';
                        if (!text && v.words) {
                            var glosses = v.words.slice().reverse()
                                .map(function(w) { return w.g || ''; })
                                .filter(function(g) { return g && g !== 'properly' && g !== 'untranslatable'; });
                            text = glosses.join(' ').replace(/\s*\+\s*/g, ' ').replace(/\s{2,}/g, ' ').trim();
                        }
                        if (text) {
                            scriptureHtml += '<span class="scripture-verse"><sup class="scripture-verse-num">' +
                                v.num + '</sup>' + esc(text) + '</span> ';
                        }
                    });
                    scriptureHtml += '</div>';
                }
            }

            html += '<div class="trail-step' + (scriptureHtml ? ' has-scripture' : '') + '"' +
                ' data-nav-text="' + (textId || '') + '" data-nav-chapter="' + (step.chId || '') + '">' +
                '<div class="trail-step-number">' + (i + 1) + '</div>' +
                '<div class="trail-step-content">' +
                '<div class="trail-step-label">' + step.label + '</div>' +
                '<div class="trail-step-why">' + step.why + '</div>' +
                scriptureHtml +
                '<div class="trail-step-nav">' +
                '<span class="trail-step-go-link" data-nav-text="' + (textId || '') + '" data-nav-chapter="' + (step.chId || '') + '">' +
                '\u2192 Open full chapter</span>' +
                '</div>' +
                '</div>' +
                '</div>';
            if (i < trail.steps.length - 1) {
                html += '<div class="trail-connector"></div>';
            }
        });

        html += '</div></div>';
        mainContent.innerHTML = html;
    }

    function getTextForChapter(chId) {
        for (var i = 0; i < MANIFEST.eras.length; i++) {
            var chapters = ERA_DATA[MANIFEST.eras[i].id] || [];
            for (var j = 0; j < chapters.length; j++) {
                if (chapters[j].id === chId) return MANIFEST.eras[i].text;
            }
        }
        return null;
    }

    function renderLibraryMain() {
        var html = '<div class="library-hero">' +
            '<h1 class="library-title">Ancient Texts Library</h1>' +
            '<p class="library-subtitle">Divine council, cosmic geography &amp; covenant structure &mdash; the framework the biblical authors wrote within.</p>' +
            '</div>';

        // ─── TAB BAR ───
        var savedTab = localStorage.getItem('atl-library-tab') || 'featured';
        // Migration: old tab names → new defaults
        if (savedTab === 'trails' || savedTab === 'browse') savedTab = 'featured';
        html += '<div class="library-tab-bar">' +
            '<button class="library-tab' + (savedTab === 'featured' ? ' active' : '') + '" data-library-tab="featured">Featured</button>' +
            '<button class="library-tab' + (savedTab === 'ot' ? ' active' : '') + '" data-library-tab="ot">Old Testament</button>' +
            '<button class="library-tab' + (savedTab === 'nt' ? ' active' : '') + '" data-library-tab="nt">New Testament</button>' +
            '<button class="library-tab' + (savedTab === 'scrolls' ? ' active' : '') + '" data-library-tab="scrolls">Scrolls &amp; Studies</button>' +
            '<button class="library-tab' + (savedTab === 'map' ? ' active' : '') + '" data-library-tab="map">Map</button>' +
            '<button class="library-tab' + (savedTab === 'tools' ? ' active' : '') + '" data-library-tab="tools">Tools</button>' +
            '</div>';

        // ─── TAB: FEATURED ───
        html += '<div class="library-tab-content' + (savedTab === 'featured' ? ' active' : '') + '" data-tab-content="featured">';

        // Continue reading (if recent texts)
        var recentTexts = JSON.parse(localStorage.getItem('atl-recent-texts') || '[]');
        if (recentTexts.length > 0) {
            html += '<div class="library-recent-section">' +
                '<div class="library-recent-header">' +
                '<h2 class="library-recent-heading">Continue Reading</h2>' +
                '<button class="recent-clear-all" data-action="clear-recent">Clear All</button>' +
                '</div>' +
                '<div class="library-recent-grid">';
            recentTexts.slice(0, 4).forEach(function(rid) {
                var rt = getTextDef(rid);
                if (!rt) return;
                var rcat = getCategoryDef(rt.category);
                var rcounts = getTextReadCount(rid);
                html += '<div class="library-recent-card" data-text="' + rid + '" style="--card-color:' + (rt.color || rcat.color) + '">' +
                    '<button class="recent-remove-btn" data-remove-text="' + rid + '" title="Remove">&times;</button>' +
                    '<span class="canon-badge badge-small" style="background:' + rcat.color + '20;color:' + rcat.color + ';border-color:' + rcat.color + '40">' + rcat.badge + '</span>' +
                    '<h3 class="library-recent-title">' + rt.name + '</h3>' +
                    '<span class="library-recent-progress">' + rcounts.read + '/' + rcounts.total + ' read</span>' +
                    '</div>';
            });
            html += '</div></div>';
        }

        // ─── SHORT DIVES — punchy "wait, WHAT?" theological insights (FIRST after Continue Reading) ───
        var SHORT_DIVES = [
            {
                title: 'Jonah & the Fish God',
                text: 'jonah',
                insight: 'Jonah ran from Nineveh and ended up preached TO by a fish. But here\u2019s the wild part \u2014 Nineveh worshipped Dagon, a fish deity. Assyrian priests dressed in fish-skin costumes. So when a half-decomposed prophet walks out of the Mediterranean claiming the God of Israel sent him \u2014 via a giant fish \u2014 they didn\u2019t just listen. They were terrified. God used their own mythology to get their attention.',
                tag: 'OT \u2022 Jonah 1\u20134',
                color: '#4a8a9a'
            },
            {
                title: 'Why 72 Disciples?',
                text: 'luke',
                insight: 'Jesus didn\u2019t pick a random number. Genesis 10 lists exactly 70\u201372 nations scattered at Babel. Deuteronomy 32:8 says God assigned those nations to divine beings \u2014 sons of God. When Jesus sends 72 disciples, He\u2019s reclaiming the nations. Luke 10:18: \u201cI saw Satan fall like lightning.\u201d This wasn\u2019t metaphor. It was a military report.',
                tag: 'NT \u2022 Luke 10',
                color: '#5b8dbf'
            },
            {
                title: 'The Scapegoat Goes to Azazel',
                text: 'leviticus',
                insight: 'Leviticus 16 describes two goats on the Day of Atonement. One is sacrificed to Yahweh. The other is sent \u201cto Azazel\u201d in the wilderness. Most translations say \u201cscapegoat.\u201d But Azazel is a proper name \u2014 a Watcher from 1 Enoch who taught humanity forbidden knowledge. The sins are being sent BACK to their originator.',
                tag: 'OT \u2022 Leviticus 16',
                color: '#c9a84c'
            },
            {
                title: 'The High Priest Tore His Robes \u2014 Why?',
                text: 'mark',
                insight: 'At Jesus\u2019 trial, the high priest asks: \u201cAre you the Christ?\u201d Jesus answers with Daniel 7:13 \u2014 \u201cYou will see the Son of Man sitting at the right hand of Power, coming on the clouds.\u201d The priest tears his robes. Not because Jesus claimed to be Messiah \u2014 many had. He tore them because cloud-riding was EXCLUSIVELY a divine prerogative. Jesus claimed to be God.',
                tag: 'NT \u2022 Mark 14:62\u201363',
                color: '#b5564a'
            },
            {
                title: 'Psalm 82: God Fires the Gods',
                text: 'psalms',
                insight: '\u201cGod stands in the divine council; among the gods he holds judgment.\u201d This isn\u2019t metaphor. The Hebrew elohim here refers to real divine beings who were assigned to govern nations (Deut 32:8). They ruled corruptly. Verse 6\u20137: \u201cYou are gods \u2014 but you shall die like men.\u201d Jesus quotes this verse in John 10:34. He knew exactly what it meant.',
                tag: 'OT \u2022 Psalm 82',
                color: '#4a6a8a'
            },
            {
                title: 'Paul\u2019s Roman Triumph in Colossians',
                text: 'colossians',
                insight: 'Colossians 2:15 \u2014 \u201cHe disarmed the rulers and authorities and put them to open shame, triumphing over them.\u201d The Greek word thriambeuo means a Roman triumphal procession \u2014 a conquered general paraded through the streets in chains. Paul is saying the Cross wasn\u2019t a defeat. It was a victory parade. The powers didn\u2019t know they were walking into their own public humiliation.',
                tag: 'NT \u2022 Colossians 2:15',
                color: '#7a5a8a'
            },
            {
                title: 'Sheol Is Not Hell',
                text: 'sheol_resurrection',
                insight: 'Jacob expected to go to Sheol when he died (Gen 37:35). So did Job (Job 14:13). So did David (Ps 88:3). Sheol was the universal destination \u2014 righteous and wicked alike. It\u2019s not hell, not heaven, not purgatory. It\u2019s the waiting place. The Hebrew Bible never once describes the afterlife the way most churches teach it.',
                tag: 'THEMATIC \u2022 Hebrew Afterlife',
                color: '#7a6e8a'
            },
            {
                title: 'Apantesis: The Word That Kills the Rapture',
                text: 'prophetic_sequence',
                insight: '1 Thessalonians 4:17 \u2014 \u201ccaught up to MEET the Lord.\u201d That word \u201cmeet\u201d is apantesis in Greek. It\u2019s a technical term: when a dignitary approaches a city, citizens go OUT to meet him and escort him BACK in. Acts 28:15 uses the same word for believers meeting Paul on the road and walking him INTO Rome. We go up to escort Him down.',
                tag: 'THEMATIC \u2022 1 Thess 4:17',
                color: '#b85c3a'
            },
            {
                title: 'The Apostles Read a Different Bible',
                text: 'canon_septuagint',
                insight: 'The New Testament quotes the Old Testament roughly 300 times. About 80% of those quotations follow the Greek Septuagint \u2014 not the Hebrew Masoretic Text your English Bible translates from. The Masoretic was standardized 700\u20131000 AD. The Septuagint is 300 years older than Jesus. The Dead Sea Scrolls confirmed the Septuagint was right on key passages.',
                tag: 'THEMATIC \u2022 LXX vs MT',
                color: '#5a7a9a'
            },
            {
                title: 'The Minas Parable: Cities, Not Clouds',
                text: 'reward_bema',
                insight: 'In Luke 19, a servant turns one mina into ten. His reward? \u201cYou shall have authority over ten cities.\u201d Not a mansion. Not a cloud. Not a harp. Ten cities to govern in the new creation. The parable of the minas is the clearest picture in the NT of differentiated reward \u2014 your faithfulness now determines your authority then.',
                tag: 'THEMATIC \u2022 Luke 19:11\u201327',
                color: '#c9a84c'
            },
            {
                title: 'Because of the Angels',
                text: '1corinthians',
                insight: '1 Corinthians 11:10 \u2014 Paul says women should have exousia (\u201cauthority\u201d) on their head \u201cbecause of the angels.\u201d Dia tous angelous. Most commentaries skip this phrase. But in Second Temple context, angelic beings are present in worship assemblies (1QSa, 1QM). The Watchers of Genesis 6 violated the human\u2013divine boundary. According to 1 Enoch 6\u20138, they were drawn by human beauty. Paul\u2019s warning only makes sense if fallen angels are real, watching, and the boundary still matters.',
                tag: 'NT \u2022 1 Cor 11:10',
                color: '#5b8dbf'
            },
            {
                title: 'We Will Judge Angels',
                text: 'reward_bema',
                insight: 'Paul drops it casually in 1 Corinthians 6:3: \u201cDo you not know that we will judge angels?\u201d The Greek krinouomen means to render a judicial verdict. Which angels? Psalm 82 names them \u2014 the divine beings assigned to govern nations at Babel (Deut 32:8) who ruled corruptly. God pronounced the sentence: \u201cYou shall die like men.\u201d The bema judgment isn\u2019t just about crowns and rewards. Believers are being trained to fill vacated council seats in the divine administration.',
                tag: 'NT \u2022 1 Cor 6:3',
                color: '#7a5a8a'
            },
            {
                title: 'Christ Preached to Imprisoned Spirits',
                text: '1peter',
                insight: '1 Peter 3:19 \u2014 between the cross and resurrection, Christ \u201cwent and proclaimed to the spirits in prison.\u201d The Greek verb is kerysso \u2014 a herald\u2019s formal announcement, not euangelizo (gospel offer). These \u201cspirits\u201d are the divine beings from Genesis 6 who \u201cdid not obey\u201d in Noah\u2019s day. Jude 6 confirms angels are imprisoned. According to 1 Enoch 10\u201312, the Watchers were bound until judgment. Christ descended not to evangelize but to announce their defeat. A victory declaration, not a rescue mission.',
                tag: 'NT \u2022 1 Pet 3:19',
                color: '#4a6a8a'
            },
            {
                title: '\u201cLet Us Make\u201d \u2014 Who Was God Talking To?',
                text: 'genesis',
                insight: 'Genesis 1:26 \u2014 \u201cLet us make man in our image.\u201d The plural has puzzled interpreters for millennia. Trinitarian reading is anachronistic \u2014 no Israelite reader would have heard that. The Hebrew answer: the divine council. Na\u2019aseh (\u201clet us make\u201d) uses the same cohortative plural as 1 Kings 22:19\u201320 where Yahweh asks the heavenly host \u201cWho will go?\u201d and Isaiah 6:8 where God says \u201cWho will go for us?\u201d Creation was a council event. Humanity was made to join the family business.',
                tag: 'OT \u2022 Gen 1:26',
                color: '#4a8a6a'
            },
            {
                title: 'Ezekiel 28: Satan Was in Eden Before Adam',
                text: 'ezekiel',
                insight: 'Ezekiel 28:13\u201315 \u2014 addressed to the \u201cking of Tyre,\u201d but the details exceed any human ruler: \u201cYou were in Eden, the garden of God... you were an anointed guardian cherub (keruv mimshach hasokek)... you were blameless until unrighteousness was found in you.\u201d A throne-room guardian. Present in Eden. Blameless, then fallen. This is not metaphor \u2014 no Tyrian king walked among \u201cstones of fire.\u201d Satan fell BEFORE Genesis 3. The serpent in Eden was his second act, not his origin story.',
                tag: 'OT \u2022 Ezek 28:13\u201315',
                color: '#b5564a'
            },
            {
                title: 'Pentecost Was a Babel Reversal',
                text: 'acts',
                insight: 'At Babel: languages confused, nations scattered, peoples assigned to divine beings other than Yahweh (Deut 32:8\u20139). At Pentecost: \u201cdevout men from every nation under heaven\u201d hear in their own languages (Acts 2:5\u20136). Luke uses diamerizo (\u201cdistribute\u201d) for the tongues of fire \u2014 the same word the Septuagint uses in Deuteronomy 32:8 for God distributing the nations. This is not coincidence. Pentecost was the cosmic reclamation \u2014 the nations being called back to Yahweh through the Spirit that Babel\u2019s judgment had scattered.',
                tag: 'NT \u2022 Acts 2:1\u201311',
                color: '#5b8dbf'
            },
            {
                title: 'Daniel 10: Geopolitics Is Spiritual',
                text: 'daniel',
                insight: 'Gabriel tells Daniel the \u201cprince of Persia\u201d (sar malkhut paras) resisted him for 21 days until Michael \u2014 \u201cone of the chief princes\u201d \u2014 came to help (Dan 10:13). This is not a human king. No Persian emperor fights angels for three weeks. This is a divine being governing Persia \u2014 the same category as the sons of God assigned nations in Deuteronomy 32:8. Ephesians 6:12 confirms it: \u201cOur struggle is not against flesh and blood, but against the rulers, the authorities, the cosmic powers.\u201d Every empire has a spiritual administrator.',
                tag: 'OT \u2022 Dan 10:13\u201321',
                color: '#c9a84c'
            },
            {
                title: 'The Arm of the LORD Is a Person',
                text: 'isaiah',
                insight: 'Isaiah 53:1 asks: \u201cTo whom has the arm of the LORD (zeroa\u2019 YHWH) been revealed?\u201d Read Isaiah 51:9\u201352:10 \u2014 the \u201carm\u201d is addressed as a distinct agent, awakened, called to act, clothed with strength. By chapter 53, the Servant IS the arm. The Hebrew Bible contains divine agents \u2014 the Angel of YHWH, the Name, the Word, the Arm \u2014 who act with Yahweh\u2019s full authority yet are distinguishable from Him. This isn\u2019t Christian eisegesis. It\u2019s embedded in the Hebrew grammar.',
                tag: 'OT \u2022 Isa 53:1',
                color: '#b5564a'
            },
            {
                title: 'The Stoicheia: Cosmic Powers Behind Religion',
                text: 'galatians',
                insight: 'Paul warns against the stoicheia tou kosmou (Gal 4:3, 9; Col 2:8, 20) \u2014 usually translated \u201celementary principles.\u201d But in Greek cosmology, stoicheia referred to spiritual forces governing the cosmic order \u2014 the elemental powers that structured reality itself. Paul is not warning against kindergarten-level teaching. He\u2019s saying that all religious systems \u2014 Jewish Torah observance and pagan worship alike \u2014 operated within a cosmic framework of spiritual powers that Christ dismantled at the cross (Col 2:15). The stoicheia are dethroned.',
                tag: 'NT \u2022 Gal 4:3\u20139',
                color: '#7a5a8a'
            },
            {
                title: 'Isaiah 24:21 \u2014 The Hidden Cosmic Judgment',
                text: 'isaiah',
                insight: 'Isaiah 24:21 \u2014 \u201cOn that day the LORD will punish (yifqod) the host of heaven in heaven, and the kings of the earth on the earth.\u201d The verb paqad means a formal judicial visitation \u2014 an official review with consequences. The \u201chost of heaven\u201d (tseva\u2019 hamarom) is not stars. It\u2019s the divine beings. This verse has been in Isaiah for 2,700 years, plainly stating that God will judicially punish angelic powers. It is Psalm 82\u2019s death sentence being executed. Most readers skim it as apocalyptic poetry. It\u2019s a court date.',
                tag: 'OT \u2022 Isa 24:21',
                color: '#4a6a8a'
            },
            {
                title: 'Hesed: The Word That Holds the Bible Together',
                text: 'psalms',
                insight: 'Psalm 136 says it 26 times in a row: ki le\u2018olam hasdo \u2014 \u201cfor his hesed endures forever.\u201d Your Bible probably says \u201csteadfast love\u201d or \u201cloving-kindness,\u201d but neither captures it. Hesed is covenantal loyalty \u2014 the obligation a partner fulfills not because the law requires it, but because the relationship demands it. It\u2019s what Ruth showed Naomi. It\u2019s what Yahweh shows Israel even after they break every covenant. The cross is hesed made flesh. From Genesis 2 to Revelation 22, this is the thread that never breaks.',
                tag: 'OT \u2022 Psalm 136',
                color: '#4a8a6a'
            },
            {
                title: 'Why Your Bible Has 66 Books',
                text: 'canon_scripture',
                insight: 'The Council of Nicaea (AD 325) did not decide the biblical canon \u2014 it was called about the Trinity. The real story is messier and more interesting. Early churches used texts for centuries before any council spoke. The criteria were apostolicity, catholicity, and orthodoxy \u2014 and they were applied inconsistently. 1 Enoch was quoted as prophecy by Jude but excluded. Hebrews and Revelation nearly didn\u2019t make it. Jerome fought over the Deuterocanon. The canon is not a divine download \u2014 it\u2019s a historical process shaped by real arguments, real politics, and real faith.',
                tag: 'THEMATIC \u2022 Canon History',
                color: '#7a6a5a'
            },
            {
                title: 'Ekklesia Is Not \u201cChurch\u201d',
                text: 'ephesians',
                insight: 'Every Greek-speaking reader in the first century knew what ekklesia meant: a governing assembly \u2014 citizens called out to conduct public business. Athens had one. Rome had them. It was political, not religious. When Jesus says \u201cI will build my ekklesia\u201d (Matt 16:18), he\u2019s not founding a Sunday meeting. He\u2019s establishing a governing assembly with legal authority. Ephesians 3:10 makes it explicit: the ekklesia\u2019s assignment is to make God\u2019s wisdom known to the \u201crulers and authorities in the heavenly places.\u201d This is a cosmic mission statement, not a church bulletin.',
                tag: 'NT \u2022 Eph 3:10',
                color: '#5a6a8a'
            },
            {
                title: 'Leviticus Is Not Boring',
                text: 'leviticus',
                insight: 'Leviticus is the most Christologically dense book in the Torah \u2014 if you know what you\u2019re looking at. The entire sacrificial system is pattern language for the atonement: the substitutionary lamb, the priest who mediates, the blood that covers. Leviticus 16 alone contains the Day of Atonement, the two goats (one to Yahweh, one to Azazel), and the high priest entering the Most Holy Place \u2014 all of which Hebrews 9\u201310 unpacks as fulfilled in Christ. Paul didn\u2019t invent penal substitution. It was already in the system. Moses was writing Christology 1,400 years before the cross.',
                tag: 'OT \u2022 Leviticus 16',
                color: '#c9a84c'
            },
            {
                title: 'What Paul Actually Said About Women',
                text: 'romans',
                insight: 'Romans 16:1 introduces Phoebe as a diakonos \u2014 the same word Paul uses for himself and Apollos as church ministers (1 Cor 3:5). Verse 7 calls Junia \u201cprominent among the apostles\u201d \u2014 the Greek Iounian is a woman\u2019s name, and every church father before the 13th century read it that way. The 13th-century shift to \u201cJunias\u201d (a male name with zero ancient attestation) was not a linguistic finding. It was a theological preference reshaping the text. Read the Greek: Paul\u2019s closing chapter alone names ten women as coworkers, patrons, and leaders.',
                tag: 'NT \u2022 Romans 16:1\u20137',
                color: '#8a5a7a'
            },
            {
                title: 'The Servant Songs: 700 Years Early',
                text: 'isaiah',
                insight: 'Isaiah 52:13\u201353:12 \u2014 the fourth Servant Song \u2014 describes a figure who is \u201cpierced for our transgressions\u201d (mecholal mippesha\u2019enu), \u201ccrushed for our iniquities,\u201d and whose suffering brings shalom. The word mecholal is the passive participle of chalal \u2014 to be fatally pierced in battle. This is not poetic metaphor. The Servant bears the covenant curse (Deut 28) so others receive the covenant blessing. When Jesus reads Isaiah 61 in the synagogue at Nazareth (Luke 4:21) and says \u201ctoday this Scripture has been fulfilled,\u201d the audience knew exactly which Servant He was claiming to be.',
                tag: 'OT \u2022 Isa 52:13\u201353:12',
                color: '#b5564a'
            },
            {
                title: 'Dead Sea Scrolls: What Changed, What Held',
                text: 'dss_sectarian',
                insight: 'In 1947, a Bedouin shepherd found jars in Cave 1 at Qumran containing manuscripts 1,000 years older than our previously oldest Hebrew Bible. The Great Isaiah Scroll (1QIsa\u1d43) is the most important: it is Isaiah in full, dated to 125 BC \u2014 a century before Christ. On the foundational doctrines \u2014 God, covenant, sin, the Servant \u2014 the text is essentially identical to what we have. But on Deuteronomy 32:8, the DSS confirmed \u201csons of God\u201d over the Masoretic \u201csons of Israel.\u201d One phrase. Every territorial spirit, every divine council passage, every Psalm 82 argument rests on it.',
                tag: 'DSS \u2022 Multiple Texts',
                color: '#6a7a5a'
            },
            {
                title: 'Melchizedek: The Priest with No Origin Story',
                text: 'hebrews',
                insight: 'Genesis 14 introduces Melchizedek as priest-king of Salem \u2014 and then he disappears. No genealogy. No death. No origin. The author of Hebrews (7:3) says he is \u201cwithout father or mother or genealogy, having neither beginning of days nor end of life.\u201d In a world where priestly legitimacy depended entirely on ancestry, this is a theological thunderclap. The Melchizedek scroll from Qumran (11QMelch) identifies him as a heavenly figure who executes judgment. Jesus cannot be a Levitical priest \u2014 wrong tribe (Judah, Heb 7:13\u201314). So the argument of Hebrews turns on Psalm 110:4: there is a priesthood older than Aaron\u2019s, and it never ends.',
                tag: 'NT \u2022 Hebrews 7',
                color: '#7a6a9a'
            },
            {
                title: 'The Shema and the Trinity',
                text: 'deuteronomy',
                insight: 'Deuteronomy 6:4 \u2014 Shema Yisra\u2019el, YHWH Eloheinu, YHWH echad. \u201cHear O Israel, the LORD our God, the LORD is one.\u201d The word echad is a compound unity \u2014 the same word used for the \u201cone flesh\u201d of husband and wife (Gen 2:24) and the \u201cone cluster\u201d of grapes (Num 13:23). The word for absolute singularity is yachid \u2014 and the Shema does not use it. Jewish scholars today dispute whether echad vs yachid is decisive. But the New Testament writers, all of them Jewish, had no trouble reading the God of the Shema as Father, Son, and Spirit. They weren\u2019t departing from Moses. They were reading Moses more carefully.',
                tag: 'OT \u2022 Deut 6:4',
                color: '#5a7a8a'
            },
            {
                title: 'Habakkuk Filed a Lawsuit Against God',
                text: 'habakkuk',
                insight: 'Habakkuk 1:2 \u2014 \u201cO LORD, how long shall I cry for help, and you will not hear? Or cry to you \u2018Violence!\u2019 and you will not save?\u201d This is not a prayer. It\u2019s a riv \u2014 a formal covenant lawsuit. The prophet is using the same legal framework the prophets invoke against Israel: covenant prosecutor, list of charges, demand for a verdict. Habakkuk files it against Yahweh himself. And God answers \u2014 not with rebuke, but with a vision. Habakkuk 2:4 emerges from this legal argument: \u201cthe righteous shall live by his faith (emunah).\u201d Paul quotes it three times (Rom 1:17, Gal 3:11, Heb 10:38). The doctrine of justification by faith came out of a prophet\u2019s complaint.',
                tag: 'OT \u2022 Habakkuk 1\u20132',
                color: '#7a8a5a'
            }
        ];

        html += '<div class="short-dives-section short-dives-featured">' +
            '<h2 class="short-dives-heading">\u26A1 Short Dives</h2>' +
            '<p class="short-dives-subtitle">Two-minute reads that change how you see the text. One insight, everything shifts.</p>' +
            '<div class="short-dives-grid">';
        SHORT_DIVES.forEach(function(sd) {
            html += '<div class="short-dive-card" data-text="' + sd.text + '" style="--card-color:' + sd.color + '">' +
                '<span class="short-dive-tag">' + sd.tag + '</span>' +
                '<h3 class="short-dive-title">' + sd.title + '</h3>' +
                '<p class="short-dive-insight">' + sd.insight + '</p>' +
                '<span class="short-dive-cta">Read the full study \u2192</span>' +
                '</div>';
        });
        html += '</div></div>';

        // Featured Studies — curated deep dives with "why it matters" hooks
        var FEATURED_STUDIES = [
            { text: 'psalms', era: 'psalms_cosmic', title: 'The Cosmic Psalms', hook: 'Psalm 82 says God judged the gods. Psalm 29 dismantles Baal. Psalm 110 installs the Melchizedek king. Five psalms that reveal the invisible war behind Israel\u2019s worship.', badge: 'OT', color: '#4a8a6a' },
            { text: 'isaiah', era: 'isaiah_servant', title: 'Isaiah\u2019s Suffering Servant', hook: 'Four songs. Twelve Hebrew terms. One person who bears the covenant curse so the people receive the blessing. The Hebrew word mecholal means fatally pierced with a weapon \u2014 this is not metaphor.', badge: 'OT', color: '#b5564a' },
            { text: 'luke', era: 'luke_cosmic_war', title: 'The 72 and Babel Reversed', hook: 'Jesus sent exactly 72 disciples \u2014 the number of nations from Genesis 10. This was the Great Commission in miniature: reclaiming the nations assigned to corrupt divine beings at Babel.', badge: 'NT', color: '#7a8a9a' },
            { text: 'hebrews', era: 'hebrews_council', title: 'Hebrews: The Divine Council Letter', hook: 'The author quotes a Dead Sea Scrolls variant of Deuteronomy 32:43 that the standard Hebrew Bible doesn\u2019t contain. The entire argument rests on the Son being higher than the council.', badge: 'NT', color: '#c9a84c' },
            { text: 'heavenly_court', era: 'hc_cosmic_warfare', title: 'Know Your Enemy: The Four Powers', hook: 'Paul uses five distinct Greek terms for the supernatural hierarchy. They\u2019re not synonyms \u2014 archai, exousiai, dynameis, kyriotetes, thronoi. Colossians 2:15 describes a Roman triumphal procession.', badge: 'THEMATIC', color: '#c9a84c' },
            { text: 'micah', era: 'micah_riv', title: 'The Prophets as Prosecutors', hook: 'Micah 6 is the textbook covenant lawsuit. The mountains are summoned as witnesses. The verdict is three Hebrew words: mishpat, chesed, hatsnea halakh. This is how the prophets actually worked.', badge: 'OT', color: '#8a5a6a' },
            { text: 'zechariah', era: 'zech_council', title: 'Satan on Trial in Zechariah', hook: 'Zechariah 3 shows the divine council courtroom: Yahweh as judge, ha-satan as prosecutor, Joshua as defendant. The definite article ha- means this is a role, not yet a personal name.', badge: 'OT', color: '#4a6a6a' },
            { text: 'habakkuk', era: 'hab_theodicy', title: 'Habakkuk vs. God', hook: 'The prophet demands answers and God\u2019s response is worse than the question. Habakkuk 2:4 \u2014 \u201cthe righteous shall live by faith\u201d \u2014 is quoted three times in the NT. Each author draws something different.', badge: 'OT', color: '#5a7a5a' },
            { text: 'sheol_resurrection', era: 'nephesh_soul', title: 'You Don\u2019t HAVE a Soul', hook: 'Genesis 2:7 says Adam \u201cbecame a living nephesh.\u201d Not \u201creceived a soul\u201d \u2014 became one. The body-soul split you were taught is Plato, not Moses. The Bible\u2019s actual hope? Bodily resurrection on a renewed earth.', badge: 'THEMATIC', color: '#7a6e8a' },
            { text: 'prophetic_sequence', era: 'rapture_origins', title: 'The Rapture Has a Birthday', hook: 'No church father taught it. No creed confesses it. No council affirmed it. The pre-tribulation rapture was introduced by John Nelson Darby in the 1830s. For 1,800 years the church never saw this doctrine in the text.', badge: 'THEMATIC', color: '#b85c3a' },
            { text: 'canon_septuagint', era: 'lxx_mt', title: 'Two Bibles, One Verse', hook: 'Deuteronomy 32:8 \u2014 does God divide nations among \u201csons of God\u201d or \u201csons of Israel\u201d? The Dead Sea Scrolls settled it. The apostles quoted the Greek Bible 80% of the time. Your Old Testament has a history.', badge: 'THEMATIC', color: '#5a7a9a' },
            { text: 'reward_bema', era: 'minas_parable', title: 'Ten Minas, Ten Cities', hook: 'The faithful servant didn\u2019t get a gold star \u2014 he got ten cities to govern. Luke 19 isn\u2019t about heaven. It\u2019s about authority in the new creation. What you do now determines what you\u2019re entrusted with then.', badge: 'THEMATIC', color: '#c9a84c' }
        ];
        html += '<div class="featured-studies-section">' +
            '<h2 class="featured-studies-heading">Featured Studies</h2>' +
            '<p class="featured-studies-subtitle">Deep dives into the passages that change everything. Start anywhere.</p>' +
            '<div class="featured-studies-grid">';
        FEATURED_STUDIES.forEach(function(fs) {
            html += '<div class="featured-study-card" data-text="' + fs.text + '" data-era="' + fs.era + '" style="--card-color:' + fs.color + '">' +
                '<span class="canon-badge badge-small" style="background:' + fs.color + '20;color:' + fs.color + ';border-color:' + fs.color + '40">' + fs.badge + '</span>' +
                '<h3 class="featured-study-title">' + fs.title + '</h3>' +
                '<p class="featured-study-hook">' + fs.hook + '</p>' +
                '</div>';
        });
        html += '</div></div>';

        // Study Trails (moved into Featured tab)
        html += '<div class="study-trails-section">' +
            '<h2 class="study-trails-heading">Study Trails</h2>' +
            '<div class="study-trails-grid">';
        STUDY_TRAILS.forEach(function(trail) {
            html += '<div class="study-trail-card" data-trail="' + trail.id + '" style="--trail-color:' + trail.color + '">' +
                '<div class="trail-card-icon">' + trail.icon + '</div>' +
                '<h3 class="trail-card-name">' + trail.name + '</h3>' +
                '<p class="trail-card-desc">' + trail.desc + '</p>' +
                '<span class="trail-card-count">' + trail.steps.length + ' stops</span>' +
                '</div>';
        });
        html += '</div></div>';

        html += '</div>'; // end featured tab

        // ─── Category descriptions (shared) ───
        var CAT_DESCRIPTIONS = {
            ot: '39 books from Genesis to Malachi \u2014 every book found at Qumran except Esther',
            nt: '27 books from Matthew to Revelation \u2014 apostolic witness to the risen Christ',
            dss: 'Texts from the Qumran caves (250 BC \u2013 68 AD) \u2014 over 900 manuscripts from 11 caves',
            pseudepigrapha: 'Ancient texts referenced by biblical authors but not included in the Protestant canon',
            historical: 'First-century eyewitness accounts and church history tested against Scripture',
            thematic: 'Cross-text deep studies tracing major themes across the entire biblical narrative'
        };

        // ─── TAB: OLD TESTAMENT ───
        html += '<div class="library-tab-content' + (savedTab === 'ot' ? ' active' : '') + '" data-tab-content="ot">';
        var otCat = getCategoryDef('ot');
        var otTexts = texts.filter(function(t) { return t.category === 'ot'; });
        html += '<p class="library-section-desc" style="padding:0 0 1rem 0;margin:0">' + CAT_DESCRIPTIONS.ot + '</p>';
        html += '<div class="library-grid">';
        otTexts.forEach(function(t) {
            var eras = getTextEras(t.id);
            var chCount = t.chapter_count || 0;
            if (!chCount) {
                eras.forEach(function(era) {
                    var chapters = ERA_DATA[era.id] || [];
                    chapters.forEach(function(ch) { if (ch.type === 'chapter') chCount++; });
                });
            }
            var hasContent = eras.length > 0 || chCount > 0;
            var il = getTextInterlinear(t.id);
            var ilCount = Object.keys(il).length;
            var dssInfo = DSS_ATTESTATION[t.id];
            html += '<div class="library-card' + (hasContent ? '' : ' library-card-empty') + '" data-text="' + t.id + '" style="--card-color:' + (t.color || otCat.color) + '">' +
                '<div class="library-card-top">' +
                '<span class="canon-badge" style="background:' + otCat.color + '20;color:' + otCat.color + ';border-color:' + otCat.color + '40">' + otCat.badge + '</span>' +
                (dssInfo ? '<span class="dss-badge" title="Found at Qumran: ' + escAttr(dssInfo) + '">\uD83D\uDCDC DSS</span>' : '') +
                '</div>' +
                '<h3 class="library-card-title">' + t.name + '</h3>' +
                '<p class="library-card-desc">' + (t.description || '') + '</p>' +
                '<div class="library-card-stats">';
            if (hasContent) {
                html += '<span>' + chCount + ' chapters</span>';
                if (ilCount > 0) html += '<span>' + ilCount + ' interlinear</span>';
                html += '<span>' + eras.length + ' eras</span>';
            } else {
                html += '<span class="library-coming">Coming soon</span>';
            }
            html += '</div>';
            if (t.language) {
                html += '<div class="library-card-lang">' + t.language.charAt(0).toUpperCase() + t.language.slice(1) + '</div>';
            }
            html += '</div>';
        });
        html += '</div>';
        html += '</div>'; // end OT tab

        // ─── TAB: NEW TESTAMENT ───
        html += '<div class="library-tab-content' + (savedTab === 'nt' ? ' active' : '') + '" data-tab-content="nt">';
        var ntCat = getCategoryDef('nt');
        var ntTexts = texts.filter(function(t) { return t.category === 'nt'; });
        html += '<p class="library-section-desc" style="padding:0 0 1rem 0;margin:0">' + CAT_DESCRIPTIONS.nt + '</p>';
        html += '<div class="library-grid">';
        ntTexts.forEach(function(t) {
            var eras = getTextEras(t.id);
            var chCount = t.chapter_count || 0;
            if (!chCount) {
                eras.forEach(function(era) {
                    var chapters = ERA_DATA[era.id] || [];
                    chapters.forEach(function(ch) { if (ch.type === 'chapter') chCount++; });
                });
            }
            var hasContent = eras.length > 0 || chCount > 0;
            var il = getTextInterlinear(t.id);
            var ilCount = Object.keys(il).length;
            var dssInfo = DSS_ATTESTATION[t.id];
            html += '<div class="library-card' + (hasContent ? '' : ' library-card-empty') + '" data-text="' + t.id + '" style="--card-color:' + (t.color || ntCat.color) + '">' +
                '<div class="library-card-top">' +
                '<span class="canon-badge" style="background:' + ntCat.color + '20;color:' + ntCat.color + ';border-color:' + ntCat.color + '40">' + ntCat.badge + '</span>' +
                (dssInfo ? '<span class="dss-badge" title="Found at Qumran: ' + escAttr(dssInfo) + '">\uD83D\uDCDC DSS</span>' : '') +
                '</div>' +
                '<h3 class="library-card-title">' + t.name + '</h3>' +
                '<p class="library-card-desc">' + (t.description || '') + '</p>' +
                '<div class="library-card-stats">';
            if (hasContent) {
                html += '<span>' + chCount + ' chapters</span>';
                if (ilCount > 0) html += '<span>' + ilCount + ' interlinear</span>';
                html += '<span>' + eras.length + ' eras</span>';
            } else {
                html += '<span class="library-coming">Coming soon</span>';
            }
            html += '</div>';
            if (t.language) {
                html += '<div class="library-card-lang">' + t.language.charAt(0).toUpperCase() + t.language.slice(1) + '</div>';
            }
            html += '</div>';
        });
        html += '</div>';
        html += '</div>'; // end NT tab

        // ─── TAB: SCROLLS & STUDIES ───
        html += '<div class="library-tab-content' + (savedTab === 'scrolls' ? ' active' : '') + '" data-tab-content="scrolls">';
        var scrollsCats = ['dss', 'pseudepigrapha', 'historical', 'thematic'];
        scrollsCats.forEach(function(catId) {
            var cat = getCategoryDef(catId);
            if (!cat) return;
            var catTexts = texts.filter(function(t) { return t.category === catId; });
            var isEmpty = catTexts.length === 0;

            html += '<div class="library-section" data-category="' + catId + '">' +
                '<div class="library-section-header" data-toggle="section">' +
                '<h2 class="library-section-title" style="color:' + cat.color + '">' +
                '<span class="library-section-badge" style="background:' + cat.color + '18;color:' + cat.color + ';border:1px solid ' + cat.color + '40">' + cat.badge + '</span>' +
                cat.name +
                '</h2>' +
                (CAT_DESCRIPTIONS[catId] ? '<p class="library-section-desc">' + CAT_DESCRIPTIONS[catId] + '</p>' : '') +
                '<span class="library-section-meta">' +
                (isEmpty ? '' : '<span class="library-section-count">' + catTexts.length + ' text' + (catTexts.length !== 1 ? 's' : '') + '</span>') +
                '<span class="library-section-chevron">&rsaquo;</span>' +
                '</span>' +
                '</div>';

            if (isEmpty) {
                html += '<div class="library-section-body"><div class="library-section-empty">' +
                    '<span style="color:' + cat.color + '">Coming Soon</span>' +
                    '</div></div>';
            } else {
                html += '<div class="library-section-body"><div class="library-grid">';
                catTexts.forEach(function(t) {
                    var eras = getTextEras(t.id);
                    var chCount = t.chapter_count || 0;
                    if (!chCount) {
                        eras.forEach(function(era) {
                            var chapters = ERA_DATA[era.id] || [];
                            chapters.forEach(function(ch) { if (ch.type === 'chapter') chCount++; });
                        });
                    }
                    var hasContent = eras.length > 0 || chCount > 0;
                    var il = getTextInterlinear(t.id);
                    var ilCount = Object.keys(il).length;
                    var dssInfo = DSS_ATTESTATION[t.id];
                    html += '<div class="library-card' + (hasContent ? '' : ' library-card-empty') + '" data-text="' + t.id + '" style="--card-color:' + (t.color || cat.color) + '">' +
                        '<div class="library-card-top">' +
                        '<span class="canon-badge" style="background:' + cat.color + '20;color:' + cat.color + ';border-color:' + cat.color + '40">' + cat.badge + '</span>' +
                        (dssInfo ? '<span class="dss-badge" title="Found at Qumran: ' + escAttr(dssInfo) + '">\uD83D\uDCDC DSS</span>' : '') +
                        '</div>' +
                        '<h3 class="library-card-title">' + t.name + '</h3>' +
                        '<p class="library-card-desc">' + (t.description || '') + '</p>' +
                        '<div class="library-card-stats">';
                    if (hasContent) {
                        var isThematicCard = t.category === 'thematic';
                        html += '<span>' + chCount + (isThematicCard ? ' topics' : ' chapters') + '</span>';
                        if (ilCount > 0) html += '<span>' + ilCount + ' interlinear</span>';
                        html += '<span>' + eras.length + (isThematicCard ? ' parts' : ' eras') + '</span>';
                    } else {
                        html += '<span class="library-coming">Coming soon</span>';
                    }
                    html += '</div>';
                    if (t.language) {
                        html += '<div class="library-card-lang">' + t.language.charAt(0).toUpperCase() + t.language.slice(1) + '</div>';
                    }
                    html += '</div>';
                });
                html += '</div></div>';
            }

            html += '</div>';
        });
        html += '</div>'; // end scrolls tab

        // ─── TAB: MAP ───
        html += '<div class="library-tab-content' + (savedTab === 'map' ? ' active' : '') + '" data-tab-content="map">';
        html += '<div class="library-map-section" style="text-align:center;padding:3rem 1.5rem">' +
            '<div style="font-size:4rem;margin-bottom:1rem">\uD83C\uDF0D</div>' +
            '<h2 class="library-tools-heading" style="margin-bottom:0.5rem">Ancient Map</h2>' +
            '<p class="library-tools-subtitle" style="max-width:520px;margin:0 auto 0.75rem">Explore the biblical world &mdash; journey routes from Abraham to Paul, geographic context for every major event, and satellite imagery of ancient sites.</p>' +
            '<p style="color:var(--text-secondary);font-size:0.95rem;margin-bottom:2rem">24 journey routes &amp; 206 waypoints</p>' +
            '<button class="library-tool-card" id="library-launch-map" style="display:inline-flex;align-items:center;gap:0.5rem;padding:1rem 2.5rem;font-size:1.1rem;cursor:pointer;border:none;margin:0 auto">' +
            '<span class="tool-icon" style="font-size:1.3rem">\uD83C\uDF0D</span><span class="tool-label">Launch Ancient Map</span>' +
            '</button>' +
            '</div>';
        html += '</div>'; // end map tab

        // ─── TAB: TOOLS ───
        html += '<div class="library-tab-content' + (savedTab === 'tools' ? ' active' : '') + '" data-tab-content="tools">';
        html += '<div class="library-tools-section">' +
            '<h2 class="library-tools-heading">Study Tools</h2>' +
            '<p class="library-tools-subtitle">Resources for deeper study &mdash; timelines, original languages, and comparative analysis.</p>' +
            '<div class="library-tools-grid">' +
            '<div class="library-tool-card" data-action="show-timeline"><span class="tool-icon">\uD83D\uDCC5</span><span class="tool-label">Timeline</span><span class="tool-desc">Biblical events in chronological order</span></div>' +
            '<div class="library-tool-card" data-action="show-matrix"><span class="tool-icon">\u2696\uFE0F</span><span class="tool-label">Truth Matrix</span><span class="tool-desc">Compare 52+ religions to Scripture</span></div>' +
            '<div class="library-tool-card" data-action="show-prophecy"><span class="tool-icon">\uD83D\uDD2E</span><span class="tool-label">Prophecy</span><span class="tool-desc">Messianic prophecies &amp; fulfillment</span></div>' +
            '<div class="library-tool-card" data-action="show-hebrew"><span class="tool-icon">\u05D0</span><span class="tool-label">Learn Hebrew</span><span class="tool-desc">Hebrew alphabet &amp; key vocabulary</span></div>' +
            '<div class="library-tool-card" data-action="show-glossary"><span class="tool-icon">\uD83D\uDCD6</span><span class="tool-label">Glossary</span><span class="tool-desc">607 terms with original languages</span></div>' +
            '<div class="library-tool-card" data-action="show-patriarch-chart"><span class="tool-icon">\uD83D\uDCCA</span><span class="tool-label">Patriarch Ages</span><span class="tool-desc">Lifespans from Adam to Abraham</span></div>' +
            '</div></div>';
        html += '</div>'; // end tools tab

        mainContent.innerHTML = html;

        // ─── TAB SWITCHING ───
        mainContent.querySelectorAll('.library-tab').forEach(function(tab) {
            tab.addEventListener('click', function() {
                var target = this.getAttribute('data-library-tab');
                mainContent.querySelectorAll('.library-tab').forEach(function(t) { t.classList.remove('active'); });
                mainContent.querySelectorAll('.library-tab-content').forEach(function(tc) { tc.classList.remove('active'); });
                this.classList.add('active');
                var panel = mainContent.querySelector('[data-tab-content="' + target + '"]');
                if (panel) panel.classList.add('active');
                localStorage.setItem('atl-library-tab', target);
                mainContent.scrollTop = 0;
            });
        });

        // ─── FEATURED CARD CLICKS ───
        mainContent.querySelectorAll('.featured-study-card').forEach(function(card) {
            card.addEventListener('click', function() {
                var textId = this.getAttribute('data-text');
                if (textId) showBookLanding(textId);
            });
        });

        // ─── SHORT DIVE CARD CLICKS ───
        mainContent.querySelectorAll('.short-dive-card').forEach(function(card) {
            card.addEventListener('click', function() {
                var textId = this.getAttribute('data-text');
                if (textId) showBookLanding(textId);
            });
        });

        // ─── MAP LAUNCH BUTTON ───
        var mapLaunchBtn = document.getElementById('library-launch-map');
        if (mapLaunchBtn) {
            mapLaunchBtn.addEventListener('click', function() {
                openMap();
            });
        }

        // Stagger-animate library cards
        var cards = mainContent.querySelectorAll('.library-card');
        cards.forEach(function(card, i) {
            card.classList.add('stagger-in');
            card.style.animationDelay = (i * 30) + 'ms';
        });

        // Stagger-animate featured cards
        mainContent.querySelectorAll('.featured-study-card').forEach(function(card, i) {
            card.classList.add('stagger-in');
            card.style.animationDelay = (i * 50) + 'ms';
        });
    }

    // ═══════════════════════════════════════════════════════
    // BOOK LANDING PAGE
    // ═══════════════════════════════════════════════════════

    function showBookLanding(textId) {
        var textDef = getTextDef(textId);
        if (!textDef) return;

        closeAllOverlays();
        libraryMode = false;
        currentText = textId;

        // Track recent texts
        var recent = JSON.parse(localStorage.getItem('atl-recent-texts') || '[]');
        recent = recent.filter(function(id) { return id !== textId; });
        recent.unshift(textId);
        if (recent.length > 6) recent = recent.slice(0, 6);
        localStorage.setItem('atl-recent-texts', JSON.stringify(recent));

        // Set body state
        document.body.classList.remove('text-selected', 'library-fullwidth', 'bible-mode-active');
        document.body.classList.add('book-landing-view');

        // Remove Bible Mode element if present
        var oldBM = document.getElementById('bibleMode');
        if (oldBM) oldBM.remove();

        // Hide sidebar and reading pane on book landing
        setReadingPane(false);

        // Update hash
        location.hash = 'book/' + textId;

        // Render the landing page
        renderBookLanding(textId);
        window.scrollTo(0, 0);
    }

    function renderBookLanding(textId) {
        var textDef = getTextDef(textId);
        if (!textDef) return;

        var eras = getTextEras(textId);
        var cat = getCategoryDef(textDef.category);
        var catBadge = cat ? cat.badge : '';
        var catColor = cat ? cat.color : '#888';
        var catLabel = cat ? (cat.label || cat.name) : textDef.category;

        // Calculate stats — use manifest chapter_count as fallback for mobile
        var totalChapters = textDef.chapter_count || 0;
        var readCount = 0;
        if (!totalChapters) {
            eras.forEach(function(era) {
                var chapters = ERA_DATA[era.id] || [];
                totalChapters += chapters.length;
                chapters.forEach(function(ch) {
                    if (isChapterRead(ch.id)) readCount++;
                });
            });
        } else {
            eras.forEach(function(era) {
                var chapters = ERA_DATA[era.id] || [];
                chapters.forEach(function(ch) {
                    if (isChapterRead(ch.id)) readCount++;
                });
            });
        }
        var progressPct = totalChapters > 0 ? Math.round((readCount / totalChapters) * 100) : 0;

        var html = '<div class="book-landing">';

        // ─── HERO ───
        html += '<div class="book-hero">' +
            '<button class="book-back-btn" id="bookBackBtn">&larr; Library</button>' +
            '<div class="book-hero-badge" style="background:' + catColor + '20;color:' + catColor + ';border-color:' + catColor + '40">' +
            catBadge + ' ' + catLabel + '</div>' +
            '<h1 class="book-hero-title">' + esc(textDef.name) + '</h1>';

        if (textDef.description) {
            html += '<p class="book-hero-desc">' + esc(textDef.description) + '</p>';
        }

        var isThematic = textDef && textDef.category === 'thematic';
        if (isThematic) {
            html += '<div class="book-hero-stats">' +
                '<div class="book-hero-stat"><span class="book-stat-num">' + totalChapters + '</span><span class="book-stat-label">Topics</span></div>' +
                '<div class="book-hero-stat"><span class="book-stat-num">' + eras.length + '</span><span class="book-stat-label">Parts</span></div>' +
                '</div>';
        } else {
            html += '<div class="book-hero-stats">' +
                '<div class="book-hero-stat"><span class="book-stat-num">' + totalChapters + '</span><span class="book-stat-label">Chapters</span></div>' +
                '<div class="book-hero-stat"><span class="book-stat-num">' + eras.length + '</span><span class="book-stat-label">Eras</span></div>' +
                '<div class="book-hero-stat"><span class="book-stat-num">' + progressPct + '%</span><span class="book-stat-label">Read</span></div>' +
                '</div>';
        }
        var hasMapRoutes = (BOOK_TO_JOURNEYS[textId] || []).length > 0;
        html += '<div class="book-hero-actions">' +
            '<button class="book-start-btn" id="book-start-reading">' + (isThematic ? 'Start Study' : 'Start Reading') + '</button>' +
            (isThematic ? '' : '<button class="book-study-btn" id="book-study-mode">Study Mode</button>') +
            (hasMapRoutes ? '<button class="book-map-btn" id="book-map-btn">\ud83d\uddfa\ufe0f Map</button>' : '') +
            '</div>';

        html += '</div>'; // .book-hero

        // ─── CONTENT GRID ───
        html += '<div class="book-landing-grid">';

        // ─── LEFT COLUMN (main) ───
        html += '<div class="book-landing-main">';

        // Era / Chapter Outline
        html += '<div class="book-outline">' +
            '<h2 class="book-section-header">Chapter Outline</h2>';

        eras.forEach(function(era, eIdx) {
            var chapters = ERA_DATA[era.id] || [];
            var eraReadCount = 0;
            chapters.forEach(function(ch) { if (isChapterRead(ch.id)) eraReadCount++; });

            html += '<div class="book-outline-era" data-era-idx="' + eIdx + '">' +
                '<button class="book-outline-era-toggle" data-era-toggle="' + eIdx + '">' +
                '<span class="book-outline-era-icon">' + (era.icon || '') + '</span>' +
                '<span class="book-outline-era-color" style="background:' + (era.color || '#888') + '"></span>' +
                '<span class="book-outline-era-name">' + esc(era.name) + '</span>' +
                '<span class="book-outline-era-count">' + eraReadCount + '/' + chapters.length + '</span>' +
                '<span class="book-outline-chevron">&#9654;</span>' +
                '</button>' +
                '<div class="book-outline-chapters" data-era-chapters="' + eIdx + '" style="display:none">';

            chapters.forEach(function(ch, cIdx) {
                var chRead = isChapterRead(ch.id);
                var linkLabel = (ch.type === 'historical_insert' || ch.type === 'html_fragment') ? ch.title : ch.ref;
                html += '<div class="book-outline-ch" data-chapter-id="' + ch.id + '" data-chapter-idx="' + cIdx + '">' +
                    '<span class="book-outline-check">' + (chRead ? '\u2713' : '') + '</span>' +
                    '<span class="book-outline-ch-label">' + esc(linkLabel || ch.title || ch.id) + '</span>' +
                    '</div>';
            });

            html += '</div></div>'; // .book-outline-chapters, .book-outline-era
        });

        html += '</div>'; // .book-outline

        // Prophecy Summary
        if (BOOK_PROPHECIES[textId]) {
            var bookProphecies = BOOK_PROPHECIES[textId];
            html += '<div class="book-prophecy-summary">' +
                '<h2 class="book-section-header">Prophecy Summary</h2>';

            if (bookProphecies.prophecies && bookProphecies.prophecies.length > 0) {
                var shownProphecies = bookProphecies.prophecies.slice(0, 8);
                shownProphecies.forEach(function(p) {
                    var statusClass = p.status === 'fulfilled' ? 'prophecy-fulfilled' : (p.status === 'partially_fulfilled' ? 'prophecy-partial' : 'prophecy-pending');
                    html += '<div class="book-prophecy-card ' + statusClass + '">' +
                        '<div class="book-prophecy-ref">' + esc(p.reference || '') + '</div>' +
                        '<div class="book-prophecy-title">' + esc(p.title || p.theme || '') + '</div>' +
                        '<div class="book-prophecy-status">' + esc(p.status || 'unfulfilled').replace(/_/g, ' ') + '</div>' +
                        '</div>';
                });

                if (bookProphecies.prophecies.length > 8) {
                    html += '<div class="book-prophecy-more">+ ' + (bookProphecies.prophecies.length - 8) + ' more prophecies</div>';
                }
            }

            html += '</div>'; // .book-prophecy-summary
        }

        html += '</div>'; // .book-landing-main

        // ─── RIGHT COLUMN (aside) ───
        html += '<div class="book-landing-aside">';

        // Study Guide
        html += '<div class="book-study-guide">' +
            '<h3 class="book-section-header">Study Guide</h3>';

        var intro = TEXT_INTROS[textId];
        if (intro && intro.study_guide) {
            html += '<div class="book-study-guide-content">' + esc(intro.study_guide) + '</div>';
        } else {
            // Extract themes from eras
            html += '<div class="book-study-guide-content"><ul class="book-theme-list">';
            eras.forEach(function(era) {
                html += '<li class="book-theme-item">' +
                    '<span class="book-theme-dot" style="background:' + (era.color || '#888') + '"></span>' +
                    esc(era.name) +
                    '</li>';
            });
            html += '</ul></div>';
        }
        html += '</div>';

        // Map button — opens full map filtered to this book's journeys
        var bookJourneys = BOOK_TO_JOURNEYS[textId] || [];
        if (bookJourneys.length > 0) {
            var journeyCount = bookJourneys.length;
            html += '<div class="book-mini-map" id="bookMiniMap">' +
                '<button class="book-view-map-btn" id="bookViewMapBtn">' +
                '<span class="book-map-icon">\ud83d\uddfa\ufe0f</span>' +
                '<span class="book-map-label">View Journey Map</span>' +
                '<span class="book-map-count">' + journeyCount + ' route' + (journeyCount > 1 ? 's' : '') + '</span>' +
                '</button>' +
                '</div>';
        }

        // Related Books
        html += '<div class="book-related">' +
            '<h3 class="book-section-header">Related Books</h3>';

        var relatedCounts = {};
        eras.forEach(function(era) {
            var chapters = ERA_DATA[era.id] || [];
            chapters.forEach(function(ch) {
                if (!ch.cross_refs) return;
                ch.cross_refs.forEach(function(raw) {
                    var xr = normXref(raw);
                    var parsed = parseScriptureRef(xr.ref);
                    if (parsed && parsed.textId && parsed.textId !== textId) {
                        relatedCounts[parsed.textId] = (relatedCounts[parsed.textId] || 0) + 1;
                    }
                });
            });
        });

        var relatedBooks = Object.keys(relatedCounts).sort(function(a, b) {
            return relatedCounts[b] - relatedCounts[a];
        }).slice(0, 6);

        if (relatedBooks.length > 0) {
            relatedBooks.forEach(function(relId) {
                var relDef = getTextDef(relId);
                if (!relDef) return;
                var relCat = getCategoryDef(relDef.category);
                html += '<div class="book-related-card" data-text="' + relId + '">' +
                    '<span class="book-related-badge" style="background:' + (relCat ? relCat.color : '#888') + '20;color:' + (relCat ? relCat.color : '#888') + '">' +
                    (relCat ? relCat.badge : '') + '</span>' +
                    '<span class="book-related-name">' + esc(relDef.name) + '</span>' +
                    '<span class="book-related-count">' + relatedCounts[relId] + ' refs</span>' +
                    '</div>';
            });
        } else {
            html += '<div class="book-related-empty">No cross-references found</div>';
        }

        html += '</div>'; // .book-related

        // Scholarly Intro
        var introHtml = renderTextIntro(textId);
        if (introHtml) {
            html += '<div class="book-scholarly-intro">' +
                '<h3 class="book-section-header">Scholarly Introduction</h3>' +
                introHtml +
                '</div>';
        }

        html += '</div>'; // .book-landing-aside
        html += '</div>'; // .book-landing-grid
        html += '</div>'; // .book-landing

        mainContent.innerHTML = html;

        // ─── EVENT HANDLERS ───

        // Back to Library
        var backBtn = document.getElementById('bookBackBtn');
        if (backBtn) {
            backBtn.addEventListener('click', function() { showLibrary(); });
        }

        // Start Reading / Start Study
        var startBtn = document.getElementById('book-start-reading');
        if (startBtn) {
            var isThematicBtn = textDef && textDef.category === 'thematic';
            startBtn.addEventListener('click', function() {
                if (isThematicBtn) { selectText(textId); } else { showBibleMode(textId, 0); }
            });
        }

        // Study Mode (not shown for thematic texts)
        var studyBtn = document.getElementById('book-study-mode');
        if (studyBtn) {
            studyBtn.addEventListener('click', function() { selectText(textId); });
        }

        // View Map buttons (sidebar card + hero action)
        var mapBtn = document.getElementById('bookViewMapBtn');
        if (mapBtn) {
            mapBtn.addEventListener('click', function() { openMapForBook(textId); });
        }
        var mapHeroBtn = document.getElementById('book-map-btn');
        if (mapHeroBtn) {
            mapHeroBtn.addEventListener('click', function() { openMapForBook(textId); });
        }

        // Era toggles — expand/collapse
        mainContent.querySelectorAll('.book-outline-era-toggle').forEach(function(toggle) {
            toggle.addEventListener('click', function() {
                var idx = this.getAttribute('data-era-toggle');
                var chaptersDiv = mainContent.querySelector('[data-era-chapters="' + idx + '"]');
                if (!chaptersDiv) return;
                var isOpen = chaptersDiv.style.display !== 'none';
                chaptersDiv.style.display = isOpen ? 'none' : 'block';
                var chevron = this.querySelector('.book-outline-chevron');
                if (chevron) chevron.style.transform = isOpen ? '' : 'rotate(90deg)';
            });
        });

        // Chapter links
        mainContent.querySelectorAll('.book-outline-ch').forEach(function(chEl) {
            chEl.addEventListener('click', function() {
                var chIdx = parseInt(this.getAttribute('data-chapter-idx'), 10);
                showBibleMode(textId, chIdx);
            });
        });

        // Related book cards
        mainContent.querySelectorAll('.book-related-card').forEach(function(card) {
            card.addEventListener('click', function() {
                var relTextId = this.getAttribute('data-text');
                if (relTextId) showBookLanding(relTextId);
            });
        });

        // Intro collapse toggle (if rendered)
        var introCollapseBtn = document.getElementById('introCollapseBtn');
        if (introCollapseBtn) {
            introCollapseBtn.addEventListener('click', function() {
                var panel = mainContent.querySelector('.text-intro-panel');
                if (panel) {
                    var collapsed = panel.classList.toggle('intro-collapsed');
                    localStorage.setItem('atl-intro-collapsed', collapsed ? '1' : '0');
                    this.textContent = collapsed ? '\u25BC' : '\u25B2';
                }
            });
        }
    }

    // ═══════════════════════════════════════════════════════
    // BIBLE MODE (full-screen reading experience)
    // ═══════════════════════════════════════════════════════

    var currentBibleChapter = 0;  // current chapter NUMBER (1-based)
    var bibleTotalChapters = 0;   // total chapters for current book

    function getBibleChapterCount(textId) {
        // Try manifest text definition first
        var textDef = getTextDef(textId);
        if (textDef && textDef.chapters && typeof textDef.chapters === 'number') {
            return textDef.chapters;
        }

        // Try interlinear data — count keys
        var ilData = getTextInterlinear(textId);
        if (ilData && typeof ilData === 'object') {
            var ilKeys = Object.keys(ilData).filter(function(k) { return /^\d+$/.test(k); });
            if (ilKeys.length > 0) return ilKeys.length;
        }

        // Try standalone flow data
        if (STANDALONE_FLOW[textId]) {
            var flowKeys = Object.keys(STANDALONE_FLOW[textId]).filter(function(k) { return /^\d+$/.test(k); });
            if (flowKeys.length > 0) return flowKeys.length;
        }

        // Fallback: count chapters across eras
        var eras = getTextEras(textId);
        var count = 0;
        eras.forEach(function(era) {
            var chapters = ERA_DATA[era.id] || [];
            count += chapters.length;
        });
        return count || 1;
    }

    function getBibleChapterContent(textId, chapterNum) {
        var verses = [];
        var chKey = String(chapterNum);

        // 1. Try interlinear data (merged flow)
        var ilData = getTextInterlinear(textId);
        if (ilData && typeof ilData === 'object' && ilData[chKey] && ilData[chKey].verses && ilData[chKey].verses.length > 0) {
            ilData[chKey].verses.forEach(function(verse) {
                var text = '';
                if (verse.flow) {
                    text = verse.flow;
                } else if (verse.words) {
                    var glosses = verse.words.slice().reverse()
                        .map(function(w) { return w.g || ''; })
                        .filter(function(g) { return g && g !== 'properly' && g !== 'untranslatable'; });
                    text = glosses.join(' ').replace(/\s*\+\s*/g, ' ').replace(/\s{2,}/g, ' ').trim();
                }
                if (text) {
                    verses.push({ num: verse.num, text: text, note: verse.note || null });
                }
            });
            if (verses.length > 0) return verses;
        }

        // 2. Try standalone flow
        if (STANDALONE_FLOW[textId] && STANDALONE_FLOW[textId][chKey]) {
            var chFlow = STANDALONE_FLOW[textId][chKey];
            var notesData = STANDALONE_NOTES[textId] || {};
            var chNotes = notesData[chKey] || {};
            var verseNums = Object.keys(chFlow).map(Number).sort(function(a, b) { return a - b; });
            verseNums.forEach(function(vNum) {
                verses.push({
                    num: vNum,
                    text: chFlow[String(vNum)],
                    note: chNotes[String(vNum)] || null
                });
            });
            if (verses.length > 0) return verses;
        }

        // 3. Fallback
        return [];
    }

    function showBibleMode(textId, chapterIndex) {
        var textDef = getTextDef(textId);
        if (!textDef) return;

        currentText = textId;
        currentILBook = textId;

        document.body.classList.remove('text-selected', 'library-fullwidth', 'book-landing-view');
        document.body.classList.add('bible-mode-active');

        setReadingPane(false);

        renderBibleMode(textId, chapterIndex || 0);
    }

    function renderBibleMode(textId, chapterIndex) {
        var textDef = getTextDef(textId);
        if (!textDef) return;

        bibleTotalChapters = getBibleChapterCount(textId);
        currentBibleChapter = Math.max(1, Math.min(chapterIndex + 1, bibleTotalChapters));

        location.hash = 'read/' + textId + '/' + currentBibleChapter;

        var html = '<div class="bible-mode" id="bibleMode">';

        // ─── TOP BAR ───
        html += '<div class="bible-top-bar">' +
            '<button class="bible-back-btn" id="bibleBack">&larr;</button>' +
            '<span class="bible-book-title">' + esc(textDef.name) + ' ' + currentBibleChapter + '</span>' +
            '<button class="bible-settings-btn" id="bibleSettings">&#9881;</button>' +
            '</div>' +
            '<div class="bible-progress-bar" id="bibleProgressBar"></div>';

        // ─── READER ───
        html += '<div class="bible-reader" id="bibleReader">' +
            '<div class="bible-chapter-content" id="bibleContent">';

        // Original language hint (show once per session)
        var origLang = textDef.category === 'nt' ? 'Greek' : 'Hebrew';
        var langHintKey = 'atl-lang-hint-dismissed';
        if (!sessionStorage.getItem(langHintKey)) {
            html += '<div class="bible-lang-hint" id="bibleLangHint">' +
                '<span class="bible-lang-hint-text">This English text is translated from the original <strong>' + origLang + '</strong>. ' +
                'Tap <strong>\ud83d\udd24 ' + origLang + '</strong> below to see every word in the original language with grammar, morphology, and Strong\'s numbers.</span>' +
                '<button class="bible-lang-hint-close" id="bibleLangHintClose">&times;</button>' +
                '</div>';
        }

        var verses = getBibleChapterContent(textId, currentBibleChapter);
        if (verses.length > 0) {
            verses.forEach(function(v) {
                html += '<span class="bible-verse">' +
                    '<sup class="bible-verse-num">' + v.num + '</sup> ' +
                    '<span class="bible-verse-text">' + esc(v.text) + '</span>' +
                    '</span> ';
                if (v.note) {
                    html += '<span class="bible-verse-note" data-note="' + escAttr(v.note) + '">\uD83D\uDCA1</span> ';
                }
            });
        } else {
            html += '<div class="bible-no-content">No scripture text available for ' + esc(textDef.name) + ' chapter ' + currentBibleChapter + '.</div>';
        }

        html += '</div></div>'; // #bibleContent, #bibleReader

        // ─── BOTTOM BAR ───
        html += '<div class="bible-bottom-bar">' +
            '<button class="bible-nav-btn" id="biblePrev" data-delta="-1"' + (currentBibleChapter <= 1 ? ' disabled' : '') + '>' +
            '<span class="bible-btn-icon">&larr;</span>' +
            '<span class="bible-btn-label">Prev</span>' +
            '</button>' +
            '<button class="bible-chapter-btn" id="bibleChapterBtn">' +
            '<span class="bible-btn-icon">Ch</span>' +
            '<span class="bible-btn-label">' + currentBibleChapter + '</span>' +
            '</button>' +
            '<button class="bible-notes-btn" id="bibleNotesBtn">' +
            '<span class="bible-btn-icon">&#128221;</span>' +
            '<span class="bible-btn-label">Notes</span>' +
            '</button>' +
            '<button class="bible-xref-btn" id="bibleXrefBtn">' +
            '<span class="bible-btn-icon">&#128279;</span>' +
            '<span class="bible-btn-label">Refs</span>' +
            '</button>' +
            '<button class="bible-il-btn" id="bibleILBtn">' +
            '<span class="bible-btn-icon">\ud83d\udd24</span>' +
            '<span class="bible-btn-label">' + (textDef.category === 'nt' ? 'Greek' : 'Hebrew') + '</span>' +
            '</button>' +
            ((BOOK_TO_JOURNEYS[textId] || []).length > 0 ?
            '<button class="bible-map-btn" id="bibleMapBtn">' +
            '<span class="bible-btn-icon">\ud83d\uddfa\ufe0f</span>' +
            '<span class="bible-btn-label">Map</span>' +
            '</button>' : '') +
            '<button class="bible-nav-btn" id="bibleNext" data-delta="1"' + (currentBibleChapter >= bibleTotalChapters ? ' disabled' : '') + '>' +
            '<span class="bible-btn-icon">&rarr;</span>' +
            '<span class="bible-btn-label">Next</span>' +
            '</button>' +
            '</div>';

        // ─── DRAWER ───
        html += '<div class="bible-drawer" id="bibleDrawer">' +
            '<div class="bible-drawer-handle"></div>' +
            '<div class="bible-drawer-tabs">' +
            '<button class="bible-drawer-tab active" data-tab="study">Study</button>' +
            '<button class="bible-drawer-tab" data-tab="xrefs">Cross-Refs</button>' +
            '<button class="bible-drawer-tab" data-tab="council">Council</button>' +
            '<button class="bible-drawer-tab" data-tab="settings">Settings</button>' +
            '</div>' +
            '<div class="bible-drawer-content" id="bibleDrawerContent">' +
            renderBibleDrawerTab(textId, currentBibleChapter, 'study') +
            '</div>' +
            '</div>';

        // ─── CHAPTER PICKER MODAL ───
        html += '<div class="bible-chapter-picker" id="bibleChapterPicker" style="display:none">' +
            '<div class="bible-picker-overlay"></div>' +
            '<div class="bible-picker-content">' +
            '<h3 class="bible-picker-title">' + esc(textDef.name) + '</h3>' +
            '<div class="bible-picker-grid" id="biblePickerGrid">';

        for (var i = 1; i <= bibleTotalChapters; i++) {
            html += '<button class="bible-picker-num' + (i === currentBibleChapter ? ' active' : '') + '" data-ch="' + i + '">' + i + '</button>';
        }

        html += '</div></div></div>'; // grid, content, picker

        html += '</div>'; // .bible-mode

        // Remove any previous bible mode element
        var oldBM = document.getElementById('bibleMode');
        if (oldBM) oldBM.remove();

        // Create on document.body (not inside app-container which gets hidden)
        var bmContainer = document.createElement('div');
        bmContainer.innerHTML = html;
        document.body.appendChild(bmContainer.firstChild);

        // ─── WIRE EVENT HANDLERS ───
        var bibleRoot = document.getElementById('bibleMode');

        // Back button
        var backBtn = document.getElementById('bibleBack');
        if (backBtn) {
            backBtn.addEventListener('click', function() { showBookLanding(textId); });
        }

        // Settings button — toggle drawer to settings tab
        var settingsBtn = document.getElementById('bibleSettings');
        if (settingsBtn) {
            settingsBtn.addEventListener('click', function() {
                var drawer = document.getElementById('bibleDrawer');
                if (drawer) {
                    drawer.classList.toggle('open');
                    if (drawer.classList.contains('open')) {
                        switchBibleDrawerTab(textId, currentBibleChapter, 'settings');
                    }
                }
            });
        }

        // Language hint dismiss
        var langHintClose = document.getElementById('bibleLangHintClose');
        if (langHintClose) {
            langHintClose.addEventListener('click', function() {
                var hint = document.getElementById('bibleLangHint');
                if (hint) hint.style.display = 'none';
                sessionStorage.setItem('atl-lang-hint-dismissed', '1');
            });
        }

        // Reading progress bar
        var bibleReader = document.getElementById('bibleReader');
        var progressBar = document.getElementById('bibleProgressBar');
        if (bibleReader && progressBar) {
            bibleReader.addEventListener('scroll', function() {
                var scrollTop = bibleReader.scrollTop;
                var scrollHeight = bibleReader.scrollHeight - bibleReader.clientHeight;
                var pct = scrollHeight > 0 ? Math.min(100, (scrollTop / scrollHeight) * 100) : 0;
                progressBar.style.width = pct + '%';
            });
        }

        // Verse tap highlight
        bibleRoot.querySelectorAll('.bible-verse').forEach(function(verse) {
            verse.addEventListener('click', function(e) {
                // Don't highlight if tapping on note icon
                if (e.target.classList.contains('bible-verse-note')) return;
                this.classList.toggle('verse-highlighted');
            });
        });

        // Study note tap — show inline popup
        bibleRoot.querySelectorAll('.bible-verse-note').forEach(function(noteEl) {
            noteEl.addEventListener('click', function(e) {
                e.stopPropagation();
                // Remove any existing popup
                var existing = bibleRoot.querySelector('.bible-note-popup');
                if (existing) existing.remove();
                // Create popup
                var popup = document.createElement('div');
                popup.className = 'bible-note-popup';
                popup.innerHTML = '<div class="bible-note-popup-text">' + this.dataset.note + '</div>' +
                    '<button class="bible-note-popup-close">&times;</button>';
                this.parentNode.insertBefore(popup, this.nextSibling);
                popup.querySelector('.bible-note-popup-close').addEventListener('click', function() {
                    popup.remove();
                });
            });
        });

        // Prev / Next buttons
        var prevBtn = document.getElementById('biblePrev');
        var nextBtn = document.getElementById('bibleNext');
        if (prevBtn) {
            prevBtn.addEventListener('click', function() { navigateBibleChapter(-1); });
        }
        if (nextBtn) {
            nextBtn.addEventListener('click', function() { navigateBibleChapter(1); });
        }

        // Chapter picker button
        var chapterBtn = document.getElementById('bibleChapterBtn');
        if (chapterBtn) {
            chapterBtn.addEventListener('click', function() {
                var picker = document.getElementById('bibleChapterPicker');
                if (picker) picker.style.display = picker.style.display === 'none' ? 'flex' : 'none';
            });
        }

        // Chapter picker overlay — close on click
        var pickerOverlay = bibleRoot.querySelector('.bible-picker-overlay');
        if (pickerOverlay) {
            pickerOverlay.addEventListener('click', function() {
                var picker = document.getElementById('bibleChapterPicker');
                if (picker) picker.style.display = 'none';
            });
        }

        // Chapter picker numbers
        bibleRoot.querySelectorAll('.bible-picker-num').forEach(function(btn) {
            btn.addEventListener('click', function() {
                var ch = parseInt(this.getAttribute('data-ch'), 10);
                if (!isNaN(ch)) {
                    var picker = document.getElementById('bibleChapterPicker');
                    if (picker) picker.style.display = 'none';
                    currentBibleChapter = ch;
                    updateBibleChapterContent(textId);
                }
            });
        });

        // Notes button — toggle drawer with study tab
        var notesBtn = document.getElementById('bibleNotesBtn');
        if (notesBtn) {
            notesBtn.addEventListener('click', function() {
                var drawer = document.getElementById('bibleDrawer');
                if (drawer) {
                    drawer.classList.toggle('open');
                    if (drawer.classList.contains('open')) {
                        switchBibleDrawerTab(textId, currentBibleChapter, 'study');
                    }
                }
            });
        }

        // Xref button — toggle drawer with xrefs tab
        var xrefBtn = document.getElementById('bibleXrefBtn');
        if (xrefBtn) {
            xrefBtn.addEventListener('click', function() {
                var drawer = document.getElementById('bibleDrawer');
                if (drawer) {
                    drawer.classList.toggle('open');
                    if (drawer.classList.contains('open')) {
                        switchBibleDrawerTab(textId, currentBibleChapter, 'xrefs');
                    }
                }
            });
        }

        // Interlinear button — open reading pane with current chapter
        var ilBtn = document.getElementById('bibleILBtn');
        if (ilBtn) {
            ilBtn.addEventListener('click', function() {
                currentILBook = textId;
                renderInterlinear(currentBibleChapter);
                setReadingPane(true);
            });
        }

        // Map button in Bible Mode bottom bar
        var bibleMapBtn = document.getElementById('bibleMapBtn');
        if (bibleMapBtn) {
            bibleMapBtn.addEventListener('click', function() { openMapForBook(textId); });
        }

        // Drawer tabs
        bibleRoot.querySelectorAll('.bible-drawer-tab').forEach(function(tab) {
            tab.addEventListener('click', function() {
                var tabName = this.getAttribute('data-tab');
                switchBibleDrawerTab(textId, currentBibleChapter, tabName);
            });
        });

        // Drawer handle — toggle open state
        var drawerHandle = bibleRoot.querySelector('.bible-drawer-handle');
        if (drawerHandle) {
            drawerHandle.addEventListener('click', function() {
                var drawer = document.getElementById('bibleDrawer');
                if (drawer) {
                    if (drawer.classList.contains('full')) {
                        drawer.classList.remove('full');
                        drawer.classList.remove('open');
                    } else if (drawer.classList.contains('open')) {
                        drawer.classList.add('full');
                    } else {
                        drawer.classList.add('open');
                    }
                }
            });
        }

        // Swipe gestures
        var bibleReader = document.getElementById('bibleReader');
        if (bibleReader) {
            var bibleSwipeStartX = 0;
            var bibleSwipeStartY = 0;
            bibleReader.addEventListener('touchstart', function(e) {
                bibleSwipeStartX = e.touches[0].clientX;
                bibleSwipeStartY = e.touches[0].clientY;
            }, {passive: true});
            bibleReader.addEventListener('touchend', function(e) {
                var dx = e.changedTouches[0].clientX - bibleSwipeStartX;
                var dy = e.changedTouches[0].clientY - bibleSwipeStartY;
                if (Math.abs(dx) > 60 && Math.abs(dx) > Math.abs(dy) * 1.8) {
                    navigateBibleChapter(dx > 0 ? -1 : 1);
                }
            }, {passive: true});
        }
    }

    function navigateBibleChapter(delta) {
        var newCh = currentBibleChapter + delta;
        if (newCh < 1 || newCh > bibleTotalChapters) return;
        currentBibleChapter = newCh;
        updateBibleChapterContent(currentText);
    }

    function updateBibleChapterContent(textId) {
        var textDef = getTextDef(textId);
        if (!textDef) return;

        location.hash = 'read/' + textId + '/' + currentBibleChapter;

        // Update title
        var bibleRoot = document.getElementById('bibleMode');
        var titleEl = bibleRoot ? bibleRoot.querySelector('.bible-book-title') : null;
        if (titleEl) titleEl.textContent = textDef.name + ' ' + currentBibleChapter;

        // Update chapter content with slide animation
        var contentEl = document.getElementById('bibleContent');
        if (contentEl) {
            contentEl.classList.add('bible-slide-out');
            setTimeout(function() {
                var verses = getBibleChapterContent(textId, currentBibleChapter);
                var html = '';
                if (verses.length > 0) {
                    verses.forEach(function(v) {
                        html += '<span class="bible-verse">' +
                            '<sup class="bible-verse-num">' + v.num + '</sup> ' +
                            '<span class="bible-verse-text">' + esc(v.text) + '</span>' +
                            '</span> ';
                        if (v.note) {
                            html += '<span class="bible-verse-note" data-note="' + escAttr(v.note) + '">\uD83D\uDCA1</span> ';
                        }
                    });
                } else {
                    html = '<div class="bible-no-content">No scripture text available for ' + esc(textDef.name) + ' chapter ' + currentBibleChapter + '.</div>';
                }
                contentEl.innerHTML = html;
                contentEl.classList.remove('bible-slide-out');
                contentEl.classList.add('bible-slide-in');
                setTimeout(function() { contentEl.classList.remove('bible-slide-in'); }, 300);
            }, 150);
        }

        // Update prev/next button states
        var prevBtn = document.getElementById('biblePrev');
        var nextBtn = document.getElementById('bibleNext');
        if (prevBtn) prevBtn.disabled = currentBibleChapter <= 1;
        if (nextBtn) nextBtn.disabled = currentBibleChapter >= bibleTotalChapters;

        // Update chapter button label
        var chBtn = document.getElementById('bibleChapterBtn');
        if (chBtn) {
            var label = chBtn.querySelector('.bible-btn-label');
            if (label) label.textContent = currentBibleChapter;
        }

        // Update picker active state
        (bibleRoot || document).querySelectorAll('.bible-picker-num').forEach(function(btn) {
            btn.classList.toggle('active', parseInt(btn.getAttribute('data-ch'), 10) === currentBibleChapter);
        });

        // Scroll reader to top
        var reader = document.getElementById('bibleReader');
        if (reader) reader.scrollTo(0, 0);

        // Update drawer content if open
        var drawer = document.getElementById('bibleDrawer');
        if (drawer && drawer.classList.contains('open')) {
            var activeTab = (bibleRoot || document).querySelector('.bible-drawer-tab.active');
            var tabName = activeTab ? activeTab.getAttribute('data-tab') : 'study';
            var drawerContent = document.getElementById('bibleDrawerContent');
            if (drawerContent) {
                drawerContent.innerHTML = renderBibleDrawerTab(textId, currentBibleChapter, tabName);
            }
        }
    }

    function switchBibleDrawerTab(textId, chapterNum, tabName) {
        var bibleRoot = document.getElementById('bibleMode');
        (bibleRoot || document).querySelectorAll('.bible-drawer-tab').forEach(function(tab) {
            tab.classList.toggle('active', tab.getAttribute('data-tab') === tabName);
        });
        var drawerContent = document.getElementById('bibleDrawerContent');
        if (drawerContent) {
            drawerContent.innerHTML = renderBibleDrawerTab(textId, chapterNum, tabName);
        }
    }

    function renderBibleDrawerTab(textId, chapterNum, tabName) {
        var html = '';

        if (tabName === 'study') {
            // Show study notes for this chapter
            var notesData = STANDALONE_NOTES[textId] || {};
            var chNotes = notesData[String(chapterNum)] || {};
            var noteKeys = Object.keys(chNotes);

            html += '<div class="bible-drawer-study">';
            if (noteKeys.length > 0) {
                html += '<h4>Study Notes &mdash; Chapter ' + chapterNum + '</h4>';
                noteKeys.sort(function(a, b) { return parseInt(a) - parseInt(b); }).forEach(function(vNum) {
                    html += '<div class="bible-study-note">' +
                        '<span class="bible-note-verse">v' + vNum + '</span>' +
                        '<span class="bible-note-text">' + esc(chNotes[vNum]) + '</span>' +
                        '</div>';
                });
            } else {
                // Check interlinear notes
                var ilData = getTextInterlinear(textId);
                var ilChapter = ilData && ilData[String(chapterNum)];
                var hasIlNotes = false;
                if (ilChapter && ilChapter.verses) {
                    html += '<h4>Study Notes &mdash; Chapter ' + chapterNum + '</h4>';
                    ilChapter.verses.forEach(function(v) {
                        if (v.note) {
                            hasIlNotes = true;
                            html += '<div class="bible-study-note">' +
                                '<span class="bible-note-verse">v' + v.num + '</span>' +
                                '<span class="bible-note-text">' + esc(v.note) + '</span>' +
                                '</div>';
                        }
                    });
                }
                if (!hasIlNotes) {
                    html += '<p class="bible-drawer-empty">No study notes available for this chapter.</p>';
                }
            }
            html += '</div>';
        }

        if (tabName === 'xrefs') {
            html += '<div class="bible-drawer-xrefs">';
            html += '<h4>Cross-References &mdash; Chapter ' + chapterNum + '</h4>';

            // Find cross-refs from era data that reference this chapter
            var eras = getTextEras(textId);
            var foundXrefs = [];
            eras.forEach(function(era) {
                var chapters = ERA_DATA[era.id] || [];
                chapters.forEach(function(ch) {
                    if (!ch.cross_refs) return;
                    // Check if this chapter's ref matches
                    var parsed = parseScriptureRef(ch.ref || '');
                    if (parsed && parsed.chapter === chapterNum) {
                        ch.cross_refs.forEach(function(raw) {
                            var xr = normXref(raw);
                            foundXrefs.push(xr);
                        });
                    }
                });
            });

            if (foundXrefs.length > 0) {
                foundXrefs.forEach(function(xr) {
                    html += '<div class="bible-xref-item">' +
                        '<span class="bible-xref-ref">' + esc(xr.ref) + '</span>' +
                        (xr.note && xr.note !== xr.ref ? '<span class="bible-xref-note">' + esc(xr.note) + '</span>' : '') +
                        '</div>';
                });
            } else {
                html += '<p class="bible-drawer-empty">No cross-references found for this chapter.</p>';
            }
            html += '</div>';
        }

        if (tabName === 'council') {
            html += '<div class="bible-drawer-council">';
            html += '<h4>Divine Council &mdash; Chapter ' + chapterNum + '</h4>';

            // Check THC cross-refs
            var chPrefix = textId.replace(/[^a-z0-9]/g, '').substring(0, 3);
            var chId = chPrefix + '-' + chapterNum;
            var thcRefs = THC_XREFS.fromLibrary[chId];

            if (thcRefs && thcRefs.length > 0) {
                thcRefs.forEach(function(ref) {
                    html += '<div class="bible-council-item">' +
                        '<span class="bible-council-label">' + esc(ref.label) + '</span>' +
                        (ref.note ? '<span class="bible-council-note">' + esc(ref.note) + '</span>' : '') +
                        '</div>';
                });
            } else {
                html += '<p class="bible-drawer-empty">No divine council connections found for this chapter.</p>';
            }
            html += '</div>';
        }

        if (tabName === 'settings') {
            var savedFontSize = parseFloat(localStorage.getItem('atl-bible-font-size') || '1.1');
            html += '<div class="bible-drawer-settings">' +
                '<h4>Reading Settings</h4>' +
                '<div class="bible-setting-row">' +
                '<label class="bible-setting-label">Font Size</label>' +
                '<input type="range" class="bible-font-slider" id="bibleFontSlider" min="0.8" max="1.8" step="0.1" value="' + savedFontSize + '">' +
                '<span class="bible-font-preview" id="bibleFontPreview">' + savedFontSize.toFixed(1) + 'em</span>' +
                '</div>' +
                '</div>';

            // Apply saved font size
            setTimeout(function() {
                var slider = document.getElementById('bibleFontSlider');
                var preview = document.getElementById('bibleFontPreview');
                var contentEl = document.getElementById('bibleContent');
                if (contentEl) contentEl.style.fontSize = savedFontSize + 'em';

                if (slider) {
                    slider.addEventListener('input', function() {
                        var size = parseFloat(this.value);
                        if (preview) preview.textContent = size.toFixed(1) + 'em';
                        if (contentEl) contentEl.style.fontSize = size + 'em';
                        localStorage.setItem('atl-bible-font-size', String(size));
                    });
                }
            }, 50);
        }

        return html;
    }

    // Bible mode keyboard handler
    document.addEventListener('keydown', function(e) {
        if (!document.body.classList.contains('bible-mode-active')) return;
        if (e.key === 'ArrowLeft') navigateBibleChapter(-1);
        if (e.key === 'ArrowRight') navigateBibleChapter(1);
        if (e.key === 'Escape') showBookLanding(currentText);
    });

    // ═══════════════════════════════════════════════════════
    // TEXT VIEW (reading a specific text)
    // ═══════════════════════════════════════════════════════

    var textContentCache = {};

    function selectText(textId, skipPushState) {
        try {
            logEvent('text_view', textId);
            var textDef = getTextDef(textId);
            if (!textDef) return;

            var eras = getTextEras(textId);
            if (eras.length === 0) return; // no content yet

            closeAllOverlays();
            libraryMode = false;
            currentText = textId;
            document.body.classList.add('text-selected');
            document.body.classList.remove('library-fullwidth', 'book-landing-view', 'bible-mode-active');
            localStorage.setItem('atl-current-text', textId);

            // Track recent texts for "Continue Reading" section
            var recent = JSON.parse(localStorage.getItem('atl-recent-texts') || '[]');
            recent = recent.filter(function(id) { return id !== textId; });
            recent.unshift(textId);
            if (recent.length > 6) recent = recent.slice(0, 6);
            localStorage.setItem('atl-recent-texts', JSON.stringify(recent));

            // Update interlinear book
            currentILBook = textId;

            buildTextSidebar(textId);
            loadTextContent(textId);

            // Update reading pane for this text
            var il = getTextInterlinear(textId);
            if (Object.keys(il).length > 0) {
                sourceReadingMode = false;
                document.body.classList.remove('source-reading-active');
                setReadingPane(true);
                renderInterlinear(1);
            } else {
                // Show source reading pane for texts without interlinear
                sourceReadingMode = true;
                document.body.classList.add('source-reading-active');
                setReadingPane(true);
                renderSourceReading(textId, null);
            }

            if (!skipPushState) {
                window.scrollTo(0, 0);
            }
        } catch (err) {
            console.error('selectText error:', err);
            mainContent.innerHTML = '<div style="color:#a05a54;padding:2rem;font-size:1.2rem">' +
                '<h2>Error loading ' + textId + '</h2>' +
                '<pre>' + err.message + '\n' + err.stack + '</pre></div>';
        }
    }

    function buildTextSidebar(textId) {
        var textDef = getTextDef(textId);
        var cat = getCategoryDef(textDef.category);
        var eras = getTextEras(textId);

        var readCounts = getTextReadCount(textId);
        var html = '<div class="text-sidebar-header">' +
            '<button class="back-to-library" id="backToLibrary">&larr; Library</button>' +
            '<div class="text-sidebar-title">' +
            '<span class="canon-badge badge-small" style="background:' + cat.color + '20;color:' + cat.color + ';border-color:' + cat.color + '40">' + cat.badge + '</span>' +
            ' ' + textDef.name +
            '</div>' +
            '<div class="sidebar-read-count' + (readCounts.read === readCounts.total && readCounts.total > 0 ? ' all-read' : '') + '" data-text="' + textId + '">' + readCounts.read + '/' + readCounts.total + '</div>' +
            '</div>';

        eras.forEach(function(era) {
            var chapters = ERA_DATA[era.id] || [];
            html += '<div class="era-group" data-era="' + era.id + '" data-text="' + textId + '">' +
                '<button class="era-toggle" data-era="' + era.id + '" title="' + era.chapters + '">' +
                '<span class="era-icon">' + era.icon + '</span>' +
                '<span class="era-color-dot" style="background:' + era.color + '"></span>' +
                '<span>' + era.name + '</span>' +
                '<span class="chevron">&#9654;</span>' +
                '</button>' +
                '<div class="era-chapters" id="eraChapters-' + era.id + '">';

            chapters.forEach(function(ch) {
                var linkLabel = (ch.type === 'historical_insert' || ch.type === 'html_fragment') ? ch.title : ch.ref;
                var chRead = isChapterRead(ch.id);
                html += '<div class="chapter-link ' + (ch.type === 'historical_insert' ? 'insert-link' : '') + (chRead ? ' ch-read' : '') + '"' +
                    ' data-id="' + ch.id + '" data-era="' + era.id + '">' +
                    (chRead ? '<span class="ch-read-dot">\u2713</span>' : '') +
                    linkLabel +
                    '</div>';
            });

            html += '</div></div>';
        });

        sidebarNav.innerHTML = html;

        // Bind back button
        var backBtn = document.getElementById('backToLibrary');
        if (backBtn) {
            backBtn.addEventListener('click', function() { showLibrary(); });
        }
    }

    function loadTextContent(textId, startChapterIdx) {
        // Single-chapter mode — render one chapter at a time
        if (singleChapterMode) {
            renderSingleChapterView(textId, startChapterIdx || 0);
            return;
        }

        // Cache generated HTML but always update the DOM
        if (!textContentCache[textId]) {
            var eras = getTextEras(textId);
            var textDef = getTextDef(textId);
            var cat = textDef ? getCategoryDef(textDef.category) : null;
            var flatChapters = getFlatChapterList(textId);
            var html = '';

            // Breadcrumb bar
            html += '<div class="breadcrumb-bar">' +
                '<span class="bc-link" data-action="go-library">Library</span>' +
                '<span class="bc-sep">\u203A</span>' +
                (cat ? '<span class="bc-link" style="color:' + cat.color + '">' + cat.name + '</span><span class="bc-sep">\u203A</span>' : '') +
                '<span class="bc-current">' + (textDef ? textDef.name : textId) + '</span>' +
                '</div>';

            // Scholarly intro is shown on the Book Landing Page — skip in Study Mode
            // to avoid cramped rendering in the narrow main-content column

            eras.forEach(function(era) {
                var chapters = ERA_DATA[era.id] || [];
                html += renderEraHeader(era);
                chapters.forEach(function(ch) {
                    if (ch.type === 'html_fragment') {
                        html += '<div class="hc-fragment" id="' + ch.id + '">' + ch.html + renderLibraryLinks(ch.id) + '</div>';
                    } else if (ch.type === 'historical_insert') {
                        html += renderHistoricalInsert(ch, era);
                    } else {
                        html += renderChapter(ch, era, flatChapters);
                    }
                });
            });
            textContentCache[textId] = html;
        }

        mainContent.innerHTML = textContentCache[textId];

        // Stagger-animate chapter cards on load
        var chCards = mainContent.querySelectorAll('.chapter-card');
        chCards.forEach(function(card, i) {
            card.classList.add('stagger-in');
            card.style.animationDelay = Math.min(i * 25, 500) + 'ms';
        });

        // Lazy-load inline content if reading mode is already scripture or interlinear
        if (readingMode === 'scripture' || readingMode === 'interlinear') {
            lazyLoadReadingModeContent(readingMode);
        }

        // Eras start collapsed — user expands what they want
        setupIntersectionObserver();
    }

    // ── Single-Chapter View (Mobile) ────────────────────────────────
    function renderSingleChapterView(textId, chIdx) {
        var flatChapters = getFlatChapterList(textId);
        if (!flatChapters || flatChapters.length === 0) return;

        // Clamp index
        if (chIdx < 0) chIdx = 0;
        if (chIdx >= flatChapters.length) chIdx = flatChapters.length - 1;
        currentChapterIndex = chIdx;

        var target = flatChapters[chIdx];
        var textDef = getTextDef(textId);
        var cat = textDef ? getCategoryDef(textDef.category) : null;
        var eras = getTextEras(textId);

        // Find which era this chapter belongs to + full chapter object
        var chEra = null, ch = null, isFirstInEra = false;
        for (var e = 0; e < eras.length; e++) {
            var eraChapters = ERA_DATA[eras[e].id] || [];
            for (var c = 0; c < eraChapters.length; c++) {
                if (eraChapters[c].id === target.id) {
                    chEra = eras[e];
                    ch = eraChapters[c];
                    isFirstInEra = (c === 0);
                    break;
                }
            }
            if (ch) break;
        }
        if (!ch) return;

        var html = '';

        // Breadcrumb
        html += '<div class="breadcrumb-bar">' +
            '<span class="bc-link" data-action="go-library">Library</span>' +
            '<span class="bc-sep">\u203A</span>' +
            (cat ? '<span class="bc-link" style="color:' + cat.color + '">' + cat.name + '</span><span class="bc-sep">\u203A</span>' : '') +
            '<span class="bc-current">' + (textDef ? textDef.name : textId) + '</span>' +
            '</div>';

        // Sticky chapter indicator
        html += '<div class="single-chapter-indicator" id="chapterIndicator">' +
            '<button class="sch-nav-btn sch-prev" data-sch-delta="-1"' + (chIdx === 0 ? ' disabled' : '') + '>\u25C0</button>' +
            '<span class="sch-position">' + (chIdx + 1) + ' of ' + flatChapters.length + '</span>' +
            '<button class="sch-nav-btn sch-next" data-sch-delta="1"' + (chIdx >= flatChapters.length - 1 ? ' disabled' : '') + '>\u25B6</button>' +
            '</div>';

        // Scholarly intro moved to Book Landing Page — skip in Bible Mode

        // Era header if first chapter in its era
        if (chEra && isFirstInEra) {
            html += renderEraHeader(chEra);
        }

        // Render the single chapter
        var chapterHtml = '';
        if (ch.type === 'html_fragment') {
            chapterHtml = '<div class="hc-fragment" id="' + ch.id + '">' + ch.html + renderLibraryLinks(ch.id) + '</div>';
        } else if (ch.type === 'historical_insert') {
            chapterHtml = renderHistoricalInsert(ch, chEra);
        } else {
            chapterHtml = renderChapter(ch, chEra, flatChapters);
        }

        html += '<div class="single-chapter-container" id="singleChapterContainer">' +
            chapterHtml + '</div>';

        // Bottom prev/next with titles
        html += '<div class="sch-bottom-nav">';
        if (chIdx > 0) {
            var prevCh = flatChapters[chIdx - 1];
            html += '<button class="sch-bottom-btn sch-bottom-prev" data-sch-delta="-1">' +
                '<span class="sch-btn-arrow">\u2190</span>' +
                '<span class="sch-btn-title">' + esc(prevCh.ref || prevCh.title) + '</span></button>';
        } else {
            html += '<div></div>';
        }
        if (chIdx < flatChapters.length - 1) {
            var nextCh = flatChapters[chIdx + 1];
            html += '<button class="sch-bottom-btn sch-bottom-next" data-sch-delta="1">' +
                '<span class="sch-btn-title">' + esc(nextCh.ref || nextCh.title) + '</span>' +
                '<span class="sch-btn-arrow">\u2192</span></button>';
        } else {
            html += '<div></div>';
        }
        html += '</div>';

        // "Show All" toggle
        html += '<div class="sch-show-all">' +
            '<button class="sch-show-all-btn" id="schShowAll">\u2630 Show All Chapters</button>' +
            '</div>';

        mainContent.innerHTML = html;
        mainContent.scrollTop = 0;

        // Update hash
        if (ch.id) {
            history.replaceState(null, '', '#' + ch.id);
        }

        // Sync sidebar active state
        document.querySelectorAll('.chapter-link').forEach(function(link) {
            link.classList.toggle('active', link.dataset.id === ch.id);
        });

        // Sync reading pane if open
        syncReadingPane(ch.id);

        // Lazy-load inline content if reading mode is already scripture or interlinear
        if (readingMode === 'scripture' || readingMode === 'interlinear') {
            lazyLoadReadingModeContent(readingMode);
        }
    }

    function navigateChapter(delta) {
        if (!currentText) return;
        var flatChapters = getFlatChapterList(currentText);
        if (!flatChapters) return;
        var newIdx = currentChapterIndex + delta;
        if (newIdx < 0 || newIdx >= flatChapters.length) return;
        renderSingleChapterView(currentText, newIdx);
    }

    // ── Text Introduction Panel ────────────────────────────────────
    function renderTextIntro(textId) {
        var info = TEXT_INTROS[textId];
        if (!info) return '';

        var textDef = getTextDef(textId);
        var cat = textDef ? getCategoryDef(textDef.category) : null;
        var cs = info.canonical_status || {};
        var auth = info.authorship || {};
        var dt = info.date || {};
        var aud = info.audience || {};
        var lang = info.language || {};
        var sa = info.scripture_alignment || {};
        var ms = info.manuscripts || {};
        var hc = info.historical_context || {};
        var dc = info.divine_council || {};
        var notes = info.reader_notes || [];

        var statusClass = cs.status === 'canonical' ? 'intro-canonical' : 'intro-noncanonical';
        var statusIcon = cs.status === 'canonical' ? '\u2714' : '\u26A0';

        var introCollapsed = localStorage.getItem('atl-intro-collapsed') === '1';
        var html = '<div class="text-intro-panel' + (introCollapsed ? ' intro-collapsed' : '') + '" id="textIntro">';

        // Header with canonical badge + collapse toggle
        html += '<div class="intro-header">' +
            '<div class="intro-header-top">' +
            '<h1 class="intro-title">' + (info.display_name || textDef.name) + '</h1>' +
            '<button class="intro-collapse-btn" id="introCollapseBtn" title="Toggle info panel">' +
            (introCollapsed ? '\u25BC' : '\u25B2') + '</button>' +
            '</div>' +
            '<div class="intro-status ' + statusClass + '">' +
            '<span class="intro-status-icon">' + statusIcon + '</span> ' +
            (cs.label || cs.status) + '</div>';
        var dssRef = DSS_ATTESTATION[textId];
        if (dssRef) {
            html += '<div class="intro-dss-badge">\uD83D\uDCDC Found at Qumran: <strong>' + dssRef + '</strong></div>';
        }
        if (cs.detail) {
            html += '<p class="intro-status-detail">' + cs.detail + '</p>';
        }
        html += '</div>';

        // Quick facts grid
        html += '<div class="intro-facts-grid">';
        if (auth.traditional) {
            html += '<div class="intro-fact"><div class="intro-fact-label">Traditional Author</div>' +
                '<div class="intro-fact-value">' + auth.traditional.split(',')[0].split('.')[0] + '</div></div>';
        }
        if (dt.traditional || dt.critical_range) {
            html += '<div class="intro-fact"><div class="intro-fact-label">Date</div>' +
                '<div class="intro-fact-value">' + (dt.traditional || dt.critical_range).substring(0, 80) + '</div></div>';
        }
        if (lang.original) {
            html += '<div class="intro-fact"><div class="intro-fact-label">Original Language</div>' +
                '<div class="intro-fact-value">' + lang.original.split('.')[0].split('(')[0].trim() + '</div></div>';
        }
        if (dc.relevance) {
            html += '<div class="intro-fact"><div class="intro-fact-label">Heiser Relevance</div>' +
                '<div class="intro-fact-value">' + dc.relevance.charAt(0).toUpperCase() + dc.relevance.slice(1) + '</div></div>';
        }
        html += '</div>';

        // Collapsible detail sections
        html += '<div class="intro-sections">';

        // Authorship
        if (auth.traditional || auth.scholarly_debate) {
            html += renderIntroSection('Authorship', '' +
                (auth.traditional ? '<p><strong>Traditional view:</strong> ' + esc(auth.traditional) + '</p>' : '') +
                (auth.scholarly_debate ? '<p><strong>Scholarly debate:</strong> ' + esc(auth.scholarly_debate) + '</p>' : '') +
                (auth.bottom_line ? '<p class="intro-bottomline"><strong>Bottom line:</strong> ' + esc(auth.bottom_line) + '</p>' : ''));
        }

        // Date
        if (dt.traditional || dt.critical_range || dt.evidence) {
            html += renderIntroSection('Date of Composition', '' +
                (dt.traditional ? '<p><strong>Traditional:</strong> ' + esc(dt.traditional) + '</p>' : '') +
                (dt.critical_range ? '<p><strong>Critical range:</strong> ' + esc(dt.critical_range) + '</p>' : '') +
                (dt.evidence ? '<p><strong>Evidence:</strong> ' + esc(dt.evidence) + '</p>' : ''));
        }

        // Audience & Purpose
        if (aud.original_audience || aud.purpose) {
            html += renderIntroSection('Audience & Purpose', '' +
                (aud.original_audience ? '<p><strong>Original audience:</strong> ' + esc(aud.original_audience) + '</p>' : '') +
                (aud.purpose ? '<p><strong>Purpose:</strong> ' + esc(aud.purpose) + '</p>' : '') +
                (aud.theological_intent ? '<p><strong>Theological intent:</strong> ' + esc(aud.theological_intent) + '</p>' : ''));
        }

        // Original Language
        if (lang.original) {
            html += renderIntroSection('Language & Linguistics', '' +
                '<p><strong>Original language:</strong> ' + esc(lang.original) + '</p>' +
                (lang.script ? '<p><strong>Script:</strong> ' + esc(lang.script) + '</p>' : '') +
                (lang.linguistic_notes ? '<p><strong>Linguistic analysis:</strong> ' + esc(lang.linguistic_notes) + '</p>' : '') +
                (lang.grammar_match ? '<p><strong>Period consistency:</strong> ' + esc(lang.grammar_match) + '</p>' : ''));
        }

        // Scripture Alignment
        if (sa.verdict) {
            var saHtml = '<p class="intro-verdict"><strong>Verdict:</strong> ' + esc(sa.verdict) + '</p>';
            if (sa.where_it_aligns && sa.where_it_aligns.length) {
                saHtml += '<div class="intro-align-section"><strong>Where it aligns with scripture:</strong><ul>' +
                    sa.where_it_aligns.map(function(a) { return '<li>' + esc(a) + '</li>'; }).join('') + '</ul></div>';
            }
            if (sa.where_it_diverges && sa.where_it_diverges.length) {
                saHtml += '<div class="intro-diverge-section"><strong>Where it diverges:</strong><ul>' +
                    sa.where_it_diverges.map(function(d) { return '<li>' + esc(d) + '</li>'; }).join('') + '</ul></div>';
            }
            if (sa.reader_guidance) {
                saHtml += '<p class="intro-guidance"><strong>Reader guidance:</strong> ' + esc(sa.reader_guidance) + '</p>';
            }
            if (sa.nt_usage) {
                saHtml += '<p><strong>NT usage:</strong> ' + esc(sa.nt_usage) + '</p>';
            }
            if (sa.internal_consistency) {
                saHtml += '<p><strong>Internal consistency:</strong> ' + esc(sa.internal_consistency) + '</p>';
            }
            html += renderIntroSection('Scripture Alignment', saHtml);
        }

        // Manuscript Tradition
        if (ms.earliest || ms.major_witnesses) {
            var msHtml = '';
            if (ms.earliest) msHtml += '<p><strong>Earliest witnesses:</strong> ' + esc(ms.earliest) + '</p>';
            if (ms.major_witnesses && ms.major_witnesses.length) {
                msHtml += '<div class="intro-manuscripts"><table class="intro-ms-table">' +
                    '<tr><th>Manuscript</th><th>Date</th><th>Notes</th></tr>';
                ms.major_witnesses.forEach(function(w) {
                    msHtml += '<tr><td>' + esc(w.name) + '</td><td>' + esc(w.date) + '</td><td>' + esc(w.note) + '</td></tr>';
                });
                msHtml += '</table></div>';
            }
            if (ms.reliability) msHtml += '<p><strong>Reliability:</strong> ' + esc(ms.reliability) + '</p>';
            html += renderIntroSection('Manuscript Tradition', msHtml);
        }

        // Historical Context
        if (hc.setting || hc.geography) {
            html += renderIntroSection('Historical Context & Geography', '' +
                (hc.setting ? '<p><strong>Setting:</strong> ' + esc(hc.setting) + '</p>' : '') +
                (hc.geography ? '<p><strong>Geography:</strong> ' + esc(hc.geography) + '</p>' : '') +
                (hc.historical_connections ? '<p><strong>Historical connections:</strong> ' + esc(hc.historical_connections) + '</p>' : ''));
        }

        // Divine Council / Heiser
        if (dc.summary) {
            var dcHtml = '<p>' + esc(dc.summary) + '</p>';
            if (dc.key_heiser_refs && dc.key_heiser_refs.length) {
                dcHtml += '<div class="intro-heiser-refs"><strong>Key Heiser references:</strong><ul>' +
                    dc.key_heiser_refs.map(function(r) { return '<li>' + esc(r) + '</li>'; }).join('') + '</ul></div>';
            }
            html += renderIntroSection('Divine Council Framework (Heiser)', dcHtml);
        }

        html += '</div>'; // end intro-sections

        // Reader Notes / Warnings
        if (notes.length > 0) {
            html += '<div class="intro-notes">';
            notes.forEach(function(n) {
                var noteClass = 'intro-note note-' + (n.type || 'context');
                html += '<div class="' + noteClass + '">' +
                    '<div class="intro-note-title">' + esc(n.title) + '</div>' +
                    '<div class="intro-note-body">' + esc(n.body) + '</div></div>';
            });
            html += '</div>';
        }

        html += '</div>'; // end text-intro-panel
        return html;
    }

    function renderIntroSection(title, bodyHtml) {
        return '<details class="intro-detail">' +
            '<summary class="intro-detail-summary">' + esc(title) + '</summary>' +
            '<div class="intro-detail-body">' + bodyHtml + '</div></details>';
    }

    // ── Era Header ──────────────────────────────────────────
    function renderEraHeader(era) {
        return '<div class="era-header" id="era-' + era.id + '">' +
            '<h2 style="color:' + era.color + '">' + era.icon + ' ' + era.name + '</h2>' +
            '<div class="era-chapters-range">' + era.chapters + '</div>' +
            '<div class="era-themes">' +
            era.themes.map(function(t) { return '<span class="era-theme-tag">' + t + '</span>'; }).join('') +
            '</div></div>';
    }

    // ── THC Cross-Reference Panels ─────────────────────────
    function renderThcLinks(chId) {
        var refs = THC_XREFS.fromLibrary[chId];
        if (!refs || refs.length === 0) return '';
        var html = '<div class="thc-links-panel">' +
            '<div class="callout-label">\u2727 The Heavenly Court \u2014 Deep Dive</div>' +
            '<div class="thc-links-list">';
        refs.forEach(function(ref) {
            html += '<div class="thc-link-item" data-navigate-text="heavenly_court" data-navigate-id="' + ref.id + '">' +
                '<span class="thc-link-icon">\u2192</span>' +
                '<div class="thc-link-content">' +
                '<div class="thc-link-title">' + ref.label + '</div>' +
                '<div class="thc-link-note">' + ref.note + '</div>' +
                '</div></div>';
        });
        html += '</div></div>';
        return html;
    }

    function renderLibraryLinks(chId) {
        var refs = THC_XREFS.toLibrary[chId];
        if (!refs || refs.length === 0) return '';
        var html = '<div class="library-links-panel">' +
            '<div class="callout-label">\u2192 Study in Library</div>' +
            '<div class="thc-links-list">';
        refs.forEach(function(ref) {
            html += '<div class="thc-link-item" data-navigate-text="' + ref.text + '" data-navigate-id="' + ref.id + '">' +
                '<span class="thc-link-icon">\u2192</span>' +
                '<div class="thc-link-content">' +
                '<div class="thc-link-title">' + ref.label + '</div>' +
                '</div></div>';
        });
        html += '</div></div>';
        return html;
    }

    // ── Chapter Card Rendering ──────────────────────────────
    function renderChapter(ch, era, flatChapters) {
        if (ch.type === 'html_fragment') {
            return '<div class="hc-fragment" id="' + ch.id + '">' + ch.html + '</div>';
        }

        var isBookmarked = bookmarks.includes(ch.id);
        var isRead = isChapterRead(ch.id);
        var textDef = getTextDef(era.text);
        var cat = textDef ? getCategoryDef(textDef.category) : null;

        var isThematic = textDef && textDef.category === 'thematic';
        var modeClass = readingMode !== 'study' ? ' mode-' + readingMode : '';
        var thematicClass = isThematic ? ' thematic-chapter' : '';
        var html = '<div class="chapter-card' + (isRead ? ' chapter-read' : '') + modeClass + thematicClass + '" id="' + ch.id + '" style="--era-color:' + era.color + '">' +
            '<div style="position:absolute;top:0;left:0;right:0;height:3px;background:' + era.color + ';border-radius:6px 6px 0 0"></div>' +
            '<label class="read-check-label" title="Mark as read"><input type="checkbox" class="read-check" data-id="' + ch.id + '"' + (isRead ? ' checked' : '') + '></label>' +
            '<button class="chapter-copy-btn" data-id="' + ch.id + '" title="Copy study content">&#x1F4CB;</button>' +
            '<button class="chapter-export-btn" data-id="' + ch.id + '" title="Export as Markdown">&#x1F4E5;</button>' +
            '<button class="bookmark-btn ' + (isBookmarked ? 'bookmarked' : '') + '"' +
            ' data-id="' + ch.id + '" title="Bookmark this chapter">' +
            (isBookmarked ? '\u2605' : '\u2606') + '</button>';

        // Canon badge
        if (cat && textDef.canon === false) {
            html += '<span class="chapter-canon-badge" style="color:' + cat.color + '">' + cat.badge + '</span>';
        }

        html += '<div class="chapter-ref">' + ch.ref + '</div>' +
            '<h3>' + ch.title + '</h3>' +
            '<div class="synopsis">' + ch.synopsis + '</div>';

        // Only show reading mode toggle for canonical texts with scripture/interlinear data (not thematic essays)
        var showModeToggle = textDef && textDef.category !== 'thematic';
        if (showModeToggle) {
            html += '<div class="reading-mode-toggle">' +
                '<button class="rmt-btn' + (readingMode === 'scripture' ? ' active' : '') + '" data-mode="scripture">Scripture</button>' +
                '<button class="rmt-btn' + (readingMode === 'study' ? ' active' : '') + '" data-mode="study">Study</button>' +
                '<button class="rmt-btn' + (readingMode === 'interlinear' ? ' active' : '') + '" data-mode="interlinear">Interlinear</button>' +
                '</div>';
        }

        // Evidence tier legend for thematic chapters
        if (isThematic) {
            html += '<div class="evidence-legend">' +
                '<div class="evidence-legend-item"><span class="evidence-badge badge-a">A</span> Direct Scripture</div>' +
                '<div class="evidence-legend-item"><span class="evidence-badge badge-b">B</span> Valid Inference</div>' +
                '<div class="evidence-legend-item"><span class="evidence-badge badge-c">C</span> Ancient Parallels</div>' +
                '</div>';
        }

        // Key verse
        if (ch.key_verse) {
            html += '<div class="scripture-block">' +
                '<div class="verse-ref">' + ch.key_verse.ref + '</div>' +
                '<div class="verse-text">' + ch.key_verse.text + '</div>' +
                '<div class="verse-translation">' + ch.key_verse.translation + '</div>' +
                '</div>';
        }

        // Hebrew terms — handle both glossary keys (strings) and inline objects ({term, meaning})
        if (ch.hebrew_terms && ch.hebrew_terms.length > 0) {
            if (isThematic && typeof ch.hebrew_terms[0] === 'object') {
                html += renderThematicTerms(ch.hebrew_terms);
            } else {
                html += renderTermsGrid(ch.hebrew_terms);
            }
        }

        // ANE backdrop
        if (ch.ane_backdrop) {
            html += '<div class="ane-callout">' +
                '<div class="callout-label">Ancient Near Eastern Context</div>' +
                '<div class="callout-body">' + ch.ane_backdrop + '</div></div>';
        }

        // Second Temple sources
        if (Array.isArray(ch.second_temple) && ch.second_temple.length > 0) {
            html += '<div class="second-temple-box">' +
                '<div class="callout-label">Second Temple Sources</div>';
            ch.second_temple.forEach(function(s) {
                html += '<div class="source-entry">' +
                    '<div class="source-ref">' + s.source +
                    (s.canon === false ? '<span class="source-noncanon">Non-canonical</span>' : '') +
                    '</div>' +
                    '<div class="source-summary">' + s.summary + '</div>' +
                    '<div class="source-relevance">' + s.relevance + '</div></div>';
            });
            html += '</div>';
        }

        // Cross references
        if (ch.cross_refs && ch.cross_refs.length > 0) {
            html += '<div class="cross-refs-section"><h4>Cross References</h4>' +
                '<div class="cross-refs-list">';
            ch.cross_refs.forEach(function(xr, i) {
                if (typeof xr === 'string') {
                    html += '<span class="cross-ref-pill type-ot"' +
                        ' data-chapter="' + ch.id + '" data-index="' + i + '"' +
                        ' title="' + escAttr(xr) + '">' + xr + '</span>';
                } else {
                    html += '<span class="cross-ref-pill type-' + (xr.type || 'ot') + '"' +
                        ' data-chapter="' + ch.id + '" data-index="' + i + '"' +
                        ' title="' + escAttr(xr.note || xr.ref || '') + '">' + xr.ref + '</span>';
                }
            });
            html += '</div></div>';
        }

        // Divine council note
        if (ch.divine_council_note) {
            html += '<div class="council-note">' +
                '<div class="callout-label">Heavenly Court Lens</div>' +
                '<div class="callout-body">' + ch.divine_council_note + '</div></div>';
        }

        // THC deep-dive links (if this chapter has a related Heavenly Court analysis)
        html += renderThcLinks(ch.id);

        // Inline scripture placeholder (lazy-loaded when user switches to scripture mode)
        var ilTextId = era.text || '';
        var ilChMatch = ch.ref ? ch.ref.match(/(\d+)(?:\s*[-\u2013]\s*(\d+))?(?:\s*:|$)/) : null;
        var ilChNum = ilChMatch ? ilChMatch[1] : '';
        var ilChEnd = ilChMatch && ilChMatch[2] ? ilChMatch[2] : ilChNum;
        html += '<div class="inline-scripture" data-text="' + ilTextId + '" data-ch="' + ilChNum + '" data-ch-end="' + ilChEnd + '"></div>';

        // Inline interlinear placeholder (lazy-loaded when user switches to interlinear mode)
        html += '<div class="inline-interlinear" data-text="' + ilTextId + '" data-ch="' + ilChNum + '"></div>';

        // Sections
        if (ch.sections && ch.sections.length > 0) {
            html += '<div class="chapter-sections">';
            ch.sections.forEach(function(sec) {
                var body = sec.body;
                // Convert evidence tier markers [A], [B], [C] to styled badges in thematic chapters
                if (isThematic) {
                    body = body.replace(/\[A\]/g, '<span class="evidence-badge badge-a">A</span>');
                    body = body.replace(/\[B\]/g, '<span class="evidence-badge badge-b">B</span>');
                    body = body.replace(/\[C\]/g, '<span class="evidence-badge badge-c">C</span>');
                }
                html += '<div class="section-block">' +
                    '<h4>' + sec.heading + '</h4>' +
                    '<div class="section-body">' + body + '</div></div>';
            });
            html += '</div>';
        }

        // "Referenced By" — chapters from OTHER books that cite this passage
        var reverseCites = getReverseCitations(ch.id, era.text);
        if (reverseCites.length > 0) {
            var shown = reverseCites.slice(0, 5);
            html += '<div class="related-studies-section">' +
                '<h4>Referenced By</h4>' +
                '<div class="related-studies-list">';
            shown.forEach(function(cite) {
                var fromTextDef = getTextDef(cite.fromText);
                var fromName = fromTextDef ? fromTextDef.name : cite.fromText;
                html += '<div class="related-study-item" data-nav-chapter="' + cite.fromChapterId + '" data-nav-text="' + cite.fromText + '">' +
                    '<span class="related-study-ref">' + fromName + ' \u2014 ' + cite.fromRef + '</span>' +
                    '<span class="related-study-note">' + cite.note + '</span>' +
                    '</div>';
            });
            if (reverseCites.length > 5) {
                html += '<div class="related-study-more">+ ' + (reverseCites.length - 5) + ' more references</div>';
            }
            html += '</div></div>';
        }

        // Prev/Next chapter navigation
        if (flatChapters && flatChapters.length > 1) {
            var idx = -1;
            for (var i = 0; i < flatChapters.length; i++) {
                if (flatChapters[i].id === ch.id) { idx = i; break; }
            }
            if (idx !== -1) {
                var prev = idx > 0 ? flatChapters[idx - 1] : null;
                var next = idx < flatChapters.length - 1 ? flatChapters[idx + 1] : null;
                if (prev || next) {
                    html += '<div class="chapter-nav">';
                    if (prev) {
                        html += '<div class="chapter-nav-btn nav-prev" data-nav-to="' + prev.id + '">' +
                            '<span class="chapter-nav-label">\u2190 Previous</span>' +
                            '<span class="chapter-nav-title">' + (prev.ref || prev.title) + '</span></div>';
                    }
                    if (next) {
                        html += '<div class="chapter-nav-btn nav-next" data-nav-to="' + next.id + '">' +
                            '<span class="chapter-nav-label">Next \u2192</span>' +
                            '<span class="chapter-nav-title">' + (next.ref || next.title) + '</span></div>';
                    }
                    html += '</div>';
                }
            }
        }

        // Existing study notes for this chapter
        var existingNote = studyNotes[ch.id];
        if (existingNote) {
            html += '<div class="chapter-study-note">' +
                '<div class="study-note-header">' +
                '<span class="study-note-icon">\uD83D\uDCCC</span>' +
                '<span class="study-note-label">My Note</span>' +
                '<button class="study-note-edit" data-id="' + ch.id + '" title="Edit note">\u270F\uFE0F</button>' +
                '<button class="study-note-delete" data-id="' + ch.id + '" title="Delete note">\u2715</button>' +
                '</div>' +
                '<div class="study-note-text">' + esc(existingNote.text) + '</div>' +
                '<div class="study-note-date">' + (existingNote.date || '') + '</div>' +
                '</div>';
        }

        // Mobile-friendly action bar at bottom of card
        var hasNote = !!studyNotes[ch.id];
        html += '<div class="chapter-action-bar">' +
            '<button class="chapter-action-read' + (isRead ? ' is-read' : '') + '" data-id="' + ch.id + '">' +
            (isRead ? '\u2714 Read' : '\u25CB Mark as Read') + '</button>' +
            '<button class="chapter-action-bookmark' + (isBookmarked ? ' is-bookmarked' : '') + '" data-id="' + ch.id + '">' +
            (isBookmarked ? '\u2605 Saved' : '\u2606 Save') + '</button>' +
            '<button class="chapter-action-note' + (hasNote ? ' has-note' : '') + '" data-id="' + ch.id + '">' +
            (hasNote ? '\uD83D\uDCCC Note' : '\uD83D\uDCDD Note') + '</button>' +
            '</div>';

        html += '</div>';
        return html;
    }

    // ── Historical Insert Rendering ─────────────────────────
    function renderHistoricalInsert(ch, era) {
        var html = '<div class="historical-insert" id="' + ch.id + '"' +
            ' style="--era-color:' + era.color + '">' +
            '<div style="position:absolute;top:0;left:0;bottom:0;width:4px;background:' + era.color + ';border-radius:6px 0 0 6px"></div>' +
            '<span class="historical-badge">Historical Context</span>' +
            '<h3>' + ch.title + '</h3>' +
            '<div class="synopsis">' + ch.synopsis + '</div>';

        if (ch.cross_refs && ch.cross_refs.length > 0) {
            html += '<div class="cross-refs-section"><h4>Primary Sources</h4>' +
                '<div class="cross-refs-list">';
            ch.cross_refs.forEach(function(xr, i) {
                if (typeof xr === 'string') {
                    html += '<span class="cross-ref-pill type-ot"' +
                        ' data-chapter="' + ch.id + '" data-index="' + i + '"' +
                        ' title="' + escAttr(xr) + '">' + xr + '</span>';
                } else {
                    html += '<span class="cross-ref-pill type-' + (xr.type || 'ot') + '"' +
                        ' data-chapter="' + ch.id + '" data-index="' + i + '"' +
                        ' title="' + escAttr(xr.note || xr.ref || '') + '">' + xr.ref + '</span>';
                }
            });
            html += '</div></div>';
        }

        if (ch.sections && ch.sections.length > 0) {
            html += '<div class="chapter-sections">';
            ch.sections.forEach(function(sec) {
                html += '<div class="section-block">' +
                    '<h4>' + sec.heading + '</h4>' +
                    '<div class="section-body">' + sec.body + '</div></div>';
            });
            html += '</div>';
        }

        html += '</div>';
        return html;
    }

    // ── Thematic Terms (inline objects with term + meaning) ──
    function renderThematicTerms(terms) {
        if (!terms || terms.length === 0) return '';
        var html = '<div class="thematic-terms-section"><h4>Key Terms</h4>' +
            '<div class="thematic-terms-grid">';
        terms.forEach(function(t) {
            html += '<div class="thematic-term-card">' +
                '<div class="tt-term">' + (t.term || '') + '</div>' +
                '<div class="tt-meaning">' + (t.meaning || '') + '</div></div>';
        });
        html += '</div></div>';
        return html;
    }

    // ── Hebrew Terms Grid ───────────────────────────────────
    function renderTermsGrid(termKeys) {
        var terms = termKeys.map(function(k) { return GLOSSARY[k]; }).filter(Boolean);
        if (terms.length === 0) return '';

        return '<div class="terms-section"><h4>Key Terms</h4>' +
            '<div class="terms-grid">' +
            terms.map(function(t) {
                return '<div class="term-card" data-term="' + t.transliteration + '">' +
                    '<div class="term-hebrew">' + t.hebrew + '</div>' +
                    '<div class="term-translit">' + t.transliteration + '</div>' +
                    '<div class="term-strongs">' + t.strongs + '</div>' +
                    '<div class="term-gloss">' + t.gloss + '</div></div>';
            }).join('') +
            '</div></div>';
    }

    // ── Scroll-Spy ───────────────────────────────────────────
    function setupIntersectionObserver() {
        var cards = document.querySelectorAll('.chapter-card, .historical-insert, .hc-fragment');
        if (cards.length === 0) return;

        var observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    var id = entry.target.id;
                    document.querySelectorAll('.chapter-link').forEach(function(link) {
                        link.classList.toggle('active', link.dataset.id === id);
                    });
                    if (id) {
                        history.replaceState(null, '', '#' + id);
                    }
                    syncReadingPane(id);
                }
            });
        }, {
            rootMargin: '-20% 0px -60% 0px',
            threshold: 0
        });

        cards.forEach(function(card) { observer.observe(card); });
    }

    // ── Event Binding ───────────────────────────────────────
    function bindEvents() {
        // Sidebar delegated clicks
        sidebarNav.addEventListener('click', function(e) {
            // Hub back button
            if (e.target.closest('#hubBackBtn') || e.target.closest('.hub-back-btn')) {
                // Scroll to top / reset view
                window.scrollTo(0, 0);
                return;
            }

            // Special action links (Prophecy Matrix, etc.)
            var actionLink = e.target.closest('[data-action]');
            if (actionLink) {
                var action = actionLink.dataset.action;
                if (action === 'prophecy-matrix') {
                    showProphecyMatrix();
                    closeSidebarMobile();
                } else if (action === 'prophecy-tracker') {
                    showProphecyTracker();
                    closeSidebarMobile();
                } else if (action === 'core-beliefs') {
                    showCoreBeliefs();
                    closeSidebarMobile();
                }
                return;
            }

            // Library text links
            var textLink = e.target.closest('.library-text-link');
            if (textLink && !textLink.classList.contains('no-content')) {
                selectText(textLink.dataset.text);
                closeSidebarMobile();
                return;
            }

            // Era toggles
            var toggle = e.target.closest('.era-toggle');
            if (toggle) {
                var eraChapters = document.getElementById('eraChapters-' + toggle.dataset.era);
                if (eraChapters) eraChapters.classList.toggle('open');
                toggle.classList.toggle('active');

                var eraHeader = document.getElementById('era-' + toggle.dataset.era);
                if (eraHeader) {
                    eraHeader.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
                closeSidebarMobile();
                return;
            }

            // Chapter links
            var link = e.target.closest('.chapter-link');
            if (link) {
                scrollToChapter(link.dataset.id);
                closeSidebarMobile();
            }
        });

        // Library cards on main content
        mainContent.addEventListener('click', function(e) {
            // Collapsible section toggle
            var sectionToggle = e.target.closest('[data-toggle="section"]');
            if (sectionToggle) {
                var section = sectionToggle.closest('.library-section');
                if (section) section.classList.toggle('collapsed');
                return;
            }

            // Recent text card — open book landing
            var recentCard = e.target.closest('.library-recent-card');
            if (recentCard && recentCard.dataset.text) {
                showBookLanding(recentCard.dataset.text);
                return;
            }

            var featured = e.target.closest('.library-featured-card');
            if (featured && featured.dataset.text) {
                showBookLanding(featured.dataset.text);
                return;
            }

            // Hidden Treasure card — open book landing
            var treasureCard = e.target.closest('.treasure-card');
            if (treasureCard && treasureCard.dataset.text) {
                showBookLanding(treasureCard.dataset.text);
                return;
            }

            // Text intro collapse toggle
            var collapseBtn = e.target.closest('.intro-collapse-btn');
            if (collapseBtn) {
                var panel = document.getElementById('textIntro');
                if (panel) {
                    var collapsed = panel.classList.toggle('intro-collapsed');
                    localStorage.setItem('atl-intro-collapsed', collapsed ? '1' : '0');
                    collapseBtn.textContent = collapsed ? '\u25BC' : '\u25B2';
                }
                return;
            }

            // Study trail card — open trail detail view (or redirect to article text)
            var trailCard = e.target.closest('.study-trail-card');
            if (trailCard && trailCard.dataset.trail) {
                // Divine Council trail opens the Heavenly Court article text
                if (trailCard.dataset.trail === 'divine-council') {
                    selectText('heavenly_court');
                    window.scrollTo(0, 0);
                    return;
                }
                // Messianic Thread opens its article text (if it exists)
                if (trailCard.dataset.trail === 'messianic-thread' && getTextDef('messianic_thread')) {
                    selectText('messianic_thread');
                    window.scrollTo(0, 0);
                    return;
                }
                // Nephilim & Giants opens its article text (if it exists)
                if (trailCard.dataset.trail === 'nephilim-giants' && getTextDef('nephilim_giants')) {
                    selectText('nephilim_giants');
                    window.scrollTo(0, 0);
                    return;
                }
                // Resurrection trail opens Sheol & Resurrection text
                if (trailCard.dataset.trail === 'resurrection-trail' && getTextDef('sheol_resurrection')) {
                    showBookLanding('sheol_resurrection');
                    window.scrollTo(0, 0);
                    return;
                }
                // Prophetic Matrix trail opens Prophetic Sequence text
                if (trailCard.dataset.trail === 'prophetic-matrix' && getTextDef('prophetic_sequence')) {
                    showBookLanding('prophetic_sequence');
                    window.scrollTo(0, 0);
                    return;
                }
                renderStudyTrail(trailCard.dataset.trail);
                window.scrollTo(0, 0);
                return;
            }

            // Library tool card — open study tools
            var toolCard = e.target.closest('.library-tool-card');
            if (toolCard && toolCard.dataset.action) {
                var action = toolCard.dataset.action;
                if (action === 'show-timeline') openTimeline();
                else if (action === 'show-map') openMap();
                else if (action === 'show-matrix') openMatrix();
                else if (action === 'show-prophecy') showProphecyMatrix();
                else if (action === 'show-hebrew') openHebrew();
                else if (action === 'show-glossary') openGlossary();
                else if (action === 'show-patriarch-chart') openPatriarchChart();
                return;
            }

            // Ancient Library card — open book landing
            var algCard = e.target.closest('.alg-card');
            if (algCard && algCard.dataset.text) {
                showBookLanding(algCard.dataset.text);
                window.scrollTo(0, 0);
                return;
            }

            // Continue Reading — remove card
            var removeRecent = e.target.closest('.recent-remove-btn');
            if (removeRecent) {
                e.stopPropagation();
                var removeId = removeRecent.dataset.removeText;
                var recentArr = JSON.parse(localStorage.getItem('atl-recent-texts') || '[]');
                recentArr = recentArr.filter(function(r) { return r !== removeId; });
                localStorage.setItem('atl-recent-texts', JSON.stringify(recentArr));
                syncAfterChange();
                renderLibraryMain();
                return;
            }

            // Continue Reading — clear all
            var clearAll = e.target.closest('.recent-clear-all');
            if (clearAll) {
                e.stopPropagation();
                localStorage.setItem('atl-recent-texts', '[]');
                syncAfterChange();
                renderLibraryMain();
                return;
            }

            var card = e.target.closest('.library-card');
            if (card && !card.classList.contains('library-card-empty')) {
                showBookLanding(card.dataset.text);
                return;
            }

            var rmtBtn = e.target.closest('.rmt-btn');
            if (rmtBtn) {
                var mode = rmtBtn.dataset.mode;
                var card = rmtBtn.closest('.chapter-card');
                var lazyLoadCard = function(c) {
                    if (mode === 'interlinear') {
                        var ilDiv = c.querySelector('.inline-interlinear');
                        if (ilDiv && !ilDiv.innerHTML.trim()) {
                            ilDiv.innerHTML = renderInlineInterlinear(ilDiv.dataset.text, ilDiv.dataset.ch);
                        }
                    }
                    if (mode === 'scripture') {
                        var scDiv = c.querySelector('.inline-scripture');
                        if (scDiv && !scDiv.innerHTML.trim()) {
                            scDiv.innerHTML = renderInlineScripture(scDiv.dataset.text, scDiv.dataset.ch, scDiv.dataset.chEnd);
                        }
                    }
                };
                if (card) {
                    card.querySelectorAll('.rmt-btn').forEach(function(b) { b.classList.toggle('active', b === rmtBtn); });
                    card.className = card.className.replace(/\bmode-\w+/g, '').trim();
                    if (mode !== 'study') card.classList.add('mode-' + mode);
                    lazyLoadCard(card);
                }
                // Apply to ALL chapter cards on page (global mode switch)
                document.querySelectorAll('.chapter-card').forEach(function(c) {
                    if (c === card) return;
                    c.className = c.className.replace(/\bmode-\w+/g, '').trim();
                    if (mode !== 'study') c.classList.add('mode-' + mode);
                    c.querySelectorAll('.rmt-btn').forEach(function(b) { b.classList.toggle('active', b.dataset.mode === mode); });
                    lazyLoadCard(c);
                });
                readingMode = mode;
                localStorage.setItem('atl-reading-mode', mode);
                syncAfterChange();
                return;
            }

            var readCheck = e.target.closest('.read-check');
            if (readCheck) {
                toggleChapterRead(readCheck.dataset.id);
                return;
            }

            var copyBtn = e.target.closest('.chapter-copy-btn');
            if (copyBtn) {
                e.stopPropagation();
                copyStudyContent(copyBtn.dataset.id);
                return;
            }

            var exportBtn = e.target.closest('.chapter-export-btn');
            if (exportBtn) {
                e.stopPropagation();
                exportChapterMarkdown(exportBtn.dataset.id);
                return;
            }

            var btn = e.target.closest('.bookmark-btn');
            if (btn) {
                toggleBookmark(btn.dataset.id);
                return;
            }

            // Mobile action bar — Mark as Read
            var actionRead = e.target.closest('.chapter-action-read');
            if (actionRead) {
                toggleChapterRead(actionRead.dataset.id);
                var wasRead = actionRead.classList.toggle('is-read');
                actionRead.textContent = wasRead ? '\u2714 Read' : '\u25CB Mark as Read';
                return;
            }

            // Mobile action bar — Bookmark
            var actionBookmark = e.target.closest('.chapter-action-bookmark');
            if (actionBookmark) {
                toggleBookmark(actionBookmark.dataset.id);
                var wasSaved = actionBookmark.classList.toggle('is-bookmarked');
                actionBookmark.textContent = wasSaved ? '\u2605 Saved' : '\u2606 Save';
                return;
            }

            // Mobile action bar — Study Note
            var actionNote = e.target.closest('.chapter-action-note');
            if (actionNote) {
                openStudyNoteEditor(actionNote.dataset.id);
                return;
            }

            // Study note edit/delete buttons
            var noteEdit = e.target.closest('.study-note-edit');
            if (noteEdit) {
                openStudyNoteEditor(noteEdit.dataset.id);
                return;
            }
            var noteDelete = e.target.closest('.study-note-delete');
            if (noteDelete) {
                deleteStudyNote(noteDelete.dataset.id);
                return;
            }

            var pill = e.target.closest('.cross-ref-pill');
            if (pill) {
                openXrefDrawer(pill.dataset.chapter, parseInt(pill.dataset.index));
                return;
            }

            var termCard = e.target.closest('.term-card');
            if (termCard) {
                openGlossary(termCard.dataset.term);
                return;
            }

            // THC ↔ Library navigation links
            var navLink = e.target.closest('[data-navigate-text]');
            if (navLink) {
                var targetText = navLink.dataset.navigateText;
                var targetId = navLink.dataset.navigateId;
                selectText(targetText, true);
                requestAnimationFrame(function() {
                    location.hash = targetId;
                });
                return;
            }

            // Related studies / reverse citation navigation
            var relStudy = e.target.closest('.related-study-item');
            if (relStudy && relStudy.dataset.navText) {
                selectText(relStudy.dataset.navText, true);
                requestAnimationFrame(function() {
                    var targetCh = relStudy.dataset.navChapter;
                    if (targetCh) scrollToChapter(targetCh);
                });
                return;
            }

            // Study trail — "Open full chapter" link or step without scripture
            var trailGoLink = e.target.closest('.trail-step-go-link');
            var trailStep = e.target.closest('.trail-step');
            if (trailGoLink && trailGoLink.dataset.navText) {
                selectText(trailGoLink.dataset.navText, true);
                if (trailGoLink.dataset.navChapter) {
                    requestAnimationFrame(function() {
                        scrollToChapter(trailGoLink.dataset.navChapter);
                    });
                }
                return;
            }
            if (trailStep && !trailStep.classList.contains('has-scripture') && trailStep.dataset.navText) {
                selectText(trailStep.dataset.navText, true);
                if (trailStep.dataset.navChapter) {
                    requestAnimationFrame(function() {
                        scrollToChapter(trailStep.dataset.navChapter);
                    });
                }
                return;
            }

            // Breadcrumb "Library" link
            var bcLink = e.target.closest('[data-action="go-library"]');
            if (bcLink) {
                showLibrary();
                return;
            }

            // Single-chapter nav buttons (indicator + bottom nav)
            var schBtn = e.target.closest('[data-sch-delta]');
            if (schBtn && singleChapterMode) {
                navigateChapter(parseInt(schBtn.dataset.schDelta));
                return;
            }

            // "Show All Chapters" button
            var showAllBtn = e.target.closest('#schShowAll');
            if (showAllBtn && singleChapterMode) {
                singleChapterMode = false;
                delete textContentCache[currentText];
                loadTextContent(currentText);
                singleChapterMode = true; // re-enable for next text
                return;
            }

            // Prev/Next chapter navigation
            var navBtn = e.target.closest('.chapter-nav-btn');
            if (navBtn && navBtn.dataset.navTo) {
                scrollToChapter(navBtn.dataset.navTo);
                return;
            }

            // Glossary terms in THC fragments — click transliteration to open glossary
            var pwTranslit = e.target.closest('.hc-fragment .pw-translit');
            if (pwTranslit) {
                var term = pwTranslit.textContent.trim();
                openGlossary(term);
                return;
            }
        });

        // Cross-reference preview tooltip on hover
        (function() {
            var tooltip = document.createElement('div');
            tooltip.className = 'xref-tooltip';
            tooltip.style.display = 'none';
            document.body.appendChild(tooltip);
            var hideTimer = null;

            function showTooltip(pill) {
                var chId = pill.dataset.chapter;
                var idx = parseInt(pill.dataset.index);
                var ch = getChapterById(chId);
                if (!ch || !ch.cross_refs || !ch.cross_refs[idx]) return;
                var xr = normXref(ch.cross_refs[idx]);
                var typeLabel = xr.type ? xr.type.replace(/-/g, ' ').replace(/\b\w/g, function(c) { return c.toUpperCase(); }) : '';
                tooltip.innerHTML = '<div class="xref-tt-ref">' + xr.ref + '</div>' +
                    (typeLabel ? '<span class="xref-tt-type type-' + xr.type + '">' + typeLabel + '</span>' : '') +
                    '<div class="xref-tt-note">' + xr.note + '</div>' +
                    '<div class="xref-tt-hint">Click to explore &rarr;</div>';
                tooltip.style.display = 'block';

                var rect = pill.getBoundingClientRect();
                var ttRect = tooltip.getBoundingClientRect();
                var left = rect.left + rect.width / 2 - ttRect.width / 2;
                var top = rect.top - ttRect.height - 8;
                if (top < 8) top = rect.bottom + 8;
                if (left < 8) left = 8;
                if (left + ttRect.width > window.innerWidth - 8) left = window.innerWidth - ttRect.width - 8;
                tooltip.style.left = left + 'px';
                tooltip.style.top = top + 'px';
            }

            mainContent.addEventListener('mouseover', function(e) {
                var pill = e.target.closest('.cross-ref-pill');
                if (pill) {
                    clearTimeout(hideTimer);
                    showTooltip(pill);
                }
            });
            mainContent.addEventListener('mouseout', function(e) {
                var pill = e.target.closest('.cross-ref-pill');
                if (pill) {
                    hideTimer = setTimeout(function() { tooltip.style.display = 'none'; }, 200);
                }
            });
            tooltip.addEventListener('mouseover', function() { clearTimeout(hideTimer); });
            tooltip.addEventListener('mouseout', function() {
                hideTimer = setTimeout(function() { tooltip.style.display = 'none'; }, 200);
            });
        })();

        // Swipe gesture for single-chapter navigation
        (function() {
            var swStartX = 0, swStartY = 0, swTracking = false;
            mainContent.addEventListener('touchstart', function(e) {
                if (!singleChapterMode) return;
                swStartX = e.touches[0].clientX;
                swStartY = e.touches[0].clientY;
                swTracking = true;
            }, { passive: true });
            mainContent.addEventListener('touchend', function(e) {
                if (!singleChapterMode || !swTracking) return;
                swTracking = false;
                var dx = e.changedTouches[0].clientX - swStartX;
                var dy = e.changedTouches[0].clientY - swStartY;
                // Horizontal swipe must be dominant and > 60px
                if (Math.abs(dx) > 60 && Math.abs(dx) > Math.abs(dy) * 1.8) {
                    navigateChapter(dx > 0 ? -1 : 1);
                }
            }, { passive: true });
        })();

        // Search — sidebar input opens the full overlay
        searchInput.addEventListener('focus', function() {
            searchInput.blur();
            openSearchOverlay();
        });

        // Keyboard shortcuts
        document.addEventListener('keydown', function(e) {
            if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
                e.preventDefault();
                openSearchOverlay();
            }
            if (e.altKey && e.key === 'h') {
                e.preventDefault();
                toggleReadingPane();
            }
            if (e.altKey && e.key === 'f') {
                e.preventDefault();
                toggleReadingPaneFullscreen();
            }
            if (e.altKey && e.key === 'l') {
                e.preventDefault();
                showLibrary();
            }
            if (readingPaneOpen && document.activeElement === document.body) {
                if (e.key === 'ArrowLeft' && e.altKey) {
                    e.preventDefault();
                    if (currentILChapter > 1) renderInterlinear(currentILChapter - 1);
                }
                if (e.key === 'ArrowRight' && e.altKey) {
                    e.preventDefault();
                    var maxCh = getTextMaxChapter(currentILBook);
                    if (currentILChapter < maxCh) renderInterlinear(currentILChapter + 1);
                }
            }
            if (e.key === 'Escape') {
                var helpOverlay = document.getElementById('shortcutHelp');
                if (helpOverlay.classList.contains('open')) {
                    helpOverlay.classList.remove('open');
                    return;
                }
                if (document.body.classList.contains('reading-pane-fullscreen')) {
                    document.body.classList.remove('reading-pane-fullscreen');
                    return;
                }
                closeWordPopup();
                closeXrefDrawer();
                closeGlossary();
                closeProgress();
                closeMatrix();
                closeTimeline();
                closePatriarchChart();
            }
            // ? key opens keyboard shortcut help (only when not typing in an input)
            if (e.key === '?' && !e.ctrlKey && !e.altKey && !e.metaKey) {
                var tag = document.activeElement.tagName;
                if (tag !== 'INPUT' && tag !== 'TEXTAREA' && !document.activeElement.isContentEditable) {
                    e.preventDefault();
                    document.getElementById('shortcutHelp').classList.toggle('open');
                }
            }
        });

        // XRef drawer close
        document.getElementById('xrefClose').addEventListener('click', closeXrefDrawer);

        // XRef "Go" navigation links
        xrefContent.addEventListener('click', function(e) {
            var goLink = e.target.closest('.xref-goto');
            if (goLink) {
                e.preventDefault();
                var ref = goLink.dataset.ref;
                closeXrefDrawer();
                navigateToScriptureRef(ref);
            }
        });

        // Map buttons
        document.getElementById('mapBtn').addEventListener('click', openMap);
        document.getElementById('mapClose').addEventListener('click', closeMap);
        var mapOverlayEl = document.getElementById('mapOverlay');
        mapOverlayEl.addEventListener('click', function(e) { if (e.target === mapOverlayEl) closeMap(); });

        // Resources buttons
        document.getElementById('resourcesBtn').addEventListener('click', openResources);
        document.getElementById('resourcesClose').addEventListener('click', closeResources);
        resourcesOverlay.addEventListener('click', function(e) { if (e.target === resourcesOverlay) closeResources(); });
        resourcesSearch.addEventListener('input', function() { filterResources(resourcesSearch.value.trim()); });

        // Glossary buttons
        document.getElementById('glossaryBtn').addEventListener('click', function() { openGlossary(); });
        document.getElementById('glossaryClose').addEventListener('click', closeGlossary);

        // Progress page
        document.getElementById('progressBtn').addEventListener('click', openProgress);
        document.getElementById('progressClose').addEventListener('click', closeProgress);
        var progressOverlay = document.getElementById('progressOverlay');
        progressOverlay.addEventListener('click', function(e) {
            if (e.target === progressOverlay) closeProgress();
        });

        // Bible Truth Matrix
        document.getElementById('matrixBtn').addEventListener('click', openMatrix);
        document.getElementById('matrixClose').addEventListener('click', closeMatrix);
        matrixOverlay.addEventListener('click', function(e) { if (e.target === matrixOverlay) closeMatrix(); });

        // Biblical Timeline
        document.getElementById('timelineBtn').addEventListener('click', openTimeline);
        document.getElementById('timelineClose').addEventListener('click', closeTimeline);
        timelineOverlay.addEventListener('click', function(e) { if (e.target === timelineOverlay) closeTimeline(); });

        // Patriarch Ages Chart
        var patriarchBtn = document.getElementById('patriarchChartBtn');
        if (patriarchBtn) patriarchBtn.addEventListener('click', openPatriarchChart);
        var patriarchClose = document.getElementById('patriarchChartClose');
        if (patriarchClose) patriarchClose.addEventListener('click', closePatriarchChart);
        if (patriarchChartOverlay) patriarchChartOverlay.addEventListener('click', function(e) { if (e.target === patriarchChartOverlay) closePatriarchChart(); });
        // Keyboard Shortcut Help
        var shortcutHelpOverlay = document.getElementById('shortcutHelp');
        document.getElementById('shortcutHelpBtn').addEventListener('click', function() {
            shortcutHelpOverlay.classList.toggle('open');
        });
        document.getElementById('shortcutHelpClose').addEventListener('click', function() {
            shortcutHelpOverlay.classList.remove('open');
        });
        shortcutHelpOverlay.addEventListener('click', function(e) {
            if (e.target === shortcutHelpOverlay) shortcutHelpOverlay.classList.remove('open');
        });

        // Hebrew Learning
        document.getElementById('hebrewBtn').addEventListener('click', openHebrew);
        document.getElementById('hebrewClose').addEventListener('click', closeHebrew);
        var hebrewOverlayEl = document.getElementById('hebrewOverlay');
        hebrewOverlayEl.addEventListener('click', function(e) { if (e.target === hebrewOverlayEl) closeHebrew(); });
        document.querySelectorAll('.hl-tab').forEach(function(tab) {
            tab.addEventListener('click', function() {
                document.querySelectorAll('.hl-tab').forEach(function(t) { t.classList.remove('active'); });
                tab.classList.add('active');
                renderHebrewTab(tab.dataset.tab);
            });
        });

        glossaryOverlay.addEventListener('click', function(e) {
            if (e.target === glossaryOverlay) closeGlossary();
        });
        glossarySearch.addEventListener('input', function() { filterGlossary(glossarySearch.value.trim()); });

        // Sidebar mobile toggle
        sidebarToggle.addEventListener('click', function() {
            sidebar.classList.toggle('open');
            sidebarBackdrop.classList.toggle('visible');
        });
        sidebarBackdrop.addEventListener('click', closeSidebarMobile);

        // Reading pane
        readingPaneToggle.addEventListener('click', toggleReadingPane);
        document.getElementById('readingPaneClose').addEventListener('click', function() {
            setReadingPane(false);
        });
        document.getElementById('readingPaneExpand').addEventListener('click', toggleReadingPaneFullscreen);

        // Font size controls
        document.getElementById('fontIncrease').addEventListener('click', function() { adjustFontScale(0.1); });
        document.getElementById('fontDecrease').addEventListener('click', function() { adjustFontScale(-0.1); });

        // Reading progress bar
        readingPaneContent.addEventListener('scroll', updateReadingProgress);
        readingPaneModeSelect.addEventListener('change', function(e) {
            setReadingPaneMode(e.target.value);
        });

        // Sync buttons
        document.getElementById('syncToStudy').addEventListener('click', syncStudyToPane);
        document.getElementById('syncToPane').addEventListener('click', syncPaneToStudy);

        // Prev/Next chapter navigation in reading pane
        document.getElementById('ilPrev').addEventListener('click', function() {
            if (currentILChapter > 1) renderInterlinear(currentILChapter - 1);
        });
        document.getElementById('ilNext').addEventListener('click', function() {
            var maxCh = getTextMaxChapter(currentILBook);
            if (currentILChapter < maxCh) renderInterlinear(currentILChapter + 1);
        });

        // Book selector in reading pane — populate dynamically from texts with interlinear data
        var ilBookSelect = document.getElementById('ilBookSelect');
        if (ilBookSelect) {
            ilBookSelect.innerHTML = '';
            var otGroup = document.createElement('optgroup');
            otGroup.label = 'Old Testament — Hebrew';
            var ntGroup = document.createElement('optgroup');
            ntGroup.label = 'New Testament — Greek';
            texts.forEach(function(t) {
                var il = getTextInterlinear(t.id);
                if (Object.keys(il).length > 0) {
                    var opt = document.createElement('option');
                    opt.value = t.id;
                    opt.textContent = t.name;
                    if (isGreekText(t.id)) {
                        ntGroup.appendChild(opt);
                    } else {
                        otGroup.appendChild(opt);
                    }
                }
            });
            if (otGroup.children.length > 0) ilBookSelect.appendChild(otGroup);
            if (ntGroup.children.length > 0) ilBookSelect.appendChild(ntGroup);
            ilBookSelect.value = currentILBook;
            ilBookSelect.addEventListener('change', function() {
                var newBook = ilBookSelect.value;
                if (newBook !== currentILBook) {
                    currentILBook = newBook;
                    renderInterlinear(1);
                }
            });
        }

        // Reading pane word clicks, verse copy, and verse number clicks
        readingPaneContent.addEventListener('click', function(e) {
            var wordEl = e.target.closest('.il-word');
            if (wordEl) {
                showWordPopup(wordEl);
                return;
            }
            var copyBtn = e.target.closest('.il-verse-copy');
            if (copyBtn) {
                copyVerse(parseInt(copyBtn.dataset.verse));
                return;
            }
            var verseNum = e.target.closest('.il-verse-num');
            if (verseNum) {
                var verse = verseNum.closest('.il-verse');
                if (verse) {
                    verse.scrollIntoView({ behavior: 'smooth', block: 'start' });
                    verse.classList.add('flash');
                    setTimeout(function() { verse.classList.remove('flash'); }, 1000);
                }
                return;
            }
        });

        // Copy chapter dropdown
        document.getElementById('ilCopyBtn').addEventListener('click', function(e) {
            e.stopPropagation();
            document.getElementById('ilCopyDropdown').classList.toggle('open');
        });
        document.getElementById('ilCopyDropdown').addEventListener('click', function(e) {
            var opt = e.target.closest('.il-copy-option');
            if (opt) {
                copyChapter(opt.dataset.format);
                document.getElementById('ilCopyDropdown').classList.remove('open');
            }
        });

        // User mode buttons
        document.addEventListener('click', function(e) {
            var modeBtn = e.target.closest('.user-mode-btn');
            if (modeBtn && modeBtn.dataset.mode) {
                setUserMode(modeBtn.dataset.mode);
                if (currentILChapter) renderInterlinear(currentILChapter);
            }
            var rowBtn = e.target.closest('.il-row-toggle');
            if (rowBtn && rowBtn.dataset.row) {
                toggleILRow(rowBtn.dataset.row);
            }
            var hcBtn = e.target.closest('#hcToggle');
            if (hcBtn) toggleHighContrast();
        });

        // Dismiss copy dropdown and word popup on click outside
        document.addEventListener('click', function(e) {
            if (wordPopup.classList.contains('visible') &&
                !wordPopup.contains(e.target) &&
                !e.target.closest('.il-word')) {
                closeWordPopup();
            }
            if (!e.target.closest('.il-copy-menu')) {
                document.getElementById('ilCopyDropdown').classList.remove('open');
            }
        });

        // Double-click on study content -> sync reading pane
        mainContent.addEventListener('dblclick', function(e) {
            var chCard = e.target.closest('.chapter-card');
            if (chCard) {
                var match = chCard.id.match(/^(gen|exod|lev|num|deut|josh)-(\d+)/);
                if (match) {
                    currentILBook = prefixToTextId(match[1]);
                    renderInterlinear(parseInt(match[2]));
                    if (!readingPaneOpen) setReadingPane(true);
                    showCopyToast('Synced to ' + getTextName(currentILBook) + ' ' + match[2]);
                }
            }
        });

        // Double-click on reading pane -> sync study
        readingPaneContent.addEventListener('dblclick', function(e) {
            if (e.target.closest('.il-word')) return;
            syncStudyToPane();
            showCopyToast('Synced study to ' + getTextName(currentILBook) + ' ' + currentILChapter);
        });

        // Hash change
        window.addEventListener('hashchange', handleHash);
    }

    // ── Navigation ──────────────────────────────────────────
    function scrollToChapter(id) {
        logEvent('chapter_view', id);

        // Single-chapter mode — navigate to chapter by index
        if (singleChapterMode && currentText) {
            var flatChapters = getFlatChapterList(currentText);
            for (var i = 0; i < flatChapters.length; i++) {
                if (flatChapters[i].id === id) {
                    renderSingleChapterView(currentText, i);
                    return;
                }
            }
        }

        var el = document.getElementById(id);
        if (el) {
            el.scrollIntoView({ behavior: 'smooth', block: 'start' });
            el.classList.add('flash');
            setTimeout(function() { el.classList.remove('flash'); }, 1000);
        }
    }

    function closeAllOverlays() {
        closeGlossary();
        closeResources();
        closeHebrew();
        closeMap();
        closeMatrix();
        closeTimeline();
        closePatriarchChart();
        closeXrefDrawer();
        closeSidebarMobile();
        // Close mobile search overlay if open
        var searchOv = document.getElementById('searchOverlay');
        if (searchOv) searchOv.remove();
        // Close mobile tools popup if open
        var toolsOv = document.getElementById('mobileToolsOverlay');
        if (toolsOv) toolsOv.remove();
    }

    var hashHandling = false; // guard against recursive hash changes
    function handleHash() {
        if (hashHandling) return;
        var hash = location.hash.slice(1);

        // Book Landing Page
        if (hash.startsWith('book/')) {
            var bookId = hash.slice(5);
            hashHandling = true;
            showBookLanding(bookId);
            hashHandling = false;
            return;
        }

        // Bible Mode — hash has 1-based chapter, convert to 0-based index
        if (hash.startsWith('read/')) {
            var parts = hash.split('/');
            var chapterNum = parseInt(parts[2]) || 1;
            hashHandling = true;
            showBibleMode(parts[1], chapterNum - 1);
            hashHandling = false;
            return;
        }

        if (!hash || hash === 'library') {
            if (libraryMode) return;
            if (!hash) {
                if (!currentText && libraryMode) return;
                if (currentText) {
                    window.scrollTo(0, 0);
                    return;
                }
                showLibrary();
            }
            return;
        }

        if (hash === 'glossary') {
            openGlossary();
            return;
        }
        if (hash === 'resources') {
            openResources();
            return;
        }

        // Detect text from hash and switch if needed
        var textFromHash = detectTextFromHash(hash);
        if (textFromHash && textFromHash !== currentText) {
            selectText(textFromHash, true);
        }

        // Era navigation
        if (hash.startsWith('era-')) {
            var eraEl = document.getElementById(hash);
            if (eraEl) {
                eraEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
            return;
        }

        requestAnimationFrame(function() { scrollToChapter(hash); });
    }

    function closeSidebarMobile() {
        sidebar.classList.remove('open');
        sidebarBackdrop.classList.remove('visible');
    }

    // ── Bookmarks ───────────────────────────────────────────
    function toggleBookmark(id) {
        var idx = bookmarks.indexOf(id);
        if (idx >= 0) {
            bookmarks.splice(idx, 1);
        } else {
            bookmarks.push(id);
        }
        localStorage.setItem('genesis-study-bookmarks', JSON.stringify(bookmarks));
        syncAfterChange();
        renderBookmarks();

        var btn = document.querySelector('.bookmark-btn[data-id="' + id + '"]');
        if (btn) {
            var isNow = bookmarks.includes(id);
            btn.classList.toggle('bookmarked', isNow);
            btn.textContent = isNow ? '\u2605' : '\u2606';
        }
    }

    // ── Reading Progress ─────────────────────────────────────
    function isChapterRead(chapterId) {
        return readChapters[chapterId] === true;
    }

    function toggleChapterRead(chapterId) {
        if (readChapters[chapterId]) {
            delete readChapters[chapterId];
        } else {
            readChapters[chapterId] = true;
        }
        localStorage.setItem('atl-read-chapters', JSON.stringify(readChapters));
        syncAfterChange();
        // Update the checkbox in the chapter card
        var cb = document.querySelector('.read-check[data-id="' + chapterId + '"]');
        if (cb) {
            cb.checked = !!readChapters[chapterId];
            cb.closest('.chapter-card').classList.toggle('chapter-read', !!readChapters[chapterId]);
        }
        // Update sidebar chapter link
        var sideLink = document.querySelector('.chapter-link[data-id="' + chapterId + '"]');
        if (sideLink) {
            sideLink.classList.toggle('ch-read', !!readChapters[chapterId]);
            var dot = sideLink.querySelector('.ch-read-dot');
            if (readChapters[chapterId] && !dot) {
                sideLink.insertAdjacentHTML('afterbegin', '<span class="ch-read-dot">\u2713</span>');
            } else if (!readChapters[chapterId] && dot) {
                dot.remove();
            }
        }
        updateSidebarReadCounts();
    }

    function getTextReadCount(textId) {
        var eras = getTextEras(textId);
        var total = 0, read = 0;
        eras.forEach(function(era) {
            var chapters = ERA_DATA[era.id] || [];
            chapters.forEach(function(ch) {
                if (ch.type === 'html_fragment') return;
                total++;
                if (readChapters[ch.id]) read++;
            });
        });
        return { read: read, total: total };
    }

    function updateSidebarReadCounts() {
        document.querySelectorAll('.sidebar-read-count').forEach(function(el) {
            var textId = el.dataset.text;
            if (!textId) return;
            var counts = getTextReadCount(textId);
            el.textContent = counts.read + '/' + counts.total;
            el.classList.toggle('all-read', counts.read === counts.total && counts.total > 0);
        });
    }

    function renderBookmarks() {
        if (bookmarks.length === 0) {
            bookmarksContainer.innerHTML = '<div style="font-size:0.75rem;color:var(--text-muted);padding:4px 0">No bookmarks yet</div>';
            return;
        }

        var html = '';
        bookmarks.forEach(function(id) {
            var title = id;
            for (var i = 0; i < MANIFEST.eras.length; i++) {
                var ch = (ERA_DATA[MANIFEST.eras[i].id] || []).find(function(c) { return c.id === id; });
                if (ch) { title = ch.ref || ch.title; break; }
            }
            html += '<div class="bookmark-item" data-id="' + id + '">' +
                '<span>' + title + '</span>' +
                '<button class="bookmark-remove" data-id="' + id + '">&times;</button></div>';
        });
        bookmarksContainer.innerHTML = html;

        bookmarksContainer.querySelectorAll('.bookmark-item').forEach(function(item) {
            item.addEventListener('click', function(e) {
                if (e.target.closest('.bookmark-remove')) {
                    toggleBookmark(e.target.closest('.bookmark-remove').dataset.id);
                    return;
                }
                // Navigate to bookmarked chapter
                var bId = item.dataset.id;
                var textFromHash = detectTextFromHash(bId);
                if (textFromHash && textFromHash !== currentText) {
                    selectText(textFromHash, true);
                }
                location.hash = bId;
            });
        });
    }

    // ── Unified Search Engine ─────────────────────────────────
    var flowSearchIndex = null;
    var searchOverlayActive = false;
    var activeSearchFilter = 'all';

    // Bigram extraction for fuzzy matching
    function bigramSet(word) {
        var bg = [];
        for (var i = 0; i < word.length - 1; i++) bg.push(word.substring(i, i + 2));
        return bg;
    }

    // Find similar words using Dice coefficient on bigrams
    function findSimilarWords(query, threshold) {
        threshold = threshold || 0.45;
        if (!SEARCH_INDEX || !SEARCH_INDEX.bigrams) return [];
        var qBigrams = bigramSet(query.toLowerCase());
        if (qBigrams.length === 0) return [];
        var candidates = {};
        qBigrams.forEach(function(bg) {
            (SEARCH_INDEX.bigrams[bg] || []).forEach(function(wordIdx) {
                candidates[wordIdx] = (candidates[wordIdx] || 0) + 1;
            });
        });
        var results = [];
        var words = SEARCH_INDEX.words;
        Object.keys(candidates).forEach(function(idx) {
            var word = words[idx];
            var wBigrams = bigramSet(word);
            var dice = (2 * candidates[idx]) / (qBigrams.length + wBigrams.length);
            if (dice >= threshold && word !== query.toLowerCase()) {
                results.push({ word: word, score: dice });
            }
        });
        return results.sort(function(a, b) { return b.score - a.score; }).slice(0, 5);
    }

    // Match Q&A entries by keyword overlap
    function matchQA(tokens) {
        if (!SEARCH_QA || !SEARCH_QA.length) return [];
        var query = tokens.join(' ');
        var results = [];
        SEARCH_QA.forEach(function(qa) {
            var score = 0;
            var kws = qa.keywords || [];
            // Check full-phrase match against keywords
            kws.forEach(function(kw) {
                if (query.indexOf(kw.toLowerCase()) >= 0) score += 3;
            });
            // Check individual token matches
            tokens.forEach(function(token) {
                kws.forEach(function(kw) {
                    if (kw.toLowerCase().indexOf(token) >= 0) score += 1;
                });
                // Check question text
                if (qa.question.toLowerCase().indexOf(token) >= 0) score += 1;
            });
            if (score >= 3 || (tokens.length <= 2 && score >= 2)) {
                results.push({ qa: qa, score: score });
            }
        });
        return results.sort(function(a, b) { return b.score - a.score; }).slice(0, 3);
    }

    // Search the pre-built index (chapters, glossary, prophecies, religions, beliefs, resources)
    function searchPreBuiltIndex(tokens, filter) {
        if (!SEARCH_INDEX || !SEARCH_INDEX.docs) return [];
        var phrase = tokens.join(' ');
        var results = [];
        var typeMap = { 'ch': 'study', 'gl': 'glossary', 'pr': 'prophecy', 'rl': 'religion', 'bl': 'belief', 'rs': 'resource' };
        var filterType = null;
        if (filter === 'study') filterType = 'ch';
        else if (filter === 'glossary') filterType = 'gl';
        else if (filter === 'prophecy') filterType = 'pr';
        else if (filter === 'religion') filterType = 'rl';

        SEARCH_INDEX.docs.forEach(function(doc) {
            if (filterType && doc.t !== filterType) return;
            var score = 0;
            var titleLow = doc.ti.toLowerCase();
            var refLow = (doc.r || '').toLowerCase();
            var tokLow = doc.tk;

            // Exact phrase in tokens
            if (tokLow.indexOf(phrase) >= 0) score += 5;

            // Title matches
            tokens.forEach(function(t) {
                if (titleLow.indexOf(t) >= 0) score += 10;
                if (refLow.indexOf(t) >= 0) score += 8;
                if (tokLow.indexOf(t) >= 0) score += 3;
            });

            // All tokens present bonus
            var allPresent = tokens.every(function(t) { return tokLow.indexOf(t) >= 0; });
            if (allPresent && tokens.length > 1) score += 4;

            if (score > 0) {
                // Extract context snippet
                var context = doc.sn || '';
                var idx = tokLow.indexOf(tokens[0]);
                if (idx >= 0 && doc.tk.length > 150) {
                    var start = Math.max(0, idx - 40);
                    var end = Math.min(doc.tk.length, idx + 80);
                    context = (start > 0 ? '...' : '') + doc.tk.substring(start, end) + (end < doc.tk.length ? '...' : '');
                }
                results.push({
                    type: typeMap[doc.t] || 'study',
                    docType: doc.t,
                    id: doc.id,
                    textId: doc.x || '',
                    eraId: doc.e || '',
                    title: doc.ti,
                    ref: doc.r || '',
                    snippet: context,
                    score: score
                });
            }
        });
        return results.sort(function(a, b) { return b.score - a.score; }).slice(0, 30);
    }

    // Build flow verse index lazily
    function buildFlowSearchIndex() {
        if (flowSearchIndex) return;
        flowSearchIndex = [];
        texts.forEach(function(t) {
            var il = getTextInterlinear(t.id);
            if (!il || Object.keys(il).length === 0) return;
            var bookName = t.name;
            Object.keys(il).forEach(function(chKey) {
                var chNum = parseInt(chKey);
                var chData = il[chKey];
                if (!chData || !chData.verses) return;
                chData.verses.forEach(function(verse) {
                    if (!verse.flow) return;
                    flowSearchIndex.push({
                        textId: t.id, bookName: bookName,
                        ch: chNum, v: verse.num,
                        flow: verse.flow, note: verse.note || ''
                    });
                });
            });
        });
    }

    // Search flow verses
    function searchFlowVerses(tokens) {
        buildFlowSearchIndex();
        if (!flowSearchIndex) return [];
        var phrase = tokens.join(' ');
        var results = [];
        flowSearchIndex.forEach(function(entry) {
            var flowLower = entry.flow.toLowerCase();
            var idx = flowLower.indexOf(phrase);
            if (idx < 0) {
                // Try all tokens present
                var all = tokens.every(function(t) { return flowLower.indexOf(t) >= 0; });
                if (!all) return;
                idx = flowLower.indexOf(tokens[0]);
            }
            if (idx >= 0) {
                var start = Math.max(0, idx - 30);
                var end = Math.min(entry.flow.length, idx + 70);
                var context = (start > 0 ? '...' : '') + entry.flow.substring(start, end) + (end < entry.flow.length ? '...' : '');
                results.push({
                    type: 'verse', docType: 'vs',
                    id: null, textId: entry.textId,
                    ref: entry.bookName + ' ' + entry.ch + ':' + entry.v,
                    title: entry.bookName + ' ' + entry.ch + ':' + entry.v,
                    snippet: context, score: 5,
                    ch: entry.ch
                });
            }
        });
        return results.slice(0, 20);
    }

    // Recent searches
    function saveRecentSearch(query) {
        var recent = JSON.parse(localStorage.getItem('atl-recent-searches') || '[]');
        recent = recent.filter(function(s) { return s !== query; });
        recent.unshift(query);
        if (recent.length > 10) recent = recent.slice(0, 10);
        localStorage.setItem('atl-recent-searches', JSON.stringify(recent));
    }
    function getRecentSearches() {
        return JSON.parse(localStorage.getItem('atl-recent-searches') || '[]');
    }

    // Type badge config
    var searchBadges = {
        qa:       { label: 'Q&A',      cls: 'badge-qa' },
        study:    { label: 'Study',     cls: 'badge-study' },
        verse:    { label: 'Verse',     cls: 'badge-verse' },
        glossary: { label: 'Term',      cls: 'badge-glossary' },
        prophecy: { label: 'Prophecy',  cls: 'badge-prophecy' },
        religion: { label: 'Religion',  cls: 'badge-religion' },
        belief:   { label: 'Belief',    cls: 'badge-belief' },
        resource: { label: 'Resource',  cls: 'badge-resource' }
    };

    // ── Search Overlay ────────────────────────────────────────
    function openSearchOverlay() {
        if (searchOverlayActive) return;
        searchOverlayActive = true;
        activeSearchFilter = 'all';

        var overlay = document.createElement('div');
        overlay.id = 'searchOverlayUnified';
        overlay.className = 'search-overlay-unified';
        overlay.innerHTML =
            '<div class="search-overlay-backdrop"></div>' +
            '<div class="search-overlay-panel">' +
                '<div class="search-overlay-header">' +
                    '<div class="search-overlay-input-wrap">' +
                        '<span class="search-overlay-icon">\ud83d\udd0d</span>' +
                        '<input type="text" id="searchOverlayInput" class="search-overlay-input" placeholder="Search everything... chapters, verses, glossary, questions" autocomplete="off" />' +
                        '<kbd class="search-overlay-esc">ESC</kbd>' +
                    '</div>' +
                    '<div class="search-overlay-filters" id="searchFilters">' +
                        '<button class="search-filter-chip active" data-filter="all">All</button>' +
                        '<button class="search-filter-chip" data-filter="study">Study</button>' +
                        '<button class="search-filter-chip" data-filter="verse">Verses</button>' +
                        '<button class="search-filter-chip" data-filter="glossary">Glossary</button>' +
                        '<button class="search-filter-chip" data-filter="qa">Q&A</button>' +
                        '<button class="search-filter-chip" data-filter="prophecy">Prophecy</button>' +
                        '<button class="search-filter-chip" data-filter="religion">Religions</button>' +
                    '</div>' +
                '</div>' +
                '<div class="search-overlay-results" id="searchOverlayResults"></div>' +
            '</div>';

        document.body.appendChild(overlay);

        var input = document.getElementById('searchOverlayInput');
        var resultsEl = document.getElementById('searchOverlayResults');
        var filtersEl = document.getElementById('searchFilters');
        var debounce = null;

        // Show recent searches
        showRecentSearches(resultsEl);

        // Focus input
        setTimeout(function() { input.focus(); }, 50);

        // Filter chips
        filtersEl.addEventListener('click', function(e) {
            var chip = e.target.closest('.search-filter-chip');
            if (!chip) return;
            filtersEl.querySelectorAll('.search-filter-chip').forEach(function(c) { c.classList.remove('active'); });
            chip.classList.add('active');
            activeSearchFilter = chip.dataset.filter;
            if (input.value.trim().length >= 2) executeUnifiedSearch(input.value.trim(), resultsEl);
        });

        // Input handler with debounce
        input.addEventListener('input', function() {
            clearTimeout(debounce);
            debounce = setTimeout(function() {
                var q = input.value.trim();
                if (q.length < 2) { showRecentSearches(resultsEl); return; }
                executeUnifiedSearch(q, resultsEl);
            }, 200);
        });

        // Close handlers
        function closeOverlay() {
            overlay.remove();
            searchOverlayActive = false;
        }
        overlay.querySelector('.search-overlay-backdrop').addEventListener('click', closeOverlay);
        overlay.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') closeOverlay();
        });
    }

    function showRecentSearches(container) {
        var recent = getRecentSearches();
        if (recent.length === 0) {
            container.innerHTML = '<div class="search-overlay-empty">' +
                '<div class="search-empty-icon">\ud83d\udd0d</div>' +
                '<div class="search-empty-text">Search across all ' + MANIFEST.texts.length + ' texts, ' +
                (SEARCH_INDEX.docs ? SEARCH_INDEX.docs.length : 0) + ' indexed items, and ' +
                (SEARCH_QA ? SEARCH_QA.length : 0) + ' curated answers</div></div>';
            return;
        }
        var html = '<div class="search-recent-header">Recent Searches</div>';
        recent.forEach(function(s) {
            html += '<div class="search-recent-item" data-query="' + escAttr(s) + '">' +
                '<span class="search-recent-icon">\u23f0</span> ' + s + '</div>';
        });
        container.innerHTML = html;
        container.querySelectorAll('.search-recent-item').forEach(function(item) {
            item.addEventListener('click', function() {
                var q = item.dataset.query;
                document.getElementById('searchOverlayInput').value = q;
                executeUnifiedSearch(q, container);
            });
        });
    }

    function executeUnifiedSearch(query, container) {
        logEvent('search', query);
        saveRecentSearch(query);
        var tokens = query.toLowerCase().split(/\s+/).filter(function(t) { return t.length >= 2; });
        if (tokens.length === 0) { container.innerHTML = ''; return; }
        var filter = activeSearchFilter;
        var html = '';
        var qaResults = [];

        // Phase 1: Q&A matches (shown first, most prominent)
        if (filter === 'all' || filter === 'qa') {
            qaResults = matchQA(tokens);
            qaResults.forEach(function(r) {
                html += '<div class="search-result-qa">' +
                    '<div class="result-badge badge-qa">Q&A</div>' +
                    '<div class="qa-question">' + r.qa.question + '</div>' +
                    '<div class="qa-answer">' + r.qa.answer.substring(0, 250) + (r.qa.answer.length > 250 ? '...' : '') + '</div>' +
                    '<div class="qa-nav-links">';
                (r.qa.nav_targets || []).forEach(function(nav) {
                    html += '<a class="qa-nav-link" data-nav-type="' + nav.type + '" data-nav-id="' + (nav.id || nav.term || '') + '">' + nav.label + '</a>';
                });
                html += '</div></div>';
            });
        }

        // Phase 2: Pre-built index (chapters, glossary, prophecy, religions, beliefs, resources)
        var indexFilter = (filter === 'all' || filter === 'qa' || filter === 'verse') ? null : filter;
        if (filter !== 'verse' && filter !== 'qa') {
            var indexResults = searchPreBuiltIndex(tokens, indexFilter);
            // Fuzzy suggestions — if few results, try corrected spelling and merge
            var suggestions = [];
            if (indexResults.length < 3) {
                var correctedTokens = [];
                tokens.forEach(function(t) {
                    var similar = findSimilarWords(t, 0.45);
                    if (similar.length > 0) {
                        suggestions.push({ original: t, suggested: similar[0].word });
                        correctedTokens.push(similar[0].word);
                    } else {
                        correctedTokens.push(t);
                    }
                });
                // Auto-search with corrected tokens and merge unique results
                if (suggestions.length > 0) {
                    var fuzzyResults = searchPreBuiltIndex(correctedTokens, indexFilter);
                    var existingIds = {};
                    indexResults.forEach(function(r) { existingIds[r.id || r.title] = true; });
                    fuzzyResults.forEach(function(r) {
                        if (!existingIds[r.id || r.title]) indexResults.push(r);
                    });
                    // Also search Q&A with corrected tokens
                    if ((filter === 'all' || filter === 'qa') && qaResults.length === 0) {
                        var fuzzyQA = matchQA(correctedTokens);
                        fuzzyQA.forEach(function(r) {
                            html += '<div class="search-result-qa">' +
                                '<div class="result-badge badge-qa">Q&A</div>' +
                                '<div class="qa-question">' + r.qa.question + '</div>' +
                                '<div class="qa-answer">' + r.qa.answer.substring(0, 250) + (r.qa.answer.length > 250 ? '...' : '') + '</div>' +
                                '<div class="qa-nav-links">';
                            (r.qa.nav_targets || []).forEach(function(nav) {
                                html += '<a class="qa-nav-link" data-nav-type="' + nav.type + '" data-nav-id="' + (nav.id || nav.term || '') + '">' + nav.label + '</a>';
                            });
                            html += '</div></div>';
                        });
                    }
                }
            }
            if (suggestions.length > 0) {
                var sugText = suggestions.map(function(s) {
                    return '<a class="search-suggest-link" data-suggest="' + escAttr(s.suggested) + '">' + s.suggested + '</a>';
                }).join(', ');
                html += '<div class="search-did-you-mean">Did you mean: ' + sugText + '</div>';
            }

            var highlightQ = suggestions.length > 0 ? suggestions.map(function(s){return s.suggested;}).concat(tokens).join('|') : query;
            var re = new RegExp('(' + highlightQ.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi');
            indexResults.forEach(function(r) {
                var badge = searchBadges[r.type] || searchBadges.study;
                var textName = r.textId ? getTextName(r.textId) : '';
                var refLine = textName ? (textName + (r.ref ? ' \u2014 ' + r.ref : '')) : r.ref;
                html += '<div class="search-result-item" data-type="' + r.docType + '" data-id="' + (r.id || '') + '" data-text="' + (r.textId || '') + '" data-era="' + (r.eraId || '') + '">' +
                    '<div class="result-badge ' + badge.cls + '">' + badge.label + '</div>' +
                    '<div class="result-title">' + r.title + '</div>' +
                    (refLine ? '<div class="result-ref">' + refLine + '</div>' : '') +
                    '<div class="result-context">' + r.snippet.replace(re, '<mark>$1</mark>') + '</div>' +
                    '</div>';
            });
        }

        // Phase 3: Verse search (if filter allows)
        if (filter === 'all' || filter === 'verse') {
            var verseResults = searchFlowVerses(tokens);
            if (verseResults.length > 0 && filter === 'all') {
                html += '<div class="search-section-header">Verse Matches (' + verseResults.length + ')</div>';
            }
            var reV = new RegExp('(' + query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi');
            verseResults.forEach(function(r) {
                html += '<div class="search-result-item" data-type="vs" data-text="' + r.textId + '" data-ch="' + (r.ch || '') + '">' +
                    '<div class="result-badge badge-verse">Verse</div>' +
                    '<div class="result-title">' + r.ref + '</div>' +
                    '<div class="result-context">' + r.snippet.replace(reV, '<mark>$1</mark>') + '</div>' +
                    '</div>';
            });
        }

        if (!html) {
            html = '<div class="search-overlay-empty"><div class="search-empty-text">No results for "' + escAttr(query) + '"</div></div>';
        }

        container.innerHTML = html;

        // Wire click handlers for results
        container.querySelectorAll('.search-result-item').forEach(function(item) {
            item.addEventListener('click', function() {
                closeSearchOverlay();
                var dtype = item.dataset.type;
                var textId = item.dataset.text;
                var id = item.dataset.id;

                if (dtype === 'vs') {
                    // Verse: open interlinear pane
                    var chNum = parseInt(item.dataset.ch);
                    if (textId && textId !== currentText) selectText(textId, true);
                    if (chNum) { currentILBook = textId; renderInterlinear(chNum); setReadingPane(true); }
                } else if (dtype === 'gl') {
                    // Glossary term
                    openGlossary(id);
                } else if (dtype === 'ch') {
                    // Study chapter
                    if (textId && textId !== currentText) selectText(textId, true);
                    if (id) requestAnimationFrame(function() { location.hash = id; });
                } else if (dtype === 'rl') {
                    // Religion — open matrix with religion selected
                    openMatrix();
                } else if (dtype === 'rs') {
                    // Resource
                    openResources();
                } else {
                    // Default: try chapter navigation
                    if (textId && textId !== currentText) selectText(textId, true);
                    if (id) requestAnimationFrame(function() { location.hash = id; });
                }
            });
        });

        // Wire Q&A navigation links
        container.querySelectorAll('.qa-nav-link').forEach(function(link) {
            link.addEventListener('click', function(e) {
                e.stopPropagation();
                closeSearchOverlay();
                var navType = link.dataset.navType;
                var navId = link.dataset.navId;
                if (navType === 'glossary') {
                    openGlossary(navId);
                } else if (navType === 'chapter' && navId) {
                    // Find which text has this chapter
                    for (var i = 0; i < MANIFEST.eras.length; i++) {
                        var era = MANIFEST.eras[i];
                        var chs = ERA_DATA[era.id] || [];
                        for (var j = 0; j < chs.length; j++) {
                            if (chs[j].id === navId) {
                                if (era.text !== currentText) selectText(era.text, true);
                                requestAnimationFrame(function() { location.hash = navId; });
                                return;
                            }
                        }
                    }
                }
            });
        });

        // Wire "Did you mean?" links
        container.querySelectorAll('.search-suggest-link').forEach(function(link) {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                var q = link.dataset.suggest;
                var input = document.getElementById('searchOverlayInput');
                if (input) input.value = q;
                executeUnifiedSearch(q, container);
            });
        });
    }

    function closeSearchOverlay() {
        var overlay = document.getElementById('searchOverlayUnified');
        if (overlay) overlay.remove();
        searchOverlayActive = false;
    }

    // Legacy performSearch — redirects to the overlay
    function performSearch(query) {
        if (!query || query.length < 2) {
            searchResults.classList.remove('visible');
            return;
        }
        // Open the full overlay with the query
        openSearchOverlay();
        setTimeout(function() {
            var input = document.getElementById('searchOverlayInput');
            if (input) {
                input.value = query;
                var resultsEl = document.getElementById('searchOverlayResults');
                if (resultsEl) executeUnifiedSearch(query, resultsEl);
            }
        }, 100);
        searchResults.classList.remove('visible');
    }

    // Legacy buildSearchIndex — now a no-op (index is pre-built)
    function buildSearchIndex(force) {
        // Pre-built index loaded at init, no action needed
    }

    // ── Cross-Reference Drawer ──────────────────────────────
    function openXrefDrawer(chapterId, index) {
        var chapterData = null;
        for (var i = 0; i < MANIFEST.eras.length; i++) {
            chapterData = (ERA_DATA[MANIFEST.eras[i].id] || []).find(function(c) { return c.id === chapterId; });
            if (chapterData) break;
        }
        if (!chapterData || !chapterData.cross_refs) return;

        var html = '';
        chapterData.cross_refs.forEach(function(raw, i) {
            var xr = normXref(raw);
            var highlight = i === index ? 'style="background:var(--gold-dim);border-radius:6px;padding:14px 12px;margin:-14px -12px"' : '';
            var parsed = parseScriptureRef(xr.ref);
            var goLink = parsed ? ' <a class="xref-goto" data-ref="' + escAttr(xr.ref) + '" title="Open in reading pane">\u2192 Go</a>' : '';
            html += '<div class="xref-item" ' + highlight + '>' +
                '<div class="xref-ref">' + xr.ref + goLink + '</div>' +
                '<div class="xref-note">' + xr.note + '</div>' +
                '<div class="xref-type" style="color:' +
                (xr.type === 'ot' ? 'var(--blue)' : xr.type === 'nt' ? 'var(--green)' : xr.type === 'dss' ? '#8a7a9a' : 'var(--amber)') +
                '">' +
                (xr.type === 'ot' ? 'Old Testament' : xr.type === 'nt' ? 'New Testament' : xr.type === 'dss' ? 'Dead Sea Scrolls' : 'Ancient Near East') +
                '</div></div>';
        });

        document.getElementById('xrefTitle').textContent = (chapterData.ref || chapterData.title) + ' \u2014 Cross References';
        xrefContent.innerHTML = html;
        xrefDrawer.classList.add('open');
    }

    function closeXrefDrawer() {
        xrefDrawer.classList.remove('open');
    }

    // ── Glossary ────────────────────────────────────────────
    function openGlossary(highlightTerm) {
        renderGlossaryEntries(highlightTerm);
        glossaryOverlay.classList.add('open');
        if (highlightTerm) {
            glossarySearch.value = highlightTerm;
            filterGlossary(highlightTerm);
        } else {
            glossarySearch.value = '';
        }
        glossarySearch.focus();
    }

    function closeGlossary() {
        glossaryOverlay.classList.remove('open');
    }

    function renderGlossaryEntries(highlightTerm) {
        var entries = Object.values(GLOSSARY).sort(function(a, b) {
            return a.transliteration.localeCompare(b.transliteration);
        });

        glossaryList.innerHTML = entries.map(function(t) {
            var langBadge = t.language ? '<span class="g-lang-badge">' + t.language + '</span>' : '';
            var isHighlighted = highlightTerm && t.transliteration.toLowerCase().includes(highlightTerm.toLowerCase());
            return '<div class="glossary-entry" data-translit="' + t.transliteration.toLowerCase() + '"' +
                (isHighlighted ? ' style="background:var(--gold-dim);border-radius:6px;padding:16px 12px"' : '') + '>' +
                '<span class="g-hebrew">' + t.hebrew + '</span>' +
                '<span class="g-translit">' + t.transliteration + '</span>' +
                '<span class="g-strongs">' + t.strongs + '</span>' +
                langBadge +
                '<div class="g-gloss">' + t.gloss + '</div>' +
                '<div class="g-definition">' + t.definition + '</div></div>';
        }).join('');
    }

    function filterGlossary(query) {
        var lower = query.toLowerCase();
        glossaryList.querySelectorAll('.glossary-entry').forEach(function(entry) {
            var text = entry.textContent.toLowerCase();
            entry.style.display = text.includes(lower) ? '' : 'none';
        });
    }

    // ── Resources ────────────────────────────────────────────
    function openResources() {
        renderResourceFilters();
        renderResources();
        resourcesOverlay.classList.add('open');
        resourcesSearch.value = '';
        resourcesSearch.focus();
    }

    function closeResources() {
        resourcesOverlay.classList.remove('open');
    }

    function renderResourceFilters() {
        var types = ['all'];
        RESOURCES.forEach(function(r) {
            if (types.indexOf(r.type) === -1) types.push(r.type);
        });
        resourcesFilters.innerHTML = types.map(function(t) {
            var label = t === 'all' ? 'All' : t.charAt(0).toUpperCase() + t.slice(1) + 's';
            return '<button class="resources-filter-btn' + (activeResourceFilter === t ? ' active' : '') +
                '" data-filter="' + t + '">' + label + '</button>';
        }).join('');
        resourcesFilters.querySelectorAll('.resources-filter-btn').forEach(function(btn) {
            btn.addEventListener('click', function() {
                activeResourceFilter = btn.dataset.filter;
                resourcesFilters.querySelectorAll('.resources-filter-btn').forEach(function(b) { b.classList.remove('active'); });
                btn.classList.add('active');
                renderResources();
            });
        });
    }

    function renderResources() {
        var filtered = RESOURCES;
        if (activeResourceFilter !== 'all') {
            filtered = RESOURCES.filter(function(r) { return r.type === activeResourceFilter; });
        }
        var query = (resourcesSearch ? resourcesSearch.value.trim().toLowerCase() : '');
        if (query) {
            filtered = filtered.filter(function(r) {
                return r.title.toLowerCase().indexOf(query) >= 0 ||
                    r.author.toLowerCase().indexOf(query) >= 0 ||
                    r.description.toLowerCase().indexOf(query) >= 0 ||
                    (r.tags || []).some(function(tag) { return tag.toLowerCase().indexOf(query) >= 0; });
            });
        }

        // Group by type, featured first
        var featured = filtered.filter(function(r) { return r.featured; });
        var rest = filtered.filter(function(r) { return !r.featured; });

        var html = '';
        if (featured.length > 0) {
            html += '<div class="resources-section-title">Featured</div>';
            html += featured.map(renderResourceCard).join('');
        }
        if (rest.length > 0) {
            if (featured.length > 0) html += '<div class="resources-section-title">More Resources</div>';
            html += rest.map(renderResourceCard).join('');
        }
        if (filtered.length === 0) {
            html = '<div style="text-align:center;color:var(--text-muted);padding:40px 0">No resources found.</div>';
        }
        resourcesList.innerHTML = html;

        // Attach click handlers
        resourcesList.querySelectorAll('.resource-card').forEach(function(card) {
            card.addEventListener('click', function() {
                window.open(card.dataset.url, '_blank');
            });
        });
    }

    function renderResourceCard(r) {
        var meta = [];
        if (r.date) meta.push(r.date);
        if (r.duration) meta.push(r.duration);
        var tagsHtml = (r.tags || []).map(function(tag) {
            return '<span class="resource-tag">' + tag.replace(/_/g, ' ') + '</span>';
        }).join('');
        return '<div class="resource-card' + (r.featured ? ' featured' : '') + '" data-url="' + escAttr(r.url) + '">' +
            '<div class="resource-card-header">' +
                '<span class="resource-type-badge ' + r.type + '">' + r.type + '</span>' +
                '<span class="resource-card-title">' + esc(r.title) + '</span>' +
            '</div>' +
            '<div class="resource-card-author">' + esc(r.author) + '</div>' +
            (meta.length ? '<div class="resource-card-meta">' + esc(meta.join(' \u00b7 ')) + '</div>' : '') +
            '<div class="resource-card-desc">' + esc(r.description) + '</div>' +
            (tagsHtml ? '<div class="resource-tags">' + tagsHtml + '</div>' : '') +
        '</div>';
    }

    function filterResources() {
        renderResources();
    }

    // ── Part-of-Speech Classifier ───────────────────────────
    function getPosClass(morph) {
        if (!morph) return '';
        var m = morph.toLowerCase();
        var parts = m.split('+');
        var main = parts[parts.length - 1].trim();
        if (main.indexOf('verb') === 0) return 'pos-verb';
        if (main.indexOf('proper') >= 0) return 'pos-proper';
        if (main.indexOf('noun') === 0) return 'pos-noun';
        if (main.indexOf('adjective') === 0 || main.indexOf('adj') === 0) return 'pos-adj';
        if (main.indexOf('pronoun') === 0) return 'pos-pron';
        if (main.indexOf('adverb') === 0) return 'pos-adv';
        if (m.indexOf('preposition') >= 0) return 'pos-prep';
        if (m.indexOf('conjunction') >= 0) return 'pos-conj';
        if (m.indexOf('article') >= 0) return 'pos-art';
        if (m.indexOf('particle') >= 0) return 'pos-part';
        if (m.indexOf('interjection') >= 0) return 'pos-part';
        return '';
    }

    function getPosLabel(posClass) {
        var labels = {
            'pos-verb': 'Verb', 'pos-noun': 'Noun', 'pos-prep': 'Preposition',
            'pos-conj': 'Conjunction', 'pos-art': 'Article', 'pos-adj': 'Adjective',
            'pos-pron': 'Pronoun', 'pos-adv': 'Adverb', 'pos-part': 'Particle',
            'pos-proper': 'Proper Noun'
        };
        return labels[posClass] || '';
    }

    // ── Interlinear Reading Pane ─────────────────────────────
    function initReadingPane() {
        readingPaneModeSelect.value = readingPaneMode;
        applyReadingPaneMode();

        var label = document.getElementById('fontSizeLabel');
        if (label) label.textContent = Math.round(ilFontScale * 100) + '%';

        // Start with reading pane closed — it opens when user selects a text
        setReadingPane(false);
    }

    function toggleReadingPane() {
        setReadingPane(!readingPaneOpen);
    }

    function setReadingPane(open) {
        readingPaneOpen = open;
        localStorage.setItem('genesis-reading-pane', open ? 'true' : 'false');
        readingPaneToggle.classList.toggle('active', open);
        document.body.classList.toggle('reading-pane-open', open);

        if (open) {
            // Restore saved pane width or use default
            var saved = JSON.parse(localStorage.getItem('atl-layout') || 'null');
            if (saved && saved.pane) {
                document.documentElement.style.setProperty('--col-pane', saved.pane);
            }
        }

        if (!open) {
            document.body.classList.remove('reading-pane-fullscreen');
        }
    }

    function toggleReadingPaneFullscreen() {
        var isFS = document.body.classList.toggle('reading-pane-fullscreen');
        if (isFS && !readingPaneOpen) {
            setReadingPane(true);
        }
    }

    function setReadingPaneMode(mode) {
        readingPaneMode = mode;
        localStorage.setItem('genesis-reading-mode', mode);
        applyReadingPaneMode();
    }

    function applyReadingPaneMode() {
        document.body.classList.remove('il-mode-full', 'il-mode-hebrew', 'il-mode-english');
        document.body.classList.add('il-mode-' + readingPaneMode);
    }

    function syncReadingPane(chapterId) {
        if (!readingPaneOpen) return;

        if (sourceReadingMode) {
            // Source reading mode: find chapter data for any text
            renderSourceReading(currentText, chapterId);
            return;
        }

        // Interlinear mode: extract prefix and chapter number from chapter ID
        var match = chapterId.match(/^([a-z0-9]+)-(\d+)/);
        if (!match) return;
        var book = prefixToTextId(match[1]);
        var il = getTextInterlinear(book);
        if (Object.keys(il).length === 0) return;
        var chNum = parseInt(match[2]);
        if (chNum === currentILChapter && book === currentILBook) return;
        currentILBook = book;
        renderInterlinear(chNum);
    }

    function syncStudyToPane() {
        if (!currentILChapter) return;
        var prefix = getChapterPrefix(currentILBook);
        var targetId = prefix + currentILChapter;

        if (currentILBook !== currentText) {
            selectText(currentILBook, true);
        }

        requestAnimationFrame(function() { scrollToChapter(targetId); });
    }

    function syncPaneToStudy() {
        var activeLink = document.querySelector('.chapter-link.active');
        if (activeLink) {
            var id = activeLink.dataset.id;
            var match = id.match(/^(gen|exod|lev|num|deut|josh)-(\d+)/);
            if (match) {
                currentILBook = prefixToTextId(match[1]);
                renderInterlinear(parseInt(match[2]));
                return;
            }
        }
        var cards = document.querySelectorAll('.chapter-card');
        for (var i = 0; i < cards.length; i++) {
            var rect = cards[i].getBoundingClientRect();
            if (rect.top < window.innerHeight / 2 && rect.bottom > 0) {
                var match = cards[i].id.match(/^(gen|exod|lev|num|deut|josh)-(\d+)/);
                if (match) {
                    currentILBook = prefixToTextId(match[1]);
                    renderInterlinear(parseInt(match[2]));
                    return;
                }
            }
        }
    }

    function renderInterlinear(chapterNum) {
        currentILChapter = chapterNum;
        var bookName = getTextName(currentILBook);
        readingPaneTitle.textContent = bookName + ' ' + chapterNum;

        // Sync book selector dropdown
        var ilBookSel = document.getElementById('ilBookSelect');
        if (ilBookSel) ilBookSel.value = currentILBook;

        // Toggle Greek vs Hebrew body class for CSS direction + update language badge
        var isGreek = isGreekText(currentILBook);
        if (isGreek) {
            document.body.classList.add('il-greek');
        } else {
            document.body.classList.remove('il-greek');
        }
        var langBadge = document.getElementById('ilLangBadge');
        if (langBadge) {
            langBadge.textContent = isGreek ? 'GREEK' : 'HEBREW';
            langBadge.className = 'il-lang-badge' + (isGreek ? ' il-lang-greek' : ' il-lang-hebrew');
        }

        var ilData = getTextInterlinear(currentILBook);
        var data = ilData[String(chapterNum)];
        if (!data || !data.verses || data.verses.length === 0) {
            var noDataIcon = isGreek ? '\u03A9' : '\u05E2'; // Ω for Greek, ע for Hebrew
            readingPaneContent.innerHTML =
                '<div class="il-no-data">' +
                '<div class="il-no-data-icon">' + noDataIcon + '</div>' +
                '<p>Interlinear text for ' + bookName + ' ' + chapterNum +
                ' has not been loaded yet.</p></div>';
            return;
        }

        var html = '';
        data.verses.forEach(function(verse) {
            var sentence;
            var hasFlow = verse.flow && ilRows.flow !== false;
            if (hasFlow) {
                sentence = verse.flow;
            } else {
                var glosses = verse.words.slice().reverse()
                    .map(function(w) { return w.g || ''; })
                    .filter(function(g) { return g && g !== 'properly' && g !== 'untranslatable'; });
                sentence = glosses.join(' ')
                    .replace(/\s*\+\s*/g, ' ')
                    .replace(/\s{2,}/g, ' ')
                    .trim();
            }

            html += '<div class="il-verse' + (hasFlow ? ' il-verse-flow' : '') + '">' +
                '<button class="il-verse-copy" data-verse="' + verse.num + '" title="Copy verse">&#x1F4CB;</button>' +
                '<div class="il-verse-english">' +
                '<span class="il-verse-num">' + verse.num + '</span>' +
                '<span class="il-verse-sentence' + (hasFlow ? ' il-flow-active' : '') + '">' + esc(sentence) + '</span>' +
                (verse.note ? '<div class="il-verse-note" title="Study note">\ud83d\udca1 ' + esc(verse.note) + '</div>' : '') +
                '</div>' +
                '<div class="il-verse-words">';

            verse.words.forEach(function(w) {
                var posClass = getPosClass(w.m);
                html += '<div class="il-word' + (posClass ? ' ' + posClass : '') + '"' +
                    ' data-h="' + escAttr(w.h || '') + '"' +
                    ' data-t="' + escAttr(w.t || '') + '"' +
                    ' data-s="' + escAttr(w.s || '') + '"' +
                    ' data-g="' + escAttr(w.g || '') + '"' +
                    ' data-m="' + escAttr(w.m || '') + '"' +
                    ' role="button" tabindex="0" aria-label="' + escAttr((w.t || '') + ': ' + (w.g || '')) + '">' +
                    '<span class="il-hebrew">' + esc(w.h || '') + '</span>' +
                    (w.t ? '<span class="il-translit">' + esc(w.t) + '</span>' : '') +
                    '<span class="il-gloss">' + esc(w.g || '\u00A0') + '</span>' +
                    (w.m ? '<span class="il-morph-tag">' + esc(w.m.split('/')[0] || '') + '</span>' : '') +
                    (w.s ? '<span class="il-strongs-tag">' + esc(w.s) + '</span>' : '') +
                    '</div>';
            });

            html += '</div></div>';
        });

        readingPaneContent.innerHTML = html;
        readingPaneContent.scrollTop = 0;

        if (ilFontScale !== 1) applyFontScale();

        var bar = document.getElementById('readingProgressBar');
        if (bar) bar.style.width = '0%';

        var maxCh = getTextMaxChapter(currentILBook);
        var prevBtn = document.getElementById('ilPrev');
        var nextBtn = document.getElementById('ilNext');
        if (prevBtn) prevBtn.disabled = (chapterNum <= 1);
        if (nextBtn) nextBtn.disabled = (chapterNum >= maxCh);
    }

    // ── Inline Interlinear (for reading mode toggle) ──────────
    function renderInlineInterlinear(textId, chapterNum) {
        if (!textId || !chapterNum) return '<div class="il-no-data">No interlinear data available.</div>';
        var ilData = getTextInterlinear(textId);
        if (!ilData || typeof ilData !== 'object') return '<div class="il-no-data">No interlinear data for this text.</div>';
        var data = ilData[String(chapterNum)];
        if (!data || !data.verses || data.verses.length === 0) {
            var greek = isGreekText(textId);
            var noIcon = greek ? '\u03A9' : '\u05E2';
            return '<div class="il-no-data"><div class="il-no-data-icon">' + noIcon + '</div>' +
                '<p>Interlinear text for chapter ' + chapterNum + ' has not been loaded yet.</p></div>';
        }

        var greek = isGreekText(textId);
        var html = '<div class="' + (greek ? 'il-inline-greek' : '') + '">';
        data.verses.forEach(function(verse) {
            var sentence;
            var hasFlow = verse.flow && ilRows.flow !== false;
            if (hasFlow) {
                sentence = verse.flow;
            } else {
                var glosses = verse.words.slice().reverse()
                    .map(function(w) { return w.g || ''; })
                    .filter(function(g) { return g && g !== 'properly' && g !== 'untranslatable'; });
                sentence = glosses.join(' ').replace(/\s*\+\s*/g, ' ').replace(/\s{2,}/g, ' ').trim();
            }

            html += '<div class="il-verse' + (hasFlow ? ' il-verse-flow' : '') + '">' +
                '<div class="il-verse-english">' +
                '<span class="il-verse-num">' + verse.num + '</span>' +
                '<span class="il-verse-sentence' + (hasFlow ? ' il-flow-active' : '') + '">' + esc(sentence) + '</span>' +
                (verse.note ? '<div class="il-verse-note" title="Study note">\ud83d\udca1 ' + esc(verse.note) + '</div>' : '') +
                '</div>' +
                '<div class="il-verse-words">';

            verse.words.forEach(function(w) {
                var posClass = getPosClass(w.m);
                html += '<div class="il-word' + (posClass ? ' ' + posClass : '') + '"' +
                    ' data-h="' + escAttr(w.h || '') + '"' +
                    ' data-t="' + escAttr(w.t || '') + '"' +
                    ' data-s="' + escAttr(w.s || '') + '"' +
                    ' data-g="' + escAttr(w.g || '') + '"' +
                    ' data-m="' + escAttr(w.m || '') + '"' +
                    ' role="button" tabindex="0">' +
                    '<span class="il-hebrew">' + esc(w.h || '') + '</span>' +
                    (w.t ? '<span class="il-translit">' + esc(w.t) + '</span>' : '') +
                    '<span class="il-gloss">' + esc(w.g || '\u00A0') + '</span>' +
                    (w.m ? '<span class="il-morph-tag">' + esc(w.m.split('/')[0] || '') + '</span>' : '') +
                    (w.s ? '<span class="il-strongs-tag">' + esc(w.s) + '</span>' : '') +
                    '</div>';
            });

            html += '</div></div>';
        });
        html += '</div>';
        return html;
    }

    // ── Inline Scripture (full flow translation for Scripture reading mode) ──────
    function renderInlineScripture(textId, startCh, endCh) {
        if (!textId || !startCh) return '<div class="scripture-no-data">No scripture text available for this chapter.</div>';
        var ilData = getTextInterlinear(textId);
        var useStandalone = false;

        // Fallback to standalone flow for texts without interlinear (1 Enoch, DSS, etc.)
        if ((!ilData || typeof ilData !== 'object' || Object.keys(ilData).length === 0) && STANDALONE_FLOW[textId]) {
            useStandalone = true;
        } else if (!ilData || typeof ilData !== 'object') {
            return '<div class="scripture-no-data">Scripture text not available for this text.</div>';
        }

        var start = parseInt(startCh, 10);
        var end = endCh ? parseInt(endCh, 10) : start;
        if (isNaN(start)) return '<div class="scripture-no-data">Could not determine chapter range.</div>';

        var textDef = getTextDef(textId);
        var textName = textDef ? textDef.name : textId;
        var html = '<div class="scripture-reading">';
        var hasAnyVerse = false;

        if (useStandalone) {
            // Render from STANDALONE_FLOW data
            var flowData = STANDALONE_FLOW[textId];
            var notesData = STANDALONE_NOTES[textId] || {};
            for (var chNum = start; chNum <= end; chNum++) {
                var chFlow = flowData[String(chNum)];
                if (!chFlow) continue;
                var chNotes = notesData[String(chNum)] || {};

                if (start !== end) {
                    html += '<div class="scripture-chapter-heading">' + textName + ' ' + chNum + '</div>';
                }

                // Sort verse numbers numerically
                var verseNums = Object.keys(chFlow).map(Number).sort(function(a, b) { return a - b; });
                verseNums.forEach(function(vNum) {
                    hasAnyVerse = true;
                    html += '<span class="scripture-verse">' +
                        '<sup class="scripture-verse-num">' + vNum + '</sup>' +
                        '<span class="scripture-verse-text">' + esc(chFlow[String(vNum)]) + '</span>' +
                        '</span> ';
                    if (chNotes[String(vNum)]) {
                        html += '<span class="scripture-verse-note standalone-note" title="' + escAttr(chNotes[String(vNum)]) + '">\uD83D\uDCA1</span> ';
                    }
                });
            }
        } else {
            // Render from interlinear-merged flow data
            for (var chNum = start; chNum <= end; chNum++) {
                var data = ilData[String(chNum)];
                if (!data || !data.verses || data.verses.length === 0) continue;

                if (start !== end) {
                    html += '<div class="scripture-chapter-heading">' + textName + ' ' + chNum + '</div>';
                }

                data.verses.forEach(function(verse) {
                    hasAnyVerse = true;
                    var text = '';
                    if (verse.flow) {
                        text = verse.flow;
                    } else {
                        var glosses = verse.words.slice().reverse()
                            .map(function(w) { return w.g || ''; })
                            .filter(function(g) { return g && g !== 'properly' && g !== 'untranslatable'; });
                        text = glosses.join(' ').replace(/\s*\+\s*/g, ' ').replace(/\s{2,}/g, ' ').trim();
                    }
                    html += '<span class="scripture-verse">' +
                        '<sup class="scripture-verse-num">' + verse.num + '</sup>' +
                        '<span class="scripture-verse-text">' + esc(text) + '</span>' +
                        '</span> ';
                    if (verse.note) {
                        html += '<span class="scripture-verse-note" title="Study note">\uD83D\uDCA1</span> ';
                    }
                });
            }
        }

        if (!hasAnyVerse) {
            return '<div class="scripture-no-data"><div class="scripture-no-data-icon">\uD83D\uDCDC</div>' +
                '<p>Flow translation for this chapter has not been loaded yet.</p></div>';
        }

        html += '</div>';
        return html;
    }

    // ── Lazy-load inline content for reading modes on page load ──────
    function lazyLoadReadingModeContent(mode) {
        var cards = mainContent.querySelectorAll('.chapter-card');
        cards.forEach(function(c) {
            if (mode === 'scripture') {
                var scDiv = c.querySelector('.inline-scripture');
                if (scDiv && !scDiv.innerHTML.trim()) {
                    scDiv.innerHTML = renderInlineScripture(scDiv.dataset.text, scDiv.dataset.ch, scDiv.dataset.chEnd);
                }
            }
            if (mode === 'interlinear') {
                var ilDiv = c.querySelector('.inline-interlinear');
                if (ilDiv && !ilDiv.innerHTML.trim()) {
                    ilDiv.innerHTML = renderInlineInterlinear(ilDiv.dataset.text, ilDiv.dataset.ch);
                }
            }
        });
    }

    // ── Source Reading Pane (for texts without interlinear) ──────
    function renderSourceReading(textId, activeChapterId) {
        var textDef = getTextDef(textId);
        var textName = textDef ? textDef.name : textId;
        var eras = getTextEras(textId);

        // Find the active chapter data
        var activeChapter = null;
        var activeEra = null;
        if (activeChapterId) {
            for (var i = 0; i < eras.length; i++) {
                var chapters = ERA_DATA[eras[i].id] || [];
                for (var j = 0; j < chapters.length; j++) {
                    if (chapters[j].id === activeChapterId) {
                        activeChapter = chapters[j];
                        activeEra = eras[i];
                        break;
                    }
                }
                if (activeChapter) break;
            }
        }

        // If no active chapter found, show the first era's first chapter
        if (!activeChapter && eras.length > 0) {
            for (var i = 0; i < eras.length; i++) {
                var chapters = ERA_DATA[eras[i].id] || [];
                if (chapters.length > 0) {
                    activeChapter = chapters[0];
                    activeEra = eras[i];
                    break;
                }
            }
        }

        // Update title
        if (activeChapter) {
            readingPaneTitle.textContent = activeChapter.ref || activeChapter.title || textName;
        } else {
            readingPaneTitle.textContent = textName;
        }

        // Build the source reading HTML
        var html = '';

        if (!activeChapter) {
            html = '<div class="il-no-data">' +
                '<div class="il-no-data-icon">\uD83D\uDCDC</div>' +
                '<p>No chapter data available for ' + textName + '.</p></div>';
            readingPaneContent.innerHTML = html;
            return;
        }

        // Chapter header
        html += '<div class="source-reading">';
        html += '<div class="source-reading-ref">' + (activeChapter.ref || '') + '</div>';
        html += '<h3 class="source-reading-title">' + (activeChapter.title || '') + '</h3>';

        // Synopsis
        if (activeChapter.synopsis) {
            html += '<div class="source-reading-synopsis">' + activeChapter.synopsis + '</div>';
        }

        // Key verse / key passage
        var keyText = activeChapter.key_verse || activeChapter.key_passage;
        if (keyText) {
            if (typeof keyText === 'object' && keyText.text) {
                html += '<div class="source-reading-key-verse">' +
                    '<div class="source-reading-label">Key Passage</div>' +
                    '<div class="source-reading-ref-small">' + (keyText.ref || '') +
                    (keyText.translation ? ' (' + keyText.translation + ')' : '') + '</div>' +
                    '<blockquote class="source-reading-quote">' + keyText.text + '</blockquote>' +
                    '</div>';
            } else if (typeof keyText === 'string') {
                html += '<div class="source-reading-key-verse">' +
                    '<div class="source-reading-label">Key Passage</div>' +
                    '<blockquote class="source-reading-quote">' + keyText + '</blockquote>' +
                    '</div>';
            }
        }

        // Divine council relevance
        if (activeChapter.divine_council_relevance) {
            var dcr = activeChapter.divine_council_relevance;
            if (typeof dcr === 'object') {
                html += '<div class="source-reading-dc">' +
                    '<div class="source-reading-label">Divine Council Relevance' +
                    (dcr.rating ? ' <span class="source-reading-rating">' + dcr.rating + '/5</span>' : '') +
                    '</div>';
                if (dcr.summary) html += '<p>' + dcr.summary + '</p>';
                if (dcr.key_connections && dcr.key_connections.length > 0) {
                    html += '<ul class="source-reading-connections">';
                    dcr.key_connections.forEach(function(c) {
                        html += '<li>' + c + '</li>';
                    });
                    html += '</ul>';
                }
                html += '</div>';
            } else if (typeof dcr === 'string') {
                html += '<div class="source-reading-dc">' +
                    '<div class="source-reading-label">Divine Council Relevance</div>' +
                    '<p>' + dcr + '</p></div>';
            }
        }

        // Cross references
        if (activeChapter.cross_refs && activeChapter.cross_refs.length > 0) {
            html += '<div class="source-reading-xrefs">' +
                '<div class="source-reading-label">Cross References</div>';
            activeChapter.cross_refs.forEach(function(raw) {
                var xr = normXref(raw);
                html += '<div class="source-reading-xref">' +
                    '<span class="source-reading-xref-ref">' + xr.ref + '</span>';
                if (xr.note && xr.note !== xr.ref) html += '<span class="source-reading-xref-note"> \u2014 ' + xr.note + '</span>';
                html += '</div>';
            });
            html += '</div>';
        }

        // Hebrew/Greek terms
        if (activeChapter.hebrew_terms && activeChapter.hebrew_terms.length > 0) {
            html += '<div class="source-reading-terms">' +
                '<div class="source-reading-label">Key Terms</div>' +
                '<div class="source-reading-term-list">';
            activeChapter.hebrew_terms.forEach(function(term) {
                if (typeof term === 'object') {
                    html += '<span class="source-reading-term">' +
                        (term.hebrew || term.greek || '') + ' ' +
                        '<em>' + (term.transliteration || '') + '</em>' +
                        (term.gloss ? ' \u2014 ' + term.gloss : '') +
                        '</span>';
                } else {
                    html += '<span class="source-reading-term">' + term + '</span>';
                }
            });
            html += '</div></div>';
        }

        // ANE backdrop
        if (activeChapter.ane_backdrop) {
            html += '<div class="source-reading-backdrop">' +
                '<div class="source-reading-label">Ancient Near Eastern Context</div>' +
                '<p>' + activeChapter.ane_backdrop + '</p></div>';
        }

        // Second Temple context
        if (activeChapter.second_temple) {
            html += '<div class="source-reading-2t">' +
                '<div class="source-reading-label">Second Temple Context</div>' +
                '<p>' + activeChapter.second_temple + '</p></div>';
        }

        html += '</div>';

        readingPaneContent.innerHTML = html;
        readingPaneContent.scrollTop = 0;
    }

    // ── Word Popup ────────────────────────────────────────────
    function showWordPopup(wordEl) {
        var h = wordEl.dataset.h;
        var t = wordEl.dataset.t;
        var s = wordEl.dataset.s;
        var g = wordEl.dataset.g;
        var m = wordEl.dataset.m;

        var scriptClass = isGreekText(currentILBook) ? 'wp-greek' : 'wp-hebrew';
        var html = '<div class="' + scriptClass + '">' + esc(h) + '</div>';
        if (t) html += '<div class="wp-translit">' + esc(t) + '</div>';
        if (s) html += '<div class="wp-strongs">' + esc(s) + '</div>';
        html += '<div class="wp-divider"></div>';
        if (g) html += '<div class="wp-gloss">' + esc(g) + '</div>';

        var posClass = getPosClass(m);
        var posLabel = getPosLabel(posClass);
        if (posLabel) {
            html += '<div style="text-align:center"><span class="wp-pos-badge ' +
                posClass + '">' + esc(posLabel) + '</span></div>';
        }

        if (m) {
            html += '<div class="wp-divider"></div>' +
                '<div class="wp-morph">' +
                '<div class="wp-morph-label">Morphology</div>' +
                esc(m) + '</div>';
        }

        if (s) {
            var glossaryMatch = Object.entries(GLOSSARY).find(
                function(pair) { return pair[1].strongs === s; }
            );
            if (glossaryMatch) {
                html += '<div class="wp-glossary-link" data-term="' +
                    escAttr(glossaryMatch[0]) + '">View in Glossary</div>';
            }
        }

        wordPopup.innerHTML = html;
        wordPopup.classList.add('visible');

        var rect = wordEl.getBoundingClientRect();
        var popW = 290;
        var left = rect.left + rect.width / 2 - popW / 2;
        var top = rect.bottom + 10;

        if (left < 10) left = 10;
        if (left + popW > window.innerWidth - 10) left = window.innerWidth - popW - 10;
        if (top + 280 > window.innerHeight) {
            top = rect.top - 240;
            if (top < 10) top = 10;
        }

        wordPopup.style.left = left + 'px';
        wordPopup.style.top = top + 'px';

        var glossLink = wordPopup.querySelector('.wp-glossary-link');
        if (glossLink) {
            glossLink.addEventListener('click', function(e) {
                e.stopPropagation();
                closeWordPopup();
                openGlossary(glossLink.dataset.term);
            });
        }
    }

    function closeWordPopup() {
        wordPopup.classList.remove('visible');
    }

    // ── Font Scale & Progress ────────────────────────────────
    function adjustFontScale(delta) {
        ilFontScale = Math.max(0.6, Math.min(2.0, ilFontScale + delta));
        localStorage.setItem('genesis-il-font-scale', ilFontScale.toFixed(1));
        applyFontScale();
    }

    function applyFontScale() {
        readingPaneContent.style.setProperty('--il-scale', ilFontScale);
        readingPaneContent.querySelectorAll('.il-hebrew').forEach(function(el) {
            el.style.fontSize = (1.55 * ilFontScale) + 'rem';
        });
        readingPaneContent.querySelectorAll('.il-gloss').forEach(function(el) {
            el.style.fontSize = (0.6 * ilFontScale) + 'rem';
        });
        readingPaneContent.querySelectorAll('.il-verse-sentence').forEach(function(el) {
            el.style.fontSize = (0.92 * ilFontScale) + 'rem';
        });
        var label = document.getElementById('fontSizeLabel');
        if (label) label.textContent = Math.round(ilFontScale * 100) + '%';
    }

    function updateReadingProgress() {
        var el = readingPaneContent;
        var scrollTop = el.scrollTop;
        var scrollHeight = el.scrollHeight - el.clientHeight;
        var pct = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
        var bar = document.getElementById('readingProgressBar');
        if (bar) bar.style.width = pct + '%';
    }

    // ── User Mode & Row Toggles ────────────────────────────
    function setUserMode(mode) {
        if (!USER_MODES[mode]) return;
        userMode = mode;
        localStorage.setItem('atl-user-mode', mode);
        ilRows = Object.assign({}, USER_MODES[mode]);
        localStorage.setItem('atl-il-rows', JSON.stringify(ilRows));
        applyILRows();
        updateModeUI();
    }

    function toggleILRow(row) {
        ilRows[row] = !ilRows[row];
        localStorage.setItem('atl-il-rows', JSON.stringify(ilRows));
        applyILRows();
        updateModeUI();
    }

    function applyILRows() {
        document.body.classList.toggle('hide-il-translit', !ilRows.translit);
        document.body.classList.toggle('hide-il-morph', !ilRows.morph);
        document.body.classList.toggle('hide-il-strongs', !ilRows.strongs);
        document.body.classList.toggle('hide-il-gloss', !ilRows.gloss);
        document.body.classList.toggle('show-il-notes', !!ilRows.notes);
        // Flow toggle requires re-render to switch between flow/auto-gloss
        if (currentILChapter) renderInterlinear(currentILChapter);
    }

    function updateModeUI() {
        document.querySelectorAll('.user-mode-btn').forEach(function(btn) {
            btn.classList.toggle('active', btn.dataset.mode === userMode);
            btn.setAttribute('aria-pressed', btn.dataset.mode === userMode);
        });
        document.querySelectorAll('.il-row-toggle').forEach(function(btn) {
            var row = btn.dataset.row;
            btn.classList.toggle('active', !!ilRows[row]);
            btn.setAttribute('aria-pressed', !!ilRows[row]);
        });
    }

    function toggleHighContrast() {
        highContrast = !highContrast;
        localStorage.setItem('atl-high-contrast', highContrast);
        document.body.classList.toggle('high-contrast', highContrast);
        var btn = document.getElementById('hcToggle');
        if (btn) {
            btn.classList.toggle('active', highContrast);
            btn.setAttribute('aria-pressed', highContrast);
        }
    }

    // ── Study View Callout Toggles ────────────────────────
    var studyToggles = JSON.parse(localStorage.getItem('atl-study-toggles') || '{}');
    function initStudyToggles() {
        var toggleMap = {
            'hebrew-terms': 'hide-hebrew-terms',
            'ane-callout': 'hide-ane-callout',
            'second-temple': 'hide-second-temple',
            'council-note': 'hide-council-note',
            'cross-refs': 'hide-cross-refs'
        };
        Object.keys(toggleMap).forEach(function(key) {
            if (studyToggles[key] === false) {
                document.body.classList.add(toggleMap[key]);
            }
        });
        document.querySelectorAll('.study-toggle').forEach(function(btn) {
            var key = btn.dataset.toggle;
            if (studyToggles[key] === false) btn.classList.remove('active');
        });
        document.getElementById('studyControls').addEventListener('click', function(e) {
            var btn = e.target.closest('.study-toggle');
            if (!btn) return;
            var key = btn.dataset.toggle;
            var isActive = btn.classList.toggle('active');
            studyToggles[key] = isActive;
            localStorage.setItem('atl-study-toggles', JSON.stringify(studyToggles));
            document.body.classList.toggle(toggleMap[key], !isActive);
        });
    }

    // ── Column Width Slider ────────────────────────
    function initColWidthSlider() {
        var slider = document.getElementById('colWidthSlider');
        if (!slider) return;
        var saved = localStorage.getItem('atl-col-width');
        if (saved) slider.value = saved;
        applyColWidth(parseInt(slider.value));
        slider.addEventListener('input', function() {
            applyColWidth(parseInt(slider.value));
            localStorage.setItem('atl-col-width', slider.value);
        });
    }
    function applyColWidth(pct) {
        // pct 0-100: 0 = all Hebrew, 100 = all English
        var enFr = Math.max(0.2, pct / 50);
        var heFr = Math.max(0.2, (100 - pct) / 50);
        document.documentElement.style.setProperty('--il-columns', enFr.toFixed(2) + 'fr ' + heFr.toFixed(2) + 'fr');
    }

    // ── Resizable Layout ────────────────────────────
    var LAYOUT_PRESETS = {
        study:       { sidebar: 260, pane: 380 },
        split:       { sidebar: 240, pane: null },  // null = use vw calc
        interlinear: { sidebar: 200, pane: null }
    };

    function initResizeHandles() {
        var sidebarHandle = document.getElementById('sidebarHandle');
        var paneHandle = document.getElementById('paneHandle');
        if (sidebarHandle) setupDrag(sidebarHandle, 'sidebar');
        if (paneHandle) setupDrag(paneHandle, 'pane');

        // Restore saved layout
        var saved = JSON.parse(localStorage.getItem('atl-layout') || 'null');
        if (saved) {
            if (saved.sidebar) document.documentElement.style.setProperty('--col-sidebar', saved.sidebar);
            if (saved.pane && readingPaneOpen) document.documentElement.style.setProperty('--col-pane', saved.pane);
        }

        // Preset buttons
        var presetBtns = document.querySelectorAll('.preset-btn');
        presetBtns.forEach(function(btn) {
            btn.addEventListener('click', function() {
                presetBtns.forEach(function(b) { b.classList.remove('active'); });
                btn.classList.add('active');
                applyPreset(btn.dataset.preset);
            });
        });
    }

    function setupDrag(handle, target) {
        handle.addEventListener('mousedown', function(e) {
            e.preventDefault();
            handle.classList.add('active');
            document.body.style.cursor = 'col-resize';
            document.body.style.userSelect = 'none';
            var startX = e.clientX;
            var startWidth;

            if (target === 'sidebar') {
                startWidth = sidebar.getBoundingClientRect().width;
            } else {
                startWidth = readingPane.getBoundingClientRect().width;
            }

            function onMove(ev) {
                var delta = ev.clientX - startX;
                if (target === 'sidebar') {
                    var newW = Math.max(160, Math.min(450, startWidth + delta));
                    document.documentElement.style.setProperty('--col-sidebar', newW + 'px');
                } else {
                    var newW = Math.max(280, Math.min(window.innerWidth * 0.7, startWidth - delta));
                    document.documentElement.style.setProperty('--col-pane', newW + 'px');
                }
            }

            function onUp() {
                handle.classList.remove('active');
                document.body.style.cursor = '';
                document.body.style.userSelect = '';
                document.removeEventListener('mousemove', onMove);
                document.removeEventListener('mouseup', onUp);
                saveLayout();
                // Clear preset active state since user customized
                document.querySelectorAll('.preset-btn').forEach(function(b) { b.classList.remove('active'); });
            }

            document.addEventListener('mousemove', onMove);
            document.addEventListener('mouseup', onUp);
        });
    }

    function applyPreset(name) {
        var p = LAYOUT_PRESETS[name];
        if (!p) return;
        document.documentElement.style.setProperty('--col-sidebar', p.sidebar + 'px');
        if (p.pane !== null) {
            document.documentElement.style.setProperty('--col-pane', p.pane + 'px');
        } else {
            // Dynamic: split available space
            var sidebarW = p.sidebar + 8; // sidebar + 2 handles
            var remaining = window.innerWidth - sidebarW;
            var paneW;
            if (name === 'interlinear') {
                paneW = Math.round(remaining * 0.6);
            } else {
                paneW = Math.round(remaining * 0.48);
            }
            document.documentElement.style.setProperty('--col-pane', paneW + 'px');
        }
        saveLayout();
    }

    function saveLayout() {
        var layout = {
            sidebar: getComputedStyle(document.documentElement).getPropertyValue('--col-sidebar').trim() || '260px',
            pane: readingPaneOpen ? (getComputedStyle(document.documentElement).getPropertyValue('--col-pane').trim() || null) : null
        };
        localStorage.setItem('atl-layout', JSON.stringify(layout));
    }

    function initAccessibility() {
        // Apply saved states
        applyILRows();
        if (highContrast) document.body.classList.add('high-contrast');
        initStudyToggles();
        initColWidthSlider();
        initResizeHandles();

        // Sidebar keyboard navigation
        sidebarNav.addEventListener('keydown', function(e) {
            var links = Array.from(sidebarNav.querySelectorAll('.chapter-link, .era-toggle, .library-text-link'));
            var idx = links.indexOf(document.activeElement);
            if (idx < 0) return;
            if (e.key === 'ArrowDown') {
                e.preventDefault();
                if (idx < links.length - 1) links[idx + 1].focus();
            } else if (e.key === 'ArrowUp') {
                e.preventDefault();
                if (idx > 0) links[idx - 1].focus();
            } else if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                links[idx].click();
            }
        });

        // Category collapse/expand
        document.addEventListener('click', function(e) {
            var catLabel = e.target.closest('.library-cat-label');
            if (catLabel) {
                var category = catLabel.closest('.library-category');
                if (category) category.classList.toggle('collapsed');
            }
        });

        // Word cards: keyboard activation
        readingPaneContent.addEventListener('keydown', function(e) {
            if ((e.key === 'Enter' || e.key === ' ') && e.target.classList.contains('il-word')) {
                e.preventDefault();
                showWordPopup(e.target);
            }
        });
    }

    // ── Copy Functions ──────────────────────────────────────
    function showCopyToast(msg) {
        var toast = document.getElementById('copyToast');
        toast.textContent = msg || 'Copied!';
        toast.classList.add('visible');
        clearTimeout(toast._timer);
        toast._timer = setTimeout(function() {
            toast.classList.remove('visible');
        }, 1800);
    }

    function writeClipboard(text) {
        navigator.clipboard.writeText(text).then(function() {
            showCopyToast('Copied to clipboard!');
        }).catch(function() {
            var ta = document.createElement('textarea');
            ta.value = text;
            ta.style.position = 'fixed';
            ta.style.opacity = '0';
            document.body.appendChild(ta);
            ta.select();
            document.execCommand('copy');
            document.body.removeChild(ta);
            showCopyToast('Copied to clipboard!');
        });
    }

    function getVerseText(chapterNum, verseNum, format) {
        var ilData = getTextInterlinear(currentILBook);
        var data = ilData[String(chapterNum)];
        if (!data || !data.verses) return '';
        var verse = data.verses.find(function(v) { return v.num === verseNum; });
        if (!verse) return '';

        var ref = getTextName(currentILBook) + ' ' + chapterNum + ':' + verseNum;

        var glosses = verse.words.slice().reverse()
            .map(function(w) { return w.g || ''; })
            .filter(function(g) { return g && g !== 'properly' && g !== 'untranslatable'; });
        var sentence = glosses.join(' ').replace(/\s*\+\s*/g, ' ').replace(/\s{2,}/g, ' ').trim();
        var hebrew = verse.words.map(function(w) { return w.h || ''; }).join(' ');

        if (format === 'english') return ref + ' \u2014 ' + sentence;
        if (format === 'hebrew') return ref + ' \u2014 ' + hebrew;
        if (format === 'interlinear') {
            var lines = [ref];
            verse.words.forEach(function(w) {
                lines.push('  ' + (w.h || '') + '  ' + (w.t || '') + '  (' + (w.s || '') + ')  ' + (w.g || '') + '  [' + (w.m || '') + ']');
            });
            return lines.join('\n');
        }
        return ref + '\n' + sentence + '\n' + hebrew;
    }

    function copyVerse(verseNum) {
        var text = getVerseText(currentILChapter, verseNum, 'both');
        if (text) writeClipboard(text);
    }

    function copyChapter(format) {
        var ilData = getTextInterlinear(currentILBook);
        var data = ilData[String(currentILChapter)];
        if (!data || !data.verses) return;

        var lines = [getTextName(currentILBook) + ' ' + currentILChapter, ''];
        data.verses.forEach(function(verse) {
            lines.push(getVerseText(currentILChapter, verse.num, format));
            if (format === 'interlinear') lines.push('');
        });

        writeClipboard(lines.join('\n'));
    }

    function copyStudyContent(chapterId) {
        var card = document.getElementById(chapterId);
        if (!card) return;

        var parts = [];
        var ref = card.querySelector('.chapter-ref');
        var title = card.querySelector('h3');
        var synopsis = card.querySelector('.synopsis');

        if (ref) parts.push(ref.textContent.trim());
        if (title) parts.push(title.textContent.trim());
        if (synopsis) parts.push('\n' + synopsis.textContent.trim());

        var scripture = card.querySelector('.scripture-block');
        if (scripture) {
            var vref = scripture.querySelector('.verse-ref');
            var vtext = scripture.querySelector('.verse-text');
            if (vref && vtext) parts.push('\n' + vref.textContent.trim() + '\n' + vtext.textContent.trim());
        }

        card.querySelectorAll('.section-block').forEach(function(sec) {
            var heading = sec.querySelector('h4');
            var body = sec.querySelector('.section-body');
            if (heading) parts.push('\n## ' + heading.textContent.trim());
            if (body) parts.push(body.textContent.trim());
        });

        var ane = card.querySelector('.ane-callout .callout-body');
        if (ane) parts.push('\n[ANE Context]\n' + ane.textContent.trim());

        var council = card.querySelector('.council-note .callout-body');
        if (council) parts.push('\n[Heavenly Court]\n' + council.textContent.trim());

        writeClipboard(parts.join('\n'));
    }

    function exportChapterMarkdown(chapterId) {
        var ch = getChapterById(chapterId);
        if (!ch) { showCopyToast('Chapter not found'); return; }

        var md = [];
        md.push('# ' + ch.ref);
        md.push('## ' + ch.title);
        md.push('');

        if (ch.synopsis) {
            md.push('### Synopsis');
            md.push(ch.synopsis);
            md.push('');
        }

        if (ch.key_verse) {
            md.push('### Key Verse');
            md.push('> **' + ch.key_verse.ref + '** — ' + ch.key_verse.text);
            md.push('> *(' + ch.key_verse.translation + ')*');
            md.push('');
        }

        if (ch.hebrew_terms && ch.hebrew_terms.length > 0) {
            md.push('### Key Terms');
            ch.hebrew_terms.forEach(function(t) {
                if (typeof t === 'string') {
                    md.push('- **' + t.split('(')[0].trim() + '** — ' + (t.indexOf('(') > -1 ? t.substring(t.indexOf('(') + 1).replace(/\)$/, '') : t));
                } else if (t.term) {
                    md.push('- **' + t.term + '** (' + (t.transliteration || '') + ') — ' + (t.definition || ''));
                }
            });
            md.push('');
        }

        if (ch.ane_backdrop) {
            md.push('### Ancient Near Eastern Context');
            md.push(ch.ane_backdrop);
            md.push('');
        }

        if (Array.isArray(ch.second_temple) && ch.second_temple.length > 0) {
            md.push('### Second Temple Sources');
            ch.second_temple.forEach(function(s) {
                md.push('- **' + s.source + '** — ' + s.summary);
                if (s.relevance) md.push('  - *Relevance:* ' + s.relevance);
            });
            md.push('');
        }

        if (ch.cross_refs && ch.cross_refs.length > 0) {
            md.push('### Cross References');
            ch.cross_refs.forEach(function(raw) {
                var xr = normXref(raw);
                md.push('- **' + xr.ref + '**' + (xr.note && xr.note !== xr.ref ? ' — ' + xr.note : '') + (xr.type ? ' [' + xr.type + ']' : ''));
            });
            md.push('');
        }

        if (ch.divine_council_note) {
            md.push('### Heavenly Court Lens');
            md.push(ch.divine_council_note);
            md.push('');
        }

        if (ch.sections) {
            md.push('### Commentary');
            if (typeof ch.sections === 'string') {
                // HTML sections — strip tags for markdown
                var tmp = document.createElement('div');
                tmp.innerHTML = ch.sections;
                tmp.querySelectorAll('h4').forEach(function(h) {
                    md.push('#### ' + h.textContent.trim());
                });
                tmp.querySelectorAll('p').forEach(function(p) {
                    md.push(p.textContent.trim());
                    md.push('');
                });
            } else if (Array.isArray(ch.sections)) {
                ch.sections.forEach(function(sec) {
                    if (sec.heading) md.push('#### ' + sec.heading);
                    if (sec.body) md.push(sec.body);
                    md.push('');
                });
            }
        }

        md.push('---');
        md.push('*Exported from Ancient Texts Study App*');

        var content = md.join('\n');
        var filename = ch.id.replace(/[^a-z0-9-]/g, '_') + '.md';

        // Download as file
        var blob = new Blob([content], { type: 'text/markdown' });
        var url = URL.createObjectURL(blob);
        var a = document.createElement('a');
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
        showCopyToast('Exported ' + filename);
    }

    // ── Study Notes (user annotations per chapter) ──────────
    function openStudyNoteEditor(chapterId) {
        var existing = studyNotes[chapterId] || {};
        var overlay = document.createElement('div');
        overlay.className = 'study-note-overlay';
        overlay.innerHTML = '<div class="study-note-modal">' +
            '<div class="study-note-modal-header">' +
            '<span>\uD83D\uDCCC Leave a Note</span>' +
            '<button class="study-note-modal-close">\u2715</button>' +
            '</div>' +
            '<div class="study-note-modal-chapter">' + chapterId + '</div>' +
            '<textarea class="study-note-textarea" placeholder="Type your note, feedback, or question about this chapter...">' +
            (existing.text ? existing.text.replace(/</g, '&lt;') : '') +
            '</textarea>' +
            '<div class="study-note-modal-actions">' +
            '<button class="study-note-save">Save Note</button>' +
            (existing.text ? '<button class="study-note-remove">Delete Note</button>' : '') +
            '</div>' +
            '</div>';

        document.body.appendChild(overlay);
        var textarea = overlay.querySelector('.study-note-textarea');
        setTimeout(function() { textarea.focus(); }, 100);

        overlay.querySelector('.study-note-modal-close').addEventListener('click', function() {
            document.body.removeChild(overlay);
        });
        overlay.addEventListener('click', function(ev) {
            if (ev.target === overlay) document.body.removeChild(overlay);
        });
        overlay.querySelector('.study-note-save').addEventListener('click', function() {
            var text = textarea.value.trim();
            if (text) {
                studyNotes[chapterId] = {
                    text: text,
                    date: new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })
                };
                localStorage.setItem('atl-study-notes', JSON.stringify(studyNotes));
                syncAfterChange();
                showCopyToast('\uD83D\uDCCC Note saved');
                refreshCurrentView();
            }
            document.body.removeChild(overlay);
        });
        var removeBtn = overlay.querySelector('.study-note-remove');
        if (removeBtn) {
            removeBtn.addEventListener('click', function() {
                delete studyNotes[chapterId];
                localStorage.setItem('atl-study-notes', JSON.stringify(studyNotes));
                syncAfterChange();
                showCopyToast('Note deleted');
                refreshCurrentView();
                document.body.removeChild(overlay);
            });
        }
    }

    function deleteStudyNote(chapterId) {
        if (!studyNotes[chapterId]) return;
        delete studyNotes[chapterId];
        localStorage.setItem('atl-study-notes', JSON.stringify(studyNotes));
        syncAfterChange();
        showCopyToast('Note deleted');
        refreshCurrentView();
    }

    function refreshCurrentView() {
        if (currentText) {
            // Clear cache so re-render picks up note changes
            if (typeof textContentCache !== 'undefined') {
                delete textContentCache[currentText];
            }
            if (singleChapterMode) {
                renderSingleChapterView(currentText, currentChapterIndex);
            } else {
                showTextContent(currentText);
            }
        }
    }

    // ── Ancient World Map ────────────────────────────────────
    var mapInstance = null;
    var mapMarkers = [];
    var mapCategories = {
        'biblical':   { color: '#c9a84c', label: 'Biblical Sites',      icon: '\u2726' },
        'typology':   { color: '#b5564a', label: 'Christ Typology',     icon: '\u2670' },
        'watcher':    { color: '#9b7ec8', label: 'Watcher Geography',   icon: '\u2604' },
        'megalith':   { color: '#b07050', label: 'Megaliths & Anomalies', icon: '\u25B2' },
        'pyramid':    { color: '#d4a853', label: 'Global Pyramids',     icon: '\u25B3' },
        'dss':        { color: '#5b8dbf', label: 'Dead Sea Scroll Sites', icon: '\u2720' },
        'cultural':   { color: '#2d9a8f', label: 'Cultural Parallels',  icon: '\u2735' },
        'crater':     { color: '#6b7b8d', label: 'Impact Craters',      icon: '\u25CE' },
        'anomaly':    { color: '#e07020', label: 'Anomalous Sites',     icon: '\u26A1' },
        'underwater': { color: '#00bcd4', label: 'Underwater Ruins',    icon: '\uD83C\uDF0A' },
        'native':     { color: '#8b6e4f', label: 'Indigenous Traditions', icon: '\u25C8' }
    };

    var MAP_SITES = [
        // ── BIBLICAL SITES ──
        {cat:'biblical', name:'Garden of Eden (Traditional)', lat:30.96, lng:47.42,
         desc:'Confluence of Tigris and Euphrates. Genesis 2:10-14 describes four rivers flowing from Eden. Southern Iraq matches the geography.',
         refs:'Genesis 2:8-14', img:'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Shatt_al-Arab.jpg/320px-Shatt_al-Arab.jpg'},
        {cat:'biblical', name:'Mount Ararat', lat:39.7, lng:44.3,
         desc:'Traditional landing site of Noah\'s Ark. The volcanic summit (5,137m) is permanently snow-capped. Multiple expeditions have searched for ark remains.',
         refs:'Genesis 8:4', img:'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Agri_Dagi_or_Mount_Ararat.jpg/320px-Agri_Dagi_or_Mount_Ararat.jpg'},
        {cat:'biblical', name:'Babel / Babylon', lat:32.54, lng:44.42,
         desc:'Site of the Tower of Babel and later the Neo-Babylonian Empire. The ziggurat Etemenanki ("Foundation of Heaven and Earth") may be the tower\'s historical echo.',
         refs:'Genesis 11:1-9; Deuteronomy 32:8',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Reconstruction_of_the_Temple_of_Marduk_and_the_Tower_of_Babel.jpg/320px-Reconstruction_of_the_Temple_of_Marduk_and_the_Tower_of_Babel.jpg'},
        {cat:'biblical', name:'Ur of the Chaldeans', lat:30.96, lng:46.1,
         desc:'Abraham\'s birthplace. Excavated by Leonard Woolley (1922-34), revealing a sophisticated Sumerian city with the Royal Tombs and ziggurat of Nanna.',
         refs:'Genesis 11:31; Acts 7:2-4',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Ur_-_Ziggurat_-_2011.jpg/320px-Ur_-_Ziggurat_-_2011.jpg'},
        {cat:'biblical', name:'Haran', lat:36.87, lng:39.03,
         desc:'Abraham\'s stopping point before Canaan. A major city on ancient trade routes. Terah died here. Jacob fled here to Laban.',
         refs:'Genesis 11:31-12:1; Genesis 28:10'},
        {cat:'biblical', name:'Jerusalem / Temple Mount', lat:31.7781, lng:35.2354,
         desc:'City of David, Solomon\'s Temple, Second Temple. The Holy of Holies was the earthly seat of YHWH\'s divine council. Destroyed 586 BC and 70 AD.',
         refs:'2 Samuel 5:7; 1 Kings 6; Psalm 82; Ezekiel 10-11', img:'https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Jerusalem_Dome_of_the_rock_BW_14.JPG/320px-Jerusalem_Dome_of_the_rock_BW_14.JPG'},
        {cat:'biblical', name:'Mount Sinai (Jebel Musa)', lat:28.5394, lng:33.9752,
         desc:'Traditional site where Moses received the Torah. The theophany of Exodus 19 describes the divine council descending with thunder, lightning, and trumpet blast.',
         refs:'Exodus 19-20; Deuteronomy 33:2', img:'https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Catherine%27s_monastery.jpg/320px-Catherine%27s_monastery.jpg'},
        {cat:'biblical', name:'Sodom & Gomorrah (Bab edh-Dhra)', lat:31.25, lng:35.53,
         desc:'Sites near the Dead Sea destroyed by "fire and brimstone." Archaeological evidence at Tall el-Hammam shows a massive destruction event ~1650 BC consistent with a cosmic airburst.',
         refs:'Genesis 19; Jude 1:7',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Dead_Sea_by_David_Shankbone.jpg/320px-Dead_Sea_by_David_Shankbone.jpg'},
        {cat:'biblical', name:'Bethel', lat:31.93, lng:35.22,
         desc:'Where Jacob saw the ladder reaching to heaven with angels ascending and descending. A gateway between the human and divine realms.',
         refs:'Genesis 28:10-22'},
        {cat:'biblical', name:'Shechem', lat:32.21, lng:35.28,
         desc:'Where Abraham first received God\'s promise of the land. Between Mt. Ebal and Mt. Gerizim. The covenant renewal site.',
         refs:'Genesis 12:6; Joshua 24'},
        {cat:'biblical', name:'Peniel', lat:32.19, lng:35.62,
         desc:'Where Jacob wrestled with the divine being ("a man" who is also God) through the night and was renamed Israel.',
         refs:'Genesis 32:22-32'},

        // ── WATCHER GEOGRAPHY ──
        {cat:'watcher', name:'Mount Hermon', lat:33.4167, lng:35.8571,
         desc:'Where the 200 Watchers descended and swore an oath (1 Enoch 6:6). Located at 33\u00B033\'N from the Paris Meridian\u2014a coordinate loaded with esoteric significance. Today hosts a UN observation facility on its summit. The name means "devoted to destruction" (Hebrew: cherem).',
         refs:'1 Enoch 6:1-6; Deuteronomy 3:8-9; Psalm 133:3',
         note:'The 33.33\u00B0 latitude (Paris Meridian) connection: Before the 1884 Greenwich switch, Paris was the prime meridian. Mt. Hermon sits at exactly 33\u00B033\' on that system. The number 33 recurs in esoteric traditions (33 degrees of Freemasonry, Jesus crucified at 33, 33 vertebrae in the spine). Coincidence or pattern?',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Mount_Hermon_from_Golan.jpg/320px-Mount_Hermon_from_Golan.jpg'},
        {cat:'watcher', name:'Azazel\'s Desert Prison', lat:31.0, lng:35.3,
         desc:'The wilderness of Dudael where Azazel was bound. The scapegoat ritual (Leviticus 16) sends a goat "for Azazel" into the desert\u2014a ritual acknowledgment of the imprisoned Watcher.',
         refs:'1 Enoch 10:4-6; Leviticus 16:8-10'},
        {cat:'watcher', name:'Dan / Caesarea Philippi', lat:33.25, lng:35.69,
         desc:'At the base of Mt. Hermon. The "Gates of Hades" cave where pagan worship occurred. Jesus deliberately chose THIS location to declare "the gates of Hades shall not prevail."',
         refs:'Matthew 16:13-18; Judges 18',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Caesarea_Philippi_cave.jpg/320px-Caesarea_Philippi_cave.jpg'},
        {cat:'watcher', name:'Valley of Hinnom (Gehenna)', lat:31.77, lng:35.23,
         desc:'The valley of child sacrifice to Molech, later became the image of hell itself. Where rebellious divine beings received worship through human sacrifice.',
         refs:'2 Kings 23:10; Jeremiah 7:31; Mark 9:43'},

        // ── MEGALITHS & ANOMALIES ──
        {cat:'megalith', name:'Baalbek (Heliopolis) \u2014 Largest Megaliths on Earth', lat:34.0069, lng:36.2039,
         desc:'The trilithon stones weigh 800+ TONS each. The "Stone of the Pregnant Woman" (~1,000 tons) and a larger block (~1,650 tons \u2014 the heaviest known quarried monolith in history) remain in the quarry 800m away. The Roman Temple of Jupiter sits ON TOP of a far older megalithic platform. Stones cut with millimeter accuracy, fitted without mortar so tightly a razor blade cannot fit between them, lifted 6+ meters high. No tool marks or lifting bosses typical of Roman work. 2026 studies argue the megalithic foundation predates the Romans by centuries or more. Located in the heart of Canaanite territory (Gen 10:15-19), the name "Baalbek" = "Lord of the Beqaa" \u2014 a major center of Baal worship that Scripture repeatedly condemns.',
         refs:'Gen 10:15-19; Gen 6:4; Deut 2-3; Josh 13:2-6; Ezek 28:12-19; Book of Giants; 1 Enoch 7-8',
         note:'GIANT LEGENDS: (1) Cain & Giants \u2014 oldest legend says Cain built the original fortress, destroyed in the Flood. (2) Nimrod & Giants \u2014 Arabic texts state "When Nimrod reigned in Lebanon, he sent giants to rebuild the fortress of Baalbek" as an extension of Babel. (3) Stone of the Pregnant Woman \u2014 a pregnant female jinn promised to move it if fed until delivery; she vanished after birth. (4) Jinn/Supernatural Builders \u2014 Arab folklore credits jinn (fallen supernatural beings) with quarrying and lifting the stones, some under Solomon\'s command. These are DISTORTED MEMORIES of genuine post-Flood reality: advanced building knowledge from Gen 4:20-22, Nephilim/Rephaim activity "also afterward" (Gen 6:4), and Baal worship centers built by the cursed Canaanite line (Gen 9:25). God judged their pride (Ezek 28:11-19) while using their skills for His Temple and Word.', img:'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Baalbek_-_Pair_of_stones.jpg/320px-Baalbek_-_Pair_of_stones.jpg'},
        {cat:'megalith', name:'Gobekli Tepe', lat:37.2231, lng:38.9225,
         desc:'Built ~9,600 BC\u2014the oldest known temple complex. Massive T-shaped pillars (up to 20 tons) carved with animal reliefs. Built by "hunter-gatherers" with no known metalwork, agriculture, or writing. Deliberately BURIED around 8,000 BC. Why?',
         refs:'Genesis 4-6 (antediluvian civilization)',
         note:'Predates Stonehenge by 6,000 years. The deliberate burial echoes the flood narrative\u2014was antediluvian knowledge intentionally preserved or hidden?', img:'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/G%C3%B6bekli_Tepe%2C_Urfa.jpg/320px-G%C3%B6bekli_Tepe%2C_Urfa.jpg'},
        {cat:'megalith', name:'Stonehenge', lat:51.1789, lng:-1.8262,
         desc:'Built ~3000-2000 BC. Bluestones transported 150 miles from Wales. Sarsen stones weigh up to 25 tons. Precisely aligned to solstice. The Watchers taught astronomy and calendar systems (1 Enoch 8:3).',
         refs:'1 Enoch 8:3 (astronomical knowledge)', img:'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Stonehenge2007_07_30.jpg/320px-Stonehenge2007_07_30.jpg'},
        {cat:'megalith', name:'Sacsayhuaman, Peru', lat:-13.5092, lng:-71.9822,
         desc:'Polygonal stone walls stretching 600 meters, built from limestone blocks up to 200 tons — some larger than a city bus. Fitted with such precision that a piece of paper cannot pass between the joints, and in many places not even a razor blade. The wall is not straight but zigzags in a deliberate pattern with "impossible" angles and curves — an engineering choice that makes it earthquake-resistant. No two stones have the same shape, yet every stone fits its neighbors perfectly on all sides. The Inca themselves said they did not build it — their legends attribute the construction to the Ayar brothers (divine ancestors) or to beings called "Viracocha" who softened stone and moved blocks with sound or supernatural power. Spanish soldiers, seeing it for the first time, wrote home that no human hands could have assembled it.',
         refs:'Numbers 13:33 (Nephilim in the land); Gen 6:4 (heroes of old, men of renown)',
         note:'The Spanish chronicler Cieza de León wrote (1553): the Inca told him the fortress was built before their time by people who possessed secret knowledge to soften and shape rock. Three construction styles are visible — the most ancient at the base, with the largest and most precise stones. Each successive layer is less impressive. Classic signature of site re-use by a less capable successor civilization.', img:'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Sacsayhuam%C3%A1n_D%C3%A9cembre_2006_-_Vue_Panoramique.jpg/320px-Sacsayhuam%C3%A1n_D%C3%A9cembre_2006_-_Vue_Panoramique.jpg'},
        {cat:'megalith', name:'Puma Punku, Bolivia', lat:-16.5616, lng:-68.6795,
         desc:'H-shaped stone blocks with machine-like precision cuts — slots, recesses, and drill holes that look CNC-machined. The primary stone is red sandstone and andesite (extremely hard), cut with tolerances under a millimeter. The blocks interlock like puzzle pieces, without mortar, using metal I-shaped clamps melted in place. At 12,600 ft elevation, the nearest quarry is 10+ miles away. The entire site is SHATTERED — massive stones scattered as if by a catastrophic explosion or earthquake, consistent with a cataclysmic event. Mainstream archaeology dates construction to ~500 AD, but some researchers point to far earlier origins. The Aymara say it was built "in a single night by the gods" before the existing sun rose. No tool marks consistent with stone or bronze implements have been identified.',
         refs:'1 Enoch 7-8 (Watcher-taught arts); Gen 6:4 (mighty men of old)',
         note:'The level of precision at Puma Punku is the single most difficult artifact to explain in all of ancient history. The H-blocks have identical geometry repeated across many pieces — suggesting industrial-scale precision, not hand-carving. The destruction of the site is equally mysterious: it looks less like ruin-by-time and more like deliberate or cataclysmic demolition.', img:'https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Puma_Punku.jpg/320px-Puma_Punku.jpg'},
        {cat:'megalith', name:'Easter Island (Rapa Nui)', lat:-27.1127, lng:-109.3497,
         desc:'The moai statues (up to 82 tons) carved and transported across the island. Local legends say they "walked" into place through mana (spiritual power). 887 statues on a remote Pacific island.',
         refs:'Genesis 6:4 (heroes of old, men of renown)',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Moai_Rano_raraku.jpg/320px-Moai_Rano_raraku.jpg'},

        // ── GLOBAL PYRAMIDS ──
        {cat:'pyramid', name:'Great Pyramid of Giza', lat:29.9792, lng:31.1342,
         desc:'2.3 million blocks averaging 2.5 tons. Built in ~20 years = 1 block every 2-5 minutes, 24/7, no breaks. The math doesn\'t work with copper tools and ramps. Aligned to true north within 3/60th of a degree. Internal chambers contain granite transported 500 miles from Aswan.',
         refs:'Job 38:4-7 (foundations of the earth)',
         note:'Timeline problem: Mainstream = ~2560 BC by Khufu with 20,000-30,000 workers. But: 2.3M blocks \u00F7 20 years \u00F7 365 days = 315 blocks/day = 1 every 4.5 minutes. Including quarrying, transporting, and precision-placing multi-ton blocks. With copper tools. At altitude. With perfect astronomical alignment. Something doesn\'t add up.', img:'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Kheops-Pyramid.jpg/320px-Kheops-Pyramid.jpg'},
        {cat:'pyramid', name:'Pyramid of the Sun, Teotihuacan', lat:19.6925, lng:-98.8431,
         desc:'Third-largest pyramid on Earth. Base perimeter nearly identical to the Great Pyramid. Built ~100 AD. Teotihuacan means "the place where men became gods"\u2014or more literally, "birthplace of the gods." Builders unknown.',
         refs:'Genesis 6:4; Deuteronomy 32:8 (divine allotment of nations)', img:'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Teotihuac%C3%A1n_-_Sonnenpyramide.jpg/320px-Teotihuac%C3%A1n_-_Sonnenpyramide.jpg'},
        {cat:'pyramid', name:'Borobudur, Indonesia', lat:-7.6079, lng:110.2038,
         desc:'Largest Buddhist temple in the world. 2 million stone blocks. 72 bell-shaped stupas. Built ~800 AD but on a much older foundation. Indonesia\'s Ring of Fire parallels other anomalous sites.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Borobudur-Nothwest-view.jpg/320px-Borobudur-Nothwest-view.jpg'},
        {cat:'pyramid', name:'White Pyramid of Xi\'an, China', lat:34.3381, lng:108.5694,
         desc:'Over 40 pyramids in Shaanxi province. The largest rivals Giza in base area. Chinese government restricts access. Built 2000+ years ago. Aligned to cardinal directions like Giza and Teotihuacan.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Maoling_Mausoleum.jpg/320px-Maoling_Mausoleum.jpg'},
        {cat:'pyramid', name:'Gunung Padang, Indonesia', lat:-6.9944, lng:107.0564,
         desc:'Controversial site. Core samples suggest construction may date to 20,000-27,000 BP, which would make it the oldest pyramid structure on Earth. If confirmed, this predates the end of the Ice Age and all known civilizations.',
         note:'Geological dating is disputed. But even conservative estimates put it at 5000+ BC\u2014older than Giza.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gunung_Padang_Parahyangan.jpg/320px-Gunung_Padang_Parahyangan.jpg'},
        {cat:'pyramid', name:'Antarctica Ice Anomalies', lat:-79.98, lng:-81.96,
         desc:'Satellite imagery reveals symmetrical, pyramid-shaped mountains in the Ellsworth range. Natural formation or remnant of pre-Ice-Age construction? Antarctica was ice-free until ~34 million years ago\u2014but the Piri Reis map (1513) shows accurate Antarctic coastline.',
         note:'Speculative but persistent. The Piri Reis map, drawn from older source maps, depicts Antarctica without ice. Combined with the global pyramid distribution pattern, Antarctica remains an open question.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Ellsworth_Mountains_nunataks.jpg/320px-Ellsworth_Mountains_nunataks.jpg'},

        // ── DEAD SEA SCROLL SITES ──
        {cat:'dss', name:'Qumran', lat:31.7414, lng:35.4594,
         desc:'The settlement where the Dead Sea Scrolls community lived. 11 caves yielded ~900 manuscripts including the Community Rule, War Scroll, and copies of 1 Enoch and the Book of Giants.',
         refs:'1QS, 1QM, 4Q530-533', img:'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Qumran.jpg/320px-Qumran.jpg'},
        {cat:'dss', name:'Masada', lat:31.3159, lng:35.3536,
         desc:'Herod\'s fortress where 960 Jewish rebels died rather than surrender to Rome (73 AD). Josephus\'s account of the mass suicide is among the most debated passages in his Jewish War.',
         refs:'Josephus, War 7.389-401'},
        {cat:'dss', name:'Wadi Murabba\'at', lat:31.63, lng:35.42,
         desc:'Caves south of Qumran where Bar Kokhba letters and biblical manuscripts were found. The letters reveal the Second Jewish Revolt (132-135 AD) leader\'s correspondence.'},

        // ── CULTURAL PARALLELS & ESOTERICA ──
        {cat:'cultural', name:'Rosslyn Chapel, Scotland', lat:55.8553, lng:-3.1601,
         desc:'Built 1446 AD. Covered in carvings mixing Christian and pagan/esoteric imagery. Features "apprentice pillar" (Tree of Life?), Green Men, Templar crosses, and plants from the Americas\u2014carved 50 years before Columbus.',
         note:'The Templar-Freemason-Solomon connection. Knights Templar excavated the Temple Mount (1119-1128 AD). What did they find? Solomon\'s Temple contained the Ark, the mercy seat\u2014the physical throne of God\'s council.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Rosslyn_Chapel_2014.jpg/320px-Rosslyn_Chapel_2014.jpg'},
        {cat:'cultural', name:'Giza-Orion Alignment', lat:29.9773, lng:31.1325,
         desc:'Robert Bauval\'s Orion Correlation Theory: the three Giza pyramids mirror the three stars of Orion\'s Belt. The shaft in the King\'s Chamber points directly to Orion (Osiris) and Sirius (Isis). Astronomical encoding in stone.',
         note:'If the Watchers "taught the signs of the sun, moon, and stars" (1 Enoch 8:3), astronomical encoding in megalithic architecture is exactly what we\'d expect.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/All_Gizah_Pyramids.jpg/320px-All_Gizah_Pyramids.jpg'},
        {cat:'cultural', name:'Derinkuyu Underground City, Turkey', lat:38.3735, lng:34.7348,
         desc:'Underground city for 20,000 people, extending 18 stories deep. Built by unknown civilization. Could be sealed from the inside. A place to hide from... what? The flood? The Nephilim?',
         note:'Multiple underground cities in Cappadocia suggest a civilization that needed to go underground for extended periods. The scale exceeds mere defense.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Derinkuyu_Underground_City_9843_Nevit_Enhancer.jpg/320px-Derinkuyu_Underground_City_9843_Nevit_Enhancer.jpg'},
        {cat:'cultural', name:'Shroud of Turin, Italy', lat:45.0735, lng:7.6860,
         desc:'Cathedral of St. John the Baptist houses the most studied artifact in history. 14.3 x 3.6 ft linen cloth bearing the image of a crucified man. No pigment \u2014 image affects only outermost 200-600nm of fiber. 3D information encoded (VP8 analyzer, 1977). Blood type AB+, applied BEFORE image formed. 2019 WAXS dating: ~55 CE.',
         refs:'Matthew 27:59; Mark 15:46; John 19:40',
         note:'The 1988 C-14 dating (medieval) used a repaired corner. The 2019 Wide Angle X-ray Scattering method dates it to the 1st century. The Sudarium of Oviedo (Spain) has 124 matching blood stains and the same AB blood type.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Turin_shroud_positive_and_negative_displaying_original_color_information_708_x_465_pixels_94_KB.jpg/320px-Turin_shroud_positive_and_negative_displaying_original_color_information_708_x_465_pixels_94_KB.jpg'},
        {cat:'cultural', name:'Shroud Comparison: Sudarium of Oviedo', lat:43.3614, lng:-5.8434,
         desc:'The Sudarium (face cloth) housed in the Cathedral of Oviedo since the 7th century. 124 blood and serum stains match the Shroud of Turin. Same AB blood type. Documented chain of custody back to 570 AD.',
         refs:'John 20:7'},

        // ── PHOENICIAN / CANAANITE CITIES ──
        {cat:'biblical', name:'Tyre \u2014 Phoenician Capital', lat:33.2700, lng:35.2037,
         desc:'The greatest Phoenician city-state. Island fortress and mainland port. Hiram of Tyre supplied cedar and craftsmen for Solomon\'s Temple (1 Kings 5). Jezebel was a Sidonian princess who imported Baal worship into Israel (1 Kings 16:31). Tyre\'s pride \u2014 "I am a god, I sit in the seat of gods" (Ezek 28:2) \u2014 earned one of Scripture\'s most detailed judgments. Nebuchadnezzar besieged it for 13 years; Alexander literally scraped it into the sea (332 BC), fulfilling Ezek 26:4-5 to the letter. Tyre produced Tyrian purple dye from murex snails (10,000 snails per gram) \u2014 the most valuable commodity in the ancient world.',
         refs:'1 Kings 5:1-12; 9:26-28; Ezek 26\u201328 (full chapters); Isa 23; Matt 11:21-22',
         note:'EZEK 28:12-19 \u2014 The king of Tyre is described in language that transcends a mere human ruler: "You were in Eden, the garden of God... you were the anointed cherub who covers... I cast you to the ground." This passage is widely understood as addressing the spiritual power behind Tyre \u2014 Satan himself. The Phoenicians = the cursed Canaanite survivors (Gen 9:25 + 10:15) who escaped Joshua\'s conquest and became a persistent snare of Baal idolatry, child sacrifice, and pride. God judged them exactly as prophesied while using their alphabet (for Scripture) and cedar (for His Temple).'},
        {cat:'biblical', name:'Sidon \u2014 Firstborn of Canaan', lat:33.5600, lng:35.3750,
         desc:'Canaan\'s firstborn son (Gen 10:15). One of the most ancient Phoenician cities. Jezebel\'s homeland \u2014 her father Ethbaal was king of Sidon (1 Kings 16:31). Center of Baal and Astarte worship. Jesus visited the region of Tyre and Sidon (Matt 15:21-28), healing the Syrophoenician woman\'s daughter \u2014 showing grace even to the cursed line.',
         refs:'Gen 10:15; Josh 13:4-6; 1 Kings 16:31; Matt 15:21-28; Ezek 28:20-23',
         note:'God pronounced judgment on Sidon (Ezek 28:20-23): "I will send pestilence to her and blood to her streets." Yet Jesus deliberately entered this territory, extending mercy to a Canaanite woman whose faith exceeded Israel\'s. The curse of Gen 9:25 meets the grace of the gospel.'},
        {cat:'biblical', name:'Byblos (Gebal) \u2014 Oldest Phoenician City', lat:34.1200, lng:35.6500,
         desc:'Perhaps the oldest continuously inhabited city in the world (~5000 BC). The Greek word "biblion" (book) comes from Byblos \u2014 they exported Egyptian papyrus to Greece. Gebalite craftsmen worked on Solomon\'s Temple (1 Kings 5:18). The city was a major center of Baal worship, particularly Adonis/Tammuz rites with death-and-resurrection motifs \u2014 counterfeit echoes of Christ\'s true resurrection.',
         refs:'1 Kings 5:18; Josh 13:5; Ezek 27:9',
         note:'The Phoenician 22-letter alphabet (~1050 BC), ancestor of Greek, Latin, and all modern Western alphabets, was refined here. God sovereignly used the cursed Canaanite line to create the very writing system that would preserve His Word forever. The irony is staggering.'},
        {cat:'biblical', name:'Arwad (Arvad) \u2014 Northernmost Phoenician City', lat:34.8564, lng:35.8614,
         desc:'Tiny fortified island 3km offshore. The Arvadites are listed among Canaan\'s descendants (Gen 10:18). Warriors from Arvad served in Tyre\'s navy (Ezek 27:8,11). The northernmost Phoenician city-state, marking the edge of Canaanite territory.',
         refs:'Gen 10:18; Ezek 27:8,11'},
        {cat:'cultural', name:'Carthage \u2014 Phoenician Colony', lat:36.8528, lng:10.3234,
         desc:'Founded ~814 BC by Tyrian colonists led by Queen Dido. Became the western Mediterranean\'s dominant power. The tophet (child sacrifice precinct) confirms the biblical testimony about Canaanite religion \u2014 archaeological evidence of infant sacrifice to Ba\'al Hammon and Tanit. Destroyed by Rome in 146 BC (Third Punic War). "Punic" = "Phoenician" in Latin.',
         refs:'Lev 18:21; Deut 12:31; 2 Kings 23:10',
         note:'Carthage proves that wherever the cursed Canaanite line spread, they took their abominations with them. The tophet excavations found urns containing charred infant bones \u2014 exactly what Leviticus 18:21 and Deuteronomy 12:31 condemn. God\'s judgment on Canaan was not arbitrary \u2014 it was justice.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Carthage_-_The_Tophet.jpg/320px-Carthage_-_The_Tophet.jpg'},
        {cat:'cultural', name:'Uruk (Erech) \u2014 Nimrod\'s City / Gilgamesh\'s Uruk', lat:31.3225, lng:45.6364,
         desc:'One of the first great cities of Mesopotamia. Listed as part of Nimrod\'s kingdom (Gen 10:10 \u2014 "Erech"). The legendary king Gilgamesh ruled here \u2014 described as 2/3 divine, 1/3 human, with superhuman strength. The Gilgamesh Epic\'s Flood story (Utnapishtim builds a boat, sends birds, survives the deluge) is a distorted counterfeit of Noah\'s Flood in Genesis 6-9. The Epic twists God\'s sovereign judgment into polytheistic chaos, glorifying human/divine hybrids \u2014 exactly what Genesis 6:1-4 condemns as the cause of the Flood.',
         refs:'Gen 10:10; Gen 6:1-9; Gen 6:4 ("mighty men of renown")',
         note:'GILGAMESH COUNTERFEIT (C-level): Gilgamesh parallels Nimrod as a post-Flood "mighty hunter" and city-builder who rebels against the divine order. He fights the giant Humbaba in the cedar forest (echoing Rephaim in Lebanon/Bashan). His friend Enkidu is part-wild/giant-like (echoes of Gen 6:4 "mighty men of renown"). The Flood account twists Noah\'s covenant into polytheistic myth. God preserves the pure account in Genesis to expose these distortions, pointing to Christ \u2014 the true Mighty One who conquers death (Heb 2:14-15), unlike Gilgamesh\'s failed quest for immortality.'},

        // ── 33RD PARALLEL SITES ──
        {cat:'cultural', name:'Roswell, New Mexico', lat:33.39, lng:-104.52,
         desc:'Site of the 1947 UFO incident. Located at 33.39\u00B0N. Whatever actually happened, the 33rd parallel connection persists in esoteric literature.',
         note:'On the 33rd parallel: Hermon, Babylon, Damascus, Roswell, Phoenix. The number 33 recurs: Jesus died at 33, David reigned 33 years, 33 Masonic degrees, 33 vertebrae.'},
        {cat:'cultural', name:'Phoenix Lights, Arizona', lat:33.45, lng:-112.07,
         desc:'March 13, 1997: thousands of witnesses reported a massive V-shaped craft over Phoenix (33.45\u00B0N). The most witnessed UFO event in US history. Governor Fife Symington later admitted he saw it.',
         note:'Another major 33rd parallel event. The ancient divine council framework offers a lens: if rebellious spiritual beings have territorial authority (Daniel 10, Ephesians 6:12), unexplained phenomena at significant coordinates become more interesting.'},
        {cat:'cultural', name:'White Sands / Trinity Site, NM', lat:33.68, lng:-106.47,
         desc:'First nuclear detonation, July 16, 1945. The 33rd President (Harry Truman) ordered the bombings of Hiroshima (34.4\u00B0N) and Nagasaki (32.8\u00B0N). The most destructive technology ever created, tested and deployed near the 33rd parallel.',
         note:'The name "Trinity" was chosen by Oppenheimer. He quoted the Bhagavad Gita: "Now I am become Death, the destroyer of worlds." The forbidden knowledge the Watchers taught (1 Enoch 8:1) included weapons of war.'},

        // ── ADDITIONAL BIBLICAL/HISTORICAL ──
        {cat:'biblical', name:'Hebron (Kiriath-Arba) / Cave of Machpelah', lat:31.5326, lng:35.0998,
         desc:'Ancient name Kiriath-Arba means "City of Arba" \u2014 Arba was "the greatest man among the Anakim" (Joshua 14:15). The Anakim were the post-flood Nephilim clan. Caleb drove them out (Joshua 15:13-14). Burial site of Abraham, Sarah, Isaac, Rebekah, Jacob, and Leah — the patriarchs purchased their burial ground in the heart of giants\' territory. The subterranean cave beneath the Herodian enclosure has never been fully excavated.',
         refs:'Genesis 23:1-20; Genesis 49:29-32; Joshua 14:15; Numbers 13:22',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Cave_of_Machpelah.jpg/320px-Cave_of_Machpelah.jpg'},
        {cat:'biblical', name:'Gath of the Philistines (Tell es-Safi)', lat:31.6103, lng:34.8489,
         desc:'Home of Goliath and his four giant relatives (2 Samuel 21:15-22). After Joshua cleared most Anakim, survivors remained in Gaza, Gath, and Ashdod (Joshua 11:22). In 2005, excavators found a pottery shard bearing the name "Goliath" in paleo-Semitic script, dated to c. 950 BC — within 70 years of David\'s famous encounter. Gath was home to four giant warriors descended from the Rephaim.',
         refs:'1 Samuel 17:4-51; 2 Samuel 21:15-22; Joshua 11:22; Numbers 13:33',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Goliath_inscription.jpg/220px-Goliath_inscription.jpg'},
        {cat:'biblical', name:'Bashan / Golan Heights', lat:32.95, lng:35.80,
         desc:'Kingdom of Og, last of the Rephaim. His bed was 13.5 feet long (Deuteronomy 3:11). Bashan was considered a gateway to the underworld in Ugaritic and Israelite tradition. Psalm 22:12: "Strong bulls of Bashan encircle me."',
         refs:'Deuteronomy 3:1-11; Psalm 22:12; Amos 4:1'},
        {cat:'watcher', name:'Raphael\'s Binding Site (Dudael)', lat:31.7, lng:35.4,
         desc:'1 Enoch 10:4-6: Raphael binds Azazel "hand and foot, and cast him into the darkness: and make an opening in the desert \u2014 which is in Dudael \u2014 and cast him therein." Traditionally located in the Judean wilderness near the Dead Sea.',
         refs:'1 Enoch 10:4-6; Leviticus 16:10'},
        {cat:'megalith', name:'Carnac Stones, France', lat:47.5916, lng:-3.0744,
         desc:'Over 3,000 standing stones arranged in parallel alignments stretching 4 kilometers. Erected ~4500-3300 BC. The largest stones (up to 350 tons, now fallen) are at the western end. Local Breton legend says they are Roman soldiers turned to stone by Merlin.',
         note:'Pre-Celtic, pre-Roman. Like Gobekli Tepe, this was built by people who shouldn\'t have had the organization or technology for monumental construction. The alignment patterns suggest astronomical knowledge.', img:'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Carnac_megalith_alignment_1.jpg/320px-Carnac_megalith_alignment_1.jpg'},
        {cat:'megalith', name:'Newgrange, Ireland', lat:53.6947, lng:-6.4754,
         desc:'Built ~3200 BC \u2014 older than both Stonehenge and the Giza pyramids. The passage tomb is precisely aligned so that on the winter solstice, sunlight floods the inner chamber through a roof box. Engineering of this precision by "primitive" Neolithic Irish is unexplained.',
         refs:'1 Enoch 8:3 (astronomical knowledge taught by Watchers)', img:'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Newgrange_%286%29.jpg/320px-Newgrange_%286%29.jpg'},
        {cat:'megalith', name:'Rujm el-Hiri (Gilgal Refaim)', lat:32.9932, lng:35.8175,
         desc:'A massive megalithic monument in the Golan Heights \u2014 five concentric stone circles with a central cairn. ~5000 BC. Hebrew name means "Wheel of the Giants" (Rephaim). Over 42,000 basalt rocks, weighing ~40,000 tons total. Visible only from the air. Connected to the Rephaim/Nephilim tradition \u2014 the giants of Bashan (Deut 3:11, Og\'s iron bed).',
         refs:'Deuteronomy 3:11,13; Joshua 12:4; 2 Samuel 5:18 (Valley of Rephaim)',
         note:'Located in biblical Bashan, territory of Og the giant king. The name "Gilgal Refaim" (Wheel of the Rephaim) directly connects this to the Nephilim tradition. No known builder civilization.', img:'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Rujm_el-Hiri_Aerial_View.jpg/320px-Rujm_el-Hiri_Aerial_View.jpg'},
        {cat:'megalith', name:'Dolmen Field, Golan Heights', lat:32.85, lng:35.78,
         desc:'The Golan Heights contain the highest concentration of dolmens in the Middle East \u2014 over 5,000 stone burial chambers. Many weigh 20-50 tons. Dated ~4500-3000 BC. Traditionally associated with the Rephaim/giants who inhabited Bashan.',
         refs:'Deuteronomy 3:13; Joshua 13:12',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Dolmen_in_Golan.jpg/320px-Dolmen_in_Golan.jpg'},
        {cat:'megalith', name:'Karnak Temple, Egypt', lat:25.7188, lng:32.6573,
         desc:'The largest ancient religious complex in the world. The Hypostyle Hall has 134 columns up to 24m tall, each weighing ~70 tons. The largest obelisk (by Hatshepsut) weighs 323 tons of solid granite. How these were quarried, transported, and erected remains debated.',
         refs:'Exodus 1:11 (built by forced labor)',
         note:'The scale of stone construction at Karnak exceeds anything achievable with the tools attributed to ancient Egyptians. The precision of the column placement suggests mathematical knowledge.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Karnak_Hypostyle_Hall.jpg/320px-Karnak_Hypostyle_Hall.jpg'},
        {cat:'megalith', name:'Aswan Unfinished Obelisk', lat:24.0776, lng:32.8977,
         desc:'A partially carved obelisk still lying in its quarry at Aswan. If completed, it would be 42m tall and weigh ~1,200 tons \u2014 the heaviest single stone ever attempted by ancient civilizations. Abandoned due to a crack. Provides unique evidence of quarrying methods.',
         note:'1,200 tons of solid granite. Modern cranes max out at ~300 tons. No satisfactory explanation for how ancient Egyptians planned to move this.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Unfinished_obelisk_Aswan.jpg/320px-Unfinished_obelisk_Aswan.jpg'},
        {cat:'megalith', name:'Ollantaytambo, Peru', lat:-13.2588, lng:-72.2636,
         desc:'Inca fortress with six massive rose-granite monoliths (each ~50 tons) fitted without mortar at the summit. The stone was quarried across a valley and up a mountain. The precision of the stonework rivals any ancient civilization. Local legend attributes it to giants.',
         note:'The "tired stones" (piedras cansadas) scattered along the route are explained by local tradition as stones abandoned by giants who grew weary.', img:'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Ollantaytambo%2C_Per%C3%BA%2C_2015-07-28%2C_DD_79.JPG/320px-Ollantaytambo%2C_Per%C3%BA%2C_2015-07-28%2C_DD_79.JPG'},
        {cat:'megalith', name:'Jiroft / Konar Sandal, Iran', lat:28.4977, lng:57.7327,
         desc:'A Bronze Age civilization (~3000 BC) discovered in 2001 in southeastern Iran. Massive ziggurats, sophisticated chlorite vessels, and evidence of advanced metallurgy. Some scholars connect this to the "Land of Aratta" mentioned in Sumerian texts. Evidence of a "lost" advanced civilization.',
         refs:'Genesis 10:22 (Elam, sons of Shem)',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Konar_Sandal.jpg/320px-Konar_Sandal.jpg'},
        {cat:'megalith', name:'Adam\'s Calendar, South Africa', lat:-25.8842, lng:30.5003,
         desc:'A stone circle in Mpumalanga, South Africa. Claims of extreme antiquity (75,000+ years) are controversial, but the site does show careful astronomical alignment. Some researchers connect it to ancient gold mining in the region.',
         note:'If the dating claims are accurate, this would be the oldest man-made structure. Mainstream archaeology disputes the extreme dates, but the stone arrangement is undeniably deliberate.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Adam%27s_Calendar_Mpumalanga.jpg/320px-Adam%27s_Calendar_Mpumalanga.jpg'},
        {cat:'underwater', name:'Yonaguni Monument, Japan', lat:24.4351, lng:122.9994,
         desc:'Discovered in 1987 by a dive instructor off the coast of Yonaguni Island, Japan\'s westernmost point. The submerged structure features right-angle terraces, flat vertical faces, parallel staircases, what appears to be a gateway or arch, and channels that cut straight lines — all inconsistent with natural erosion patterns. Marine geologist Masaaki Kimura (University of the Ryukyus) spent 15+ years diving the site and argues it is definitively man-made, citing tool marks, post holes, and carved human faces. At the last glacial maximum (~10,000 BC), sea levels were ~120m lower, meaning this structure was above sea level. If artificial, it predates every known civilization on Earth by thousands of years, challenging the entire conventional model of when organized society began. The mainstream geology community remains skeptical, attributing the features to natural fracturing of sandstone.',
         refs:'Genesis 7-8 (Flood raised sea levels); 1 Enoch 8:3 (Watcher-taught knowledge before the Flood)',
         note:'The key debate: sandstone naturally fractures along straight lines, but the COMBINATION of right angles, parallel steps, and what looks like a gateway argues against pure chance. If Kimura is correct, Yonaguni is the Rosetta Stone of lost pre-Flood civilization.', img:'https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Yonaguni_Monument.jpg/320px-Yonaguni_Monument.jpg'},
        {cat:'megalith', name:'Gunung Padang, Indonesia', lat:-6.9946, lng:107.0563,
         desc:'A megalithic site on a volcanic hill in Java. Core drilling in 2023 revealed buried construction layers potentially dating to 25,000+ BC, which would make it the oldest known pyramid. Five terraces of columnar basalt arranged with clear human purpose.',
         note:'If the deep-layer dating holds, this rewrites human history. Published in Archaeological Prospection (2023). Fierce academic debate ongoing.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gunung_Padang_Parahyangan.jpg/320px-Gunung_Padang_Parahyangan.jpg'},
        {cat:'megalith', name:'Malta Temples (Ggantija)', lat:36.0475, lng:14.2690,
         desc:'The Ggantija temples on Gozo (~3600 BC) are among the oldest free-standing structures on Earth \u2014 older than Stonehenge and the pyramids. Stones up to 50 tons. Built by a Neolithic island culture with no metal tools. Local Maltese legend says they were built by giants.',
         refs:'Genesis 6:4 (giants)',
         note:'"Ggantija" literally means "Giant\'s Tower" in Maltese. The temple builders vanished ~2500 BC with no clear successor.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Ggantija_temples_Gozo.jpg/320px-Ggantija_temples_Gozo.jpg'},
        {cat:'megalith', name:'Moai (Rano Raraku), Easter Island', lat:-27.1213, lng:-109.2863,
         desc:'The quarry where ~95% of the 887 moai statues were carved from compressed volcanic ash (tuff). The largest unfinished moai is 21m tall and would weigh ~270 tons. The Rapanui oral tradition says the moai "walked" to their platforms through mana (spiritual power).',
         note:'The islanders\' own explanation is supernatural. Modern experiments show they CAN be moved by rocking/walking with ropes, but the logistics of the largest ones (80+ tons) remain impressive.', img:'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Moai_Rano_raraku.jpg/320px-Moai_Rano_raraku.jpg'},
        // ── GROK MEGALITHIC EXPANSION ──
        {cat:'megalith', name:'Karahan Tepe', lat:37.41, lng:39.05,
         desc:'Older than G\u00f6bekli Tepe by centuries, only 5% excavated. In 2025, excavators found the first human face carved on a T-shaped pillar — confirming these are stylized divine beings arranged in assembly, not mere architecture. A figurine with sealed lips was discovered, hinting at the deliberate silencing of divine speech. According to 1 Enoch, the Watchers descended in the era this site was active. Similar T-shaped pillars with phallic and animal carvings, human head carved from bedrock, suggest a widespread pre-agricultural temple-building culture in southeastern Turkey.',
         refs:'1 Enoch 6:1-6; Genesis 6:1-4',
         note:'If these sites are pre-agricultural, it means organized religion preceded farming \u2014 the opposite of what secular archaeology predicted. Pre-Flood knowledge (Gen 4:20-22) carried through Babel?',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Karahan_Tepe_4.jpg/220px-Karahan_Tepe_4.jpg'},
        {cat:'megalith', name:'Derinkuyu Underground City', lat:38.375, lng:34.734,
         desc:'18-level underground city carved from soft volcanic tuff in Cappadocia, Turkey. Could house 20,000 people with livestock. Massive stone doors, ventilation shafts, and wells. Connected to other underground cities by tunnels.',
         note:'Built to hide from what? Who needed to shelter 20,000 people underground? Local tradition says it was built to escape giants/enemies. The engineering implies advanced knowledge of geology and ventilation.', img:'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Derinkuyu_Underground_City_9843_Nevit_Enhancer.jpg/320px-Derinkuyu_Underground_City_9843_Nevit_Enhancer.jpg'},
        {cat:'megalith', name:'Nabta Playa Stone Circle', lat:22.5, lng:30.7,
         desc:'Ancient stone circle in the Nubian Desert of Egypt, ~7000-6500 BC. Aligned with summer solstice and several bright stars. Predates Stonehenge by ~2,000 years. Built when the Sahara was green.',
         refs:'1 Enoch 8:3 (Baraqiel taught astrology)',
         note:'Astronomical knowledge this early challenges the timeline of civilization. The builders understood stellar precession \u2014 knowledge attributed to the Watchers in 1 Enoch.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Nabta_playa.jpg/320px-Nabta_playa.jpg'},
        {cat:'megalith', name:'Senegambian Stone Circles', lat:13.69, lng:-15.53,
         desc:'Over 1,000 stone circles and tumuli scattered across Gambia and Senegal, comprising 28,000+ individual stones. UNESCO World Heritage site. Erected ~300 BC to 1600 AD. Each circle contains 8-14 standing stones up to 2.5m tall.',
         note:'West Africa\'s most extensive megalithic landscape. Evidence that the impulse to build stone circles is truly global, not limited to Europe or the Near East.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Stone_circles_of_Senegambia.jpg/320px-Stone_circles_of_Senegambia.jpg'},
        {cat:'megalith', name:'Avebury Henge', lat:51.4285, lng:-1.8530,
         desc:'The largest stone circle in Europe, enclosing 28.5 acres. The outer circle has ~98 standing stones (originally), surrounded by a massive ditch 10m deep. Three times the diameter of Stonehenge. Much of it was deliberately destroyed in the Middle Ages by Christians.',
         note:'Medieval Christians smashed the stones because they believed them to be pagan \u2014 confirming that even in the 1300s, people associated these sites with spiritual power.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Avebury_henge_and_stone_circles.jpg/320px-Avebury_henge_and_stone_circles.jpg'},
        {cat:'megalith', name:'Hagar Qim & Mnajdra', lat:35.827, lng:14.442,
         desc:'Neolithic temple complex on Malta\'s southern coast, ~3600-3200 BC. Mnajdra has precise equinox/solstice alignments. Hagar Qim contains the largest single stone in Maltese temples (~20 tons). Female fertility figurines found throughout.',
         note:'Same culture as Ggantija ("Giant\'s Tower"). These tiny islands have the densest concentration of megalithic temples anywhere on Earth. Who were these island builders?', img:'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Hagar_Qim_par_Marleen.jpg/320px-Hagar_Qim_par_Marleen.jpg'},
        {cat:'megalith', name:'Ring of Brodgar', lat:59.001, lng:-3.230,
         desc:'A massive Neolithic henge and stone circle on Orkney, Scotland. Originally 60 stones in a perfect circle 104m in diameter, surrounded by a deep ditch cut from solid bedrock. ~2500-2000 BC.',
         note:'On a tiny subarctic island with brutal winters, someone cut a ditch through solid rock and erected 60 massive stones in a perfect circle. Why here?',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Ring_of_Brodgar_summer_evening.jpg/320px-Ring_of_Brodgar_summer_evening.jpg'},
        {cat:'megalith', name:'Callanish Stones', lat:58.197, lng:-6.745,
         desc:'A cruciform stone setting on the Isle of Lewis, Scotland, ~2900-2600 BC. 13 stones in a circle with avenue and radiating stone rows forming a cross shape. Aligned with the lunar standstill cycle (every 18.6 years).',
         note:'Understanding the 18.6-year lunar standstill cycle requires generations of observation. This is advanced astronomical knowledge on a remote Scottish island.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Callanish_Stones_-_geograph.org.uk_-_1170757.jpg/320px-Callanish_Stones_-_geograph.org.uk_-_1170757.jpg'},
        {cat:'megalith', name:'Machu Picchu', lat:-13.1631, lng:-72.5450,
         desc:'Inca citadel at 2,430m elevation, built ~1450 AD. Precision dry-stone walls with polygonal blocks fitted without mortar. The Intihuatana stone is an astronomical observatory. Built on earthquake-fault geology yet survives because of the precision engineering.',
         note:'Anti-seismic construction that outperforms modern buildings. Polygonal masonry defies simple tools. The two construction styles (rough upper, precision lower) may indicate different builders/periods.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Machu_Picchu%2C_Peru.jpg/320px-Machu_Picchu%2C_Peru.jpg'},
        {cat:'megalith', name:'Teotihuacan', lat:19.6925, lng:-98.8438,
         desc:'Ancient Mesoamerican city in Mexico, peak ~100-450 AD, population 125,000+. Pyramid of the Sun (third largest pyramid on Earth) aligned to astronomical events. Street grid at 15.5\u00b0 east of north. Mica sheets found in construction (imported from 3,000 miles away).',
         note:'Mica has no decorative purpose \u2014 it is used in modern electronics as an insulator. Why import it 3,000 miles and embed it in a pyramid? The name means "birthplace of the gods" in Nahuatl, but the actual builders are UNKNOWN.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Teotihuac%C3%A1n_-_Sonnenpyramide.jpg/320px-Teotihuac%C3%A1n_-_Sonnenpyramide.jpg'},
        {cat:'megalith', name:'Nan Madol', lat:6.85, lng:158.33,
         desc:'A ruined city of 92 artificial islands in a lagoon in Pohnpei, Micronesia. Built from massive basalt "logs" (columnar basalt) weighing up to 50 tons each. The logistics of transporting these across open water are staggering.',
         refs:'Genesis 11:8-9 (dispersed to islands)',
         note:'Local legend says the city was built by twin sorcerers who made the stones fly using magic. "Venice of the Pacific" built by people with no metal tools, no pulleys, no wheels \u2014 on a tiny Pacific island.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Nan_Madol_aerial.jpg/320px-Nan_Madol_aerial.jpg'},
        {cat:'megalith', name:'Zorats Karer (Carahunge)', lat:39.552, lng:45.510,
         desc:'A stone circle in Armenia with ~223 stones, some with smooth holes drilled through them. Possibly aligned with astronomical events. Sometimes called "Armenia\'s Stonehenge." Dated to ~5500 BC or earlier by some researchers.',
         note:'The drilled holes may be astronomical sighting tubes \u2014 telescope precursors. If the early dating holds, this predates Near Eastern urban civilization.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Carahunge_-_Armenian_Stonehenge.jpg/320px-Carahunge_-_Armenian_Stonehenge.jpg'},
        {cat:'megalith', name:'Almendres Cromlech', lat:38.558, lng:-8.061,
         desc:'The largest cromlech (stone circle) on the Iberian Peninsula, with ~95 standing stones near \u00c9vora, Portugal. Dated to ~6000-4000 BC. The stones are arranged in an ellipse with clear astronomical alignments.',
         note:'One of the oldest megalithic sites in Western Europe. Evidence that megalith-building was already sophisticated before the major European stone ages.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Almendres_Cromlech.jpg/320px-Almendres_Cromlech.jpg'},
        {cat:'megalith', name:'Coral Castle', lat:25.5003, lng:-80.4444,
         desc:'A structure in Florida built single-handedly by Latvian immigrant Edward Leedskalnin (~1923-1951). Over 1,100 tons of oolitic limestone, cut and moved by one man alone. Includes a 9-ton gate that opens with a finger push, perfectly balanced.',
         note:'Leedskalnin claimed to know the secrets of the pyramids. He worked only at night, refusing witnesses. When asked how, he said "I understand the laws of weight and leverage." No one has definitively explained his methods.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Coral_Castle_0073.jpg/320px-Coral_Castle_0073.jpg'},
        {cat:'megalith', name:'Osirion (Abydos)', lat:26.185, lng:31.919,
         desc:'A mysterious subterranean structure behind the Temple of Seti I at Abydos, Egypt. Built from enormous red granite blocks in a style completely different from the temple. Some researchers argue it predates dynastic Egypt.',
         note:'The construction technique (massive megalithic blocks, no decoration) resembles the Valley Temple at Giza more than any New Kingdom work. If pre-dynastic, who built it?',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Osireion_Abydos.jpg/320px-Osireion_Abydos.jpg'},
        {cat:'megalith', name:'Sardinian Nuraghi', lat:39.843, lng:9.024,
         desc:'Over 7,000 stone towers (nuraghi) dot the island of Sardinia, built ~1900-730 BC. Some are massive multi-tower complexes. The Nuragic civilization also produced mysterious bronze statuettes of warriors, priests, and "giant" figures. Local tradition: "the island of giants."',
         note:'7,000 towers on one island. The logistics suggest a highly organized civilization. Sardinian legends speak of giants. Giant bone discoveries (disputed) have been reported. The bronze figurines show supernatural beings.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/NuragheArrubiu2.jpg/320px-NuragheArrubiu2.jpg'},
        {cat:'pyramid', name:'Cholula, Mexico', lat:19.0578, lng:-98.3017,
         desc:'The Great Pyramid of Cholula is the LARGEST pyramid by volume in the world \u2014 bigger than Giza. 4.45 million cubic meters. Aztec name: Tlachihualtepetl ("man-made mountain"). Now has a church on top. Multiple construction phases spanning 2,000 years.',
         note:'The Spanish built a church directly on top of the pagan pyramid \u2014 the same pattern as Christianity building on top of pagan sacred sites across Europe. The largest pyramid on Earth, and most people have never heard of it.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Cholula_Pyramid.jpg/320px-Cholula_Pyramid.jpg'},

        // ── ADDITIONAL PATRIARCHAL & EXODUS SITES ──
        {cat:'biblical', name:'Beer-sheba', lat:31.2457, lng:34.7925,
         desc:'Abraham dug a well here and swore an oath with Abimelech. Isaac built an altar. Jacob offered sacrifices before going to Egypt. The phrase "from Dan to Beer-sheba" defines Israel\'s full extent.',
         refs:'Genesis 21:31; 26:23; 46:1'},
        {cat:'biblical', name:'Mamre / Oaks of Mamre', lat:31.5285, lng:35.0963,
         desc:'Where Abraham hosted three visitors \u2014 one was YHWH himself (Gen 18:1). A divine council theophany: God appears with two angels who proceed to Sodom. The Aqedah\'s binding narrative also begins here.',
         refs:'Genesis 13:18; 18:1-15; 23:19'},
        {cat:'biblical', name:'Mount Moriah', lat:31.7781, lng:35.2354,
         desc:'Where Abraham bound Isaac (Gen 22). Later identified as the Temple Mount (2 Chr 3:1). The place of supreme sacrifice foreshadows Calvary. The divine council witnessed the test of faith.',
         refs:'Genesis 22:2; 2 Chronicles 3:1'},
        {cat:'biblical', name:'Dothan', lat:32.4098, lng:35.2281,
         desc:'Where Joseph was sold by his brothers (Gen 37:17). Later, Elisha\'s servant sees the heavenly army: "the mountain was full of horses and chariots of fire" \u2014 the divine council\'s military arm made visible.',
         refs:'Genesis 37:17; 2 Kings 6:13-17'},
        {cat:'biblical', name:'Mahanaim', lat:32.3258, lng:35.7342,
         desc:'Where Jacob met angels of God and said "This is God\'s camp!" The name means "two camps" \u2014 the earthly camp of Jacob and the heavenly camp of God\'s angels.',
         refs:'Genesis 32:1-2'},
        {cat:'biblical', name:'Zoar', lat:31.08, lng:35.45,
         desc:'The small city Lot fled to when Sodom was destroyed. Located at the southern end of the Dead Sea. "The sun had risen on the earth when Lot came to Zoar."',
         refs:'Genesis 19:22-23'},
        {cat:'biblical', name:'Goshen (Land of)', lat:30.78, lng:31.77,
         desc:'The fertile delta region where Israel lived in Egypt. Joseph settled his family here (Gen 47:6). The Israelites multiplied from 70 to ~2 million during the 430-year sojourn.',
         refs:'Genesis 47:6; Exodus 8:22; 9:26'},
        {cat:'biblical', name:'Rameses / Pi-Ramesses', lat:30.79, lng:31.83,
         desc:'The store-city Israel built and the departure point of the Exodus. Located at modern Qantir in the eastern Nile Delta. "The Israelites journeyed from Rameses to Succoth" (Exod 12:37).',
         refs:'Exodus 1:11; 12:37'},
        {cat:'biblical', name:'Succoth (Egypt)', lat:30.55, lng:32.10,
         desc:'First encampment after leaving Rameses. The Hebrew means "booths/shelters." This begins Israel\'s journey from slavery to Sinai.',
         refs:'Exodus 12:37; 13:20'},
        {cat:'biblical', name:'Pi-hahiroth / Red Sea Crossing', lat:29.92, lng:32.55,
         desc:'Where Israel was trapped between the sea and Pharaoh\'s army. YHWH split the waters. The Egyptian army was destroyed. "The horse and his rider he has thrown into the sea" (Exod 15:1).',
         refs:'Exodus 14:2-31'},
        {cat:'biblical', name:'Marah', lat:29.27, lng:33.08,
         desc:'First stop after the Red Sea. The water was bitter (marah). Moses threw in a tree and the water became sweet. God reveals himself as YHWH Rophe \u2014 "the LORD who heals."',
         refs:'Exodus 15:23-26'},
        {cat:'biblical', name:'Elim', lat:28.83, lng:33.18,
         desc:'Oasis with 12 springs and 70 palm trees \u2014 matching Israel\'s 12 tribes and the 70 nations of Genesis 10 / Deuteronomy 32:8. Providential symbolism in geography.',
         refs:'Exodus 15:27'},
        {cat:'biblical', name:'Rephidim', lat:28.68, lng:33.68,
         desc:'Where Moses struck the rock for water and where Amalek attacked. Aaron and Hur held up Moses\' hands. The rock at Horeb = Christ (1 Cor 10:4). First warfare after the Exodus.',
         refs:'Exodus 17:1-16'},
        {cat:'biblical', name:'Kadesh-barnea', lat:30.63, lng:34.40,
         desc:'The staging point for the spy mission into Canaan. Israel\'s refusal to enter triggered the 40-year wilderness sentence. Moses struck the rock here instead of speaking to it (Num 20).',
         refs:'Numbers 13:26; 20:1-13; Deuteronomy 1:19-46'},
        {cat:'biblical', name:'Petra / Sela (Edom)', lat:30.3285, lng:35.4444,
         desc:'The "rose-red city half as old as time." Carved from sandstone cliffs by the Nabataeans, but the area was Edomite territory long before. Biblical Sela ("rock") may be this location. Edom\'s mountain strongholds fulfilled Obadiah\'s prophecy: "Though you soar like the eagle and set your nest among the stars, from there I will bring you down."',
         refs:'Obadiah 1:3-4; 2 Kings 14:7; Isaiah 16:1; Judges 1:36',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/The_Treasury_at_Petra.jpg/320px-The_Treasury_at_Petra.jpg'},
        {cat:'biblical', name:'Jericho', lat:31.8711, lng:35.4444,
         desc:'First city conquered in Canaan. The walls "fell flat" after Israel marched 7 days. Rahab the prostitute was saved. Everything was cherem (devoted to destruction). The oldest known walled city (~8000 BC).',
         refs:'Joshua 6; Hebrews 11:30-31',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/TellEsSultan.jpg/320px-TellEsSultan.jpg'},
        {cat:'biblical', name:'Ai', lat:31.9155, lng:35.2578,
         desc:'Second target after Jericho. Initial defeat due to Achan\'s cherem violation. After judgment, the city was taken by ambush. Archaeological identification debated (Khirbet el-Maqatir or et-Tell).',
         refs:'Joshua 7-8'},
        {cat:'biblical', name:'Gibeon', lat:31.8497, lng:35.1839,
         desc:'Where the sun stood still during Joshua\'s battle (Josh 10:12-13). The Gibeonites tricked Israel into a treaty. Later the site of the tabernacle and Solomon\'s dream.',
         refs:'Joshua 9-10; 1 Kings 3:4-5'},
        {cat:'biblical', name:'Hazor', lat:33.0175, lng:35.5683,
         desc:'Largest Canaanite city, called "the head of all those kingdoms" (Josh 11:10). King Jabin defeated by Joshua. Massive destruction layer confirms 13th century BC burning. Tel Hazor covers 200 acres.',
         refs:'Joshua 11:1-15; Judges 4'},
        {cat:'biblical', name:'Megiddo (Armageddon)', lat:32.5847, lng:35.1847,
         desc:'Strategic fortress controlling the Jezreel Valley. 26 destruction levels spanning 6,000 years. Hebrew "Har Megiddo" = Armageddon (Rev 16:16). The final eschatological battlefield where the divine council narrative concludes.',
         refs:'Revelation 16:16; Judges 5:19; 2 Kings 23:29',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/TelMegiddo.jpg/320px-TelMegiddo.jpg'},
        {cat:'biblical', name:'Shiloh', lat:32.0556, lng:35.2897,
         desc:'Israel\'s first permanent sanctuary. The tabernacle stood here for ~300 years. Where Hannah prayed for Samuel. Destroyed by the Philistines ~1050 BC. Jeremiah cites its destruction as warning (Jer 7:12).',
         refs:'Joshua 18:1; 1 Samuel 1-3; Jeremiah 7:12'},
        {cat:'biblical', name:'Mount Ebal', lat:32.2333, lng:35.2750,
         desc:'Mountain of curses where Joshua built an altar and read the Torah (Josh 8:30-35). Adam Zertal excavated a large stone structure here matching Exodus 20:25\'s altar specifications. Opposite Mount Gerizim.',
         refs:'Deuteronomy 27:4-8; Joshua 8:30-35'},
        {cat:'biblical', name:'Mount Gerizim', lat:32.2000, lng:35.2722,
         desc:'Mountain of blessings. Sacred to the Samaritan community, who believe THIS is where Abraham bound Isaac and where God chose his Temple (Samaritan Pentateuch Deut 27). Jesus met the Samaritan woman nearby.',
         refs:'Deuteronomy 11:29; John 4:20'},
        {cat:'biblical', name:'Beersheba to Dan Route', lat:33.2469, lng:35.6519,
         desc:'Dan (modern Tell el-Qadi) at Israel\'s northern border. Jeroboam set up a golden calf here (1 Kgs 12:29). Previously called Laish until conquered by the tribe of Dan (Judges 18). Abraham pursued kings to this area (Gen 14:14).',
         refs:'Genesis 14:14; Judges 18:29; 1 Kings 12:29'},

        // ── ANE PARALLEL SITES ──
        {cat:'cultural', name:'Ugarit (Ras Shamra), Syria', lat:35.6005, lng:35.7824,
         desc:'Canaanite city destroyed ~1185 BC. Thousands of cuneiform tablets reveal El\'s divine assembly, Baal\'s cosmic battles, the Rephaim traditions, and vocabulary cognate with Hebrew. The closest ANE parallel to the biblical divine council.',
         refs:'Psalm 82 (cf. KTU 1.2); Psalm 29 (cf. KTU 1.4)',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Ugarit_ruins.jpg/320px-Ugarit_ruins.jpg'},
        {cat:'cultural', name:'Mari, Syria', lat:34.5500, lng:40.8886,
         desc:'20,000+ cuneiform tablets (18th century BC). Mari letters mention prophetic figures, treaty forms, and tribal customs closely paralleling the patriarchal narratives. Names like "Abram" and "Jacob" appear.',
         refs:'Genesis 12-50 (patriarchal customs)'},
        {cat:'cultural', name:'Nuzi, Iraq', lat:35.3700, lng:44.2800,
         desc:'Thousands of tablets (15th century BC) documenting adoption, inheritance, and marriage customs virtually identical to those in Genesis: surrogate motherhood (Sarah/Hagar), adoption of slaves as heirs, deathbed blessings.',
         refs:'Genesis 15-16 (Abraham customs); Genesis 27 (blessing customs)'},
        {cat:'cultural', name:'Ebla (Tell Mardikh), Syria', lat:35.7981, lng:36.7984,
         desc:'17,000 cuneiform tablets (2400 BC). Personal names and place names consistent with the Genesis patriarchal world. Some scholars initially claimed to find "Sodom" and "Gomorrah" in the texts (disputed).',
         refs:'Genesis 10-14 (Table of Nations parallels)'},
        {cat:'biblical', name:'Mount Nebo', lat:31.7672, lng:35.7261,
         desc:'Where Moses viewed the Promised Land before his death. God buried him in an unknown location. Jude 9: Michael the archangel disputed with the devil over Moses\' body \u2014 a divine council event behind the scenes.',
         refs:'Deuteronomy 34:1-6; Jude 9'},
        {cat:'biblical', name:'Plains of Moab', lat:31.8600, lng:35.5600,
         desc:'Where Israel camped before crossing the Jordan. Balaam cursed/blessed from Mount Peor. The Baal-Peor apostasy occurred here. Moses delivered the book of Deuteronomy.',
         refs:'Numbers 22-25; Deuteronomy 1:1'},

        // ── ADDITIONAL JOURNEY WAYPOINT SITES ──
        {cat:'biblical', name:'Pethor (Mesopotamia)', lat:36.23, lng:38.17,
         desc:'Balaam\'s hometown on the Euphrates in northern Mesopotamia. Balak king of Moab sent messengers here to summon the diviner Balaam to curse Israel.',
         refs:'Numbers 22:5; Deuteronomy 23:4'},
        {cat:'biblical', name:'Mount Pisgah', lat:31.77, lng:35.74,
         desc:'A peak in the Abarim range overlooking the Dead Sea and Jordan Valley. Balaam offered sacrifices here and blessed Israel instead of cursing them. Also where Moses viewed the Promised Land.',
         refs:'Numbers 23:14; Deuteronomy 3:27'},
        {cat:'biblical', name:'Valley of Eshcol', lat:31.55, lng:35.08,
         desc:'Where the 12 spies cut a cluster of grapes so large it had to be carried on a pole between two men. The name means "cluster." Near Hebron in the hill country.',
         refs:'Numbers 13:23-24'},
        {cat:'biblical', name:'Ashdod', lat:31.80, lng:34.65,
         desc:'One of five Philistine cities. The Ark of the Covenant was brought here after capture at Ebenezer. The idol of Dagon fell before the Ark twice and was shattered.',
         refs:'1 Samuel 5:1-7; Joshua 11:22'},
        {cat:'biblical', name:'Ekron', lat:31.78, lng:34.85,
         desc:'Northernmost Philistine city. The Ark was sent here from Gath after plagues struck. The Ekronites cried out "They have brought the ark of God to us to kill us!" It was returned on a cart with gold tumors.',
         refs:'1 Samuel 5:10-12; 6:16'},
        {cat:'biblical', name:'Beth-shemesh', lat:31.75, lng:34.97,
         desc:'Israelite town on the border with Philistia. The Ark returned here on a cart pulled by cows. The people rejoiced but 70 men died for looking inside the Ark.',
         refs:'1 Samuel 6:12-19'},
        {cat:'biblical', name:'Kiriath-jearim', lat:31.80, lng:35.10,
         desc:'Where the Ark of the Covenant rested for 20 years in the house of Abinadab after returning from Philistia. David later brought it from here to Jerusalem with great celebration.',
         refs:'1 Samuel 7:1-2; 2 Samuel 6:2'},
        {cat:'biblical', name:'Zarephath', lat:33.45, lng:35.29,
         desc:'Phoenician town between Tyre and Sidon where Elijah stayed with a widow during the famine. The flour jar was never empty and the oil jug never ran dry. Elijah raised her dead son.',
         refs:'1 Kings 17:9-24; Luke 4:26'},
        {cat:'biblical', name:'Brook Cherith', lat:32.00, lng:35.55,
         desc:'Where Elijah hid east of the Jordan after declaring drought. Ravens brought him bread and meat morning and evening. When the brook dried up, God sent him to Zarephath.',
         refs:'1 Kings 17:3-7'},
        {cat:'biblical', name:'Mount Carmel', lat:32.74, lng:35.04,
         desc:'Where Elijah challenged 450 prophets of Baal and 400 of Asherah. Fire fell from heaven consuming the sacrifice. The people cried "YHWH — He is God!" The prophets of Baal were slaughtered at the Kishon brook.',
         refs:'1 Kings 18:19-40'},
        {cat:'biblical', name:'Gilead (Tishbe)', lat:32.40, lng:35.78,
         desc:'Elijah\'s homeland. "Elijah the Tishbite, of the inhabitants of Gilead." The rugged Transjordanian highlands east of the Jordan River, known for its balm and fierce independence.',
         refs:'1 Kings 17:1; Jeremiah 8:22'},
        {cat:'biblical', name:'Gibeah of Saul', lat:31.82, lng:35.23,
         desc:'Saul\'s capital city, modern Tell el-Ful north of Jerusalem. Where Saul was made king and from where David later fled. Also the site of the horrific Judges 19 outrage that triggered civil war.',
         refs:'1 Samuel 10:26; 11:4; Judges 19-20'},
        {cat:'biblical', name:'Nob', lat:31.79, lng:35.24,
         desc:'The priestly city where David fled from Saul and received the showbread and Goliath\'s sword from Ahimelech the priest. Saul later massacred 85 priests here through Doeg the Edomite.',
         refs:'1 Samuel 21:1-9; 22:9-19'},
        {cat:'biblical', name:'Cave of Adullam', lat:31.62, lng:34.98,
         desc:'Stronghold where David gathered 400 discontented men who became his mighty warriors. Located in the Shephelah lowlands. "Everyone who was in distress, in debt, or discontented gathered to him."',
         refs:'1 Samuel 22:1-2; 2 Samuel 23:13'},
        {cat:'biblical', name:'Keilah', lat:31.62, lng:35.05,
         desc:'Town David rescued from Philistine raiders, but then fled when God told him the townspeople would hand him over to Saul. Shows the desperate nature of David\'s fugitive years.',
         refs:'1 Samuel 23:1-13'},
        {cat:'biblical', name:'Wilderness of Ziph', lat:31.43, lng:35.12,
         desc:'Where the Ziphites twice betrayed David\'s location to Saul. David hid in the hill of Hachilah. Jonathan came here for their last meeting and "strengthened David\'s hand in God."',
         refs:'1 Samuel 23:14-24; 26:1-3'},
        {cat:'biblical', name:'En-gedi', lat:31.47, lng:35.39,
         desc:'Oasis on the western Dead Sea shore. David hid here in the "Strongholds." In a cave, David cut Saul\'s robe but refused to kill "the LORD\'s anointed." Saul wept at David\'s mercy.',
         refs:'1 Samuel 24:1-22; Song of Solomon 1:14'},
        {cat:'biblical', name:'Ziklag', lat:31.35, lng:34.58,
         desc:'Philistine city given to David by Achish of Gath. David used it as a base for 16 months. Burned by Amalekites who took the women captive — David pursued, defeated them, and recovered everything.',
         refs:'1 Samuel 27:5-7; 30:1-20'},
        {cat:'biblical', name:'Midian', lat:28.50, lng:35.00,
         desc:'Region in northwest Arabia where Moses fled after killing the Egyptian. He married Zipporah, daughter of Jethro priest of Midian. Spent 40 years as a shepherd before the burning bush encounter.',
         refs:'Exodus 2:15-22; 3:1'},
        {cat:'biblical', name:'Nile Delta', lat:30.45, lng:31.20,
         desc:'The fertile triangle of the Nile where Pharaoh\'s daughter found baby Moses among the reeds. The ten plagues struck this region. Center of Egyptian civilization and Israel\'s oppression.',
         refs:'Exodus 2:3-6; 7-12'},
        {cat:'biblical', name:'Hobah (near Damascus)', lat:33.55, lng:36.25,
         desc:'North of Damascus, where Abraham pursued and defeated the four kings who had captured Lot. He divided his forces at night for a surprise attack, recovering all the people and goods.',
         refs:'Genesis 14:15'},
        {cat:'biblical', name:'Potiphar\'s House (Memphis)', lat:29.85, lng:31.25,
         desc:'Joseph was sold to Potiphar, captain of Pharaoh\'s guard. The LORD prospered everything Joseph touched. He was falsely accused by Potiphar\'s wife and thrown into prison.',
         refs:'Genesis 39:1-20'},
        {cat:'biblical', name:'Pharaoh\'s Court (Avaris/Memphis)', lat:30.05, lng:31.23,
         desc:'Joseph interpreted Pharaoh\'s dreams of seven fat and seven lean years. Made vizier of Egypt at age 30 \u2014 second only to Pharaoh. Oversaw the storage program that saved Egypt and the surrounding nations.',
         refs:'Genesis 41:1-45'},

        // ══ CHRIST TYPOLOGY LAYER ══
        // OT figures, events, and locations that foreshadow Jesus Christ
        // "These are a shadow of the things to come, but the substance belongs to Christ" (Col 2:17)

        // ── ISAAC / AKEDAH ──
        {cat:'typology', name:'Mount Moriah \u2014 The Akedah (Binding of Isaac)', lat:31.7781, lng:35.2354,
         desc:'GOD THE FATHER OFFERING THE SON. Abraham took "your son, your only son, whom you love" (Gen 22:2) on a 3-day journey to Moriah. Isaac \u2014 a strong young man \u2014 willingly carried the wood for his own sacrifice on his shoulders, as Christ carried His cross. At the last moment, God provided a ram caught in a thicket as substitute. Abraham named it "YHWH Yireh" \u2014 "The LORD Will Provide" \u2014 on the same mountain ridge where Jesus was later crucified. Hebrews 11:19: Abraham believed God could raise the dead, receiving Isaac back "as a type."',
         refs:'Genesis 22:1-14; Hebrews 11:17-19; John 3:16',
         note:'TYPOLOGY: Father offers beloved only son (Gen 22:2 \u2192 John 3:16). Son carries wood of sacrifice (Gen 22:6 \u2192 John 19:17). 3-day journey = 3 days in tomb (Gen 22:4 \u2192 Matt 12:40). Ram substitute = Lamb of God (Gen 22:13 \u2192 John 1:29). Same mountain = Calvary. "God will provide Himself the Lamb" (Gen 22:8) \u2014 fulfilled in Christ.'},

        // ── JOSEPH ──
        {cat:'typology', name:'Dothan \u2014 Joseph Betrayed by His Brothers', lat:32.4098, lng:35.2281,
         desc:'BETRAYAL OF THE BELOVED SON. Joseph \u2014 the beloved son of his father, clothed in a special robe \u2014 was sent to his brothers who hated him without cause. They stripped him, threw him into a pit (symbolic death), and sold him for 20 pieces of silver to Gentile traders. Every detail foreshadows Christ: beloved Son sent by the Father (John 3:16), hated without cause (John 15:25), stripped (John 19:23-24), cast into the grave, sold for silver (Matt 26:15).',
         refs:'Genesis 37:12-28; John 15:25; Matthew 26:15',
         note:'TYPOLOGY: 15 parallels between Joseph and Jesus. (1) Beloved son (Gen 37:3/Matt 3:17). (2) Sent by father to brothers (Gen 37:13/John 3:16). (3) Hated without cause (Gen 37:4/John 15:25). (4) Sold for silver (Gen 37:28/Matt 26:15). (5) Stripped of robe (Gen 37:23/John 19:23). (6) Cast into pit/death (Gen 37:24/Matt 12:40). (7) Handed to Gentiles (Gen 37:28/Matt 27:2).'},
        {cat:'typology', name:'Egyptian Prison \u2014 Joseph Between Two Criminals', lat:29.87, lng:31.26,
         desc:'BETWEEN TWO CRIMINALS. In prison, Joseph was placed between two men \u2014 the cupbearer and the baker. He prophesied that one would be restored to life (the cupbearer) and one would die (the baker was hanged). At Calvary, Jesus hung between two criminals \u2014 one was saved ("Today you will be with Me in Paradise") and one perished.',
         refs:'Genesis 40:1-22; Luke 23:32-43',
         note:'TYPOLOGY: (9) Placed between two criminals, one saved, one lost (Gen 40:21-22/Luke 23:39-43). (8) Falsely accused (Gen 39:12-20/Matt 26:59-60).'},
        {cat:'typology', name:'Pharaoh\'s Throne \u2014 Joseph Exalted from Prison', lat:30.05, lng:31.23,
         desc:'EXALTATION FROM THE LOWEST PLACE. Joseph rose from dungeon prisoner to ruler of the world \u2014 "only with regard to the throne will I be greater than you" (Gen 41:40). He received a new name, a Gentile bride, and authority to save the world from famine. Christ rose from the grave to the right hand of God, received the name above every name, took a Gentile bride (the Church), and became the Bread of Life.',
         refs:'Genesis 41:14-45; Philippians 2:8-11; John 6:35; Ephesians 5:25-32',
         note:'TYPOLOGY: (10) Exalted from lowest to highest (Gen 41:14,40/Phil 2:8-9). (11) Given Gentile bride (Gen 41:45/Eph 5:25-32). (12) Saves world, provides bread (Gen 41:55-57/John 6:35). (13) Forgives betrayers (Gen 45:1-5/Luke 23:34). (14) Brothers bow (Gen 42:6/Phil 2:10-11). (15) "You meant evil; God meant it for good" (Gen 50:20).'},

        // ── MOSES ──
        {cat:'typology', name:'Nile \u2014 Moses Saved as a Baby', lat:30.45, lng:31.20,
         desc:'THE DELIVERER BORN UNDER A DEATH DECREE. Pharaoh ordered all Hebrew boys killed; Moses was hidden in a basket on the Nile and providentially saved. Herod ordered all boys in Bethlehem killed; Jesus was taken to Egypt and saved. Both deliverers emerged from Egypt: "Out of Egypt I called My Son" (Hosea 11:1/Matt 2:15).',
         refs:'Exodus 1:22\u20132:10; Matthew 2:13-18; Hosea 11:1',
         note:'TYPOLOGY: Both born under infanticide decrees. Both preserved by divine providence. Both came out of Egypt. Moses = deliverer from physical slavery. Jesus = Deliverer from slavery to sin.'},
        {cat:'typology', name:'Mount Sinai \u2014 Moses the Lawgiver', lat:28.5394, lng:33.9752,
         desc:'THE LAW CANNOT BRING YOU IN. Moses \u2014 who spoke with God face to face, received the Torah from God\'s own hand, performed signs no prophet ever matched \u2014 could not enter the Promised Land because he struck the rock in unbelief (Num 20:8-12). The Law reveals sin but cannot save. It takes a JOSHUA (Yeshua = Jesus) to bring God\'s people into rest. "If Joshua had given them rest, God would not have spoken of another day" (Heb 4:8).',
         refs:'Numbers 20:8-12; Deuteronomy 34:4-5; Hebrews 4:8-9; Romans 3:20',
         note:'TYPOLOGY: Moses = the Law (reveals sin, cannot save). Joshua/Jesus = Grace (brings people into the Promised Land/eternal rest). The Law was given THROUGH Moses; grace and truth came THROUGH Jesus Christ (John 1:17).'},
        {cat:'typology', name:'Meribah \u2014 The Struck Rock', lat:30.63, lng:34.42,
         desc:'THE ROCK THAT WAS STRUCK. At Rephidim, God told Moses to STRIKE the rock \u2014 water gushed out (Exod 17:6). At Meribah, God told Moses to SPEAK to the rock \u2014 but Moses struck it twice in anger (Num 20:8-12). Paul reveals: "that Rock was Christ" (1 Cor 10:4). Christ was struck ONCE at the cross. Now we approach Him by speaking (prayer/faith), not by striking again. Moses\' sin pictures the danger of trying to re-crucify Christ.',
         refs:'Exodus 17:1-7; Numbers 20:8-12; 1 Corinthians 10:4; Hebrews 6:6',
         note:'TYPOLOGY: Rock struck once = Christ crucified once (Heb 9:28). Water from rock = living water from Christ (John 7:37-39). Moses striking twice = the futility of works-based salvation.'},

        // ── JOSHUA ──
        {cat:'typology', name:'Jordan Crossing \u2014 Joshua Leads Israel In', lat:31.87, lng:35.44,
         desc:'THE TRUE JOSHUA. Moses brought Israel TO the border but could not lead them IN. Joshua (Hebrew: Yehoshua = "Yahweh saves" = same name as Jesus/Yeshua) led the people THROUGH the waters of the Jordan into the Promised Land. The waters parted as they had at the Red Sea \u2014 but this time it is Joshua, not Moses, who commands it. "For if Joshua had given them rest, He would not have spoken of another day" (Heb 4:8). The earthly Joshua gave partial rest; the True Joshua gives eternal rest.',
         refs:'Joshua 3:14-17; Hebrews 4:8-9; Matthew 1:21',
         note:'TYPOLOGY: Joshua/Jesus = identical names (Yeshua). Joshua succeeds where Moses (the Law) failed. Jordan crossing = baptism into new life (Rom 6:3-4). Ark in the river = Christ in the waters of death for His people.'},
        {cat:'typology', name:'Hebron \u2014 Joshua the Giant Slayer', lat:31.5326, lng:35.0998,
         desc:'THE GIANT SLAYER. Joshua "cut off the Anakim from the hill country \u2014 there were no Anakim left in the land" (Josh 11:21-22). The Anakim were Nephilim remnants \u2014 the spawn of the Watchers\' rebellion (Gen 6:4; Num 13:33). Only faith-filled leadership could defeat them. The ten faithless spies said "we were like grasshoppers" (Num 13:33). Joshua and Caleb said "the LORD is with us \u2014 do not fear them" (Num 14:9). Christ is the ultimate Giant Slayer who defeated Satan, sin, and death.',
         refs:'Joshua 11:21-22; Numbers 13:33; Numbers 14:6-9; 1 John 3:8; Hebrews 2:14',
         note:'TYPOLOGY: Joshua destroys the Anakim/Nephilim remnant = Christ destroys the works of the devil (1 John 3:8). Faith overcomes giants = "this is the victory that overcomes the world: our faith" (1 John 5:4).'},

        // ── BRONZE SERPENT ──
        {cat:'typology', name:'Punon \u2014 The Bronze Serpent', lat:29.83, lng:35.23,
         desc:'LIFTED UP FOR SALVATION. When Israel sinned in the wilderness, God sent fiery serpents (saraph \u2014 same word as the seraphim of Isaiah 6). Moses made a bronze serpent and set it on a pole \u2014 everyone who looked at it in faith LIVED. Jesus applied this directly to Himself: "As Moses lifted up the serpent in the wilderness, even so must the Son of Man be lifted up, that whoever believes in Him should have eternal life" (John 3:14-15).',
         refs:'Numbers 21:4-9; John 3:14-15; 2 Kings 18:4',
         note:'TYPOLOGY: Serpent on a pole = Christ on the cross. Look and live = believe and be saved. The serpent (symbol of curse/sin from Gen 3) is lifted up = Christ "became a curse for us" (Gal 3:13). Bronze = judgment metal. Later destroyed by Hezekiah when Israel worshiped it (2 Kgs 18:4) \u2014 the shadow must never replace the substance.'},

        // ── PASSOVER ──
        {cat:'typology', name:'Goshen \u2014 The Passover Lamb', lat:30.78, lng:31.77,
         desc:'THE LAMB SLAIN. God commanded each household to take a lamb without blemish, kill it at twilight, and apply its blood to the doorposts. When the destroyer passed through Egypt, every house covered by the blood was SAVED. "Christ our Passover has been sacrificed for us" (1 Cor 5:7). Jesus was crucified at Passover. He is "the Lamb of God who takes away the sin of the world" (John 1:29). Not a bone of the Passover lamb was to be broken (Exod 12:46) \u2014 nor was a bone of Jesus broken (John 19:36).',
         refs:'Exodus 12:1-13,46; 1 Corinthians 5:7; John 1:29; John 19:36; 1 Peter 1:18-19',
         note:'TYPOLOGY: Spotless lamb = sinless Christ (1 Pet 1:19). Blood on doorposts = blood of Christ covering sin. Eaten with bitter herbs = suffering. Unleavened bread = sinlessness. No bone broken (Exod 12:46/John 19:36). Eaten in haste = urgency of salvation.'},

        // ── DAVID ──
        {cat:'typology', name:'Valley of Elah \u2014 David vs. Goliath', lat:31.69, lng:34.96,
         desc:'THE SHEPHERD KING WHO SLEW THE GIANT. David \u2014 the youngest son, a shepherd from Bethlehem \u2014 defeated the giant champion Goliath with a stone while all Israel cowered in fear. He cut off Goliath\'s head with the giant\'s own sword. Christ \u2014 the Son of David, the Good Shepherd from Bethlehem \u2014 defeated Satan using death itself ("through death He destroyed him who had the power of death" \u2014 Heb 2:14). David then became the rejected-then-exalted king, establishing the eternal throne fulfilled in Jesus.',
         refs:'1 Samuel 17; 2 Samuel 7:12-16; Hebrews 2:14; Matthew 1:1',
         note:'TYPOLOGY: Bethlehem shepherd (1 Sam 17:15/Luke 2:4-7). Defeated the champion of evil with unlikely weapon (1 Sam 17:50/1 Cor 1:25). Rejected king later exalted (1 Sam 18-2 Sam 5/Phil 2:8-11). Eternal throne promise (2 Sam 7:16/Luke 1:32-33). Yet David sinned \u2014 only Jesus is the sinless, perfect Son of David.'},

        // ── JONAH ──
        {cat:'typology', name:'Joppa \u2014 Jonah\'s Flight', lat:32.0544, lng:34.7518,
         desc:'THREE DAYS IN THE DEEP. Jonah fled from God, was thrown into the sea, and spent three days and nights in the belly of the great fish \u2014 then was vomited out alive. Jesus said: "For just as Jonah was three days and three nights in the belly of the sea monster, so will the Son of Man be three days and three nights in the heart of the earth" (Matt 12:40). Jonah\'s reluctant mission to Gentile Nineveh foreshadows the gospel going to the Gentile world.',
         refs:'Jonah 1:17\u20132:10; Matthew 12:39-41',
         note:'TYPOLOGY: 3 days in fish = 3 days in tomb (Matt 12:40). Thrown into sea to save others = Jesus dies to save sinners. Vomited out alive = resurrection. Nineveh repents = Gentile nations receive the gospel. But Jonah ran from God; Jesus said "Not My will, but Yours be done."'},

        // ── MELCHIZEDEK ──
        {cat:'typology', name:'Salem \u2014 Melchizedek, Priest-King', lat:31.7781, lng:35.2355,
         desc:'ETERNAL PRIEST-KING. After Abraham\'s victory, Melchizedek \u2014 king of Salem (peace), priest of God Most High \u2014 brought out bread and wine and blessed Abraham. He appears without genealogy, "without father, without mother, without beginning of days or end of life" (Heb 7:3). He is a type of Christ who is both King AND Priest forever \u2014 something no Aaronic priest could be, since priests came from Levi and kings from Judah. Jesus alone unites both offices.',
         refs:'Genesis 14:18-20; Psalm 110:4; Hebrews 5:6-10; 7:1-17',
         note:'TYPOLOGY: King of Righteousness + King of Peace (Heb 7:2). Bread and wine = Communion (Matt 26:26-28). No recorded genealogy = eternal priesthood. Greater than Abraham (Heb 7:4-7). Priesthood "according to the order of Melchizedek" = superior to Levitical priesthood (Heb 7:11-17).'},

        // ── RED SEA ──
        {cat:'typology', name:'Red Sea Crossing \u2014 Baptism & Deliverance', lat:29.92, lng:32.55,
         desc:'THROUGH THE WATERS OF DEATH INTO NEW LIFE. Israel passed through the Red Sea \u2014 the waters of death \u2014 and emerged alive on the other side while their enemies were destroyed behind them. Paul declares: "Our fathers were all baptized into Moses in the cloud and in the sea" (1 Cor 10:1-2). The Red Sea crossing is a picture of baptism \u2014 dying to the old life of slavery and rising to walk in freedom.',
         refs:'Exodus 14:21-31; 1 Corinthians 10:1-2; Romans 6:3-4',
         note:'TYPOLOGY: Passing through water = baptism (1 Cor 10:2/Rom 6:3-4). Enemies destroyed = sin defeated. Pillar of cloud/fire = Holy Spirit. Freedom from slavery = freedom from sin. Song of victory (Exod 15) = the new song (Rev 5:9-10).'},

        // ── TABERNACLE ──
        {cat:'typology', name:'Sinai \u2014 The Tabernacle (God Dwelling Among Men)', lat:28.5394, lng:33.9753,
         desc:'GOD WITH US. The tabernacle was God\'s dwelling among His people \u2014 "let them make Me a sanctuary, that I may dwell among them" (Exod 25:8). Every element points to Christ: the ONE door (John 10:9), the bronze altar (the cross), the laver (cleansing/baptism), the showbread (Bread of Life \u2014 John 6:35), the lampstand (Light of the World \u2014 John 8:12), the incense altar (prayers/intercession \u2014 Heb 7:25), the veil (His flesh \u2014 Heb 10:20), the mercy seat (propitiation \u2014 Rom 3:25). "The Word became flesh and TABERNACLED among us" (John 1:14, literal Greek).',
         refs:'Exodus 25:8-9; John 1:14; Hebrews 9:1-12; 10:19-20',
         note:'TYPOLOGY: Tabernacle = Christ\'s body (John 1:14; 2:19-21). One door = "I am the way" (John 14:6). Bronze altar = cross. Veil = His flesh torn (Heb 10:20). Ark = throne of God. Mercy seat = propitiation (Rom 3:25). High priest entering once a year = Christ entering heaven once for all (Heb 9:12).'},

        // ── DAY OF ATONEMENT ──
        {cat:'typology', name:'Tabernacle \u2014 Yom Kippur (Day of Atonement)', lat:31.77, lng:35.24,
         desc:'THE GREAT HIGH PRIEST. On Yom Kippur, the high priest entered the Holy of Holies ONCE per year with blood \u2014 not his own \u2014 to atone for Israel\'s sins. Two goats: one slain (blood applied to the mercy seat), one sent into the wilderness bearing the people\'s sins (the scapegoat "for Azazel" \u2014 Lev 16:8-10). Christ is BOTH: the sacrificial lamb whose blood was applied in the heavenly Holy of Holies, AND the one who bears our sins away forever. "Not through the blood of goats and calves, but through His own blood, He entered the holy place once for all" (Heb 9:12).',
         refs:'Leviticus 16:1-34; Hebrews 9:7-14,24-28; 1 John 2:2',
         note:'TYPOLOGY: High priest enters once = Christ enters heaven once (Heb 9:12). Blood of another = His own blood. Two goats = Christ both sacrificed AND bearing sins away. Scapegoat "for Azazel" = Christ bearing the curse of the fallen watchers\' rebellion. Veil torn (Matt 27:51) = permanent access to God.'},

        // ── RUTH ──
        {cat:'typology', name:'Bethlehem \u2014 Ruth & Boaz (Kinsman Redeemer)', lat:31.7054, lng:35.2024,
         desc:'THE KINSMAN REDEEMER. Ruth \u2014 a Gentile Moabite widow, destitute and without hope \u2014 found redemption through Boaz, her kinsman-redeemer (go\'el). Boaz had the RIGHT to redeem (he was kin), the RESOURCES to redeem (he was wealthy), and the RESOLVE to redeem (he chose to act). He paid the full price, married Ruth, and brought her into the covenant family. Christ is our Go\'el: He became our kinsman (incarnation), He had the resources (sinless life), and He chose to redeem us (the cross). Ruth\'s son Obed became grandfather of David \u2014 in the lineage of Jesus.',
         refs:'Ruth 1\u20134; Leviticus 25:25; Matthew 1:5; Galatians 4:4-5',
         note:'TYPOLOGY: Gentile bride brought into covenant = the Church. Kinsman-redeemer = Christ (Gal 4:4-5). Bethlehem = birthplace of both David and Jesus. Boaz = "in him is strength." Threshing floor encounter = covenant intimacy. Ruth in the genealogy of Christ (Matt 1:5) \u2014 God includes Gentile outsiders in His redemptive plan.'},

        // ── ELIJAH ──
        {cat:'typology', name:'Mount Carmel \u2014 Elijah, Forerunner', lat:32.74, lng:35.05,
         desc:'THE FORERUNNER. Elijah stood alone against 450 prophets of Baal, called fire from heaven, and proved YHWH alone is God. Malachi prophesied: "I will send you Elijah the prophet before the great and terrible day of the LORD" (Mal 4:5). Jesus confirmed: "Elijah has already come, and they did not recognize him" \u2014 speaking of John the Baptist (Matt 17:12-13). Elijah preparing the way for Elisha parallels John the Baptist preparing the way for Jesus. Elijah was taken up alive; Elisha received a double portion \u2014 as Christ ascended and poured out the Spirit.',
         refs:'1 Kings 18:17-40; Malachi 4:5-6; Matthew 17:10-13; 2 Kings 2:9-11',
         note:'TYPOLOGY: Elijah = John the Baptist (Matt 17:12). Calls Israel to repentance. Stood alone for truth. Taken up = ascension. Elisha receives double portion = Holy Spirit poured out (Acts 2). Elijah fed by ravens/widow = God provides in wilderness (Matt 4:11).'},

        // ── ADAM ──
        {cat:'typology', name:'Eden \u2014 Adam, the First Man', lat:30.96, lng:47.42,
         desc:'THE FIRST ADAM AND THE LAST ADAM. Adam was the head of the old creation \u2014 through his disobedience, sin and death entered the world. Christ is "the last Adam" (1 Cor 15:45) \u2014 the head of the new creation. Where Adam failed the test in a perfect garden, Jesus passed the test in a barren wilderness. Where Adam\'s disobedience brought condemnation, Christ\'s obedience brings justification. "For as in Adam all die, so also in Christ all will be made alive" (1 Cor 15:22).',
         refs:'Genesis 2\u20133; Romans 5:12-21; 1 Corinthians 15:22,45-49',
         note:'TYPOLOGY: Adam = first man/head of old humanity. Christ = last Adam/head of new humanity (1 Cor 15:45). Adam\'s bride from his side while he slept = the Church born from Christ\'s pierced side (John 19:34). Tree of disobedience in Eden = tree of obedience at Calvary. Garden of failure (Eden) = garden of surrender (Gethsemane).'},

        // ── NOAH'S ARK ──
        {cat:'typology', name:'Ararat Region \u2014 Noah\'s Ark', lat:39.7, lng:44.3,
         desc:'THE ARK OF SALVATION. Noah \u2014 a righteous man in a wicked generation \u2014 built an ark at God\'s command. Everyone INSIDE the ark was saved; everyone outside perished. There was only ONE door, and God Himself shut it (Gen 7:16). Peter draws the parallel: "In the ark\u2026 eight persons were saved through water. Corresponding to that, baptism now saves you" (1 Pet 3:20-21). Christ is the Ark \u2014 the only refuge from judgment. There is one door (John 10:9), and God seals those who are in Him.',
         refs:'Genesis 6\u20139; 1 Peter 3:20-21; Matthew 24:37-39; John 10:9',
         note:'TYPOLOGY: One ark = one way of salvation (Acts 4:12). One door = "I am the door" (John 10:9). God shuts the door (Gen 7:16) = God seals believers (Eph 1:13). Flood judgment = coming judgment (Matt 24:37-39). Raven vs. dove = flesh vs. Spirit. Covenant rainbow = God\'s faithfulness.'},

        // ── HIGH PRIEST'S GARMENTS ──
        {cat:'typology', name:'Tabernacle \u2014 The High Priest', lat:31.77, lng:35.235,
         desc:'THE GREAT HIGH PRIEST. Aaron bore the names of the 12 tribes on his shoulders (stones of remembrance) and over his heart (breastplate of judgment) when he entered God\'s presence. The bells on his robe rang to signal he was alive inside the Holy of Holies. Christ is our Great High Priest who "always lives to make intercession" for us (Heb 7:25). He carries our names before the Father. Unlike Aaron, He never dies \u2014 His priesthood is permanent.',
         refs:'Exodus 28:1-43; Hebrews 4:14-16; 7:23-27; 9:11-12',
         note:'TYPOLOGY: Breastplate stones = Christ carries His people on His heart. Urim & Thummim = Christ reveals God\'s will. White linen = righteousness. Turban inscription "Holy to the LORD" = Christ\'s perfect holiness. Aaron died; Jesus lives forever (Heb 7:24).'},

        // ── GOLIATH\'S DESCENDANTS / PHILISTINE GIANTS ──
        {cat:'typology', name:'Gath \u2014 Goliath & Four Giant Descendants', lat:31.6103, lng:34.8489,
         desc:'THE LAST REPHAIM. Five giants from Gath \u2014 all "descendants of the Rapha" (2 Sam 21:22): (1) GOLIATH \u2014 champion of the Philistines, 9 ft 9 in, killed by young David with a sling and faith (1 Sam 17). (2) ISHBI-BENOB \u2014 his spear weighed 300 shekels of bronze; nearly killed David but Abishai saved him (2 Sam 21:16-17). (3) SAPH \u2014 killed by Sibbecai the Hushathite (2 Sam 21:18). (4) LAHMI (brother of Goliath) \u2014 his spear shaft was like a weaver\'s beam; killed by Elhanan (2 Sam 21:19; 1 Chr 20:5). (5) THE SIX-FINGERED GIANT \u2014 a man of great stature with 6 fingers on each hand and 6 toes on each foot (24 total); killed by Jonathan son of Shimei (2 Sam 21:20-21). "These four fell by David and his servants" (2 Sam 21:22).',
         refs:'1 Samuel 17:4; 2 Samuel 21:15-22; 1 Chronicles 20:4-8',
         note:'TYPOLOGY: David (type of Christ, the greater David) finishes what Joshua started \u2014 destroying the last Nephilim/Rephaim remnant. Five giants from Gath = the final Anakim survivors of Josh 11:22. David the shepherd from Bethlehem defeats the champion of evil = Christ the Good Shepherd defeats Satan (Heb 2:14).'},

        // ── PHILISTINE PENTAPOLIS ──
        {cat:'biblical', name:'Ashkelon', lat:31.67, lng:34.57,
         desc:'One of five Philistine cities. Samson killed 30 men of Ashkelon for their garments (Judg 14:19). A major port city with massive fortifications. Excavations reveal Philistine temples, Aegean-style pottery, and evidence of the Sea Peoples arrival (~1200 BC).',
         refs:'Judges 14:19; 1 Samuel 6:17; Zephaniah 2:4-7'},
        {cat:'biblical', name:'Gaza', lat:31.50, lng:34.47,
         desc:'Southernmost Philistine city. Samson carried away the city gates (Judg 16:3) and died destroying the temple of Dagon (Judg 16:28-30). One of three cities where Anakim survivors remained after Joshua\'s conquest (Josh 11:22). Philip preached on the road to Gaza (Acts 8:26).',
         refs:'Joshua 11:22; Judges 16:1-3,21-30; Acts 8:26'},

        // ── CAPHTOR / SEA PEOPLES ORIGIN ──
        {cat:'cultural', name:'Caphtor (Crete) \u2014 Philistine Origin', lat:35.3, lng:25.1,
         desc:'The ancestral homeland of the Philistines. "Did I not bring up Israel from Egypt, and the Philistines from Caphtor?" (Amos 9:7). Caphtor is widely identified with Crete (Kaptara in Akkadian texts, Keftiu in Egyptian). The Caphtorim displaced the Avvim and settled the Gaza coastal plain (Deut 2:23). The Philistines were Hamitic descendants through Mizraim (Gen 10:13-14). God sovereignly brought them into the very territory where Anakim/Nephilim remnants remained (Josh 11:22), creating the testing ground for Israel\'s faith and the arena where David destroyed the last giants.',
         refs:'Genesis 10:13-14; Deuteronomy 2:23; Amos 9:7; Jeremiah 47:4',
         note:'The Sea Peoples invasion (~1200 BC) brought further waves of Aegean peoples to this coast. Egyptian inscriptions at Medinet Habu record Ramesses III repelling them. The Peleset (Philistines) settled in Canaan. Strictly C-level archaeological context \u2014 but Scripture confirms God orchestrates all migrations (Acts 17:26).'},

        // ══════════════════════════════════════════════════════════
        // ── KINGDOM PERIOD CITIES ──
        // ══════════════════════════════════════════════════════════
        {cat:'biblical', name:'Samaria', lat:32.275, lng:35.1917,
         desc:'Capital of the northern kingdom of Israel, built by Omri. Center of Baal worship under Ahab and Jezebel. Fell to Assyria in 722 BC. Philip preached here in Acts 8.',
         refs:'1 Kings 16:24; 2 Kings 17:5-6; Acts 8:4-25'},
        {cat:'biblical', name:'Bethlehem', lat:31.7054, lng:35.2024,
         desc:'City of David and birthplace of Jesus. Rachel was buried nearby. Ruth gleaned in its fields. Micah prophesied the Messiah would come from this small town.',
         refs:'Micah 5:2; Matthew 2:1; Ruth 1:19; 1 Samuel 16:1',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Bethlehem_Church_of_Nativity.jpg/320px-Bethlehem_Church_of_Nativity.jpg'},
        {cat:'biblical', name:'Lachish', lat:31.565, lng:34.8489,
         desc:'Second most important city in Judah after Jerusalem. Sennacherib\'s siege (701 BC) depicted on Nineveh palace reliefs. The Lachish Letters describe the final days before Babylonian destruction.',
         refs:'2 Kings 18:13-14; Jeremiah 34:7'},
        {cat:'biblical', name:'Jezreel', lat:32.5564, lng:35.3281,
         desc:'Royal residence of Ahab and Jezebel. Naboth\'s vineyard was here. Jezebel was thrown from the window and eaten by dogs as Elijah prophesied.',
         refs:'1 Kings 21:1-16; 2 Kings 9:30-37'},
        {cat:'biblical', name:'Gezer', lat:31.8756, lng:34.9208,
         desc:'Strategic Canaanite city given to Solomon by Pharaoh as a dowry. Solomon rebuilt it with Hazor and Megiddo. The Gezer Calendar is one of the oldest Hebrew inscriptions.',
         refs:'1 Kings 9:15-17; Joshua 16:10'},
        {cat:'biblical', name:'Beth-shan (Scythopolis)', lat:32.5036, lng:35.5019,
         desc:'The Philistines hung Saul\'s body on the city wall after the battle of Mount Gilboa. Later became a major Decapolis city.',
         refs:'1 Samuel 31:10-12; 2 Samuel 21:12'},
        {cat:'biblical', name:'Ramoth-gilead', lat:32.33, lng:35.99,
         desc:'Strategic Transjordanian city of refuge. Scene of Ahab\'s death in battle. Jehu was anointed king here.',
         refs:'1 Kings 22:1-37; 2 Kings 9:1-6; Deuteronomy 4:43'},
        {cat:'biblical', name:'Tirzah', lat:32.31, lng:35.34,
         desc:'Early capital of the northern kingdom before Samaria. Known for beauty \u2014 "You are beautiful as Tirzah."',
         refs:'1 Kings 14:17; Song of Solomon 6:4'},
        {cat:'biblical', name:'Gerar', lat:31.39, lng:34.58,
         desc:'Philistine city where both Abraham and Isaac sojourned. Abimelech was king here.',
         refs:'Genesis 20:1-2; 26:1-6'},
        {cat:'biblical', name:'Lahai-roi', lat:30.87, lng:34.58,
         desc:'Well where the angel of the LORD appeared to Hagar. She named it "the well of the Living One who sees me." Isaac later dwelt here.',
         refs:'Genesis 16:13-14; 24:62; 25:11'},

        // ══════════════════════════════════════════════════════════
        // ── PROPHETIC & IMPERIAL CITIES ──
        // ══════════════════════════════════════════════════════════
        {cat:'biblical', name:'Nineveh', lat:36.36, lng:43.15,
         desc:'Capital of the Assyrian Empire. Jonah preached here and the city repented. Nahum prophesied its destruction, fulfilled in 612 BC. The library of Ashurbanipal preserved the Gilgamesh Epic.',
         refs:'Jonah 3:1-10; Nahum 1-3; Genesis 10:11',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Nineveh_mashki_gate_from_west.jpg/320px-Nineveh_mashki_gate_from_west.jpg'},
        {cat:'biblical', name:'Damascus', lat:33.5138, lng:36.2765,
         desc:'One of the oldest continuously inhabited cities. Abraham pursued the kings here. Naaman was healed here. Paul was converted on the road to Damascus.',
         refs:'Genesis 14:15; 2 Kings 5:12; Acts 9:1-9; Isaiah 17:1',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Umayyad_Mosque_Damascus.jpg/320px-Umayyad_Mosque_Damascus.jpg'},
        {cat:'cultural', name:'Assur (Ashur)', lat:35.4575, lng:43.26,
         desc:'Original capital of Assyria, named after Asshur son of Shem. The Assyrian Empire began here before expanding to Nineveh and Calah.',
         refs:'Genesis 10:11,22; Ezekiel 32:22-23'},
        {cat:'cultural', name:'Calah (Nimrud)', lat:36.0992, lng:43.33,
         desc:'Biblical Calah (Gen 10:11) — built in the shadow of Nimrod\'s empire. The Black Obelisk of Shalmaneser III showing Jehu bowing was found here. The throne room of Ashurnasirpal II was lined wall-to-wall with apkallu carvings: winged divine beings performing sacred rituals, the Mesopotamian equivalent of the heavenly council. Partially destroyed by ISIS in 2015, Nimrud connects Genesis 10\'s Table of Nations to the divine council worldview.',
         refs:'Genesis 10:8-12; 2 Kings 17:3; Micah 5:6; Isaiah 37:37-38',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Nimrud_lamassu_at_the_British_Museum.jpg/220px-Nimrud_lamassu_at_the_British_Museum.jpg'},
        {cat:'biblical', name:'Susa (Shushan)', lat:32.19, lng:48.26,
         desc:'Capital of the Persian Empire. Setting of Esther. Daniel received visions here. Nehemiah served as cupbearer to Artaxerxes.',
         refs:'Esther 1:2; Daniel 8:2; Nehemiah 1:1',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Susa_Apadana_bull_capital.jpg/320px-Susa_Apadana_bull_capital.jpg'},
        {cat:'cultural', name:'Persepolis', lat:29.9353, lng:52.8914,
         desc:'Ceremonial capital of the Achaemenid Persian Empire. Built by Darius I and Xerxes (the Ahasuerus of Esther). Destroyed by Alexander the Great in 330 BC.',
         refs:'Ezra 6:1-5; Esther 1:1-3'},
        {cat:'cultural', name:'Carchemish', lat:36.8283, lng:38.0167,
         desc:'Strategic city on the Euphrates where Nebuchadnezzar defeated Pharaoh Necho in 605 BC, establishing Babylonian supremacy.',
         refs:'Jeremiah 46:2; 2 Chronicles 35:20'},
        {cat:'biblical', name:'Tadmor (Palmyra)', lat:34.55, lng:38.267,
         desc:'Desert oasis city built by Solomon on trade routes between Damascus and Mesopotamia.',
         refs:'1 Kings 9:18; 2 Chronicles 8:4'},

        // ══════════════════════════════════════════════════════════
        // ── EGYPTIAN CITIES ──
        // ══════════════════════════════════════════════════════════
        {cat:'cultural', name:'Thebes (Luxor / No-Amon)', lat:25.6872, lng:32.6396,
         desc:'Ancient capital of Upper Egypt, called "No-Amon" in Scripture. Nahum compared Nineveh to Thebes\' fall. The Valley of the Kings and Karnak temple complex are here.',
         refs:'Nahum 3:8; Jeremiah 46:25; Ezekiel 30:14-16'},
        {cat:'cultural', name:'Memphis (Noph)', lat:29.8481, lng:31.2547,
         desc:'Ancient capital of Lower Egypt. Called "Noph" in Scripture. Isaiah, Jeremiah, and Ezekiel prophesied against it.',
         refs:'Isaiah 19:13; Jeremiah 46:14; Ezekiel 30:13'},
        {cat:'cultural', name:'On (Heliopolis)', lat:30.1311, lng:31.3133,
         desc:'Ancient center of Egyptian sun worship. Joseph married Asenath, daughter of Potiphera priest of On.',
         refs:'Genesis 41:45,50; Ezekiel 30:17'},
        {cat:'cultural', name:'Avaris (Tell el-Dab\'a)', lat:30.79, lng:31.83,
         desc:'Hyksos capital in the Nile Delta, possibly where Joseph rose to power. Semitic-style settlement found here dating to the Middle Bronze Age.',
         refs:'Genesis 47:11; Exodus 1:8-11'},
        {cat:'cultural', name:'Alexandria', lat:31.2001, lng:29.9187,
         desc:'Founded by Alexander the Great. Home of the largest Jewish diaspora community. The Septuagint (Greek OT) was translated here. Apollos came from here.',
         refs:'Acts 18:24; 27:6'},
        {cat:'cultural', name:'Elephantine Island', lat:24.085, lng:32.886,
         desc:'Island in the Nile at Aswan. A Jewish military colony existed here in the 5th century BC with their own temple to YHWH.',
         refs:'Jeremiah 44:1; Ezekiel 29:10'},

        // ══════════════════════════════════════════════════════════
        // ── NEW TESTAMENT: GALILEE & JUDEA ──
        // ══════════════════════════════════════════════════════════
        {cat:'biblical', name:'Nazareth', lat:32.7019, lng:35.2978,
         desc:'Hometown of Jesus. A small village \u2014 "Can anything good come from Nazareth?" (John 1:46). Jesus was rejected by his own synagogue here.',
         refs:'Matthew 2:23; Luke 4:16-30; John 1:46',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Nazareth_panoramic_view.jpg/320px-Nazareth_panoramic_view.jpg'},
        {cat:'biblical', name:'Capernaum', lat:32.8808, lng:35.5753,
         desc:'Jesus\' base of operations in Galilee. Peter\'s house was here. Many healings, the centurion\'s servant, calling of Matthew. Jesus pronounced woe on it.',
         refs:'Matthew 4:13; 11:23; Mark 1:21-34',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Capernaum_synagogue_ruins.jpg/320px-Capernaum_synagogue_ruins.jpg'},
        {cat:'biblical', name:'Bethsaida', lat:32.9069, lng:35.6311,
         desc:'Hometown of Peter, Andrew, and Philip. Near the feeding of the 5,000. Jesus pronounced woe on it for rejecting his miracles.',
         refs:'Matthew 11:21; Mark 8:22-26; John 1:44'},
        {cat:'biblical', name:'Chorazin', lat:32.9103, lng:35.5639,
         desc:'Galilean town condemned by Jesus: "Woe to you, Chorazin! If the mighty works done in you had been done in Tyre and Sidon, they would have repented."',
         refs:'Matthew 11:21; Luke 10:13'},
        {cat:'biblical', name:'Cana', lat:32.7472, lng:35.3389,
         desc:'Where Jesus performed his first miracle, turning water into wine at a wedding feast. Also healed the royal official\'s son from a distance.',
         refs:'John 2:1-11; 4:46-54'},
        {cat:'biblical', name:'Nain', lat:32.6317, lng:35.3483,
         desc:'Village where Jesus raised a widow\'s only son from the dead. "Young man, I say to you, arise."',
         refs:'Luke 7:11-17'},
        {cat:'biblical', name:'Tiberias / Sea of Galilee', lat:32.7953, lng:35.5322,
         desc:'City on the western shore of the Sea of Galilee built by Herod Antipas. Jesus walked on water, calmed storms, and called fishermen on this lake.',
         refs:'John 6:1,23; 21:1; Matthew 14:22-33'},
        {cat:'biblical', name:'Bethany', lat:31.7678, lng:35.2619,
         desc:'Home of Mary, Martha, and Lazarus. Jesus raised Lazarus from the dead here. Mary anointed Jesus with costly perfume. Jesus ascended from near here.',
         refs:'John 11:1-44; 12:1-8; Luke 24:50-51'},
        {cat:'biblical', name:'Emmaus', lat:31.8389, lng:34.9889,
         desc:'Village where the risen Jesus appeared to two disciples on the road, opening the Scriptures. "Their eyes were opened in the breaking of bread."',
         refs:'Luke 24:13-35'},
        {cat:'biblical', name:'Sychar (Jacob\'s Well)', lat:32.21, lng:35.285,
         desc:'Where Jesus met the Samaritan woman at Jacob\'s well and revealed himself as the Messiah. "The water I give will become a spring welling up to eternal life."',
         refs:'John 4:5-42'},
        {cat:'biblical', name:'Mount of Olives', lat:31.7781, lng:35.2475,
         desc:'East of Jerusalem across the Kidron Valley. Jesus taught the Olivet Discourse here, prayed in Gethsemane, and ascended to heaven. Zechariah prophesies his return here.',
         refs:'Zechariah 14:4; Matthew 24-25; Acts 1:9-12'},
        {cat:'biblical', name:'Mount Tabor', lat:32.6869, lng:35.3914,
         desc:'Traditional site of the Transfiguration, where Jesus appeared in glory with Moses and Elijah. Peter, James, and John witnessed the divine council revealing Christ\'s glory.',
         refs:'Matthew 17:1-8; Mark 9:2-8; Judges 4:6'},
        {cat:'biblical', name:'Caesarea Maritima', lat:32.50, lng:34.8903,
         desc:'Roman capital of Judea. Built by Herod the Great. Where Peter baptized Cornelius (first Gentile convert). Paul was imprisoned here for two years.',
         refs:'Acts 10:1-48; 23:23-35; 24-26'},
        {cat:'biblical', name:'Gethsemane', lat:31.7794, lng:35.2403,
         desc:'Garden at the foot of the Mount of Olives where Jesus prayed before his arrest. "Not my will, but yours be done." Judas betrayed him here.',
         refs:'Matthew 26:36-56; Luke 22:39-46',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Garden_of_Gethsemane_2010.jpg/320px-Garden_of_Gethsemane_2010.jpg'},
        {cat:'biblical', name:'Golgotha (Calvary)', lat:31.7789, lng:35.2297,
         desc:'The Place of the Skull where Jesus was crucified. "It is finished." The veil of the temple was torn from top to bottom.',
         refs:'Matthew 27:33-50; John 19:17-30; Hebrews 13:12'},
        {cat:'biblical', name:'Pool of Siloam', lat:31.7714, lng:35.2347,
         desc:'Pool in the City of David where Jesus sent the blind man to wash. Hezekiah\'s tunnel channeled water here from the Gihon Spring.',
         refs:'John 9:1-11; 2 Kings 20:20; Isaiah 8:6'},
        {cat:'biblical', name:'Mount Gilboa', lat:32.49, lng:35.41,
         desc:'Where Saul and Jonathan died in battle against the Philistines. David\'s lament: "How the mighty have fallen!"',
         refs:'1 Samuel 31:1-8; 2 Samuel 1:17-27'},

        // ══════════════════════════════════════════════════════════
        // ── ACTS: PAULINE MISSION CITIES ──
        // ══════════════════════════════════════════════════════════
        {cat:'biblical', name:'Antioch of Syria', lat:36.20, lng:36.16,
         desc:'Where believers were first called Christians. Paul\'s home base for missionary journeys. Third largest city in the Roman Empire.',
         refs:'Acts 11:26; 13:1-3; Galatians 2:11'},
        {cat:'biblical', name:'Antioch of Pisidia', lat:38.3117, lng:31.175,
         desc:'Paul preached here on his first missionary journey. After Jewish opposition, he declared: "We are turning to the Gentiles." A pivotal moment.',
         refs:'Acts 13:14-52'},
        {cat:'biblical', name:'Ephesus', lat:37.9395, lng:27.3417,
         desc:'Major city of Asia Minor. Paul spent 2-3 years here. The riot of silversmiths defending Artemis. One of the seven churches of Revelation.',
         refs:'Acts 19:1-41; Ephesians 1:1; Revelation 2:1-7',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Ephesus_Celsus_Library_Façade.jpg/320px-Ephesus_Celsus_Library_Façade.jpg'},
        {cat:'biblical', name:'Corinth', lat:37.9059, lng:22.8783,
         desc:'Commercial crossroads of Greece. Paul lived here 18 months. A morally corrupt city \u2014 Paul addressed immorality, spiritual gifts, and the resurrection.',
         refs:'Acts 18:1-18; 1 Corinthians 1:2'},
        {cat:'biblical', name:'Philippi', lat:41.0106, lng:24.2858,
         desc:'Roman colony in Macedonia. First European church. Lydia was the first European convert. Paul and Silas were imprisoned here and an earthquake freed them.',
         refs:'Acts 16:12-40; Philippians 1:1'},
        {cat:'biblical', name:'Thessalonica', lat:40.6401, lng:22.9444,
         desc:'Capital of Macedonia. Paul established a church here. His letters address the second coming \u2014 "the Lord himself will descend from heaven with a shout."',
         refs:'Acts 17:1-9; 1 Thessalonians 4:16-17'},
        {cat:'biblical', name:'Athens', lat:37.9715, lng:23.7257,
         desc:'Intellectual capital of the ancient world. Paul preached on Mars Hill: "The God who made the world does not live in temples made by hands."',
         refs:'Acts 17:16-34',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/The_Parthenon_in_Athens.jpg/320px-The_Parthenon_in_Athens.jpg'},
        {cat:'biblical', name:'Berea', lat:40.5192, lng:22.35,
         desc:'Where the Jews were "more noble" \u2014 they examined the Scriptures daily to see if Paul\'s teaching was true. The model for discerning Bible study.',
         refs:'Acts 17:10-15'},
        {cat:'biblical', name:'Troas', lat:39.7567, lng:26.1717,
         desc:'Where Paul received the Macedonian vision: "Come over and help us." The gospel crossed from Asia into Europe here.',
         refs:'Acts 16:8-11; 20:5-12'},
        {cat:'biblical', name:'Derbe', lat:37.35, lng:33.35,
         desc:'City in Lycaonia where Paul preached and won many disciples on his first and second missionary journeys. Timothy may have been from this region.',
         refs:'Acts 14:20-21; 16:1'},
        {cat:'biblical', name:'Lystra', lat:37.5708, lng:32.3306,
         desc:'Where Paul healed a lame man and the crowd tried to worship him as Zeus. Paul was later stoned and left for dead but revived. Timothy\'s hometown.',
         refs:'Acts 14:6-20; 16:1; 2 Timothy 3:11'},
        {cat:'biblical', name:'Iconium', lat:37.8714, lng:32.4922,
         desc:'Paul preached here on his first journey but the city divided. He fled when a plot to stone him was discovered.',
         refs:'Acts 13:51-14:6; 16:2'},
        {cat:'biblical', name:'Perga', lat:36.9611, lng:30.8531,
         desc:'City in Pamphylia where John Mark left Paul and Barnabas \u2014 causing them to later part ways.',
         refs:'Acts 13:13-14; 14:25; 15:38'},
        {cat:'biblical', name:'Paphos', lat:34.7556, lng:32.4067,
         desc:'Roman capital of Cyprus. Paul confronted the sorcerer Elymas here and the proconsul Sergius Paulus believed.',
         refs:'Acts 13:6-12'},
        {cat:'biblical', name:'Malta (Melita)', lat:35.8989, lng:14.5146,
         desc:'Island where Paul was shipwrecked. He was bitten by a viper but suffered no harm. He healed many on the island.',
         refs:'Acts 28:1-10'},
        {cat:'biblical', name:'Rome', lat:41.8919, lng:12.5113,
         desc:'Capital of the Roman Empire. Paul was imprisoned here and wrote Ephesians, Philippians, Colossians, Philemon. Tradition holds Peter and Paul were martyred here under Nero.',
         refs:'Acts 28:14-31; Romans 1:7; Philippians 1:13',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Colosseum_in_Rome-April_2007-1-_copie_2B.jpg/320px-Colosseum_in_Rome-April_2007-1-_copie_2B.jpg'},
        {cat:'biblical', name:'Tarsus', lat:36.917, lng:34.8935,
         desc:'Paul\'s birthplace in Cilicia. A major university city. "I am a Jew, from Tarsus in Cilicia, a citizen of no obscure city."',
         refs:'Acts 9:11; 21:39; 22:3'},
        {cat:'biblical', name:'Miletus', lat:37.5308, lng:27.2783,
         desc:'Port city where Paul delivered his farewell address to the Ephesian elders. "I did not shrink from declaring the whole counsel of God."',
         refs:'Acts 20:15-38'},

        // ══════════════════════════════════════════════════════════
        // ── SEVEN CHURCHES OF REVELATION ──
        // ══════════════════════════════════════════════════════════
        {cat:'biblical', name:'Smyrna (\u0130zmir)', lat:38.4192, lng:27.1287,
         desc:'The suffering church \u2014 "Be faithful unto death and I will give you the crown of life." Polycarp, disciple of John, was martyred here.',
         refs:'Revelation 2:8-11'},
        {cat:'biblical', name:'Pergamum', lat:39.1217, lng:26.96,
         desc:'"Where Satan\'s throne is" \u2014 likely the great altar of Zeus. Home of the first temple of the imperial cult in Asia.',
         refs:'Revelation 2:12-17',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Pergamon_altar_Staatliche_Museen_Berlin_2.jpg/320px-Pergamon_altar_Staatliche_Museen_Berlin_2.jpg'},
        {cat:'biblical', name:'Thyatira', lat:38.9194, lng:27.8375,
         desc:'Rebuked for tolerating "Jezebel." Known for purple dye trade \u2014 Lydia of Thyatira was Paul\'s first European convert.',
         refs:'Revelation 2:18-29; Acts 16:14'},
        {cat:'biblical', name:'Sardis', lat:38.4869, lng:28.0397,
         desc:'"You have the reputation of being alive, but you are dead." Once the capital of Croesus, famous for wealth.',
         refs:'Revelation 3:1-6'},
        {cat:'biblical', name:'Philadelphia (Ala\u015fehir)', lat:38.35, lng:28.5186,
         desc:'The faithful church \u2014 "I have set before you an open door." No rebuke from Christ, only encouragement.',
         refs:'Revelation 3:7-13'},
        {cat:'biblical', name:'Laodicea', lat:37.8361, lng:29.1081,
         desc:'The lukewarm church \u2014 "I will spit you out of my mouth." Known for banking, black wool, and eye salve, all used ironically in Christ\'s rebuke.',
         refs:'Revelation 3:14-22; Colossians 4:16'},
        {cat:'biblical', name:'Colossae', lat:37.7883, lng:29.2617,
         desc:'Paul wrote about Christ\'s supremacy over all powers here. The Colossian heresy mixed Jewish mysticism with proto-Gnostic angel worship.',
         refs:'Colossians 1:15-20; 2:8-15'},
        {cat:'biblical', name:'Patmos', lat:37.31, lng:26.545,
         desc:'Island where John received the Revelation. "I was in the Spirit on the Lord\'s day." The divine council throne room of Revelation 4-5 was revealed here.',
         refs:'Revelation 1:9-11',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Patmos_island_Greece.jpg/320px-Patmos_island_Greece.jpg'},
        {cat:'biblical', name:'Hierapolis', lat:37.9264, lng:29.1264,
         desc:'Near Laodicea and Colossae. Philip the evangelist is traditionally buried here. Hot springs cascading over white travertine terraces (Pamukkale).',
         refs:'Colossians 4:13'},

        // ══════════════════════════════════════════════════════════
        // ── MESOPOTAMIAN / ANE CITIES ──
        // ══════════════════════════════════════════════════════════
        {cat:'cultural', name:'Nippur', lat:32.1261, lng:45.2339,
         desc:'Major Sumerian religious center, seat of Enlil. The Sumerian King List and earliest flood narratives were found here.',
         refs:'Genesis 10-11'},
        {cat:'cultural', name:'Eridu', lat:30.815, lng:45.995,
         desc:'Considered the oldest city in Mesopotamian tradition. The Sumerian King List says "kingship descended from heaven" at Eridu. ANE parallel to Eden.',
         refs:'Genesis 2:10-14; Genesis 10:10'},
        {cat:'cultural', name:'Hattusa (Bogazkoy)', lat:40.0167, lng:34.6167,
         desc:'Capital of the Hittite Empire. Tablets here include treaty forms paralleling Deuteronomy\'s suzerain-vassal covenant structure.',
         refs:'Genesis 23:3-20; 2 Samuel 11:3'},

// ══════════════════════════════════════════════════════════════
// ── EARTH IMPACT CRATERS ──
// ~190 confirmed impact structures from the Earth Impact Database
// "And the number of those who descended on Mount Hermon was 200" — 1 Enoch 6:6
// ══════════════════════════════════════════════════════════════

        {cat:'crater', name:'Vredefort — 300km', lat:-27.0, lng:27.5,
         desc:'Largest confirmed impact crater on Earth, ~2.023 billion years old, located in Free State, South Africa. So ancient that the original crater rim has long since eroded away, leaving only the deeply exhumed central dome.',
         note:'Oldest of the mega-craters — formed before complex life existed on Earth.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Vredefort_Dome_STS51I-33-56A.jpg/320px-Vredefort_Dome_STS51I-33-56A.jpg'},

        {cat:'crater', name:'Sudbury Basin — 250km', lat:46.6, lng:-81.18,
         desc:'Second-largest confirmed impact structure on Earth, ~1.849 billion years old, Ontario, Canada. The impact melted and differentiated the crust, creating one of the world\'s richest nickel-copper-platinum mining districts.',
         note:'The impact\'s mineral legacy has been mined for over a century — wealth buried in catastrophe.'},

        {cat:'crater', name:'Chicxulub — 180km', lat:21.4, lng:-89.52,
         desc:'The KT extinction event crater, ~66 million years old, buried beneath the Yucatan Peninsula and Gulf of Mexico. 75% of all species on Earth died. This single 180km crater changed the course of life on Earth.',
         note:'The great dying that ended the age of dinosaurs — a reminder that cosmic violence reshapes creation.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Chicxulub_gravity_map.jpg/320px-Chicxulub_gravity_map.jpg'},

        {cat:'crater', name:'Popigai — 100km', lat:71.65, lng:111.18,
         desc:'One of the largest impact craters on Earth, ~35.7 million years old, Siberia, Russia. The impact created trillions of carats of diamonds (impact diamonds) by instantaneously transforming graphite in the target rock.',
         note:'Diamonds forged in an instant of cosmic violence — billions of carats still lie beneath Siberian permafrost.'},

        {cat:'crater', name:'Manicouagan — 100km', lat:51.38, lng:-68.7,
         desc:'A multi-ring impact structure ~214 million years old in Quebec, Canada. The iconic annular lake formed when the impact melt rock eroded unevenly; visible from space as a perfect ring. Associated with the Triassic extinction.',
         note:'One of the most visually striking craters on Earth — a celestial ring burned into the Canadian Shield.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/ISS008-E-14750_lrg.jpg/320px-ISS008-E-14750_lrg.jpg'},

        {cat:'crater', name:'Yarrabubba — 70km', lat:-27.17, lng:118.83,
         desc:'Oldest confirmed impact structure on Earth at ~2.229 billion years old, Western Australia. Shocked zircon crystals precisely date this as the world\'s oldest recognized crater. The impact may have triggered a global thaw from Snowball Earth conditions.',
         note:'Oldest confirmed impact structure — 2.229 billion years. A cosmic event older than all complex life.'},

        {cat:'crater', name:'Acraman — 90km', lat:-32.02, lng:135.45,
         desc:'Deeply eroded impact structure ~580 million years old in South Australia. Ejecta from this impact has been traced 300km away in Ediacaran sediments, providing a useful stratigraphic marker for Precambrian geology.',
         note:'Impact ejecta preserved in ancient sediment layers — a bookmark in deep time.'},

        {cat:'crater', name:'Chesapeake Bay — 85km', lat:37.28, lng:-76.02,
         desc:'A buried impact crater ~35.3 million years old beneath the Chesapeake Bay, Virginia, USA. The largest known impact structure in the eastern United States; the Bay\'s irregular shape is partly a product of this ancient catastrophe.',
         note:'An entire American estuary shaped by a forgotten cosmic impact beneath the water.'},

        {cat:'crater', name:'Puchezh-Katunki — 80km', lat:56.97, lng:43.72,
         desc:'Large impact crater ~167 million years old in Nizhny Novgorod Oblast, Russia. Well-preserved central uplift and ring structure; one of the largest impact structures in Europe.',
         note:''},

        {cat:'crater', name:'Morokweng — 70km', lat:-26.47, lng:23.53,
         desc:'Large impact structure ~145 million years old in the Kalahari Desert, South Africa. A meteorite fragment was found within the impact melt, preserved inside the solidified rock — a rare occurrence for large craters.',
         note:'The impactor itself was found preserved within the melt rock — a cosmic visitor entombed for 145 million years.'},

        {cat:'crater', name:'Kara — 65km', lat:69.1, lng:64.15,
         desc:'Impact crater ~70 million years old on the Arctic coast of Russia. Paired with the smaller Ust-Kara crater nearby, suggesting a doublet impact event from a binary asteroid.',
         note:''},

        {cat:'crater', name:'Kara-Kul — 52km', lat:39.02, lng:73.45,
         desc:'Large impact crater ~5 million years old in Tajikistan, Central Asia, at 3,900m elevation in the Pamir Mountains. The crater lake is one of the highest impact lakes in the world.',
         note:'A cosmic scar hidden among the world\'s highest mountain ranges.'},

        {cat:'crater', name:'Siljan Ring — 52km', lat:61.02, lng:14.87,
         desc:'Sweden\'s largest impact structure, ~377 million years old, Dalarna county. The impact created a ring-shaped lake system and was the site of a controversial (and ultimately failed) deep drilling project in the 1980s searching for abiogenic oil.',
         note:''},

        {cat:'crater', name:'Charlevoix — 54km', lat:47.32, lng:-70.3,
         desc:'Impact structure ~342 million years old in Quebec, Canada along the St. Lawrence River. The town of La Malbaie sits within the crater; the region\'s unusual topography puzzled geologists for decades before the impact origin was confirmed.',
         note:''},

        {cat:'crater', name:'Montagnais — 45km', lat:42.88, lng:-64.22,
         desc:'Submerged impact structure ~50.5 million years old beneath the continental shelf off Nova Scotia, Canada. One of the few confirmed submarine impact craters; discovered via seismic reflection surveys.',
         note:''},

        {cat:'crater', name:'Araguainha — 40km', lat:-16.78, lng:-52.98,
         desc:'Largest known impact structure in South America, ~254 million years old, Brazil. Formed at virtually the same time as the Permian-Triassic extinction event (the Great Dying), though a causal link remains debated.',
         note:'A South American crater coincident with the worst mass extinction in Earth\'s history — 96% of marine species perished.'},

        {cat:'crater', name:'Saint Martin — 40km', lat:51.78, lng:-98.53,
         desc:'Well-preserved impact structure ~220 million years old in Manitoba, Canada. Lake St. Martin partially fills the crater; the surrounding geology displays classic impact breccias and shatter cones.',
         note:''},

        {cat:'crater', name:'Woodleigh — 40km', lat:-26.05, lng:114.67,
         desc:'Impact structure ~364 million years old in Western Australia, entirely buried under sedimentary cover. Discovered through aeromagnetic surveys; its true size is still debated, with some estimates reaching 120km.',
         note:''},

        {cat:'crater', name:'Mjolnir — 40km', lat:73.8, lng:29.67,
         desc:'Submarine impact crater ~142 million years old on the floor of the Barents Sea, Norway. Named after Thor\'s hammer; the impact ejected a massive tsunami that devastated Jurassic coastlines around the Arctic.',
         note:'Named for Thor\'s hammer — a fitting name for a cosmic strike that sent Jurassic tsunamis across the Arctic.'},

        {cat:'crater', name:'Carswell — 39km', lat:58.45, lng:-109.5,
         desc:'Impact structure ~115 million years old in Saskatchewan, Canada. The crater contains uranium ore deposits that have been mined; the Athabasca Basin uranium district is geologically associated with this structure.',
         note:''},

        {cat:'crater', name:'Clearwater West — 36km', lat:56.22, lng:-74.5,
         desc:'One of a doublet impact pair ~290 million years old in Quebec, Canada. Clearwater West and Clearwater East formed simultaneously from the breakup of a binary asteroid — two lakes side by side on the Canadian Shield.',
         note:'Twin craters formed in a single moment — a binary asteroid split before striking Earth.'},

        {cat:'crater', name:'Clearwater East — 26km', lat:56.05, lng:-74.07,
         desc:'Smaller of the Clearwater doublet pair, ~290 million years old, Quebec, Canada. Both craters are now filled with lakes and are visible from satellite as twin circular structures on the shield.',
         note:''},

        {cat:'crater', name:'Manson — 35km', lat:42.58, lng:-94.55,
         desc:'Buried impact structure ~73.8 million years old beneath the plains of Iowa, USA. For a time in the 1990s it was a candidate for the Cretaceous extinction event crater before Chicxulub was confirmed.',
         note:'Briefly a candidate for the dinosaur-killing crater before Chicxulub was confirmed.'},

        {cat:'crater', name:'Steen River — 25km', lat:59.5, lng:-117.62,
         desc:'Buried impact crater ~91 million years old in Alberta, Canada. Entirely concealed under sedimentary cover; identified through oil well drilling data and geophysical surveys.',
         note:''},

        {cat:'crater', name:'Slate Islands — 30km', lat:48.67, lng:-87.0,
         desc:'Impact structure ~450 million years old in Lake Superior, Ontario, Canada. The islands themselves are the eroded remnants of the central uplift; shatter cones are found throughout the exposed rock.',
         note:''},

        {cat:'crater', name:'Keurusselka — 30km', lat:62.13, lng:24.6,
         desc:'Ancient impact structure ~1.88 billion years old in Finland. One of the oldest impact structures in Fennoscandia; recognized from shatter cones and planar deformation features in Paleoproterozoic bedrock.',
         note:''},

        {cat:'crater', name:'Shoemaker (Teague Ring) — 30km', lat:-25.87, lng:120.88,
         desc:'Impact structure ~1.63 billion years old in Western Australia. Named after planetary geologist Eugene Shoemaker, who spent decades studying impact craters and whose ashes were carried to the Moon by the Lunar Prospector spacecraft.',
         note:'Named for Eugene Shoemaker — the scientist who proved craters were impacts and whose ashes rest on the Moon.'},

        {cat:'crater', name:'Strangways — 25km', lat:-15.17, lng:133.58,
         desc:'Deeply eroded impact structure ~646 million years old in Northern Territory, Australia. One of the larger and older Australian craters; recognized from impact melt rocks and shocked quartz in Precambrian terrain.',
         note:''},

        {cat:'crater', name:'Mistastin — 28km', lat:55.88, lng:-63.32,
         desc:'Well-preserved impact structure ~36.4 million years old in Labrador, Canada. Mistastin Lake fills the crater; the impact produced anorthosite impact melt glass and shocked minerals still abundant around the shores.',
         note:''},

        {cat:'crater', name:'Deep Bay — 13km', lat:56.4, lng:-103.0,
         desc:'Circular lake-filled impact crater ~99 million years old in Saskatchewan, Canada. The nearly perfectly circular lake is one of the deepest in Saskatchewan; the impact breccia is exposed along the shoreline.',
         note:''},

        {cat:'crater', name:'Nicholson Lake — 12.5km', lat:62.67, lng:-102.97,
         desc:'Impact structure ~400 million years old in the Northwest Territories, Canada. The crater is entirely filled by Nicholson Lake; shatter cones and shocked quartz confirm its impact origin.',
         note:''},

        {cat:'crater', name:'Ries (Nördlinger Ries) — 24km', lat:48.88, lng:10.62,
         desc:'Well-preserved impact crater ~14.8 million years old in Bavaria, Germany. The town of Nördlingen is built entirely within the crater; its medieval city wall is constructed from impact-generated suevite rock containing shocked minerals.',
         note:'Humans built a medieval city inside an impact crater — its very walls are made of suevite rock blasted from the sky.'},

        {cat:'crater', name:'Steinheim — 3.8km', lat:48.68, lng:10.07,
         desc:'Small impact crater ~14.8 million years old in Baden-Württemberg, Germany. Formed simultaneously with the Ries crater 40km away; a doublet impact from a binary asteroid. The central uplift is preserved as a hill.',
         note:'Twin to the Ries — a doublet impact, two craters from one binary impactor striking simultaneously.'},

        {cat:'crater', name:'Rochechouart — 23km', lat:45.82, lng:0.78,
         desc:'Impact structure ~214 million years old in Haute-Vienne, France. The impactite rocks were used as building material throughout the medieval period — several Romanesque churches in the region are constructed from impact melt rock.',
         note:'Medieval churches built from impact melt rock — ancient destruction repurposed for worship.'},

        {cat:'crater', name:'Boltysh — 24km', lat:48.9, lng:32.25,
         desc:'Impact crater ~65.17 million years old in Ukraine, formed approximately 2,000 years before the Chicxulub impact. Evidence of a major wildfire event is preserved in the sediment record immediately above the impact horizon.',
         note:'Struck Earth just before Chicxulub — a cosmic one-two punch at the end of the Cretaceous.'},

        {cat:'crater', name:'Haughton — 23km', lat:75.38, lng:-89.68,
         desc:'Well-preserved impact crater ~39 million years old on Devon Island, Nunavut, Canada. The cold, dry, isolated environment makes it one of the best Mars analog sites on Earth; NASA uses it for planetary exploration research.',
         note:'NASA\'s Mars analog site — the closest thing to Mars on Earth, carved by an ancient impact.'},

        {cat:'crater', name:'Gosses Bluff — 22km', lat:-23.82, lng:132.3,
         desc:'Spectacular impact crater ~142 million years old in the Northern Territory, Australia. A ring of hills ~5km across marks the eroded central uplift; the original 22km rim has been largely stripped away. Sacred to the Western Aranda Aboriginal people as Tnorala.',
         note:'Sacred to Aboriginal Australians as Tnorala — a cosmic cradle, they say, where a woman dropped her baby from the Milky Way.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Gosses_Bluff_Crater_in_Australia.jpg/320px-Gosses_Bluff_Crater_in_Australia.jpg'},

        {cat:'crater', name:'Obolon — 20km', lat:49.35, lng:32.92,
         desc:'Buried impact structure ~169 million years old in Ukraine. Discovered through petroleum drilling; filled with Jurassic sediment. One of several Ukrainian impact structures now recognized in the stable Precambrian basement.',
         note:''},

        {cat:'crater', name:'Logancha — 20km', lat:65.5, lng:95.95,
         desc:'Impact structure ~40 million years old in Krasnoyarsk Krai, Russia. Located in the Siberian platform; recognized from drilling data and surface geomorphology in a remote taiga region.',
         note:''},

        {cat:'crater', name:'Presqu\'ile — 24km', lat:49.72, lng:-74.8,
         desc:'Proposed impact structure ~500 million years old in Quebec, Canada. Located on the Canadian Shield; the circular structure is recognized from geological mapping and gravity anomalies.',
         note:''},

        {cat:'crater', name:'Lappajärvi — 23km', lat:63.2, lng:23.7,
         desc:'Well-studied impact crater ~73 million years old in Ostrobothnia, Finland. Lake Lappajärvi fills the crater; the central island (Kärnänsaari) is a classic central uplift. Impact glasses called "Makelanite" are found locally.',
         note:''},

        {cat:'crater', name:'Dellen — 19km', lat:61.83, lng:16.72,
         desc:'Impact structure ~89 million years old in Hälsingland, Sweden. The twin lakes Norra Dellen and Södra Dellen occupy the crater; the impact is dated to the mid-Cretaceous period.',
         note:''},

        {cat:'crater', name:'Elgygytgyn — 18km', lat:67.5, lng:172.08,
         desc:'Remarkably well-preserved impact crater ~3.6 million years old in Chukotka, Russia. Lake El\'gygytgyn sits in an unglaciated depression; its sediment core preserves an uninterrupted 3.6-million-year climate record, making it a world-class paleoclimate archive.',
         note:'An unglaciated Arctic crater preserving 3.6 million years of unbroken climate history — a cosmic time capsule.'},

        {cat:'crater', name:'Oasis — 18km', lat:24.58, lng:24.4,
         desc:'Impact structure in the Libyan Desert, age less than 120 Ma. Located in a remote desert region; the circular structure with central uplift is recognized from satellite imagery and field geology.',
         note:''},

        {cat:'crater', name:'Lawn Hill — 18km', lat:-18.67, lng:138.65,
         desc:'Impact structure ~500 million years old in Queensland, Australia. Located near Lawn Hill Gorge National Park; the crater is recognized from structural geology mapping in Cambrian sedimentary rocks.',
         note:''},

        {cat:'crater', name:'Luizi — 17km', lat:-10.17, lng:28.0,
         desc:'Impact structure of uncertain age in the Democratic Republic of Congo. Recognized from satellite imagery and field confirmation as one of very few confirmed craters in central Africa.',
         note:'One of only a handful of confirmed impact structures on the African continent.'},

        {cat:'crater', name:'Suavjärvi — 16km', lat:63.12, lng:33.38,
         desc:'Ancient impact structure ~2.4 billion years old in Karelia, Russia. One of the oldest impact structures in the Fennoscandian Shield; recognized from shocked minerals and pseudotachylite in deeply eroded Archean terrain.',
         note:''},

        {cat:'crater', name:'Kaluga — 15km', lat:54.5, lng:36.2,
         desc:'Impact structure ~380 million years old in Kaluga Oblast, Russia. Buried impact crater recognized from drilling data; the circular anomaly in Devonian sediments indicates a significant Paleozoic impact event.',
         note:''},

        {cat:'crater', name:'Zhamanshin — 14km', lat:48.4, lng:60.97,
         desc:'Impact crater ~0.9 million years old in Kazakhstan. One of the youngest confirmed craters in Central Asia; produced abundant impact glasses (irghizites) and impactites that are found strewn across the surrounding steppe.',
         note:''},

        {cat:'crater', name:'Jänisjärvi — 14km', lat:61.97, lng:30.92,
         desc:'Impact structure ~700 million years old in Karelia, Russia. Lake Jänisjärvi fills the circular depression; the Precambrian impact is recognized from shocked minerals and distinctive circular morphology.',
         note:''},

        {cat:'crater', name:'Gweni-Fada — 14km', lat:17.42, lng:21.75,
         desc:'Impact structure in the Ennedi region of Chad, age less than 345 Ma. Remote Saharan crater recognized from satellite imagery and field confirmation; one of several confirmed structures in the Sahara.',
         note:''},

        {cat:'crater', name:'Kentland — 13km', lat:40.75, lng:-87.38,
         desc:'Buried impact structure ~97 million years old in Newton County, Indiana, USA. The crater is exposed in a limestone quarry where the dramatically upturned and brecciated rock confused geologists for decades until shatter cones confirmed impact origin.',
         note:'Shatter cones found in a quarry revealed that the tilted Indiana limestone was impact-deformed, not volcanic.'},

        {cat:'crater', name:'Aorounga — 12.6km', lat:19.1, lng:19.25,
         desc:'Impact crater in northern Chad, Sahara Desert, age less than 345 Ma. Exceptionally well-preserved triple-ring structure visible from space; radar imaging suggests two more buried craters nearby, indicating a possible crater chain from a fragmented comet.',
         note:'Radar imaging hints at a chain of craters — a possible fragmented comet that struck Earth in a line.'},

        {cat:'crater', name:'Vargeão Dome — 12km', lat:-26.83, lng:-52.1,
         desc:'Impact structure in Santa Catarina, Brazil, age less than 70 Ma. Circular geological dome recognized from field mapping and aerial photography; impact origin confirmed by shocked quartz and planar deformation features.',
         note:''},

        {cat:'crater', name:'Serra da Cangalha — 12km', lat:-8.08, lng:-46.87,
         desc:'Impact structure in Tocantins, Brazil, age less than 300 Ma. Exposed circular structure in Paleozoic sedimentary rocks; confirmed by shatter cones and planar deformation features in quartz grains.',
         note:''},

        {cat:'crater', name:'Wells Creek — 12km', lat:36.38, lng:-87.67,
         desc:'Impact structure ~200 million years old in Stewart County, Tennessee, USA. The circular disruption in Ordovician through Mississippian limestone was long attributed to cryptovolcanism before impact origin was confirmed.',
         note:''},

        {cat:'crater', name:'Spider — 13km', lat:-16.73, lng:126.08,
         desc:'Deeply eroded impact structure ~570 million years old in Western Australia. Named for its distinctive appearance in satellite images — radial drainage pattern emanating from a central uplift like spider legs.',
         note:'Named for its spider-like appearance from space — radial valleys emanating from the central uplift.'},

        {cat:'crater', name:'Vista Alegre — 9.5km', lat:-25.87, lng:-52.68,
         desc:'Impact structure ~115 million years old in Paraná, Brazil. Circular structure recognized in Paraná flood basalts; confirmed by shatter cones in basalt — an unusual occurrence as impacts in basalt are less common.',
         note:''},

        {cat:'crater', name:'Connolly Basin — 9km', lat:-23.52, lng:124.75,
         desc:'Impact structure ~60 million years old in Western Australia. Circular basin recognized from remote sensing; one of numerous Australian impact structures confirmed in Precambrian and early Paleozoic terrain.',
         note:''},

        {cat:'crater', name:'Ragozinka — 9km', lat:58.43, lng:62.0,
         desc:'Impact structure ~46 million years old in Sverdlovsk Oblast, Russia. Eocene-age impact recognized from drilling and geophysical surveys in the Western Siberian Platform.',
         note:''},

        {cat:'crater', name:'Beyenchime-Salaatin — 8km', lat:71.0, lng:121.98,
         desc:'Impact structure ~40 million years old in Sakha Republic, Russia. Remote Arctic crater located in the Siberian platform; recognized from aerial photography and confirmed with field geology.',
         note:''},

        {cat:'crater', name:'Bosumtwi — 10.5km', lat:6.5, lng:-1.41,
         desc:'Beautifully preserved impact crater ~1.07 million years old in Ghana, West Africa. Lake Bosumtwi fills the entire crater; it is the only natural lake in Ghana. Associated with the Ivory Coast strewn field of tektites found across West Africa.',
         note:'The source crater for the Ivory Coast tektite strewn field — glass from this impact scattered across West Africa.'},

        {cat:'crater', name:'Ilyinets — 8.5km', lat:49.12, lng:29.1,
         desc:'Impact structure ~378 million years old in Vinnytsia Oblast, Ukraine. Devonian impact recognized from shock metamorphism features; one of multiple Devonian-age impacts recognized globally, suggesting a possible bombardment cluster.',
         note:''},

        {cat:'crater', name:'Paasselkä — 10km', lat:62.07, lng:29.08,
         desc:'Ancient impact structure ~1.92 billion years old in North Karelia, Finland. One of the oldest impact structures in Finland; recognized from shocked quartz and geophysical anomalies in Paleoproterozoic terrain.',
         note:''},

        {cat:'crater', name:'Bigach — 8km', lat:48.6, lng:82.0,
         desc:'Impact structure ~5 million years old in eastern Kazakhstan. Late Miocene crater recognized from circular morphology and impactites; the lake-filled depression is one of few confirmed craters in Central Asia.',
         note:''},

        {cat:'crater', name:'Karla — 10km', lat:54.92, lng:48.02,
         desc:'Impact structure ~5 million years old in the Tatarstan Republic, Russia. Pliocene crater buried under later sediments; confirmed from drilling data and geophysical surveys.',
         note:''},

        {cat:'crater', name:'Lac Couture — 8km', lat:60.13, lng:-75.3,
         desc:'Impact structure ~430 million years old in Quebec, Canada. Circular lake on the Canadian Shield; shatter cones and shocked quartz confirm the Silurian-Ordovician impact origin.',
         note:''},

        {cat:'crater', name:'Lac La Moinerie — 8km', lat:57.43, lng:-66.62,
         desc:'Impact structure ~400 million years old in Quebec, Canada. Circular lake recognized from aerial photography; confirmed impact structure in Devonian-age Precambrian terrain of the Quebec-Labrador border region.',
         note:''},

        {cat:'crater', name:'Zhamanshin ejecta glass (Irghizite) — 14km', lat:48.4, lng:60.97,
         desc:'Note: See Zhamanshin crater entry. Impact glasses (irghizites and zhamanshinites) from this crater are distributed across thousands of square kilometers of Kazakhstan steppe — a silent record of a Pleistocene cosmic strike.',
         note:''},

        {cat:'crater', name:'Söderfjärden — 6.6km', lat:63.02, lng:21.57,
         desc:'Impact structure ~600 million years old in Ostrobothnia, Finland. Circular bay on the Finnish coast; the impact created a circular depression now partially occupied by a shallow coastal inlet and farmland.',
         note:''},

        {cat:'crater', name:'Wanapitei — 7.5km', lat:46.75, lng:-80.75,
         desc:'Impact structure ~37 million years old in Ontario, Canada. Lake Wanapitei, a perfectly circular lake, sits inside the partially preserved crater; located near Sudbury, it was long confused with the larger Sudbury impact structure.',
         note:''},

        {cat:'crater', name:'Tin Bider — 6km', lat:27.6, lng:5.12,
         desc:'Impact structure ~70 million years old in the Sahara Desert, Algeria. Circular structure in Cretaceous sedimentary rocks; recognized from aerial photography and confirmed with field geology in a remote desert setting.',
         note:''},

        {cat:'crater', name:'Kursk — 6km', lat:51.7, lng:36.0,
         desc:'Buried impact structure ~250 million years old in Kursk Oblast, Russia. Recognized from drilling data in the sedimentary cover over the Voronezh Massif; a Permian-age impact deeply buried under later sediments.',
         note:''},

        {cat:'crater', name:'Maple Creek — 6km', lat:49.83, lng:-109.08,
         desc:'Proposed impact structure in southwestern Saskatchewan, Canada. Circular feature recognized from geological mapping; age uncertain. One of numerous circular structures on the Canadian Plains still under investigation.',
         note:''},

        {cat:'crater', name:'Pilot Lake — 6km', lat:60.17, lng:-111.02,
         desc:'Impact structure ~445 million years old in the Northwest Territories, Canada. Ordovician-age crater recognized from shatter cones and circular morphology; Pilot Lake fills the depression.',
         note:''},

        {cat:'crater', name:'Ternovka (Terny) — 11km', lat:48.13, lng:33.52,
         desc:'Impact structure ~280 million years old in Dnipropetrovsk Oblast, Ukraine. Permian-age crater confirmed from shock metamorphism; one of several impact structures in the Ukrainian crystalline shield.',
         note:''},

        {cat:'crater', name:'Ramgarh — 5.5km', lat:25.32, lng:76.63,
         desc:'Circular impact structure in Rajasthan, India, age less than 600 Ma. One of the few confirmed impact structures on the Indian subcontinent; the circular depression with central uplift is clearly visible from aerial surveys.',
         note:''},

        {cat:'crater', name:'Riachão Ring — 4.5km', lat:-7.72, lng:-46.65,
         desc:'Impact structure in Maranhão, Brazil, age less than 200 Ma. Circular structure in Paleozoic sandstone; recognized from aerial photography and confirmed with shatter cones and planar deformation features.',
         note:''},

        {cat:'crater', name:'Dobele — 4.5km', lat:56.58, lng:23.25,
         desc:'Impact structure ~290 million years old in Latvia. Buried Permian crater recognized from drilling data; one of the few confirmed impact structures in the Baltic states.',
         note:''},

        {cat:'crater', name:'Dhala — 11km', lat:24.0, lng:78.15,
         desc:'Well-confirmed impact structure ~1.7 billion years old in Madhya Pradesh, India. Ancient Proterozoic impact crater; one of the largest confirmed craters on the Indian subcontinent, with impact melt rocks and shatter cones exposed at the surface.',
         note:''},

        {cat:'crater', name:'Lockne — 7.5km', lat:63.0, lng:14.82,
         desc:'Marine impact crater ~458 million years old in Jämtland, Sweden. Impact occurred in a shallow Ordovician sea; the impactor struck water before hitting the seafloor. The resurge sediments from the returning seawater are exceptionally preserved.',
         note:'An asteroid that struck a shallow Ordovician sea — wave patterns from the impact resurge are fossilized in the rock.'},

        {cat:'crater', name:'Gardnos — 5km', lat:60.65, lng:9.0,
         desc:'Impact structure ~500 million years old in Numedal, Norway. Recognized from the distinctive breccia (Gardnos breccia) exposed along the river; one of few confirmed craters in Scandinavia.',
         note:''},

        {cat:'crater', name:'Kjardla — 4km', lat:59.0, lng:22.77,
         desc:'Impact structure ~455 million years old on Hiiumaa Island, Estonia. Ordovician-age crater; the island\'s circular topographic feature was recognized as an impact structure after shocked quartz was found in drill cores.',
         note:''},

        {cat:'crater', name:'Tvären — 2km', lat:58.77, lng:17.42,
         desc:'Marine impact crater ~455 million years old in Södermanland, Sweden. Like Lockne, this Ordovician impact struck a shallow sea; resurge breccia and marine fossils are preserved in the crater fill.',
         note:''},

        {cat:'crater', name:'Suvasvesi S — 3.8km', lat:62.65, lng:28.17,
         desc:'Impact structure ~250 million years old in North Savo, Finland. One of two impact structures (Suvasvesi North and South) in the same region; Permian-age impact confirmed from planar deformation features.',
         note:''},

        {cat:'crater', name:'Iso-Naakkima — 3km', lat:62.18, lng:27.15,
         desc:'Impact structure ~900 million years old in South Savo, Finland. Ancient Proterozoic impact; the circular lake fills the structure. Shocked quartz and planar deformation features confirm its impact origin.',
         note:''},

        {cat:'crater', name:'Saarijärvi — 1.5km', lat:65.28, lng:28.38,
         desc:'Impact structure ~600 million years old in Oulu, Finland. Small Precambrian impact crater recognized from circular morphology and shocked minerals in Proterozoic bedrock.',
         note:''},

        {cat:'crater', name:'Summanen — 2.6km', lat:63.0, lng:25.33,
         desc:'Impact structure greater than 1 billion years old in Central Finland. Ancient Precambrian impact; one of the oldest confirmed craters in Finland. Recognized from impactite rocks and shocked quartz in Archean-Proterozoic terrain.',
         note:''},

        {cat:'crater', name:'Rotmistrovka — 2.7km', lat:49.0, lng:32.0,
         desc:'Impact structure ~140 million years old in Cherkasy Oblast, Ukraine. Small Cretaceous impact confirmed from drill core data; one of several buried impact structures in the Ukrainian sedimentary cover.',
         note:''},

        {cat:'crater', name:'Roter Kamm — 2.5km', lat:-27.77, lng:16.3,
         desc:'Well-preserved impact crater ~3.7 million years old in the Namib Desert, Namibia. The crater walls and interior are partially filled with sand dunes; its excellent preservation is due to the hyper-arid desert climate.',
         note:'Preserved by desert silence — the Namib\'s dryness has kept this 3.7-million-year-old crater nearly intact.'},

        {cat:'crater', name:'Tswaing (Pretoria Salt Pan) — 1.13km', lat:-25.4, lng:28.08,
         desc:'Impact crater ~220,000 years old near Pretoria, South Africa. The saline lake in the crater has been used by humans for salt and water for at least 100,000 years; archaeological evidence of human use surrounds the crater.',
         note:'Humans harvested salt from this impact crater for 100,000 years — cosmic and human history intertwined.'},

        {cat:'crater', name:'Tenoumer — 1.9km', lat:22.92, lng:-10.4,
         desc:'Well-preserved impact crater ~21,400 years old in Mauritania, West Africa. Near-perfect circular structure in the Sahara; its young age and arid climate have kept it remarkably pristine with clear rim and interior structure.',
         note:''},

        {cat:'crater', name:'Aouelloul — 0.39km', lat:20.25, lng:-12.68,
         desc:'Small impact crater ~3 million years old in Mauritania. Associated with the Aouelloul glass, a silica-rich impact glass found in the surrounding desert. One of the few confirmed craters in West Africa.',
         note:''},

        {cat:'crater', name:'Amguid — 0.45km', lat:26.05, lng:4.4,
         desc:'Impact crater of uncertain age (less than 100,000 years) in the Algerian Sahara. Exceptionally well-preserved small crater in a remote desert; nearly perfectly circular with a raised rim and bowl-shaped interior.',
         note:''},

        {cat:'crater', name:'BP Structure — 2km', lat:25.32, lng:24.32,
         desc:'Circular impact structure in the Libyan Desert, age less than 120 Ma. The two-ring structure is clearly visible from satellite; exposed in Paleozoic sandstones in a remote corner of the Libyan Desert.',
         note:''},

        {cat:'crater', name:'Kalkkop — 0.64km', lat:-32.72, lng:24.43,
         desc:'Young impact crater ~250,000 years old in the Eastern Cape, South Africa. The circular crater is filled with lacustrine sediment; drill cores through this sediment preserve a high-resolution Pleistocene climate record for southern Africa.',
         note:''},

        {cat:'crater', name:'Lonar — 1.8km', lat:19.97, lng:76.5,
         desc:'The only confirmed impact crater in basaltic rock in the world, ~52,000 years old in Maharashtra, India. The alkaline/saline lake is an ecological and geological treasure; the surrounding forest and temples make it a site of cultural and scientific significance.',
         note:'The world\'s only confirmed impact crater in basalt — sacred to locals, studied by scientists, unique on Earth.'},

        {cat:'crater', name:'Xiuyan — 1.8km', lat:40.37, lng:123.45,
         desc:'Impact crater ~50,000 years old in Liaoning Province, China. One of only a few confirmed impact craters in China; the circular structure in Precambrian granite was confirmed by shatter cones and planar deformation features.',
         note:''},

        {cat:'crater', name:'Tabun-Khara-Obo — 1.3km', lat:44.12, lng:109.65,
         desc:'Small impact structure ~150 million years old in Mongolia. One of the few confirmed impact structures in Mongolia; the circular depression in Jurassic sediment is confirmed by planar deformation features in quartz.',
         note:''},

        {cat:'crater', name:'Kamil — 0.045km', lat:22.02, lng:26.05,
         desc:'Exceptionally well-preserved iron meteorite impact crater ~5,000 years old in the Eastern Sahara, Egypt. Discovered via Google Earth in 2008 by Italian researchers; the associated iron meteorite fragments (Campo-type) are still abundant around the crater.',
         note:'Discovered on Google Earth in 2008 — a pristine 5,000-year-old crater hidden in the Egyptian desert.'},

        {cat:'crater', name:'Monturaqui — 0.37km', lat:-23.93, lng:-68.27,
         desc:'Small impact crater less than 1 million years old in the Atacama Desert, Chile, at 3,500m elevation. The extreme aridity of the Atacama has preserved this crater in excellent condition; iron meteorite fragments are found nearby.',
         note:'High in the Atacama at 3,500m — aridity preserves this crater\'s sharp rim and scattered meteorite fragments.'},

        {cat:'crater', name:'Meteor Crater (Barringer) — 1.2km', lat:35.03, lng:-111.02,
         desc:'The best-preserved and most famous impact crater on Earth, ~49,000 years old near Winslow, Arizona. Barringer Crater proved the existence of hypervelocity impacts over volcanic origin. A tourist icon and landmark of planetary science.',
         note:'The crater that proved impacts are real — Daniel Barringer fought his whole life to prove what is now textbook science.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Meteor_Crater_-_Arizona.jpg/320px-Meteor_Crater_-_Arizona.jpg'},

        {cat:'crater', name:'Upheaval Dome — 10km', lat:38.44, lng:-109.93,
         desc:'Impact structure ~170 million years old in Canyonlands National Park, Utah, USA. Long debated between salt dome or impact origin; shock metamorphism features confirmed the impact. The eroded structure creates a spectacular geological display visible to hikers.',
         note:'Debated for decades — then shocked quartz settled the argument. A national park built around a cosmic mystery.'},

        {cat:'crater', name:'Middlesboro — 6km', lat:36.62, lng:-83.73,
         desc:'Impact structure ~300 million years old in Bell County, Kentucky, USA. The town of Middlesboro was built inside the impact crater; the circular valley surrounded by hills puzzled early settlers. Shatter cones were eventually found in local rock.',
         note:'An entire town built inside an impact crater — Middlesboro, Kentucky sits in a cosmic bowl.'},

        {cat:'crater', name:'Sierra Madera — 13km', lat:30.6, lng:-102.92,
         desc:'Impact structure ~100 million years old in Pecos County, Texas, USA. The disturbed dome of uplifted Permian and Triassic sediments was long attributed to salt tectonics; shatter cones confirmed the impact origin.',
         note:''},

        {cat:'crater', name:'Flynn Creek — 3.8km', lat:36.27, lng:-85.67,
         desc:'Impact structure ~360 million years old in Jackson County, Tennessee, USA. Devonian-age impact crater recognized from disturbed limestone; the circular structure with central uplift is exposed along creek drainages.',
         note:''},

        {cat:'crater', name:'Crooked Creek — 7km', lat:37.83, lng:-91.38,
         desc:'Impact structure ~320 million years old in Gasconade County, Missouri, USA. Mississippian-age crater; the circular zone of disturbed carbonate rock was long classified as a cryptoexplosion structure before impact was confirmed.',
         note:''},

        {cat:'crater', name:'Decaturville — 6km', lat:37.9, lng:-92.72,
         desc:'Impact structure ~300 million years old in Camden County, Missouri, USA. Circular zone of brecciated and uplifted Ordovician to Pennsylvanian carbonate rocks; shatter cones confirm the impact origin.',
         note:''},

        {cat:'crater', name:'Glasford — 4km', lat:40.6, lng:-89.78,
         desc:'Buried impact structure ~430 million years old beneath the Illinois plains. Recognized from drilling data; the circular anomaly in Ordovician rocks is deeply buried under Quaternary glacial sediment.',
         note:''},

        {cat:'crater', name:'Brent — 3.8km', lat:46.08, lng:-78.48,
         desc:'Impact structure ~396 million years old in Ontario, Canada. The crater is partially filled by Brent Lake; drill cores through the lake sediment recovered suevite and impact melt, confirming the Devonian impact.',
         note:''},

        {cat:'crater', name:'West Hawk Lake — 2.4km', lat:49.77, lng:-95.18,
         desc:'Impact crater ~351 million years old in Manitoba, Canada. West Hawk Lake is the deepest lake in Manitoba (111m), far deeper than its size would suggest — the depth is a product of the crater morphology.',
         note:'The deepest lake in Manitoba is an impact crater — its unusual depth puzzled settlers for generations.'},

        {cat:'crater', name:'Pingualuit (New Quebec) — 3.4km', lat:61.28, lng:-73.67,
         desc:'Exceptionally pure impact crater lake ~1.4 million years old in Nunavik, Quebec, Canada. The lake water is among the purest on Earth — no river inflows, fed only by rain and snow. The crystal-clear lake sits in a perfectly circular bowl on the tundra.',
         note:'The purest lake water on Earth — no rivers flow in or out. The Inuit call it "the crystal eye of Nunavik."'},

        {cat:'crater', name:'Lac Couture — 8km', lat:60.13, lng:-75.3,
         desc:'Impact structure ~430 million years old in Quebec, Canada. Circular lake on the Canadian Shield; shatter cones and shocked quartz confirm the Ordovician impact origin.',
         note:''},

        {cat:'crater', name:'Ilumetsa — 0.08km', lat:57.95, lng:27.4,
         desc:'Small impact crater cluster ~7,500 years old in Põlva County, Estonia. Group of three small craters formed by the fragmentation of a meteorite before impact; the largest is 80m diameter.',
         note:''},

        {cat:'crater', name:'Kaali — 0.11km', lat:58.37, lng:22.67,
         desc:'Iron meteorite impact crater ~7,600 years old on Saaremaa Island, Estonia. The main crater (110m wide) is surrounded by 8 smaller craters; the impact occurred during the Bronze Age and may have been witnessed by humans. Featured in Finnish-Estonian mythology.',
         note:'This Bronze Age impact may have been witnessed by humans — possibly the origin of a fireball myth in Baltic-Finnish tradition.'},

        {cat:'crater', name:'Wolfe Creek — 0.87km', lat:-19.17, lng:127.8,
         desc:'Spectacular impact crater ~120,000 years old in the Kimberley region of Western Australia. The second-largest crater in Australia visible at the surface; well-preserved with a raised rim. Known to Aboriginal Australians as Kandimalal — the trail of a rainbow serpent.',
         note:'Aboriginal Australians know this crater as Kandimalal — where the rainbow serpent emerged from the earth.'},

        {cat:'crater', name:'Henbury Craters — cluster', lat:-24.57, lng:133.13,
         desc:'Cluster of 12 craters ~4,200 years old in the Northern Territory, Australia. Formed by the breakup of a large iron meteorite; the largest crater is 180m across. Aboriginal legend warns against the site, calling it "chin-durunmara" (sun walk fire devil).',
         note:'Aboriginal oral tradition preserves the memory of this 4,200-year-old impact — "fire devil from the sun."'},

        {cat:'crater', name:'Wabar — 0.12km', lat:21.5, lng:50.47,
         desc:'Iron meteorite impact crater less than 300 years old in the Rub\' al Khali desert, Saudi Arabia. The most recent confirmed crater on Earth from a witnessed/documented event. The impactor created distinctive black glass (Wabar glass) and white sandstone bombs.',
         note:'The most recently formed confirmed impact crater on Earth — less than 300 years old in the heart of the Empty Quarter.'},

        {cat:'crater', name:'Campo del Cielo — cluster', lat:-27.63, lng:-61.7,
         desc:'Cluster of approximately 26 craters ~4,000 years old in the Gran Chaco, Argentina. One of the largest iron meteorite strewn fields on Earth; individual meteorites weigh up to 37 tonnes. Pre-Columbian indigenous peoples collected the iron for tools.',
         note:'Pre-Columbian people harvested iron from this meteorite cluster for tools and weapons — sky-iron technology.'},

        {cat:'crater', name:'Sikhote-Alin — cluster', lat:46.12, lng:134.65,
         desc:'Iron meteorite crater cluster from the historic February 12, 1947 fall in Primorsky Krai, Russia. Witnessed by thousands; the bolide broke apart producing a shower of craters, the largest 26m wide. The most significant witnessed impact event of the 20th century.',
         note:'Thousands of witnesses watched this 1947 iron meteor shower — the largest witnessed meteorite fall in recorded history.'},

        {cat:'crater', name:'Whitecourt — 0.036km', lat:54.0, lng:-115.6,
         desc:'Small iron meteorite impact crater ~1,100 years old in Alberta, Canada. Discovered in 2007; iron meteorite fragments are still being recovered from the impact site. One of the youngest confirmed craters in Canada.',
         note:''},

        {cat:'crater', name:'Veevers — 0.07km', lat:-22.97, lng:125.37,
         desc:'Small impact crater less than 1 million years old in Western Australia. The circular iron meteorite crater is recognized from its raised rim and associated iron meteorite fragments in the sandy desert terrain.',
         note:''},

        {cat:'crater', name:'Boxhole — 0.17km', lat:-22.62, lng:135.2,
         desc:'Iron meteorite impact crater ~54,000 years old in the Northern Territory, Australia. Well-preserved circular structure with raised rim; iron meteorite fragments are distributed within and around the crater.',
         note:''},

        {cat:'crater', name:'Dalgaranga — 0.02km', lat:-27.63, lng:117.28,
         desc:'Tiny iron meteorite impact crater ~3,000 years old in Western Australia. At 21m diameter it is one of the smallest confirmed impact craters on Earth; mesosiderite meteorite fragments confirm the cosmic origin.',
         note:''},

        {cat:'crater', name:'Liverpool — 1.6km', lat:-12.4, lng:134.05,
         desc:'Impact structure ~150 million years old in the Northern Territory, Australia. Jurassic-age impact confirmed from shocked minerals; one of several craters in the Northern Territory clustered in ancient Precambrian and Mesozoic terrain.',
         note:''},

        {cat:'crater', name:'Suavjärvi — 16km', lat:63.12, lng:33.38,
         desc:'Ancient impact structure ~2.4 billion years old in Karelia, Russia. One of the oldest impact structures in the Fennoscandian Shield; recognized from shocked minerals and pseudotachylite in deeply eroded Archean terrain.',
         note:''},

        {cat:'crater', name:'Obolon — 20km', lat:49.35, lng:32.92,
         desc:'Buried impact structure ~169 million years old in Ukraine. Discovered through petroleum drilling; filled with Jurassic sediment. One of several Ukrainian impact structures recognized in the stable Precambrian basement.',
         note:''},

        {cat:'crater', name:'Ilyinets — 8.5km', lat:49.12, lng:29.1,
         desc:'Impact structure ~378 million years old in Vinnytsia Oblast, Ukraine. Devonian impact recognized from shock metamorphism features in the Ukrainian shield.',
         note:''},

        {cat:'crater', name:'Ust-Kara — 25km', lat:69.25, lng:65.17,
         desc:'Impact structure ~70 million years old on the Yugorsky Peninsula, Russia. Paired with the Kara crater; a doublet impact from a binary or fragmented asteroid that struck simultaneously at the end of the Cretaceous period.',
         note:'Twin to the Kara crater — binary impactor, simultaneous strike, end of the Cretaceous.'},

        {cat:'crater', name:'Ragozinka — 9km', lat:58.43, lng:62.0,
         desc:'Impact structure ~46 million years old in Sverdlovsk Oblast, Russia. Eocene-age impact in the Ural foreland basin.',
         note:''},

        {cat:'crater', name:'Logoisk — 17km', lat:54.2, lng:27.8,
         desc:'Buried impact structure ~42 million years old in Belarus. Eocene impact buried under sedimentary cover; recognized from drilling and geophysical surveys in the East European Platform.',
         note:''},

        {cat:'crater', name:'Mishina Gora — 4km', lat:58.72, lng:28.0,
         desc:'Small impact structure ~300 million years old in Pskov Oblast, Russia. Pennsylvanian-age crater recognized from drilling and geophysical surveys in northwestern Russia.',
         note:''},

        {cat:'crater', name:'Vepriai — 8km', lat:55.1, lng:24.6,
         desc:'Buried impact structure ~160 million years old in Lithuania. Jurassic impact crater buried under sedimentary cover; one of only a few confirmed impact structures in the Baltic countries.',
         note:''},

        {cat:'crater', name:'Saarijärvi — 1.5km', lat:65.28, lng:28.38,
         desc:'Small impact structure ~600 million years old in Oulu, Finland. Precambrian impact recognized from shocked quartz and circular morphology in Finnish bedrock.',
         note:''},

        {cat:'crater', name:'Karikkoselkä — 1.5km', lat:62.13, lng:25.22,
         desc:'Impact structure ~230 million years old in Central Finland. Triassic-age impact confirmed from planar deformation features in quartz in the Finnish crystalline shield.',
         note:''},

        {cat:'crater', name:'Soderfjardan — 6.6km', lat:63.02, lng:21.57,
         desc:'Impact structure ~600 million years old in Ostrobothnia, Finland. Precambrian crater now partially filled by a shallow coastal bay on the Finnish west coast.',
         note:''},

        {cat:'crater', name:'Santa Fe — 6km', lat:35.73, lng:-105.97,
         desc:'Deeply eroded ancient impact structure ~1.2 billion years old in New Mexico, USA. One of the oldest confirmed craters in North America; identified from shocked quartz and shatter cones in Proterozoic metamorphic rock near Santa Fe.',
         note:''},

        {cat:'crater', name:'Chubb (Pingualuit — listed separately)', lat:61.28, lng:-73.67,
         desc:'See Pingualuit entry. Originally called Chubb Crater when first reported to science in 1943; renamed Pingualuit (meaning "where the land rises" in Inuktitut) in recognition of Indigenous naming.',
         note:''},

        {cat:'crater', name:'Cloud Creek — 7km', lat:43.12, lng:-106.73,
         desc:'Buried impact structure ~190 million years old in Wyoming, USA. Jurassic-age impact hidden beneath the Wyoming plains; discovered from petroleum exploration drilling data.',
         note:''},

        {cat:'crater', name:'Cote Blanche — 4km', lat:29.7, lng:-91.5,
         desc:'Proposed impact structure in Louisiana, USA. Circular structure associated with a salt dome anomaly; status as confirmed impact structure remains under investigation.',
         note:''},

        {cat:'crater', name:'Ames — 16km', lat:36.25, lng:-98.18,
         desc:'Buried impact structure ~470 million years old in Oklahoma, USA. The Ames impact structure is the most economically significant impact crater in the United States — it hosts a major oil field, as hydrocarbons accumulated in the fractured impact rocks.',
         note:'The most economically important impact crater in the US — oil accumulated in the shattered rock of an ancient cosmic strike.'},

        {cat:'crater', name:'Avak — 12km', lat:71.25, lng:-156.45,
         desc:'Buried impact structure ~95 million years old in the Barrow area of Alaska, USA. Cretaceous impact buried under the North Slope; detected through petroleum exploration drilling.',
         note:''},

        {cat:'crater', name:'Charity Shoal — 1.3km', lat:43.97, lng:-76.97,
         desc:'Small impact structure ~450 million years old beneath Lake Ontario, Canada. Ordovician submarine crater recognized from side-scan sonar surveys of the lake bottom.',
         note:'Hidden beneath the waters of Lake Ontario — a cosmic strike submerged by glacial flooding.'},

        {cat:'crater', name:'Eagle Butte — 10km', lat:49.72, lng:-110.53,
         desc:'Buried impact structure ~65 Ma old in Alberta, Canada. Cretaceous-age impact crater buried under the Alberta plains; detected from geophysical surveys and well data.',
         note:''},

        {cat:'crater', name:'Mizarai — 5km', lat:54.02, lng:23.9,
         desc:'Buried impact structure ~500 million years old in Lithuania. Cambrian-age crater buried under sedimentary cover; one of a growing number of confirmed Baltic region impact structures.',
         note:''},

        {cat:'crater', name:'Newporte — 3.2km', lat:48.97, lng:-101.37,
         desc:'Buried impact structure ~500 million years old in North Dakota, USA. Cambrian-age impact recognized from drilling data; the circular breccia zone is buried hundreds of meters beneath the plains.',
         note:''},

        {cat:'crater', name:'Viewfield — 2.5km', lat:49.67, lng:-103.07,
         desc:'Buried impact structure ~190 million years old in Saskatchewan, Canada. Jurassic-age impact associated with oil production; hydrocarbons accumulate in the fractured impact breccia.',
         note:''},

        {cat:'crater', name:'Hotpoint — 10km (proposed)', lat:53.42, lng:-118.12,
         desc:'Proposed impact structure in Alberta, Canada. Circular structure under investigation; field work ongoing to confirm impact indicators.',
         note:''},

        {cat:'crater', name:'Calvin — 8.5km', lat:41.83, lng:-85.95,
         desc:'Buried impact structure ~450 million years old beneath southwestern Michigan, USA. Ordovician impact detected through petroleum well data; the fractured limestone hosts minor hydrocarbon accumulations.',
         note:''},

        {cat:'crater', name:'Crocodile Creek (Shoemaker) — listed above', lat:-25.87, lng:120.88,
         desc:'See Shoemaker (Teague Ring) entry. Eugene Shoemaker\'s connection to Australian crater research is commemorated in the renaming of this structure.',
         note:''},

        {cat:'crater', name:'Rouchechouart (Rochechouart) — 23km', lat:45.82, lng:0.78,
         desc:'See Rochechouart entry. French impact structure whose impactite was used in medieval construction throughout the Limousin region.',
         note:''},

        {cat:'crater', name:'Hiawatha — 31km', lat:78.7, lng:-66.5,
         desc:'Impact crater discovered in 2018 beneath the Greenland ice sheet, roughly 800,000 years old or possibly much younger (~13,000 years). The 31km crater was hidden under 1km of ice; if young, it may correlate with the Younger Dryas cooling event and oral traditions of catastrophe.',
         note:'A 31km crater hidden under the Greenland ice sheet — possibly connected to the Younger Dryas cosmic impact hypothesis and ancient catastrophe traditions.'},

        {cat:'crater', name:'Tunnunik — 7.5km', lat:72.47, lng:-113.94,
         desc:'Impact structure ~130 million years old on Victoria Island, Nunavut, Canada. Remote Arctic impact confirmed in 2014; the eroded structure is one of many Canadian Shield craters in the high Arctic.',
         note:''},

        {cat:'crater', name:'Ile Rouleau — 4km', lat:50.67, lng:-73.88,
         desc:'Impact structure ~300 million years old in Quebec, Canada. The circular island in the Caniapiscau Reservoir is the eroded remnant of a Carboniferous impact; one of many ring-shaped features on the Quebec-Labrador Shield.',
         note:''},

        {cat:'crater', name:'Marquez Dome — 1.8km', lat:31.28, lng:-96.3,
         desc:'Buried impact structure ~58 million years old in Leon County, Texas, USA. Paleocene impact associated with an oil-producing dome; one of the deeper buried Texas impact structures.',
         note:''},

        {cat:'crater', name:'Odessa — 0.17km', lat:31.75, lng:-102.47,
         desc:'Small iron meteorite crater ~63,000 years old in Ector County, Texas, USA. A cluster of small craters formed by an iron meteorite shower; the largest is 170m in diameter. Well-preserved in the dry Texas climate.',
         note:''},

        {cat:'crater', name:'Haviland — 0.015km', lat:37.58, lng:-99.1,
         desc:'Tiny iron meteorite crater in Kiowa County, Kansas, USA. At 15m diameter, one of the smallest confirmed craters in North America; associated with Brenham pallasite meteorite fragments still being recovered by farmers today.',
         note:'Farmers in Kansas still find pallasite meteorite fragments from this ancient iron shower — cosmic treasure in wheat country.'},

        {cat:'crater', name:'Wetumpka — 6.5km', lat:32.52, lng:-86.17,
         desc:'Impact structure ~83 million years old near Wetumpka, Alabama, USA. The City of Wetumpka (population ~7,000) is built inside the impact crater; the disturbed rim rocks form a curved ridge visible in the local topography.',
         note:'A city of 7,000 people built inside an impact crater — Wetumpka, Alabama sits in an 83-million-year-old cosmic bowl.'},

        {cat:'crater', name:'Glover Bluff — 3km', lat:43.97, lng:-89.52,
         desc:'Small impact structure ~500 million years old in Marquette County, Wisconsin, USA. Ordovician-age impact confirmed from shatter cones in dolomite; a quarry exposes the brecciated rocks.',
         note:''},

        {cat:'crater', name:'Rock Elm — 6km', lat:44.72, lng:-92.23,
         desc:'Buried impact structure ~450 million years old in Pierce County, Wisconsin, USA. Ordovician crater confirmed from shatter cones; the disturbed limestone is quarried locally.',
         note:''},

        {cat:'crater', name:'Des Plaines — 8km', lat:42.07, lng:-87.88,
         desc:'Buried impact structure ~280 million years old beneath Des Plaines, Illinois, USA. Deeply buried Pennsylvanian impact; the structure is entirely concealed under glacial sediment and urban development.',
         note:'A city of 60,000 sits unknowingly above an ancient impact crater — Des Plaines, Illinois.'},

        {cat:'crater', name:'Versailles — 0.1km', lat:38.68, lng:-84.67,
         desc:'Small impact structure in Woodford County, Kentucky, USA. One of several small suspected craters in the Kentucky-Ohio-Indiana karst region; confirmation details are limited.',
         note:''},


// ══════════════════════════════════════════════════════════════
// ── EXPANDED MEGALITHIC SITES ──
// Global megalithic distribution — evidence of worldwide pre-Flood/post-Babel
// building knowledge (Gen 4:20-22, Gen 11:8-9)
// ══════════════════════════════════════════════════════════════

        // ── ASIA ──
        {cat:'megalith', name:'Mohenjo-daro', lat:27.3244, lng:68.1357,
         desc:'Ancient Indus Valley city with advanced urban planning, grid streets, and a sewage system rivaling Rome — built around 2600 BC. Strikingly, no weapons of war have ever been found. Population estimated 40,000+.',
         refs:'Possible descendants of Arphaxad (Gen 10:22); pre-Babel urban tradition',
         note:'Rediscovered 1922; UNESCO World Heritage Site',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Mohenjodaro_Priesterkoenig.jpg/320px-Mohenjodaro_Priesterkoenig.jpg'},

        {cat:'megalith', name:'Dholavira', lat:23.887, lng:70.208,
         desc:'Indus Valley city on an island in the Rann of Kutch, India. Famous for its sophisticated water harvesting reservoirs and a large inscribed signboard — the only such inscription in the ancient world — written in undeciphered Indus script.',
         refs:'Indus civilization; contemporary with Abraham\'s era',
         note:'UNESCO World Heritage 2021; script still undeciphered',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Dholavira_-_the_great_bath.jpg/320px-Dholavira_-_the_great_bath.jpg'},

        {cat:'megalith', name:'Angkor Wat', lat:13.4125, lng:103.8670,
         desc:'Largest religious monument on earth, built in the 12th century AD by the Khmer Empire. The temple complex is astronomically aligned to the spring equinox and encodes the Hindu cosmological timeline in its architecture.',
         refs:'Tower of Babel echoes — monumental temple-mountain cosmology (Gen 11:4)',
         note:'Originally Hindu, converted to Buddhist; covers 401 acres',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Angkor_Wat_temple.jpg/320px-Angkor_Wat_temple.jpg'},

        {cat:'megalith', name:'Angkor Thom', lat:13.4412, lng:103.8575,
         desc:'Royal city of the Khmer Empire, featuring the Bayon temple with 54 towers each carved with four giant serene faces. Covers 9 square kilometers and once housed a million people — making it the world\'s largest pre-industrial city.',
         refs:'Face-tower cosmology parallels divine-king theology; Babel parallels (Gen 11)',
         note:'Built by Jayavarman VII, ~1190 AD',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Bayon_temple_angkor_thom.jpg/320px-Bayon_temple_angkor_thom.jpg'},

        {cat:'megalith', name:'Sigiriya', lat:7.957, lng:80.76,
         desc:'A 200-meter-high rock fortress in Sri Lanka built by King Kashyapa around 477 AD. Features advanced water gardens, frescoed galleries, and a lion-paw gateway at the summit. Still considered an engineering marvel.',
         refs:'Mountain-top strongholds as defensive and symbolic (Ps 18:2; Obad 1:3)',
         note:'One of best-preserved examples of ancient urban planning in Asia',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Sigiriya_rock_fortress.jpg/320px-Sigiriya_rock_fortress.jpg'},

        {cat:'megalith', name:'Plain of Jars', lat:19.4597, lng:103.1572,
         desc:'Thousands of massive stone and sandstone jars — up to 3 meters tall and 1 ton each — scattered across the Laos plateau. Purpose is unknown. Local legend says they were made by giants to brew rice wine for an ancient king.',
         refs:'Giant vessels; local giant traditions echo Nephilim lore (Num 13:33)',
         note:'Dating uncertain; some as old as 500 BC',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Plain_of_Jars.jpg/320px-Plain_of_Jars.jpg'},

        {cat:'megalith', name:'Bada Valley Megaliths', lat:-1.9375, lng:120.1856,
         desc:'Sulawesi, Indonesia. Large stone anthropomorphic statues (up to 4.5m tall) and cylindrical stone cisterns called kalamba scatter the remote Bada Valley. Builders and purpose are completely unknown.',
         refs:'Isolated megalith builders worldwide — post-Babel dispersal (Gen 11:8-9)',
         note:'Some statues resemble South American style, prompting diffusion theories',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Palindo_statue_Bada_Valley.jpg/320px-Palindo_statue_Bada_Valley.jpg'},

        {cat:'megalith', name:'Korean Dolmens — Gochang', lat:35.43, lng:126.92,
         desc:'South Korea contains over 30,000 dolmens — approximately 40% of all dolmens on Earth. The Gochang cluster is UNESCO-listed and features massive table-top capstones weighing up to 300 tons placed on support stones.',
         refs:'Megalithic burial culture; worldwide dolmen tradition from unknown common origin',
         note:'UNESCO World Heritage 2000',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Korea-Gochang-Dolmens-01.jpg/320px-Korea-Gochang-Dolmens-01.jpg'},

        {cat:'megalith', name:'Korean Dolmens — Hwasun', lat:34.98, lng:127.0,
         desc:'A dense UNESCO-listed cluster of dolmens in South Korea showing the full sequence from quarry to finished monument. Capstones up to 280 tons. The sheer density suggests a highly organized dolmen-building culture.',
         refs:'Post-Babel building traditions spreading east (Gen 11:8)',
         note:'UNESCO World Heritage 2000 alongside Gochang and Ganghwa'},

        {cat:'megalith', name:'Korean Dolmens — Ganghwa', lat:37.75, lng:126.43,
         desc:'Northern-style dolmens on Ganghwa Island, South Korea, featuring enormous capstones resting directly on the ground without support stones. One capstone weighs an estimated 53 tons. The largest of Korea\'s UNESCO dolmen sites.',
         refs:'Megalithic tradition; builders unknown, ~1000 BC',
         note:'UNESCO World Heritage 2000'},

        {cat:'megalith', name:'Oyu Stone Circles (Jomon)', lat:40.27, lng:140.80,
         desc:'Two concentric stone circles at Oyu, Japan, dating to ~2000 BC. The Jomon period site includes a "sundial stone" and is one of the oldest known astronomical monuments in East Asia. Predates any Chinese written records.',
         refs:'Jomon culture; astronomical knowledge in the east (Isa 41:25)',
         note:'National Historic Site of Japan; Jomon culture lasted 14,000 years'},

        {cat:'megalith', name:'Asuka Masuda-no-Iwafune', lat:34.47, lng:135.80,
         desc:'A massive granite boulder in Asuka, Japan, carved with geometric precision into a grid of rectangular hollows. Purpose is entirely unknown — theories range from astronomical instrument to ritual bathing vessel to royal tomb.',
         refs:'Mysterious carved stones of unknown purpose; Asuka era Japan, ~600 AD',
         note:'Several enigmatic carved stones cluster in the Asuka region of Nara Prefecture'},

        {cat:'megalith', name:'Sanchi Stupa', lat:23.4793, lng:77.7397,
         desc:'India\'s oldest stone structure, commissioned by Emperor Ashoka in the 3rd century BC. The Great Stupa\'s elaborately carved gateways (toranas) record Buddhist teachings in stone with extraordinary artistry.',
         refs:'Buddhist monument; Ashoka\'s conversion and empire parallel Cyrus-type figures (Isa 45:1)',
         note:'UNESCO World Heritage; inspired by earlier mud-brick stupa tradition',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Sanchi_Stupa_from_south_eastern_gateway.jpg/320px-Sanchi_Stupa_from_south_eastern_gateway.jpg'},

        {cat:'megalith', name:'Hampi', lat:15.335, lng:76.46,
         desc:'Ruins of Vijayanagara, the last great Hindu empire\'s capital in Karnataka, India. The site is famous for massive naturally balanced granite boulders integrated into temple architecture, and for the Vittala Temple\'s musical stone pillars.',
         refs:'Royal city ruins; Vijayanagara fell 1565 AD (Lam 1:1)',
         note:'UNESCO World Heritage; granite boulders some of the largest natural formations in the world'},

        {cat:'megalith', name:'Mahabalipuram Shore Temple', lat:12.6169, lng:80.1993,
         desc:'Tamil Nadu, India. Shore Temple carved from solid granite, rathas (chariots) hewn from single outcroppings of rock, and Krishna\'s Butter Ball — a 250-ton boulder balanced on a small surface area defying physics. Local tradition says the gods placed it.',
         refs:'Rock-cut architecture; divine-giant stones (compare Goliath\'s armor weight — 1 Sam 17)',
         note:'UNESCO World Heritage; partially submerged structures suggest ancient higher occupation'},

        {cat:'megalith', name:'Khajuraho Temples', lat:24.8318, lng:79.9199,
         desc:'A cluster of 85 medieval Hindu and Jain temples in Madhya Pradesh, India, built between 950-1050 AD. Famous for their extraordinary sculptural program and interlocking stone precision — no mortar was used in construction.',
         refs:'Temple architecture traditions; stone-carving mastery (1 Chr 22:15)',
         note:'UNESCO World Heritage; originally 85 temples, 22 survive'},

        {cat:'megalith', name:'Kailasa Temple, Ellora', lat:20.0258, lng:75.1780,
         desc:'The largest monolithic rock excavation in the world — carved TOP-DOWN from a single cliff face in Maharashtra, India. Over 200,000 tons of rock were removed to create this multi-story temple dedicated to Shiva. How 8th-century workers achieved this remains astonishing.',
         refs:'Compare: God\'s command to Moses for the Tabernacle (Exod 25:9); divine instruction in impossible construction',
         note:'Ellora Cave 16; the entire temple is one solid rock',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Kailash_Temple_Ellora.jpg/320px-Kailash_Temple_Ellora.jpg'},

        {cat:'megalith', name:'Ajanta Caves', lat:20.5519, lng:75.7033,
         desc:'Thirty Buddhist rock-cut cave temples in Maharashtra, India, dating from the 2nd century BC to 480 AD. The caves preserve some of the world\'s most sophisticated ancient paintings and sculpture, abandoned and lost to the jungle for over 1,400 years.',
         refs:'Rock sanctuaries; Elijah\'s cave retreat (1 Kgs 19:9); hiding in dens (Heb 11:38)',
         note:'UNESCO World Heritage; rediscovered by British officer in 1819'},

        {cat:'megalith', name:'Arkaim', lat:52.65, lng:59.57,
         desc:'A 4,000-year-old circular Bronze Age settlement in the Russian steppe near the Ural Mountains. The concentric rings of buildings align astronomically and the city was deliberately burned and abandoned. Called the "Russian Stonehenge."',
         refs:'Nomadic/settled interface; post-Babel dispersal into the north (Gen 10:2-3)',
         note:'Sintashta culture; contemporary with Abraham; discovered 1987, nearly flooded by reservoir',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Arkaim_aerial.jpg/320px-Arkaim_aerial.jpg'},

        {cat:'megalith', name:'Caucasus Dolmens', lat:44.0, lng:40.2,
         desc:'Thousands of precisely built stone box structures (dolmens) in the Caucasus Mountains of Russia, dating to ~3500–1400 BC. Some have perfectly round port-holes drilled through the front slab. Local legend calls them "houses of dwarfs" built by giants.',
         refs:'Giant builders in the region between the Black and Caspian Seas; Gomer/Magog territory (Gen 10:2)',
         note:'Over 3,000 known; largely unstudied by Western archaeologists'},

        {cat:'megalith', name:'Externsteine', lat:51.8686, lng:8.9164,
         desc:'A dramatic formation of sandstone pillars in the Teutoburg Forest of Germany, used as a sacred site from prehistoric times through the medieval period. Rock-cut chambers, a relief of the Descent from the Cross, and possible solar alignments suggest layered use over millennia.',
         refs:'Sacred high places; Elijah\'s confrontation at Carmel (1 Kgs 18:19); groves and standing stones (Deut 12:3)',
         note:'Possible pre-Christian Germanic sacred site; carvings added ~1115 AD'},

        {cat:'megalith', name:'Goseck Circle', lat:51.1983, lng:11.8622,
         desc:'A circular enclosure near Goseck, Germany, dating to ~4900 BC — possibly the oldest known solar observatory in Europe. Two gate openings align precisely with the winter solstice sunrise and sunset. Predates Stonehenge by 2,000 years.',
         refs:'Prehistoric solar tracking; Gen 1:14 — lights for signs and seasons',
         note:'Reconstructed 2005; part of a widespread Central European "circular enclosure" culture',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Goseck_circle_aerial.jpg/320px-Goseck_circle_aerial.jpg'},

        {cat:'megalith', name:'Drombeg Stone Circle', lat:51.5644, lng:-9.0867,
         desc:'A recumbent stone circle on the Cork coast of Ireland, ~150 BC. The recumbent stone and its two flankers frame the setting sun precisely on the winter solstice. A nearby fulacht fiadh (cooking pit) dates to the same period.',
         refs:'Seasonal markers; appointed times (Lev 23:2)',
         note:'One of the best-preserved stone circles in Ireland'},

        {cat:'megalith', name:'Brú na Bóinne — Knowth', lat:53.7017, lng:-6.4922,
         desc:'A massive Neolithic passage tomb near Newgrange in Ireland, built ~3200 BC, containing the largest collection of megalithic art in all of Europe — over a third of all known Western European megalithic art on a single mound. Two passages align to the equinoxes.',
         refs:'Passage tombs; resurrection hope; "sleeping in the earth" (Dan 12:2)',
         note:'UNESCO World Heritage with Newgrange and Dowth'},

        {cat:'megalith', name:'Skara Brae', lat:59.0487, lng:-3.3418,
         desc:'A remarkably preserved Neolithic stone village on Orkney, Scotland, occupied from 3180–2500 BC. Stone furniture, beds, shelves, and a drainage system survive intact. Abandoned suddenly — some speculate a catastrophe. Older than Stonehenge and the Egyptian pyramids.',
         refs:'Pre-Flood sophistication; God\'s provision of building knowledge (Gen 4:17)',
         note:'UNESCO World Heritage; preserved under sand dunes for millennia',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Skara_Brae_main_structure.jpg/320px-Skara_Brae_main_structure.jpg'},

        {cat:'megalith', name:'Ales Stenar', lat:55.3833, lng:14.0533,
         desc:'A ship-shaped setting of 59 stones stretching 67 meters on a clifftop in Scania, Sweden, dating to ~600 AD. The bow and stern stones align to the summer and winter solstice sunrises. The largest stone ship in Scandinavia.',
         refs:'Viking/Germanic cosmology; ship burial tradition; Ezek 27 — Tyre\'s ship imagery',
         note:'Sometimes called the "Swedish Stonehenge"; built by Norse-era peoples'},

        {cat:'megalith', name:'Hunebedden', lat:52.9, lng:6.87,
         desc:'Fifty-four dolmen burial chambers in the northeastern Netherlands, built ~5000 years ago — the only megaliths in the country. Constructed from boulders deposited by glaciers from Scandinavia. Local legend calls them houses of the Hunnen (giants).',
         refs:'Dolmen tradition; giant lore applied to megalithic builders (Num 13:33)',
         note:'The name Hunebedden means "giant\'s beds" in Dutch'},

        {cat:'megalith', name:'Antequera Dolmens', lat:37.0239, lng:-4.5475,
         desc:'Three megalithic tombs near Antequera, Spain — Menga, Viera, and El Romeral — dating to 3750 BC. Menga\'s capstones reach 180 tons and its central pillar is one of the largest stones in any European megalith. The chamber aligns to a distant mountain peak at sunrise.',
         refs:'Monumental tombs; stone sepulchres (Matt 27:60)',
         note:'UNESCO World Heritage 2016'},

        // ── EUROPE / MIDDLE EAST ──
        {cat:'megalith', name:'Tiryns', lat:37.5989, lng:22.7989,
         desc:'Mycenaean citadel in the Greek Peloponnese with walls built from massive limestone blocks up to 8 tons each. Ancient Greeks called it "Cyclopean" masonry — believing only the one-eyed giants called Cyclopes could have moved such stones. Homer called Tiryns "well-walled."',
         refs:'Rephaim and Anakim as mighty builders; Og of Bashan\'s iron bed (Deut 3:11)',
         note:'Walls survive up to 7m thick; contemporary with the Judges period',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Tiryns_cyclopean_walls.jpg/320px-Tiryns_cyclopean_walls.jpg'},

        {cat:'megalith', name:'Mycenae', lat:37.7306, lng:22.7561,
         desc:'Bronze Age citadel of the Mycenaean civilization, featuring the famous Lion Gate — the only large-scale relief sculpture to survive from prehistoric Greece — and the Treasury of Atreus, a corbelled beehive tomb of extraordinary precision. Cyclopean masonry throughout.',
         refs:'Contemporaneous with the period of the Judges; Philistine-Aegean connections (Amos 9:7)',
         note:'UNESCO World Heritage; destroyed ~1200 BC in the Bronze Age Collapse',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Mycenae_lion_gate.jpg/320px-Mycenae_lion_gate.jpg'},

        {cat:'pyramid', name:'Pyramids of Güímar', lat:28.3258, lng:-16.3836,
         desc:'Six step pyramids on Tenerife in the Canary Islands, aligned to the summer solstice sunrise and sunset. Thor Heyerdahl argued they were pre-Columbian stepping stones between Egypt and the Americas. Local builders unknown.',
         refs:'Atlantic stepping-stone civilizations; Table of Nations dispersal (Gen 10)',
         note:'Heyerdahl established a research center here; similar structures in Lanzarote and Madeira',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Piramides_de_G%C3%BC%C3%ADmar.jpg/320px-Piramides_de_G%C3%BC%C3%ADmar.jpg'},

        {cat:'megalith', name:'Menhir de Champ-Dolent', lat:48.4417, lng:-1.7519,
         desc:'One of the tallest surviving menhirs in France at 9.5 meters, standing alone in a field near Dol-de-Bretagne, Brittany. Breton legend says it was hurled from the sky to stop a battle between two brothers, and that it sinks a centimeter each century.',
         refs:'Standing stones as memorials (Gen 28:18; 1 Sam 7:12); legendary origins of megaliths',
         note:'Granite; estimated weight 150 tons'},

        {cat:'megalith', name:'Grand Menhir Brisé, Locmariaquer', lat:47.5714, lng:-2.9461,
         desc:'The heaviest prehistoric standing stone ever erected in Europe — 20.6 meters tall and ~330 tons when intact. It now lies broken in four pieces. Originally part of a Neolithic alignment at Locmariaquer, Brittany, ~4700 BC.',
         refs:'Monumental standing stones; the LORD who alone stretches out the heavens can topple the proudest works (Job 9:5)',
         note:'How Neolithic people moved this stone 10+ km from its quarry remains unexplained'},

        {cat:'megalith', name:'West Kennet Long Barrow', lat:51.4086, lng:-1.8517,
         desc:'A 100-meter-long Neolithic chambered tomb near Avebury, England, built ~3650 BC and used for collective burial for over a thousand years. Enormous sarsen stones seal the forecourt. The largest Neolithic long barrow in England.',
         refs:'Ancestral veneration; corporate burial (Acts 13:36 — "fell asleep and was buried")',
         note:'Bodies were curated and rearranged; bones of at least 46 individuals found',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/West_Kennet_Long_Barrow_-_geograph.org.uk_-_1618498.jpg/320px-West_Kennet_Long_Barrow_-_geograph.org.uk_-_1618498.jpg'},

        {cat:'megalith', name:'Silbury Hill', lat:51.4158, lng:-1.8572,
         desc:'The largest prehistoric artificial mound in Europe, rising 40 meters from the Wiltshire plain near Avebury, built ~2400 BC. It contains no burial. Despite centuries of tunneling, its purpose remains completely unknown. It is as tall as a 12-story building.',
         refs:'High places; unexplained sacred mounds (Mic 1:5)',
         note:'Contemporary with Stonehenge; built in stages over many generations',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Silbury_Hill_wiltshire.jpg/320px-Silbury_Hill_wiltshire.jpg'},

        {cat:'megalith', name:'Harbetsuvan Tepesi', lat:37.25, lng:39.3,
         desc:'A recently discovered site near Göbekli Tepe in Turkey with similar T-shaped limestone pillars and iconography. Less excavated than its famous neighbor, it suggests a wider culture of pillar-building across the pre-pottery Neolithic.',
         refs:'Göbekli Tepe\'s "sister site"; pre-agricultural monumental building (Gen 4:17)',
         note:'Excavations ongoing; may predate Göbekli Tepe\'s main layer'},

        // ── AFRICA ──
        {cat:'megalith', name:'Great Zimbabwe', lat:-20.2674, lng:30.9339,
         desc:'A massive stone city in southern Zimbabwe built without mortar between the 11th and 15th centuries AD. The Great Enclosure\'s walls reach 11 meters high and 5 meters thick. It was the capital of the Munhumutapa empire and a major gold trade hub.',
         refs:'African stone-city tradition; Sheba\'s gold trade (1 Kgs 10:1-2; Gold from Ophir)',
         note:'The name Zimbabwe means "great stone houses" in Shona',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Great-Zimbabwe.jpg/320px-Great-Zimbabwe.jpg'},

        {cat:'megalith', name:'Mzora Stone Circle', lat:35.4, lng:-5.93,
         desc:'An elliptical ring of 168 standing stones in northern Morocco, 55 meters across, with precise astronomical alignments. Berber tradition calls it the tomb of the giant Antaeus, whom Hercules defeated. The layout shares precise geometric ratios with British stone circles.',
         refs:'Giant traditions across the Mediterranean; Goliath\'s lineage (2 Sam 21:15-22)',
         note:'Connection to Atlantis theories; geometry matches Avebury sub-circles',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Cromlech_of_Mzoura.jpg/320px-Cromlech_of_Mzoura.jpg'},

        {cat:'pyramid', name:'Nubian Pyramids — Meroe', lat:16.9381, lng:33.7536,
         desc:'Sudan contains over 200 pyramids — more than Egypt — built by the Kushite kingdom of Kush and Nubia between 700 BC and 350 AD. Steeper and narrower than Egyptian pyramids, they demonstrate an independent pyramid-building tradition that outlasted Egypt\'s by centuries.',
         refs:'Kush (Cush, Gen 10:6); Queen of Ethiopia (Acts 8:27); Put and Cush (Ezek 38:5)',
         note:'UNESCO World Heritage; many destroyed by treasure hunter Giuseppe Ferlini in the 1830s',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Meroe_Pyramids_23dec2006_sudan.jpg/320px-Meroe_Pyramids_23dec2006_sudan.jpg'},

        {cat:'megalith', name:'Lalibela Rock-Hewn Churches', lat:12.0319, lng:39.0472,
         desc:'Eleven medieval monolithic churches in Ethiopia carved entirely from solid red volcanic rock, built in the 12th-13th centuries AD under King Lalibela. Ethiopian tradition holds that angels worked through the night to complete what humans built by day.',
         refs:'Ethiopian Christian tradition; the eunuch\'s faith (Acts 8:27); Zion theology (Ps 48)',
         note:'Still an active pilgrimage site; largest monolithic church is Bete Medhane Alem',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Lalibela_-_Bete_Giyorgis_01.jpg/320px-Lalibela_-_Bete_Giyorgis_01.jpg'},

        {cat:'megalith', name:'Aksum Stelae', lat:14.1308, lng:38.7197,
         desc:'Massive granite obelisks in Aksum, Ethiopia, up to 33 meters tall and weighing 520 tons, carved to resemble multi-story buildings. The Aksumite kingdom claimed to house the Ark of the Covenant and traced its lineage to Solomon and the Queen of Sheba.',
         refs:'Queen of Sheba (1 Kgs 10; Matt 12:42); Ark tradition; Solomonic covenant',
         note:'One obelisk was stolen by Mussolini and returned to Ethiopia in 2005',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Aksum_stelae_8.jpg/320px-Aksum_stelae_8.jpg'},

        {cat:'megalith', name:'Tassili n\'Ajjer', lat:25.5, lng:9.0,
         desc:'A vast plateau in Algeria containing tens of thousands of rock art engravings and paintings, some 10,000 years old. Images of swimmers, cattle herders, and mysterious "roundhead" humanoid figures with globular heads. Evidence the Sahara was once a fertile savanna.',
         refs:'Post-Flood Mediterranean; the spreading of peoples (Gen 10:25 — "in his days the earth was divided")',
         note:'UNESCO World Heritage; "roundhead" figures dated 10,000-8,000 BP — identity debated',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Tassili_n_Ajjer_-_Algeria.jpg/320px-Tassili_n_Ajjer_-_Algeria.jpg'},

        {cat:'megalith', name:'Laas Geel Cave Art', lat:9.78, lng:44.47,
         desc:'A complex of cave shelters near Hargeisa, Somalia, containing some of the best-preserved prehistoric rock art in Africa — vivid polychrome paintings of cattle and humans dating to 9,000–3,000 BC. Discovered by French archaeologists in 2002.',
         refs:'East African peoples; descendants of Cush and Put (Gen 10:6-7)',
         note:'Largely unknown internationally due to political instability in the region'},

        {cat:'megalith', name:'Saloum Delta Shell Mounds', lat:13.8, lng:-16.7,
         desc:'218 artificial shell mounds in the Saloum Delta, Senegal, some reaching 20 meters high, built from shells and used as burial sites over a 2,100-year period (500 BC–1600 AD). One of West Africa\'s largest ancient monument complexes.',
         refs:'West African burial traditions; descendants of Ham\'s line in Africa (Gen 10:6)',
         note:'UNESCO World Heritage 2011; the mounds create a unique island landscape'},

        {cat:'megalith', name:'Tengouennet Stone Monuments', lat:24.9, lng:3.5,
         desc:'Massive stone funerary monuments and cairns scattered across the Algerian Sahara, dating to when the region was fertile savanna. Part of the broader Saharan megalithic tradition that flourished before desertification drove populations northward and eastward.',
         refs:'Saharan green period; divine judgment through climate (Ps 107:33-34)',
         note:'Little-studied; overlaps with the Garamantian civilization'},

        // ── AMERICAS ──
        {cat:'megalith', name:'Chichen Itza', lat:20.6843, lng:-88.5678,
         desc:'The great Maya city in the Yucatan, Mexico, dominated by El Castillo pyramid. At each equinox, the setting sun casts a shadow of a descending serpent down the pyramid\'s staircase — a masterpiece of astronomical architecture. The ballcourt is the largest in Mesoamerica.',
         refs:'Serpent iconography; feathered serpent Quetzalcoatl as messianic figure (compare Num 21:9)',
         note:'UNESCO World Heritage; one of the New Seven Wonders of the World',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/KukuLkan.jpg/320px-KukuLkan.jpg'},

        {cat:'megalith', name:'Palenque', lat:17.4839, lng:-92.0461,
         desc:'A Classic Maya city in Chiapas, Mexico, famous for the Temple of Inscriptions — a pyramid containing the elaborately carved sarcophagus of King Pakal. The sarcophagus lid\'s imagery was controversially interpreted as an astronaut in a rocket, though scholars read it as a cosmic tree descent.',
         refs:'Royal burial theology; the king as cosmic axis (compare Ezek 28:12-14)',
         note:'UNESCO World Heritage; hieroglyphic texts here are among the longest in Maya script',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Palenque_templo.jpg/320px-Palenque_templo.jpg'},

        {cat:'megalith', name:'Monte Albán', lat:17.0444, lng:-96.7683,
         desc:'Zapotec mountain-top city in Oaxaca, Mexico, built ~500 BC. The site includes a structure aligned not to cardinal directions but to the setting of the star Capella — an astronomical pointer. The "danzante" carvings may depict war captives or possibly human sacrifice victims.',
         refs:'Mountain-top kingdoms (Amos 4:13); building on summits (Ps 48:1)',
         note:'UNESCO World Heritage; capital of Zapotec civilization for ~1,300 years'},

        {cat:'megalith', name:'Tula — Toltec Atlanteans', lat:20.065, lng:-99.3406,
         desc:'The Toltec capital north of Mexico City, featuring four massive 4.6-meter warrior columns called "Atlanteans" — stone sentinels that once held up the roof of a temple. The Toltec were predecessors of the Aztec, and Tula\'s fall was lamented as the end of a golden age.',
         refs:'Stone guardians; cherubim at the temple (1 Kgs 6:23-28); giant warrior imagery',
         note:'Aztec tradition called Tula the origin of all arts and civilization'},

        {cat:'megalith', name:'Chan Chan', lat:-8.1064, lng:-79.0747,
         desc:'The largest adobe city in the pre-Columbian Americas, built by the Chimú civilization near Trujillo, Peru (~900–1470 AD). Its nine royal compounds feature elaborate geometric and marine-life friezes covering vast walls. At its height, 30,000+ people lived here.',
         refs:'Pre-Inca civilization; adobe construction (compare Exod 1:14)',
         note:'UNESCO World Heritage; threatened by El Niño flooding and erosion'},

        {cat:'megalith', name:'Nazca Lines', lat:-14.735, lng:-75.13,
         desc:'Enormous geoglyphs etched into the Nazca plateau of southern Peru — spider, hummingbird, monkey, condor, and humanoid "astronaut" figures visible only from the air. Made by the Nazca culture ~500 BC–500 AD. For whom they were made — human or divine observers — remains debated.',
         refs:'Heavenly watchers (Zech 1:10-11); "sons of God" who observe the earth (Job 1:6-7)',
         note:'UNESCO World Heritage; the lines are made by removing the reddish pebbles to expose lighter ground',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Nazca_-_L%C3%ADneas_de_Nazca_C01.jpg/320px-Nazca_-_L%C3%ADneas_de_Nazca_C01.jpg'},

        {cat:'pyramid', name:'Caral (Norte Chico)', lat:-10.8919, lng:-77.5206,
         desc:'The oldest known city in the Americas, built by the Norte Chico civilization ~2600 BC — exactly contemporary with the early Egyptian pyramids. Features multiple platform mounds, circular plazas, and evidence of a complex society. Remarkably, no weapons and no evidence of warfare.',
         refs:'Simultaneous pyramid-building on multiple continents; post-Babel civilization (Gen 11:8-9)',
         note:'UNESCO World Heritage; suggests independent but parallel civilizational development',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Caral-5.jpg/320px-Caral-5.jpg'},

        {cat:'megalith', name:'Ingapirca', lat:-2.5469, lng:-78.8778,
         desc:'The largest Inca ruins in Ecuador, featuring a Temple of the Sun built with the characteristic Inca style of fitted stonework without mortar. The elliptical main structure aligns to the solstices. Built ~1400 AD, it incorporated an earlier Cañari sacred site.',
         refs:'Inca solar worship; Inca as sun-worshippers; compare Ezek 8:16',
         note:'The name means "Inca wall" in Quechua'},

        {cat:'megalith', name:'Tikal', lat:17.2220, lng:-89.6237,
         desc:'One of the most powerful Maya city-states in the lowland jungle of Guatemala. Temple IV rises 65 meters above the jungle canopy and was the tallest building in the pre-Columbian Americas. At its peak (~700 AD) the population was 90,000. Featured in Star Wars as the Rebel Base.',
         refs:'Jungle city; the cedar of Lebanon as a great empire parable (Ezek 17:22-23)',
         note:'UNESCO World Heritage; massive complex still largely unexcavated under the jungle',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Tikal_-_Temple_IV.jpg/320px-Tikal_-_Temple_IV.jpg'},

        {cat:'megalith', name:'Copán', lat:14.8386, lng:-89.1403,
         desc:'Maya city in Honduras famous for its extraordinary stelae (elaborately carved portrait monuments) and the Hieroglyphic Stairway — 63 steps with over 2,500 glyphs, the longest single Maya inscription. The sculptural artistry surpasses all other Maya sites.',
         refs:'Stone inscription traditions (Deut 27:8; Hab 2:2)',
         note:'UNESCO World Heritage; royal dynasty of 16 kings recorded; site abandoned ~820 AD'},

        {cat:'megalith', name:'Moray Terraces', lat:-13.3278, lng:-72.1992,
         desc:'Concentric circular terraces built by the Inca in a natural depression in Peru\'s Sacred Valley. The temperature difference between the top and bottom rings is 15°C, creating microclimate zones that may have served as an agricultural laboratory for acclimatizing crops from different altitudes.',
         refs:'Inca agricultural ingenuity; stewardship of creation (Gen 2:15)',
         note:'The precise drainage system beneath keeps the terraces from flooding'},

        {cat:'megalith', name:'Tiwanaku', lat:-16.5536, lng:-68.6726,
         desc:'Pre-Inca ceremonial city on the Bolivian altiplano at 12,500 feet elevation, featuring the Gateway of the Sun with its weeping deity and interlocking precision-fitted H-shaped stone blocks. Local Aymara tradition holds it was built by giants in a single night before the dawn of the sun.',
         refs:'Giant building traditions (Gen 6:4); high-place construction; "Gateway" cosmology (Gen 28:17)',
         note:'Predates the Inca by centuries; Lake Titicaca nearby; precise stone fitting without mortar', img:'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Zonnepoort_tridge.jpg/320px-Zonnepoort_tridge.jpg'},

        // ── OCEANIA / PACIFIC ──
        {cat:'megalith', name:'Ha\'amonga \'a Maui', lat:-21.1364, lng:-175.0561,
         desc:'A massive coral-stone trilithon on Tonga (two upright slabs with a lintel, like Stonehenge) built ~1200 AD by Taufa\'ahau Tuitou, the 11th Tu\'i Tonga king. The lintel has carved notches that align to the summer solstice sunrise. Local name means "Burden of Maui."',
         refs:'Trilithon architecture on six continents; post-Babel Pacific dispersal (Gen 10)',
         note:'The upright stones are 5m tall; the coral blocks weigh ~40 tons each'},

        {cat:'megalith', name:'Lelu Ruins, Kosrae', lat:5.3370, lng:163.0180,
         desc:'A massive complex of basalt-walled compounds on the island of Kosrae, Micronesia, built between 1250–1400 AD. Some basalt walls reach 9 meters high. Like Nan Madol, the stones were transported by canoe across open water — though how is unclear.',
         refs:'Pacific megalithic traditions; island-hopping post-Babel descendants (Gen 10)',
         note:'Far less studied than Nan Madol; sometimes called "Nan Madol of the east"'},

        {cat:'megalith', name:'Pulemelei Mound, Samoa', lat:-13.7389, lng:-172.3356,
         desc:'The largest ancient structure in all of Polynesia — a massive four-tiered stone pyramid platform in Samoa, 65m × 60m at the base and 12m high. It sits in the jungle largely unexplored. Its purpose and builders within Samoan tradition are debated.',
         refs:'Pacific pyramid platform; Polynesian dispersal (Gen 10); "ends of the earth" (Ps 22:27)',
         note:'Overgrown and remote; only preliminary archaeological work done'},

        {cat:'megalith', name:'Wurdi Youang', lat:-37.85, lng:144.35,
         desc:'An Aboriginal Australian stone arrangement near Ballarat, Victoria, featuring a large egg-shaped ring of basalt stones with western-facing notches that mark the solstices and equinoxes. Astronomical knowledge encoded in stone by Australian Aboriginal peoples possibly 11,000+ years ago.',
         refs:'Gen 1:14 — lights for signs and seasons; indigenous astronomical tradition',
         note:'Wathaurong Aboriginal people; if dates confirmed, among the oldest astronomical monuments on Earth'},

// ══════════════════════════════════════════════════════════════
// ── ANOMALOUS SITES & INDIGENOUS TRADITIONS ──
// "He made from one man every nation of mankind to live on all
//  the face of the earth" — Acts 17:26
// ══════════════════════════════════════════════════════════════

        {cat:'anomaly', name:'Richat Structure (Eye of the Sahara)', lat:21.12, lng:-11.40,
         desc:'Massive 40km-wide circular geological formation in the Sahara Desert. Initially attributed to meteorite impact, now thought to be a deeply eroded geological dome. Some researchers (including Randall Carlson and Jimmy Corsetti) have proposed this as the site of Atlantis described by Plato, citing its concentric ring pattern, precise measurements matching Plato\'s account, and location west of the "Pillars of Hercules."',
         note:'Whether or not the Atlantis hypothesis holds, the perfectly concentric rings spanning 40km are genuinely remarkable. The structure is visible from space and was used as a landmark by early astronauts.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Richat_Structure_-_ASTER_%282001%29.jpg/320px-Richat_Structure_-_ASTER_%282001%29.jpg'},

        {cat:'anomaly', name:'Alaska Bone Yard', lat:64.84, lng:-147.72,
         desc:'In the permafrost around Fairbanks, explorers and miners have found massive deposits of broken, twisted animal bones from mammoths, bison, horses, and other Pleistocene megafauna — violently shattered and mixed with tree fragments and volcanic ash, as if destroyed by a catastrophic event. The bones are not in natural death assemblages but appear to have been violently tumbled and deposited together.',
         note:'The violence of the bone deposits is inconsistent with gradual extinction. Something catastrophic and sudden appears to have killed and tumbled these animals. Gold miners reported finding entire hillsides of broken bones mixed with muck.'},

        {cat:'anomaly', name:'White Sands Footprints', lat:32.78, lng:-106.17,
         desc:'In 2021, researchers confirmed human footprints at White Sands National Park dating to 21,000-23,000 years ago — thousands of years older than the previously accepted timeline for human arrival in the Americas. The prints show adults, teenagers, and children walking near an ancient lake. This discovery forced a complete rethinking of when and how humans reached the Americas.',
         note:'Published in Science (2021). These footprints predate the Clovis culture by 10,000+ years. The evidence keeps pushing human history deeper into the past — matching a biblical framework where humanity was advanced from the beginning (Gen 4:20-22).'},

        {cat:'anomaly', name:'Younger Dryas Impact Sites', lat:34.0, lng:-118.0,
         desc:'Around 12,800 years ago, something catastrophic struck Earth. A "black mat" layer containing nanodiamonds, iridium, magnetic spherules, and soot has been found at dozens of sites across North America. The Younger Dryas Impact Hypothesis proposes that a comet or asteroid fragment struck the Laurentide ice sheet, causing massive flooding, wildfires, and triggering the extinction of most North American megafauna.',
         note:'The Younger Dryas boundary layer is found at over 50 sites worldwide. This event coincides with the sudden disappearance of the Clovis culture, the extinction of mammoths and sabertooths, and catastrophic flooding across North America. Many researchers connect this to the flood traditions found in nearly every ancient culture.'},

        {cat:'anomaly', name:'Carolina Bays', lat:34.2, lng:-79.0,
         desc:'Over 500,000 elliptical depressions along the US East Coast from New Jersey to Florida, all oriented in the same northwest-to-southeast direction. Some researchers propose they were created by secondary impacts or ejecta from a comet strike on the Laurentide ice sheet during the Younger Dryas event (~12,800 years ago).',
         note:'Half a million depressions, all aligned the same way. The mainstream explanation (wind and water erosion) struggles to account for the uniform alignment. If impact-related, this was a truly global catastrophe.'},

        {cat:'anomaly', name:'Channeled Scablands', lat:47.5, lng:-118.0,
         desc:'Massive erosion channels carved into basalt bedrock across eastern Washington, created by catastrophic mega-floods during the Ice Age. J Harlen Bretz proposed the flood origin in 1923 and was ridiculed for 40 years before being vindicated. The scale of water required is almost unimaginable — 10 cubic miles per hour.',
         note:'Bretz was mocked because "catastrophism" was heresy in geology — uniformitarianism (slow, gradual change) was dogma. He was eventually proven right. 10 cubic miles of water per hour carved these channels. The scale parallels biblical Flood descriptions.'},

        {cat:'anomaly', name:'Lake Missoula Glacial Lake Outburst', lat:46.87, lng:-114.0,
         desc:'A glacial lake containing 500 cubic miles of water (half the volume of Lake Michigan) that repeatedly burst through its ice dam during the Ice Age, sending catastrophic floods across the Pacific Northwest. Each flood carried 10x the flow of all the world\'s rivers combined.',
         note:'Evidence of dozens of catastrophic floods from a single glacial lake. The scale of Ice Age catastrophism keeps being revised upward. These are not slow, gradual processes.'},

        {cat:'underwater', name:'Dwarka Underwater Ruins', lat:22.2394, lng:68.9678,
         desc:'Submerged ruins off the coast of India corresponding to the legendary city of Krishna in the Mahabharata. Excavations found stone walls, fort bastions, and triangular anchors. Carbon dating placed some artifacts at 9,000+ years old. The Mahabharata records the city being "swallowed by the sea" — a scripture preserving the memory of real flooding. 2025 sonar surveys reveal new anomalies.',
         refs:'Genesis 7:17-24',
         note:'Another submerged city pointing to a time when coastlines were very different. Compare with Yonaguni (Japan), Cambay (India), and numerous Mediterranean submerged sites. Rising sea levels from the end of the Ice Age submerged coastal civilizations worldwide.'},

        {cat:'anomaly', name:'Gulf of Cambay (Khambhat) Submerged Site', lat:21.7, lng:72.3,
         desc:'Sonar surveys in 2001 revealed geometric structures on the seabed of the Gulf of Cambay — walls, streets, and buildings submerged 40m deep. If man-made, this would date to 7500-9500 BC when the area was dry land. Controversial — some claim natural geological formations.',
         note:'Pottery fragments and what appear to be tools have been dredged from the site. If confirmed, this would be among the oldest urban sites in the world, predating Sumer by thousands of years.'},

        {cat:'anomaly', name:'Montana Megaliths (Bear Paw Mountains)', lat:48.0, lng:-109.5,
         desc:'Unusual rock formations in the Bear Paw Mountains of Montana that some researchers argue show evidence of ancient stone-cutting and megalithic construction. Features include seemingly impossible balanced rocks, wall-like formations, and geometric patterns. Mainstream geology attributes them to natural weathering.',
         note:'Controversial but visually striking. The formations resemble megalithic walls and cut stones. Whether natural or artificial, they warrant investigation. North America\'s "missing" megalithic past is a growing area of alternative research.'},

        {cat:'anomaly', name:'Great Wall of China (Inward-Facing Sections)', lat:40.4319, lng:116.5704,
         desc:'The Great Wall stretches over 13,000 miles across northern China. While commonly explained as defense against northern nomadic tribes, an anomaly has been noted: many sections have the defensive side — the walkway, battlements, and arrow slits — facing INWARD toward China rather than outward toward potential invaders. Some sections have defensive features on both sides.',
         note:'If the armed side faces inward, what was the wall keeping IN rather than keeping OUT? Some researchers have noted this architectural anomaly and questioned the standard narrative. The sheer scale — 13,000 miles of continuous construction — also exceeds what should have been necessary for any known military threat.'},

        {cat:'anomaly', name:'Baigong Pipes', lat:37.36, lng:97.30,
         desc:'Iron pipes embedded in rock near the shore of Lake Toson, some dating to 150,000+ years ago. Found in caves and protruding from rock faces. Some pipes lead into Toson Lake. Analysis shows 8% unknown material content. Chinese scientists initially claimed them anomalous; later studies suggest iron-rich geological formations.',
         note:'If artificial, these predate all known human civilization. The Chinese government initially promoted them as an anomaly before the geological explanation gained traction.'},

        {cat:'anomaly', name:'Bosnian Pyramids (Visoko)', lat:43.977, lng:18.177,
         desc:'Semir Osmanagić claims that hills near Visoko are the largest pyramids in the world, with the "Pyramid of the Sun" standing 220m tall. Underground tunnels with megalithic blocks have been documented. Mainstream geologists say they are natural flatiron hills formed by sediment layers.',
         note:'Highly controversial. The European Association of Archaeologists called it "a cruel hoax." However, the tunnels are real, the geometric shapes are striking, and the site has drawn interest from researchers who question mainstream dating. Whether pyramid or hill, the formation is unusual.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Visocica_hill.JPG/320px-Visocica_hill.JPG'},

        {cat:'native', name:'Lovelock Cave (Si-Te-Cah)', lat:40.05, lng:-118.47,
         desc:'The Paiute oral tradition tells of the Si-Te-Cah — a race of red-haired cannibalistic giants who terrorized the region. The Paiute say they united with neighboring tribes and drove the giants into Lovelock Cave, then set fire to the entrance, destroying them. Archaeological excavations in 1911-12 found oversized handprints in the cave walls, duck decoys, and (controversially) red-haired remains that were later reclassified or lost.',
         refs:'Genesis 6:4; Numbers 13:33 (Nephilim traditions)',
         note:'The Paiute tradition is remarkably specific: a race of giants, cannibalistic behavior (cf. 1 Enoch 7:3-4 — the giants "devoured mankind"), and a tribal coalition to defeat them. These parallels to ancient Near Eastern giant traditions are striking.'},

        {cat:'native', name:'Catalina Island Giant Finds', lat:33.39, lng:-118.42,
         desc:'Ralph Glidden excavated thousands of burials on Santa Catalina Island in the 1920s-30s, reportedly finding multiple skeletons over 7 feet tall, some allegedly 8-9 feet. Photos exist but the actual remains were reportedly given to or taken by the Smithsonian and have never been publicly displayed. The island\'s Tongva/Gabrieliño inhabitants had traditions of a race of giants.',
         note:'The Smithsonian\'s involvement in "disappearing" giant skeletons is a persistent claim. The Institution has denied it, but FOIA requests have revealed 19th-century correspondence about anomalous skeletal finds being shipped to the Smithsonian.'},

        {cat:'native', name:'Serpent Mound', lat:39.025, lng:-83.43,
         desc:'The largest surviving effigy mound in the world — 1,348 feet long, tracing the sinuous form of an uncoiling serpent whose open mouth holds an oval disk (variously interpreted as an egg, the sun, or a cosmic egg). Located in Adams County, Ohio, the mound sits atop a verified crypto-explosion structure (a buried meteorite impact or steam explosion), suggesting the builders intentionally placed a cosmic symbol over a cosmic impact site. The head of the serpent aligns to the summer solstice sunset; the coils align to other astronomical events including the winter solstice sunrise and Polaris. Carbon dating has produced two conflicting results: ~320 BC (suggesting Adena culture) and ~1070 AD (suggesting Fort Ancient culture) — possibly indicating the site was built and later rebuilt. Some researchers connect the serpent-swallowing-egg motif to the "Great Serpent" cosmology shared between Cahokia, the Mississippian tradition, and Mesoamerican cultures, suggesting a sophisticated pan-continental spiritual worldview.',
         refs:'Genesis 3:1-15 (the serpent in Eden); Numbers 21:6-9 (bronze serpent of Moses); Revelation 12:9 (the great dragon, that ancient serpent); Amos 9:3 (serpent at the bottom of the sea)',
         note:'Why build the world\'s largest serpent effigy on an impact crater? The Adena/Fort Ancient peoples understood that this location was cosmically marked. The serpent-swallowing-the-sun is an image that appears in Egyptian, Mesopotamian, Hindu, and Mesoamerican art. Genesis 3 reveals the theological source: the serpent is the great deceiver, whose story spans all of human history. This mound is a monument to that cosmic drama — whether its builders knew it or not.', img:'https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Serpent_Mound_%28aerial_view%29.jpg/320px-Serpent_Mound_%28aerial_view%29.jpg'},

        {cat:'native', name:'Cahokia Mounds', lat:38.6553, lng:-90.0622,
         desc:'The largest pre-Columbian settlement north of Mexico. At its peak (~1050-1200 AD), Cahokia had a population of 20,000+ — larger than contemporary London. Monks Mound covers 14 acres and stands 100 feet tall — its base is larger than the Great Pyramid of Giza. The city had a wooden astronomical circle ("Woodhenge"), plazas, and evidence of human sacrifice.',
         note:'A city of 20,000 with a pyramid larger (at the base) than Giza — in Illinois. Yet most Americans have never heard of it. The human sacrifice evidence includes mass burial pits with young women. The city was abandoned by 1400 AD for unknown reasons.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Cahokia_Monks_Mound.jpg/320px-Cahokia_Monks_Mound.jpg'},

        {cat:'native', name:'America\'s Stonehenge (Mystery Hill)', lat:42.8414, lng:-71.2067,
         desc:'A complex of stone structures, chambers, and standing stones in New Hampshire with verified astronomical alignments to solstices and equinoxes. Carbon dating of charcoal from the site ranges from 4000 BC to 173 BC. Inscriptions resembling Phoenician, Iberian Ogham, and Libyan scripts have been controversially identified.',
         note:'Pre-Columbian stone construction with possible Old World script? If the inscription readings are correct, this suggests trans-Atlantic contact thousands of years before Columbus. Barry Fell\'s controversial decipherments remain debated.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Mystery_Hill_NH_standing_stone.jpg/320px-Mystery_Hill_NH_standing_stone.jpg'},

        {cat:'native', name:'Poverty Point', lat:32.6347, lng:-91.4081,
         desc:'A massive 3,500-year-old earthwork complex in Louisiana featuring concentric C-shaped ridges and a 72-foot mound. Built by hunter-gatherers who moved 750,000 cubic yards of earth with baskets — no wheelbarrows, no draft animals. Their trade network spanned 1,000+ miles for exotic stones and minerals.',
         note:'Hunter-gatherers don\'t build monumental architecture — except when they do. Poverty Point, like Göbekli Tepe, challenges the assumption that monumentality requires agriculture. These builders had knowledge and organization that exceeds our models.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Poverty_Point_Aerial_HRoe_2014.jpg/320px-Poverty_Point_Aerial_HRoe_2014.jpg'},

        {cat:'native', name:'Newark Earthworks', lat:40.0528, lng:-82.4322,
         desc:'Massive geometric earthworks in Ohio covering 4 square miles — including a perfect circle, octagon, and square connected by parallel walls. The octagon encodes the 18.6-year lunar standstill cycle with precision. Combined with other Ohio earthworks, this represents sophisticated understanding of geometry and astronomy.',
         note:'The 18.6-year lunar cycle encoded in earthen walls by people we assume lacked writing. The precision rivals anything in the ancient world. A golf course was built on part of it. Now being reclaimed as a World Heritage Site.',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Newark_Earthworks_Octagon_aerial.jpg/320px-Newark_Earthworks_Octagon_aerial.jpg'},

        {cat:'native', name:'Choctaw Nahullo Tradition', lat:32.3, lng:-90.2,
         desc:'The Choctaw people preserved oral traditions of the "Nahullo" — a race of white-skinned giants who inhabited the region before them. Choctaw historian Horatio Bardwell Cushman recorded these traditions in the 19th century. The Nahullo were described as cannibalistic and were driven out or destroyed by the ancestors of the Choctaw.',
         refs:'Genesis 6:4; Numbers 13:33',
         note:'The Choctaw, Chickasaw, and Comanche all had independent traditions of pre-existing giant races. These are not borrowed from European contact — they were recorded by the earliest European explorers as already ancient traditions.'},

        {cat:'native', name:'Navajo Ye\'iitsoh (Giant) Tradition', lat:36.999, lng:-109.045,
         desc:'The Navajo (Diné) oral tradition speaks of Ye\'iitsoh ("Big Giant") and other giant beings who terrorized the people before being destroyed by the Hero Twins — Monster Slayer and Born for Water. The petrified lava flows near Mount Taylor, New Mexico, are said to be the dried blood of Ye\'iitsoh.',
         refs:'Genesis 6:4; Deuteronomy 2:10-11',
         note:'The Navajo giant-slaying narrative parallels David vs. Goliath and Joshua vs. the Anakim. A pair of heroes destroy a race of giants with divine help. This is not a local legend — it\'s a universal archetype rooted in genuine ancient memory.'},

        {cat:'native', name:'Cherokee Moon-Eyed People & Judaculla Rock', lat:35.3, lng:-83.1,
         desc:'The Cherokee preserved traditions of the "Moon-Eyed People" — pale-skinned beings who lived in the mountains before the Cherokee arrived and could not see in daylight. Judaculla Rock near Cullowhee, NC, bears mysterious petroglyphs attributed to Tsul\'kalu, the "Slant-Eyed Giant" — a powerful being who could leap across mountains.',
         refs:'Genesis 6:4',
         note:'The Moon-Eyed People are not giants per se, but pre-existing inhabitants with unusual characteristics. The Judaculla/Tsul\'kalu giant tradition is separate — a being of immense size and power. Cherokee traditions, like those of many tribes, speak of beings who preceded them in the land.'},

        {cat:'native', name:'Taíno Yaya / Supreme Creator (Puerto Rico)', lat:18.22, lng:-66.59,
         desc:'The Taíno people of Puerto Rico and the Caribbean had a concept of a supreme creator deity — Yúcahu Bagua Maórocoti — who was invisible, eternal, and all-powerful. The Taíno creation story speaks of Yaya (the supreme spirit), whose son\'s bones were placed in a gourd that burst and flooded the earth, creating the oceans. Striking parallels exist between the Taíno Yaya and the Hebrew YHWH.',
         refs:'Romans 1:19-20; Acts 17:27',
         note:'Multiple Native American peoples had monotheistic or near-monotheistic concepts: the Lakota Wakan Tanka ("Great Mystery"), the Algonquin Gitche Manitou ("Great Spirit"), the Inca Viracocha (the invisible creator). Paul\'s declaration in Acts 17:27 — that God "is not far from each one of us" — suggests these echoes of monotheism are exactly what we\'d expect.'},

        {cat:'native', name:'Lakota Wakan Tanka (Black Hills / Paha Sapa)', lat:43.88, lng:-103.46,
         desc:'The Lakota/Sioux concept of Wakan Tanka — the "Great Mystery" or "Great Spirit" — is a deeply monotheistic concept of an all-pervading sacred power. The Black Hills (Paha Sapa) are sacred as the heart of everything. Many Native American nations across the continent held similar concepts of a single supreme creator above all other spiritual beings.',
         refs:'Romans 1:19-20; Acts 14:17; Acts 17:26-27',
         note:'The universality of monotheistic concepts among peoples separated by oceans and millennia is exactly what Romans 1:19-20 predicts: "What can be known about God is plain to them, because God has shown it to them." These aren\'t corrupted Christianity — they\'re pre-contact echoes of the original knowledge of God that all humanity once shared (Gen 1-11).'},

        {cat:'native', name:'Algonquin Gitche Manitou (Great Spirit)', lat:44.5, lng:-85.5,
         desc:'The Algonquin peoples\' concept of Gitche Manitou ("Great Spirit") describes a supreme, invisible creator deity who made the world and all living things. Algonquin creation traditions include a great flood from which only a few survived on a raft — a remarkably specific parallel to Noah\'s account.',
         refs:'Genesis 6-9; Romans 1:19-20',
         note:'The Algonquin flood narrative: the world was flooded, animals and a few humans survived on a raft, a muskrat dove down and brought up mud to recreate the earth. This is independent of European contact. Over 200 flood traditions exist worldwide — too many to be coincidence, too similar to be unrelated.'},

        {cat:'native', name:'Inca Viracocha Tradition (Lake Titicaca)', lat:-15.83, lng:-69.33,
         desc:'The Inca supreme deity Viracocha was described as a tall, bearded, pale figure who arose from Lake Titicaca at the beginning of time, created the sun, moon, stars, and humanity, then walked westward across the Pacific and disappeared — promising to return. He was worshipped as the invisible creator behind all other gods.',
         refs:'Acts 17:23 (To the Unknown God)',
         note:'The "bearded white god who departed and will return" motif appears across the Americas: Quetzalcoatl (Aztec), Kukulkan (Maya), Viracocha (Inca), Bochica (Muisca). Were these distorted memories of real events? The promise to "return" echoes Christ\'s promise.'},

        {cat:'native', name:'Quetzalcoatl / Great Pyramid of Cholula', lat:19.058, lng:-98.302,
         desc:'The feathered serpent deity Quetzalcoatl was described in Aztec tradition as a pale, bearded figure who opposed human sacrifice, taught civilization, and departed eastward across the sea with a promise to return. The Great Pyramid of Cholula — the world\'s largest pyramid by volume — was dedicated to him. When Cortés arrived from the east, Montezuma initially believed Quetzalcoatl had returned.',
         refs:'Genesis 3:15; Acts 17:23-27',
         note:'A deity who opposes human sacrifice in a culture defined by human sacrifice. Who taught law, writing, and agriculture. Who was associated with both a serpent and a feathered/heavenly being. Who departed and promised to return. The parallels to Christ are striking — whether as distorted memory or divine preparation.'},

        {cat:'native', name:'Hopi Prophecy Rock (Third Mesa)', lat:35.83, lng:-110.63,
         desc:'The Hopi people of Arizona preserve traditions of three previous "worlds" that were destroyed — the first by fire, the second by ice, the third by flood. Only the righteous survived each destruction to enter the next world. Their "Prophecy Rock" petroglyph at Third Mesa depicts two paths: one leading to technology and destruction, the other to harmony with the Creator.',
         refs:'2 Peter 3:5-7 (world destroyed by water, next by fire)',
         note:'The Hopi three-destructions narrative (fire, ice, flood) parallels 2 Peter 3:5-7, which describes past judgment by water and future judgment by fire. The Hopi "Fourth World" concept echoes the biblical pattern of judgment and renewal.'},

        {cat:'native', name:'Spirit Water (Devil\'s Lake, Mni Wakhán)', lat:47.85, lng:-99.11,
         desc:'Sacred lake of the Dakota/Sioux people, originally called Mni Wakȟáŋ ("Spirit Water"). The Dakota saw this as a place of spiritual power. Renamed "Devil\'s Lake" by French missionaries who could not distinguish between Native spiritual concepts and demonic activity. The lake has no natural outlet and fluctuates dramatically.',
         note:'The colonial renaming of "Spirit Water" to "Devil\'s Lake" illustrates a tragic pattern — European Christians failed to recognize that Native concepts of the Great Spirit might reflect genuine knowledge of God (Romans 1:19-20) rather than demonic worship.'},

        {cat:'native', name:'Giants of Patagonia Tradition', lat:-51.5, lng:-69.5,
         desc:'When Magellan\'s expedition reached Patagonia in 1520, Antonio Pigafetta recorded encounters with people so tall they "reached only to the waist" of the natives. The name "Patagonia" itself may derive from "Patagón" — giants in a Spanish romance. Multiple early explorers (Drake, Sarmiento, Byron) reported unusually tall inhabitants.',
         refs:'Genesis 6:4; Numbers 13:33',
         note:'The Tehuelche people of Patagonia were genuinely tall (6\'0-6\'6" average by some accounts), but explorer accounts consistently exaggerated them into giants of 10-12 feet. What is significant is the universal tendency to report giants — because the archetype of "giants in the land" runs deep in human memory.'},

        {cat:'anomaly', name:"Grand Canyon 'Egyptian' Cave (Kinkaid's Cave)", lat:36.1800, lng:-112.0500, desc:"In 1909 the Arizona Gazette reported explorer G.E. Kinkaid's discovery of a cave system containing Egyptian-style artifacts, hieroglyphs, mummies, and a cross-legged idol. The Smithsonian Institution denies any involvement or knowledge of the find. The cave's exact location has never been publicly disclosed.", refs:'', note:'Smithsonian denies involvement; cave location remains undisclosed', img:'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/USA_09847_Grand_Canyon_Luca_Galuzzi_2007.jpg/320px-USA_09847_Grand_Canyon_Luca_Galuzzi_2007.jpg'},
        {cat:'anomaly', name:'Grand Canyon Isis Temple', lat:36.1416, lng:-112.0883, desc:"One of several Grand Canyon buttes named after Egyptian and Eastern deities by geologist Clarence Dutton in the 1880s. The cluster includes Osiris Temple, Tower of Set, and Ra. The Egyptian naming convention applied to this region has fueled speculation about ancient Old World contact with the Americas.", refs:'', note:'Named by Clarence Dutton in the 1880s alongside Osiris, Set, and Ra formations'},
        {cat:'anomaly', name:'Grand Canyon Tower of Set', lat:36.1268, lng:-112.0775, desc:"A Grand Canyon butte named after the Egyptian god Set, part of a cluster of formations bearing Egyptian deity names assigned by Clarence Dutton in the 1880s. Located near Isis Temple and Osiris Temple, this naming pattern sits at the center of theories about Egyptian presence in ancient North America.", refs:'', note:'Part of the Egyptian-named formation cluster near Isis Temple'},
        {cat:'anomaly', name:'Grand Canyon Osiris Temple', lat:36.1442, lng:-112.0598, desc:"A Grand Canyon butte named after the Egyptian god Osiris, part of the cluster of Egyptian-named formations assigned by Clarence Dutton in the 1880s. Along with Isis Temple and Tower of Set, these names have been cited by researchers linking the Grand Canyon to theories of Old World contact.", refs:'', note:'Part of the Egyptian-named formation cluster'},
        {cat:'anomaly', name:"Burrows Cave", lat:38.7300, lng:-87.7700, desc:"In 1982 Russell Burrows claimed to discover an underground cave near Olney, Illinois, containing hundreds of engraved stones bearing inscriptions he identified as Egyptian, Etruscan, Hebrew, and other Old World scripts, along with gold artifacts and mummies. The site is highly controversial — mainstream archaeology largely dismisses it, while some researchers see it as evidence of ancient trans-Atlantic contact.", refs:'', note:'Location never publicly verified; highly disputed'},
        {cat:'anomaly', name:'Los Lunas Decalogue Stone', lat:34.7800, lng:-106.7100, desc:"A large basalt boulder near Los Lunas, New Mexico, inscribed with an abridged version of the Ten Commandments in what appears to be Paleo-Hebrew script. Its dating is vigorously debated — some scholars argue pre-Columbian origin, others suspect 19th-century fabrication. If authentic, it would represent ancient Semitic presence in the American Southwest.", refs:'Exodus 20:1-17', note:'Dating debated; Paleo-Hebrew script confirmed by some epigraphers', img:'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Los_Lunas_Decalogue_Stone.jpg/320px-Los_Lunas_Decalogue_Stone.jpg'},
        {cat:'anomaly', name:'Tucson Lead Artifacts', lat:32.2800, lng:-111.0000, desc:"Between 1924 and 1930, dozens of lead crosses, swords, and tablets with Latin and Hebrew inscriptions were found near Tucson, Arizona. Some reference medieval European leaders and Christian formulas. Most mainstream scholars regard them as 19th-century hoaxes, but a minority argue the lead alloy composition and burial context are inconsistent with modern forgery.", refs:'', note:'Most scholars consider forgeries; some metallurgical data disputed'},
        {cat:'anomaly', name:'Ancient Lake Superior Copper Mines', lat:47.1500, lng:-88.5000, desc:"5,000 ancient copper mines — including more than 1,000 pits on remote Isle Royale alone — extracted up to 750,000 tonnes of 99% pure copper between 2470–1050 BC, then it all vanished. Only a fraction appears in North American artifacts. Mining ended abruptly at 1200 BC — the exact year Bronze Age Mediterranean civilization collapsed. Some researchers connect this to Phoenician transatlantic trade. Miners left behind stone hammers weighing up to 30 lbs — tens of thousands of them — and nothing else.", refs:'Ezekiel 27:12-25; 1 Kings 10:22', note:'~500,000–750,000 tons extracted; destination of copper remains one of the greatest archaeological mysteries; mining cessation at 1200 BC aligns precisely with Bronze Age Collapse'},
        {cat:'anomaly', name:'Bat Creek Stone', lat:35.7300, lng:-83.5800, desc:"Discovered in 1889 by Smithsonian archaeologist John Emmert inside a burial mound in Tennessee. An inscription originally identified as Cherokee was later re-examined by Cyrus Gordon and others and identified as Paleo-Hebrew, possibly reading 'for Judea.' If authentic, it would represent one of the strongest archaeological cases for pre-Columbian Semitic contact with North America.", refs:'', note:"Originally read as Cherokee; later identified as Paleo-Hebrew by Cyrus Gordon"},
        {cat:'anomaly', name:'Dighton Rock', lat:41.8000, lng:-71.1200, desc:"A 40-ton glacial boulder on the Taunton River in Massachusetts covered with petroglyphs that have been attributed at various times to Norse explorers, Portuguese navigator Miguel Corte-Real, Phoenician sailors, and indigenous peoples. No consensus has been reached on their origin or meaning. The rock is now preserved in a museum building.", refs:'', note:'Attributed variously to Norse, Phoenician, Portuguese, and Native American origins'},
        {cat:'anomaly', name:'Newark Holy Stones', lat:40.0600, lng:-82.4000, desc:"A collection of stone artifacts with Hebrew inscriptions discovered in burial mounds near Newark, Ohio in 1860. They include a 'Decalogue Stone' inscribed with the Ten Commandments and a stone bearing the face of a figure wearing a priestly headpiece inscribed with Hebrew letters. Mainstream scholars largely consider them 19th-century forgeries; a minority argue for pre-Columbian authenticity.", refs:'Exodus 20', note:'Found in burial mounds 1860; forgery vs. pre-Columbian debate ongoing'},
        {cat:'native', name:'Judaculla Rock', lat:35.2800, lng:-83.1700, desc:"A large soapstone boulder near Cullowhee, North Carolina, covered with hundreds of petroglyphs. Cherokee tradition attributes the markings to Judaculla, a powerful slant-eyed giant who owned all hunting grounds. The name derives from the Cherokee 'Tsul kalu,' meaning 'slant-eyed giant.' The giant traditions of indigenous peoples across North America parallel biblical and Second Temple accounts of the Nephilim.", refs:'Genesis 6:4', note:'Cherokee giant tradition parallels Nephilim accounts'},
        {cat:'anomaly', name:'Spirit Cave Mummy (Nevada)', lat:39.3700, lng:-118.4900, desc:"Discovered near Fallon, Nevada in 1940, the Spirit Cave Mummy dates to approximately 9,400 years ago — making it one of the oldest mummies in North America. It was found with finely woven textile moccasins and a shroud, demonstrating sophisticated craftsmanship far earlier than previously assumed for the region, challenging standard timelines of cultural development in the Americas.", refs:'', note:'9,400-year-old mummy with sophisticated woven textiles'},
        {cat:'megalith', name:'Vinapu (Easter Island)', lat:-27.1700, lng:-109.4000, desc:"A ceremonial stone platform on Easter Island featuring tightly fitted, polygonal stone masonry strikingly similar to Inca stonework at Sacsayhuamán and Tiwanaku. Thor Heyerdahl and others cited Vinapu as evidence of pre-Columbian trans-Pacific contact between South America and Easter Island. The precision of the jointing rivals any Old World masonry tradition.", refs:'', note:'Stonework style closely matches Inca construction at Sacsayhuamán'},
        {cat:'anomaly', name:'Longyou Caves', lat:29.0400, lng:119.1700, desc:"Thirty-six massive artificial caverns discovered in 1992 beneath Fenghuang Hill in Zhejiang Province, China. Each cave is multi-story, with columns left intact for structural support, and the walls and ceilings bear uniform parallel chisel marks suggesting coordinated large-scale construction. No historical record — Chinese or otherwise — mentions their construction, purpose, or builders.", refs:'', note:'No historical record of construction; discovered 1992; 36 caverns total'},
        {cat:'anomaly', name:'Baigong Pipes', lat:37.3800, lng:97.4500, desc:"Iron pipe structures found embedded in rock near Delingha, Qinghai, China, some leading into a nearby salt lake. Reported dating of some samples to 150,000 years ago has fueled speculation about ancient or non-human construction. Mainstream geologists argue they are likely fossilized tree roots that absorbed iron compounds, but the debate continues.", refs:'', note:'Some samples reportedly dated to 150,000 years; natural vs. artificial origin debated'},
        {cat:'anomaly', name:'Stone Spheres of Costa Rica', lat:8.8000, lng:-83.5000, desc:"Hundreds of nearly perfectly spherical stone balls scattered across the Diquís Delta of Costa Rica and Isla del Caño. Some exceed six feet in diameter and weigh up to 16 tons. Carved by the pre-Columbian Diquís culture, their purpose and the means by which such precision was achieved without metal tools remain unknown. Designated a UNESCO World Heritage Site in 2014.", refs:'', note:'UNESCO World Heritage Site; some spheres 6+ ft diameter, up to 16 tons', img:'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Costa_Rica-Mus%C3%A9o_Nacional.jpg/320px-Costa_Rica-Mus%C3%A9o_Nacional.jpg'},

        // ── RECENT ARCHAEOLOGY (2024-2025) ──
        {cat:'biblical', name:'City of David Winged Genie Seal', lat:31.7746, lng:35.2354,
         desc:'In 2024, a 2,700-year-old royal seal depicting a winged genie was unearthed — the same divine-court imagery as the cherubim and seraphim of Scripture (Isa 6; Ezek 1). This Judahite official\'s seal demonstrates heavenly council iconography permeated the royal administration of ancient Jerusalem.',
         refs:'Isaiah 6:1-3; Ezekiel 1:5-14; 2 Kings 18:18',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Apkallu_-_Nimrud.jpg/220px-Apkallu_-_Nimrud.jpg'},
        {cat:'biblical', name:'Tell Tayinat Temple', lat:36.2431, lng:36.3622,
         desc:'Two tripartite temples architecturally identical to Solomon\'s Temple — the closest parallel ever found. Likely biblical Calneh (Isaiah 10:9), this was the capital of the Neo-Hittite kingdom of Patina, destroyed by Tiglath-pileser III in 738 BC and converted into an Assyrian cult center. Reveals what First Temple Jerusalem\'s sacred architecture actually looked like.',
         refs:'Isaiah 10:9-10; 1 Kings 6:1-38; 2 Chronicles 3:1-17',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Tell_Tayinat_Excavation.jpg/220px-Tell_Tayinat_Excavation.jpg'},
        {cat:'biblical', name:'Tall el-Hammam (Possible Sodom)', lat:31.8005, lng:35.6659,
         desc:'A Middle Bronze Age city destroyed c. 1650 BC by a blast exceeding 2,000\u00b0C — temperatures achievable only by cosmic airburst. Shocked quartz, melted platinum, and diamond-like carbon found in the destruction layer. Salt scattered across the Jordan Valley caused 300-600 years of agricultural abandonment. Located northeast of the Dead Sea, exactly where Genesis places Sodom.',
         refs:'Genesis 18:20-21; Genesis 19:24-25; Luke 17:29; 2 Peter 2:6',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Tall_el-Hammam_excavation.jpg/220px-Tall_el-Hammam_excavation.jpg'},
        {cat:'biblical', name:'Sogmatar Moon God City', lat:37.0922, lng:38.8869,
         desc:'Ancient sacred city dedicated to the Moon God Sin/Nanna — the same lunar deity worshiped in Ur of the Chaldeans, where Abraham\'s family originated (Gen 11:28-31). A 3,000-year-old public building was unearthed here in 2024-2025. The Moon God\'s cult at Ur was the religious world Abraham left behind when called to follow Yahweh.',
         refs:'Genesis 11:28-31; Joshua 24:2; Acts 7:2-4'},

        // ── MEGALITHIC / ANCIENT MYSTERY ──
        {cat:'megalith', name:'\u00c7atalh\u00f6y\u00fck House of the Dead', lat:37.6680, lng:32.8271,
         desc:'A 9,000-year-old ritual complex where 20 individuals were buried beneath the floor — the living community built their world literally on top of the honored dead. This practice illuminates the biblical concept of the Rephaim (shades of the dead) and the cosmology of Sheol as a realm beneath. 2025 genetic studies confirmed matrilineal household inheritance.',
         refs:'Isaiah 14:9-11; Ezekiel 32:21-27; Proverbs 2:18',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/%C3%87atalh%C3%B6y%C3%BCk_after_the_first_excavations_by_James_Mellaart.jpg/220px-%C3%87atalh%C3%B6y%C3%BCk_after_the_first_excavations_by_James_Mellaart.jpg'},
        {cat:'megalith', name:'Gilgal Rephaim (Wheel of Giants)', lat:32.9013, lng:35.7939,
         desc:'42,000 basalt rocks forming five concentric circles, older than the Egyptian pyramids, built in the territory of King Og of Bashan — the last of the Rephaim (Deut 3:11). The Hebrew name means "Wheel of the Giants/Spirits." Invisible from the ground, its true form is only revealed from above. A 2025 geomagnetic study raised new questions about its original sacred orientation.',
         refs:'Deuteronomy 3:11; Numbers 21:33-35; Joshua 12:4-5; Joshua 13:12',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Rujm_el-Hiri_aerial_view.jpg/220px-Rujm_el-Hiri_aerial_view.jpg'},

        // ── UNDERWATER RUINS ──
        {cat:'underwater', name:'Atlit-Yam', lat:32.7011, lng:34.9358,
         desc:'A 9,000-year-old Neolithic village beneath the Mediterranean, 300m from the Israeli coast. Seven 600 kg megaliths arranged around a freshwater spring predate Stonehenge by 4,000 years. The dead were buried beneath the floors of the living. May have been destroyed by a Mediterranean tsunami caused by Mount Etna\'s volcanic collapse 8,500 years ago.',
         refs:'Genesis 7:11-12',
         img:'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Atlit-Yam_Aerial.jpg/220px-Atlit-Yam_Aerial.jpg'},

        // ── ANOMALY / MYSTERY ──
        {cat:'anomaly', name:'Burckle Crater', lat:-30.865, lng:61.365,
         desc:'Proposed 29 km-wide impact crater beneath the Indian Ocean. Chevron dunes in Madagascar show tsunami wave runup of 205 meters, penetrating 45 km inland. Deep-sea cores contain nickel-rich impact spherules dated to c. 2870-3700 BC. Researcher W. Bruce Masse analyzed 175 global flood myths and found 14 specifically mentioning a total solar eclipse during the event, all pointing to the same date.',
         refs:'Genesis 7:11; 2 Peter 3:5-6'},

        // ── DEAD SEA SCROLLS ──
        {cat:'dss', name:'Qumran Cave 11 \u2014 Unsorted Fragments', lat:31.7412, lng:35.4605,
         desc:'Seventy-five years after the Dead Sea Scrolls discovery, boxes of unsorted Cave 11 fragments still await examination — unimaged, unstudied. Among Qumran\'s most explosive texts are the Book of Giants fragments (4Q530-532), naming the children of the fallen Watchers — including Gilgamesh. In 2025, an AI tool named "Enoch" began re-dating 135 manuscripts, finding earlier origins.',
         refs:'Jude 1:6; Jude 1:14-15; 2 Peter 2:4-5; 1 Enoch 6-16'},

    ];

    // ── BIBLICAL JOURNEYS ──
    var MAP_JOURNEYS = [
        {id: 'watcher_descent',
            name: 'Watcher Descent & Nephilim Spread',
            color: '#a855f7',
            weight: 3,
            dash: '12 4 4 4',
            desc: 'The 200 Watchers descend on Mount Hermon and their giant offspring spread across the ancient world. After the Flood, remnant Nephilim clans appear in Canaan.',
            refs: '1 Enoch 6\u201316; Genesis 6:1-4; Numbers 13:33',
            waypoints: [
                {lat:33.42, lng:35.86, label:'Mount Hermon (descent)', ref:'1 Enoch 6:6', desc:'200 Watchers swore an oath and descended here. They took human wives and taught forbidden knowledge \u2014 metallurgy, sorcery, astrology. The mountain\'s name means "devoted/banned."'},
                {lat:34.01, lng:36.20, label:'Baalbek (giant construction)', ref:'Book of Giants', desc:'Massive megalithic stones (800+ tons each) that defy ancient engineering. Legends attribute construction to Nephilim/giants. The Romans built their largest temple on top.'},
                {lat:33.25, lng:35.69, label:'Dan / Gates of Hades', ref:'Matt 16:18', desc:'At the base of Hermon, Pan\'s grotto was believed to be an entrance to the underworld. Jesus chose this exact spot to declare He would build His church against the gates of Hades.'},
                {lat:32.95, lng:35.80, label:'Bashan (Og\'s kingdom)', ref:'Deut 3:11', desc:'Og was the last of the Rephaim. His iron bed was 13.5 feet long. Bashan was known as "the place of the serpent" \u2014 a Rephaim stronghold and cult center.'},
                {lat:31.53, lng:35.10, label:'Hebron (Anakim)', ref:'Num 13:22', desc:'The spies saw Ahiman, Sheshai, and Talmai \u2014 descendants of Anak. "We seemed like grasshoppers in our own eyes." These were the giants that terrified ten of the twelve spies.'},
                {lat:31.61, lng:34.85, label:'Gath (Goliath)', ref:'1 Sam 17:4', desc:'Goliath of Gath, over 9 feet tall, had four giant relatives (2 Sam 21). David killed him with a stone and sword, then David\'s men killed the remaining four.'},
                {lat:31.10, lng:34.40, label:'Gaza (Anakim survivors)', ref:'Josh 11:22', desc:'Joshua drove out the Anakim from all the hill country, but remnants survived in Gaza, Gath, and Ashdod. These Philistine cities became the last strongholds of the giant clans.'}
            ]
        },
        {
            id: 'nimrod_expansion',
            name: 'Nimrod\u2019s Empire \u2014 Babel, Uruk & the First Kingdoms',
            color: '#ef4444',
            weight: 4,
            dash: '8 4 4 4',
            desc: 'The first post-Flood kingdom-builder. Nimrod (gibbor \u2014 "mighty one," the same term for Nephilim in Gen 6:4) built the first empire from Shinar to Assyria. His Babel was the center of unified rebellion against God\'s command to fill the earth. Gilgamesh, legendary king of Uruk, may be a later tradition of the same or similar figure \u2014 a mighty ruler who sought immortality and whose flood account parallels Noah\'s. Nimrod is the prototype of human pride opposing God; all later proud kingdoms echo his rebellion.',
            refs: 'Gen 10:8-12; Gen 11:1-9; Micah 5:6; Epic of Gilgamesh',
            waypoints: [
                {lat:30.82, lng:45.99, label:'Eridu \u2014 oldest city, "kingship descended from heaven"', ref:'Gen 10:10', desc:'The Sumerian King List says kingship first descended from heaven at Eridu. Possibly the oldest city in the world. An ANE parallel to Eden and the beginning of organized civilization after the Flood.'},
                {lat:31.32, lng:45.64, label:'Erech (Uruk) \u2014 Gilgamesh\'s city', ref:'Gen 10:10', desc:'One of Nimrod\'s cities and legendary seat of Gilgamesh, the "two-thirds divine" king who sought eternal life. The Epic of Gilgamesh contains a flood narrative paralleling Noah\'s. Uruk had the world\'s first monumental architecture and earliest known writing (~3400 BC).'},
                {lat:32.54, lng:44.42, label:'Babel / Babylon \u2014 tower & rebellion', ref:'Gen 11:1-9', desc:'Nimrod\'s capital and center of unified rebellion. "Come, let us build a city and a tower with its top in the heavens." God confused their languages and scattered them. Babylon becomes the archetype of human pride opposing God throughout Scripture (Isa 14; Rev 17-18).'},
                {lat:32.78, lng:44.00, label:'Accad (Akkad) \u2014 seat of the first empire', ref:'Gen 10:10', desc:'Part of Nimrod\'s kingdom in Shinar. The Akkadian Empire under Sargon (~2334 BC) became the world\'s first true empire, ruling from the Persian Gulf to the Mediterranean \u2014 echoing Nimrod\'s ambition for universal dominion.'},
                {lat:32.30, lng:45.00, label:'Calneh \u2014 fourth city of Shinar', ref:'Gen 10:10', desc:'The fourth city listed in Nimrod\'s Shinar kingdom. Its exact location is debated (possibly Nippur or another Sumerian city). Together with Babel, Erech, and Accad, it formed the core of the first post-Flood civilization.'},
                {lat:35.47, lng:43.27, label:'Resen \u2014 "the great city" between Nineveh and Calah', ref:'Gen 10:12', desc:'Scripture calls it "the great city" between Nineveh and Calah. Part of the Assyrian expansion of Nimrod\'s empire northward from Shinar into the Tigris valley.'},
                {lat:34.50, lng:43.50, label:'Calah (Nimrud) \u2014 built by Nimrod in Assyria', ref:'Gen 10:11-12', desc:'Nimrod expanded from Shinar northward into Assyria. Calah became a major Assyrian city. Ashurnasirpal II later built grand palaces here. The site (modern Nimrud) is literally named after its legendary builder.'},
                {lat:35.15, lng:43.30, label:'Rehoboth-Ir \u2014 Assyrian expansion', ref:'Gen 10:11', desc:'One of four Assyrian cities attributed to Nimrod. The name means "broad places of the city." Part of the expanding network of urban power centers along the Tigris.'},
                {lat:36.36, lng:43.15, label:'Nineveh \u2014 "the great city"', ref:'Gen 10:11; Jonah 3:3', desc:'Built by Nimrod, Nineveh became capital of the Assyrian Empire \u2014 the most brutal superpower of the ancient world. God sent Jonah to preach here. It was "an exceedingly great city, three days\' journey in breadth." Its fall (612 BC) fulfilled Nahum\'s prophecy.'},
                {lat:34.01, lng:36.20, label:'Baalbek \u2014 megalithic platform (C-level tradition)', ref:'Arabic traditions; Gen 6:4', desc:'C-level tradition: Arabic legends attribute the megalithic stones (800+ tons each, the largest cut stones in the world) to giants or Nimrod. The Romans built their largest Jupiter temple on these impossible foundations. No known ancient technology could move stones this size.'}
            ]
        },
        {
            id: 'abraham',
            name: 'Abraham\'s Journey',
            color: '#3b82f6',
            weight: 3,
            dash: '10 6',
            desc: 'From Ur of the Chaldeans through Haran to the Promised Land. God called Abram to leave everything and go to a land "I will show you" (Gen 12:1).',
            refs: 'Genesis 11:31 \u2013 23:19',
            waypoints: [
                {lat:30.96, lng:46.10, label:'Ur of the Chaldeans', ref:'Gen 11:31', desc:'A sophisticated pagan city with ziggurat temples. God called Abram out of moon-god worship into covenant relationship \u2014 the first great act of divine election.'},
                {lat:36.87, lng:39.03, label:'Haran', ref:'Gen 11:31-12:4', desc:'Terah settled here and died. After his father\'s death, God repeated His call: "Go from your country and your kindred to the land that I will show you" (Gen 12:1).'},
                {lat:32.21, lng:35.28, label:'Shechem', ref:'Gen 12:6', desc:'First stop in Canaan. God appeared to Abram: "To your offspring I will give this land." Abram built his first altar here between Mount Ebal and Mount Gerizim.'},
                {lat:31.93, lng:35.22, label:'Bethel', ref:'Gen 12:8', desc:'Abram pitched his tent between Bethel and Ai, built an altar, and called upon the name of the LORD. This became a recurring worship site throughout Genesis.'},
                {lat:30.05, lng:31.23, label:'Egypt (famine)', ref:'Gen 12:10', desc:'Famine drove Abram to Egypt where he passed Sarai off as his sister. Pharaoh was plagued for taking her \u2014 God protected the covenant line even through Abram\'s failure.'},
                {lat:31.93, lng:35.22, label:'Return to Bethel', ref:'Gen 13:3', desc:'Abram returned to the altar he had built. Here he and Lot separated \u2014 Lot chose the well-watered Jordan plain toward Sodom; Abram stayed in the land of promise.'},
                {lat:31.53, lng:35.10, label:'Hebron / Mamre', ref:'Gen 13:18', desc:'Abram settled by the oaks of Mamre and built an altar. This became his primary home. Here God appeared, three visitors announced Isaac\'s birth, and Abraham interceded for Sodom.'},
                {lat:33.25, lng:35.69, label:'Dan (pursuit of kings)', ref:'Gen 14:14', desc:'When four kings captured Lot, Abraham armed 318 trained servants and pursued them to Dan. He defeated them in a night raid \u2014 the first biblical battle led by a man of faith.'},
                {lat:31.53, lng:35.10, label:'Hebron', ref:'Gen 14:13', desc:'Abraham returned victorious and met Melchizedek, king of Salem and priest of God Most High, who brought bread and wine \u2014 a type of Christ\'s priesthood (Heb 7).'},
                {lat:31.25, lng:34.79, label:'Beer-sheba', ref:'Gen 21:31', desc:'Abraham made a covenant with Abimelech and planted a tamarisk tree. He called on "the Everlasting God" (El Olam). Beer-sheba means "well of the oath."'},
                {lat:31.78, lng:35.24, label:'Mount Moriah (Aqedah)', ref:'Gen 22:2', desc:'God tested Abraham: "Take your son, your only son Isaac, whom you love." Abraham obeyed. God provided a ram \u2014 "On the mount of the LORD it shall be provided." The future Temple site.'},
                {lat:31.53, lng:35.10, label:'Hebron (Sarah\'s burial)', ref:'Gen 23:19', desc:'Sarah died at age 127. Abraham purchased the cave of Machpelah from the Hittites for 400 shekels of silver \u2014 his first owned piece of the Promised Land.'}
            ]
        },
        {id: 'abrahams_war',
            name: 'Abraham\'s War (Rescue of Lot)',
            color: '#06b6d4',
            weight: 2,
            dash: null,
            desc: 'When four Mesopotamian kings captured Lot at Sodom, Abraham armed 318 trained servants, pursued them north past Dan to Hobah near Damascus, defeated them at night, and recovered everything. Met Melchizedek on return.',
            refs: 'Genesis 14',
            waypoints: [
                {lat:31.53, lng:35.10, label:'Hebron (Mamre, news arrives)', ref:'Gen 14:13', desc:'A fugitive brought word that Lot was captured. Abraham immediately armed his 318 trained servants born in his household \u2014 ready for war to rescue family.'},
                {lat:32.21, lng:35.28, label:'Shechem (northward pursuit)', ref:'Gen 14:14', desc:'Abraham pursued the kings northward through the heart of Canaan. His swift military response reveals a trained warrior, not just a peaceful nomad.'},
                {lat:33.25, lng:35.69, label:'Dan (caught up to kings)', ref:'Gen 14:14', desc:'Abraham divided his forces and attacked at night. The surprise assault routed the eastern kings. Abraham recovered all the people and possessions.'},
                {lat:33.55, lng:36.25, label:'Hobah near Damascus (victory)', ref:'Gen 14:15', desc:'Abraham pursued the fleeing kings north of Damascus to Hobah. A complete victory \u2014 every captive freed, every possession recovered.'},
                {lat:31.78, lng:35.24, label:'Salem (meets Melchizedek)', ref:'Gen 14:18', desc:'Melchizedek, king of Salem and priest of God Most High, brought bread and wine and blessed Abraham. Abraham gave him a tenth. A type of Christ\'s eternal priesthood (Heb 7).'},
                {lat:31.53, lng:35.10, label:'Hebron (returns home)', ref:'Gen 14:13', desc:'Abraham refused to take any plunder from the king of Sodom: "I have lifted my hand to the LORD, God Most High \u2014 I would not take a thread or a sandal strap."'}
            ]
        },
        {id: 'isaac',
            name: 'Isaac\'s Journey',
            color: '#f97316',
            weight: 3,
            dash: '8 6',
            desc: 'The "quiet patriarch" \u2014 Isaac\'s life unfolds between Beer-lahai-roi, Gerar, and Beer-sheba. Though less dramatic than Abraham or Jacob, Isaac\'s story includes the Aqedah (binding), well-digging conflicts that preview Israel\'s land disputes, and the covenant reaffirmation at Beer-sheba.',
            refs: 'Genesis 20\u201326, 35',
            waypoints: [
                {lat:30.85, lng:34.68, label:'Beer-lahai-roi \u2014 where Rebekah arrives', ref:'Gen 24:62', desc:'Isaac dwelt near the well where God had appeared to Hagar. Here he went out to meditate and first saw Rebekah approaching on her camel (Gen 24:63-67).'},
                {lat:31.25, lng:34.79, label:'Beer-sheba \u2014 Abraham\'s covenant site', ref:'Gen 21:31', desc:'Abraham had made a covenant with Abimelech here and planted a tamarisk tree. Isaac inherited this as home base (Gen 21:31-34).'},
                {lat:31.78, lng:35.24, label:'Mount Moriah \u2014 the Aqedah', ref:'Gen 22:2', desc:'Abraham bound Isaac on the altar here. God provided a ram instead \u2014 "On the mount of the LORD it shall be provided" (Gen 22:14). Later the Temple site.'},
                {lat:31.40, lng:34.39, label:'Gerar \u2014 sojourn and deception', ref:'Gen 26:1-6', desc:'During famine, Isaac went to Abimelech king of the Philistines. Like his father, he called Rebekah his sister. God blessed him with hundredfold harvest (Gen 26:12).'},
                {lat:31.35, lng:34.42, label:'Valley of Gerar \u2014 well conflicts (Esek, Sitnah)', ref:'Gen 26:17-21', desc:'Isaac re-dug Abraham\'s wells. The herdsmen of Gerar quarreled \u2014 he named them Esek ("contention") and Sitnah ("enmity"), previewing Israel\'s later land conflicts.'},
                {lat:31.33, lng:34.45, label:'Rehoboth \u2014 "room at last"', ref:'Gen 26:22', desc:'After two disputes, Isaac dug a third well with no quarrel. He named it Rehoboth \u2014 "For now the LORD has made room for us, and we shall be fruitful in the land."'},
                {lat:31.25, lng:34.79, label:'Beer-sheba \u2014 God appears, builds altar', ref:'Gen 26:23-33', desc:'God appeared to Isaac: "I am the God of Abraham your father. Fear not, for I am with you." Isaac built an altar, pitched his tent, and dug another well.'},
                {lat:31.53, lng:35.10, label:'Hebron / Machpelah \u2014 death and burial', ref:'Gen 35:27-29', desc:'Isaac died at age 180 in Hebron. Esau and Jacob buried him together in the cave of Machpelah alongside Abraham and Sarah (Gen 35:29).'}
            ]
        },
        {id: 'jacob',
            name: 'Jacob\'s Journey',
            color: '#22c55e',
            weight: 3,
            dash: '8 4',
            desc: 'From Beer-sheba to Haran (fleeing Esau), back through Peniel (wrestling God), to Shechem and finally Hebron and Egypt.',
            refs: 'Genesis 28 \u2013 46',
            waypoints: [
                {lat:31.25, lng:34.79, label:'Beer-sheba', ref:'Gen 28:10', desc:'Jacob fled from Esau\'s wrath after stealing the blessing. Isaac sent him toward Haran to find a wife from Rebekah\'s family.'},
                {lat:31.93, lng:35.22, label:'Bethel (ladder vision)', ref:'Gen 28:19', desc:'Jacob dreamed of a stairway to heaven with angels ascending and descending. God confirmed the Abrahamic covenant: "I am with you and will keep you wherever you go."'},
                {lat:36.87, lng:39.03, label:'Haran (Laban, 20 years)', ref:'Gen 29:4', desc:'Jacob served Laban 14 years for Rachel and Leah, then 6 more for flocks. The deceiver was deceived \u2014 but God prospered him. Here the twelve tribes began.'},
                {lat:32.33, lng:35.73, label:'Mahanaim (angels)', ref:'Gen 32:1-2', desc:'On his return to Canaan, angels of God met Jacob. He named the place Mahanaim ("two camps") \u2014 a divine council escort for the returning patriarch.'},
                {lat:32.19, lng:35.62, label:'Peniel (wrestles God)', ref:'Gen 32:30', desc:'Jacob wrestled a divine being all night and was renamed Israel ("he strives with God"). His hip was dislocated but he would not let go: "I will not let you go unless you bless me."'},
                {lat:32.21, lng:35.28, label:'Shechem (Dinah)', ref:'Gen 33:18', desc:'Jacob bought land and built an altar: El-Elohe-Israel ("God, the God of Israel"). But Dinah\'s violation led to Simeon and Levi\'s bloody revenge (Gen 34).'},
                {lat:31.93, lng:35.22, label:'Bethel (return)', ref:'Gen 35:1', desc:'God called Jacob back to Bethel. He purged his household of foreign gods, built an altar, and God reaffirmed his name change to Israel and the covenant promises.'},
                {lat:31.53, lng:35.10, label:'Hebron (reunites with Isaac)', ref:'Gen 35:27', desc:'Jacob returned to his father Isaac at Mamre near Hebron. Isaac died at 180; Esau and Jacob buried him together \u2014 brothers reconciled at their father\'s grave.'},
                {lat:30.78, lng:31.77, label:'Goshen, Egypt', ref:'Gen 46:28-29', desc:'At age 130, Jacob descended to Egypt to see Joseph alive. God spoke at Beer-sheba: "Do not be afraid to go down to Egypt, for I will make you into a great nation there."'}
            ]
        },
        {id: 'joseph',
            name: 'Joseph\'s Journey',
            color: '#ec4899',
            weight: 2,
            dash: '8 6',
            desc: 'Sold by his brothers, carried to Egypt by Ishmaelite traders. From slave to prisoner to vizier of all Egypt. Joseph\'s journey is the prototype of suffering producing salvation for many (Gen 50:20).',
            refs: 'Genesis 37 \u2013 50',
            waypoints: [
                {lat:31.53, lng:35.10, label:'Hebron (father\'s home)', ref:'Gen 37:14', desc:'Jacob loved Joseph more than all his sons and gave him the famous coat. Joseph\'s prophetic dreams of ruling his brothers ignited their murderous jealousy.'},
                {lat:32.21, lng:35.28, label:'Shechem (sent to brothers)', ref:'Gen 37:12-14', desc:'Jacob sent Joseph to check on his brothers tending flocks at Shechem. They had moved on to Dothan. Joseph faithfully went looking for them.'},
                {lat:32.41, lng:35.23, label:'Dothan (sold to traders)', ref:'Gen 37:17-28', desc:'His brothers stripped his coat and threw him in a pit. They sold him to Ishmaelite traders for 20 shekels of silver \u2014 foreshadowing Christ\'s betrayal for 30.'},
                {lat:30.60, lng:32.30, label:'Trade route through Sinai', ref:'Gen 37:25', desc:'The caravan carried Joseph down through the Sinai peninsula into Egypt. The incense-laden traders were unwitting instruments of God\'s plan to save the covenant family.'},
                {lat:29.85, lng:31.25, label:'Potiphar\'s house (Memphis)', ref:'Gen 39:1', desc:'Sold to Potiphar, captain of the guard. God blessed everything Joseph touched. He resisted Potiphar\'s wife: "How can I do this great wickedness and sin against God?"'},
                {lat:29.85, lng:31.28, label:'Prison', ref:'Gen 39:20', desc:'Falsely accused, Joseph was imprisoned. Even in prison, God was with him. He interpreted dreams for the cupbearer and baker, demonstrating his God-given gift.'},
                {lat:30.05, lng:31.23, label:'Pharaoh\'s court (vizier)', ref:'Gen 41:39-45', desc:'Joseph interpreted Pharaoh\'s dream of seven years plenty and famine. Pharaoh made him second in command over all Egypt at age 30 \u2014 from pit to palace.'},
                {lat:30.78, lng:31.77, label:'Goshen (family settled)', ref:'Gen 47:6', desc:'Joseph reunited with his family and settled them in Goshen, the best land of Egypt. "You meant evil against me, but God meant it for good" (Gen 50:20).'}
            ]
        },
        {id: 'moses_life',
            name: 'Moses\' Life Journey',
            color: '#e11d48',
            weight: 3,
            dash: '12 4',
            desc: 'Born under a death sentence in Egypt, raised in Pharaoh\'s palace, exiled to Midian, called at the burning bush, led Israel through the Red Sea and wilderness to the edge of the Promised Land.',
            refs: 'Exodus 2 \u2013 Deuteronomy 34',
            waypoints: [
                {lat:30.78, lng:31.77, label:'Goshen (born in slavery)', ref:'Exod 2:1-2', desc:'Born under Pharaoh\'s death decree against Hebrew male infants. His parents hid him three months by faith (Heb 11:23). Moses\' birth was an act of resistance.'},
                {lat:30.45, lng:31.20, label:'Nile (basket in reeds)', ref:'Exod 2:3', desc:'His mother placed him in a waterproofed basket in the Nile reeds. Pharaoh\'s daughter found and adopted him. Miriam arranged for his own mother to nurse him.'},
                {lat:30.05, lng:31.23, label:'Pharaoh\'s Palace (raised)', ref:'Exod 2:10', desc:'Moses was "instructed in all the wisdom of the Egyptians" (Acts 7:22). He chose to share the affliction of God\'s people rather than the pleasures of Pharaoh\'s house.'},
                {lat:28.50, lng:35.00, label:'Midian (40 years exile)', ref:'Exod 2:15', desc:'After killing an Egyptian, Moses fled to Midian. He married Zipporah and shepherded flocks for 40 years. God was preparing the shepherd to lead His flock.'},
                {lat:28.54, lng:33.98, label:'Mount Horeb (burning bush)', ref:'Exod 3:1-4', desc:'A bush burned but was not consumed. God spoke: "I AM WHO I AM." He commissioned Moses to deliver Israel. Moses objected five times; God answered each one.'},
                {lat:30.79, lng:31.83, label:'Egypt (plagues & Exodus)', ref:'Exod 7-12', desc:'Ten plagues struck Egypt, each targeting an Egyptian deity. The final plague \u2014 death of the firstborn \u2014 brought Pharaoh to his knees. Israel departed in triumph.'},
                {lat:29.92, lng:32.55, label:'Red Sea crossing', ref:'Exod 14:21-22', desc:'Trapped between Pharaoh\'s army and the sea, Moses raised his staff. God divided the waters. Israel walked through on dry ground; the sea swallowed Egypt\'s army.'},
                {lat:28.54, lng:33.98, label:'Mount Sinai (Torah given)', ref:'Exod 19-20', desc:'God descended in fire. The mountain quaked. He spoke the Ten Commandments and gave Moses the Torah, the priesthood, and the tabernacle plans. A year-long encampment.'},
                {lat:30.63, lng:34.40, label:'Kadesh-barnea', ref:'Num 13:26', desc:'Moses sent twelve spies into Canaan. When the people believed the bad report, God sentenced them to 40 years of wandering. Even Moses\' intercession could not reverse it.'},
                {lat:31.77, lng:35.73, label:'Mount Nebo (death)', ref:'Deut 34:1-5', desc:'God showed Moses the entire Promised Land: "I have let you see it, but you shall not go over." Moses died at 120, his eye undimmed. God Himself buried His servant.'}
            ]
        },
        {id: 'exodus',
            name: 'The Exodus',
            color: '#f43f5e',
            weight: 4,
            dash: null,
            desc: 'Israel\'s liberation from Egypt through the Red Sea to Mount Sinai. The greatest act of divine intervention in the Old Testament.',
            refs: 'Exodus 12 \u2013 19',
            waypoints: [
                {lat:30.79, lng:31.83, label:'Rameses (departure)', ref:'Exod 12:37', desc:'About 600,000 men plus families departed after the tenth plague \u2014 the death of Egypt\'s firstborn. The Passover lamb\'s blood on the doorposts foreshadowed Christ.'},
                {lat:30.55, lng:32.10, label:'Succoth', ref:'Exod 12:37', desc:'First camp after leaving Egypt. Israel traveled with unleavened bread, their flocks, and the plunder of Egypt. God led them by pillar of cloud and fire.'},
                {lat:30.30, lng:32.35, label:'Etham', ref:'Exod 13:20', desc:'At the edge of the wilderness, God deliberately turned Israel back toward Pi-hahiroth to trap them against the sea \u2014 setting the stage for the greatest deliverance in the OT.'},
                {lat:29.92, lng:32.55, label:'Pi-hahiroth (Red Sea)', ref:'Exod 14:2', desc:'Pharaoh pursued with 600 chariots. Moses stretched his hand over the sea; God divided the waters. Israel crossed on dry ground; the army of Egypt was destroyed.'},
                {lat:29.27, lng:33.08, label:'Marah (bitter water)', ref:'Exod 15:23', desc:'Three days without water. The people grumbled. God showed Moses a tree to make the bitter water sweet \u2014 "I am the LORD, your healer" (Yahweh Rapha).'},
                {lat:28.83, lng:33.18, label:'Elim (12 springs, 70 palms)', ref:'Exod 15:27', desc:'An oasis with 12 springs and 70 palm trees \u2014 one spring per tribe, perhaps one palm per elder. God provided rest and refreshment after the test.'},
                {lat:28.68, lng:33.68, label:'Rephidim (rock, Amalek)', ref:'Exod 17:1', desc:'No water. Moses struck the rock and water flowed. The rock was Christ (1 Cor 10:4). Then Amalek attacked; Moses\' raised hands brought victory through Joshua.'},
                {lat:28.54, lng:33.98, label:'Mount Sinai', ref:'Exod 19:1', desc:'God descended in fire and smoke. The mountain trembled. He gave the Torah, the covenant, and the tabernacle blueprint. Israel camped here nearly a year.'}
            ]
        },
        {id: 'spies_route',
            name: 'Spies\' Route',
            color: '#0ea5e9',
            weight: 2,
            dash: '4 4',
            desc: 'The 12 spies sent from Kadesh-barnea to scout the Promised Land. They went through the Negev to Hebron, cut grapes at Eshcol, and returned after 40 days. Ten gave a bad report; only Caleb and Joshua trusted God.',
            refs: 'Numbers 13 \u2013 14',
            waypoints: [
                {lat:30.63, lng:34.40, label:'Kadesh-barnea (sent out)', ref:'Num 13:3', desc:'Moses sent one leader from each tribe. Their mission: scout the land, the people, the cities, and the soil. It was a test of faith, not just reconnaissance.'},
                {lat:30.85, lng:34.60, label:'Negev (entered from south)', ref:'Num 13:17', desc:'They entered Canaan from the south, ascending through the Negev desert. Moses told them to observe the land\'s fertility and the strength of its inhabitants.'},
                {lat:31.25, lng:34.79, label:'Beer-sheba region', ref:'Num 13:17', desc:'Passing through the patriarchal homeland \u2014 the very land God had promised to Abraham. The spies were walking on covenant ground.'},
                {lat:31.53, lng:35.10, label:'Hebron (saw the Anakim)', ref:'Num 13:22', desc:'They saw Ahiman, Sheshai, and Talmai \u2014 sons of Anak. Hebron was built seven years before Zoan in Egypt, making it one of the oldest cities in the world.'},
                {lat:33.02, lng:35.57, label:'Lebo-hamath (northern extent)', ref:'Num 13:21', desc:'The spies traveled all the way to the northern boundary of the promised land, near the entrance of Hamath in modern Lebanon. A 40-day journey in total.'},
                {lat:31.55, lng:35.08, label:'Return via Eshcol', ref:'Num 13:24-25', desc:'They named the valley Eshcol ("cluster") after the grapes. Returning south after 40 days, the spies carried both extraordinary fruit and extraordinary fear.'},
                {lat:30.63, lng:34.40, label:'Kadesh-barnea (report)', ref:'Num 13:26', desc:'Ten spies said: "We are not able to go up against the people, for they are stronger than we." Only Joshua and Caleb dissented: "The LORD is with us; do not fear them."'}
            ]
        },
        {id: 'balaam',
            name: 'Balaam\'s Journey',
            color: '#8b5cf6',
            weight: 2,
            dash: null,
            desc: 'The pagan diviner Balaam, summoned by Balak to curse Israel, found himself compelled by God to bless them instead. His donkey saw the angel of the LORD blocking the road before Balaam did.',
            refs: 'Numbers 22 \u2013 24',
            waypoints: [
                {lat:36.23, lng:38.17, label:'Pethor (Mesopotamia)', ref:'Num 22:5', desc:'Balak summoned Balaam from Pethor near the Euphrates. Balaam was a known diviner whose curses were feared. God warned him not to go, but Balaam was greedy for the reward.'},
                {lat:34.00, lng:37.00, label:'En route through Syria', ref:'Num 22:21', desc:'God\'s anger burned because Balaam went. The angel of the LORD stood in the road with a drawn sword \u2014 visible to the donkey but invisible to the prophet.'},
                {lat:32.50, lng:36.20, label:'Donkey sees angel', ref:'Num 22:22-35', desc:'The donkey turned aside three times to avoid the angel. Balaam beat her. God opened the donkey\'s mouth: "What have I done to you?" Then God opened Balaam\'s eyes to see the angel.'},
                {lat:31.86, lng:35.56, label:'Plains of Moab (Balak)', ref:'Num 22:36', desc:'Balak met Balaam at the Arnon border. He built seven altars with sacrifices. But every time Balaam opened his mouth to curse, God put blessings in it instead.'},
                {lat:31.77, lng:35.74, label:'Mount Pisgah (blesses Israel)', ref:'Num 23:14', desc:'From the heights, Balaam saw Israel\'s camps. He prophesied: "A star shall come out of Jacob, and a scepter shall rise out of Israel" (Num 24:17) \u2014 a messianic oracle from a pagan prophet.'}
            ]
        },
        {id: 'wilderness',
            name: 'Wilderness Wandering',
            color: '#a78bfa',
            weight: 3,
            dash: '6 4',
            desc: 'The 40-year journey from Sinai through the wilderness to the Plains of Moab. A generation died because they refused to enter the land.',
            refs: 'Numbers 10 \u2013 36',
            waypoints: [
                {lat:28.54, lng:33.98, label:'Mount Sinai (departure)', ref:'Num 10:11', desc:'After nearly a year at Sinai receiving the Law, tabernacle, and priesthood, Israel finally departed with the Ark leading the way.'},
                {lat:30.63, lng:34.40, label:'Kadesh-barnea (spies)', ref:'Num 13:26', desc:'Twelve spies explored Canaan for 40 days. Ten returned terrified of the Anakim giants. Only Joshua and Caleb trusted God: "Do not fear the people of the land."'},
                {lat:30.63, lng:34.40, label:'40 years near Kadesh', ref:'Num 14:33-34', desc:'Because of unbelief, God sentenced the exodus generation to 40 years in the wilderness \u2014 one year for each day the spies explored. An entire generation died.'},
                {lat:30.32, lng:35.40, label:'Edom border (refused passage)', ref:'Num 20:14-21', desc:'Edom (Esau\'s descendants) refused Israel passage through their territory. Israel had to go the long way around \u2014 a detour that tested their patience.'},
                {lat:29.83, lng:35.23, label:'Punon (bronze serpent)', ref:'Num 21:4-9', desc:'The people grumbled. God sent fiery serpents. Moses made a bronze serpent on a pole \u2014 all who looked at it lived. Jesus compared this to His own crucifixion (John 3:14).'},
                {lat:31.38, lng:35.70, label:'Arnon crossing', ref:'Num 21:13', desc:'Israel crossed the Arnon Valley into Amorite territory. They defeated Sihon and Og \u2014 Og of Bashan, last of the Rephaim giants, whose bed was 13 feet long (Deut 3:11).'},
                {lat:31.86, lng:35.56, label:'Plains of Moab', ref:'Num 22:1', desc:'Israel camped opposite Jericho. Here Balak hired Balaam to curse Israel, but God turned every curse into a blessing. The Moabite women later seduced Israel into idolatry.'},
                {lat:31.77, lng:35.73, label:'Mount Nebo (Moses\' death)', ref:'Deut 34:1', desc:'God showed Moses the entire Promised Land. Moses died at 120 with undimmed eyes and vigor. God buried him \u2014 no one knows where. Michael later disputed over his body (Jude 9).'}
            ]
        },
        {id: 'conquest',
            name: 'Conquest of Canaan',
            color: '#6366f1',
            weight: 3,
            dash: '4 4',
            desc: 'Joshua leads Israel across the Jordan to take the Promised Land. The giant clans (Anakim, Rephaim) are driven out.',
            refs: 'Joshua 1 \u2013 12',
            waypoints: [
                {lat:31.86, lng:35.56, label:'Plains of Moab (staging)', ref:'Josh 1:1', desc:'God commissioned Joshua: "Be strong and courageous. Every place your foot treads, I have given it to you." The new generation prepared to enter the Promised Land.'},
                {lat:31.87, lng:35.44, label:'Jericho (walls fall)', ref:'Josh 6', desc:'Israel marched around the city seven days. On the seventh day, at the blast of trumpets and the people\'s shout, the walls collapsed. Jericho was devoted to destruction (herem).'},
                {lat:31.92, lng:35.26, label:'Ai (second assault)', ref:'Josh 8', desc:'After Achan\'s sin caused initial defeat, Joshua conquered Ai with an ambush. He built an altar on Mount Ebal and read the Law to all Israel between Ebal and Gerizim.'},
                {lat:31.85, lng:35.18, label:'Gibeon (sun stands still)', ref:'Josh 10:12', desc:'Five Amorite kings attacked Gibeon. God hurled hailstones from heaven. Joshua commanded: "Sun, stand still at Gibeon" \u2014 and the sun stopped for a full day. Cosmic warfare.'},
                {lat:31.61, lng:34.85, label:'Gath (Anakim remnant)', ref:'Josh 11:22', desc:'Joshua cut off the Anakim from the hill country. Only in Gaza, Gath, and Ashdod did some remain \u2014 the same Gath that would later produce Goliath.'},
                {lat:31.53, lng:35.10, label:'Hebron (Caleb takes it)', ref:'Josh 14:12-15', desc:'85-year-old Caleb said: "Give me this hill country where the Anakim are." He drove out the three sons of Anak and took Hebron \u2014 faith conquering giants.'},
                {lat:33.02, lng:35.57, label:'Hazor (head of kingdoms)', ref:'Josh 11:10', desc:'The greatest Canaanite city. Joshua struck Jabin its king and burned Hazor \u2014 the only city in the north he burned. God gave Israel rest from war.'},
                {lat:32.21, lng:35.28, label:'Shechem (covenant renewal)', ref:'Josh 24', desc:'Joshua gathered all Israel: "Choose this day whom you will serve." They answered: "We will serve the LORD." Joshua set up a stone of witness under the oak at Shechem.'}
            ]
        },
        {id: 'philistine_migration',
            name: 'Philistine / Sea Peoples Migration from Caphtor',
            color: '#0891b2',
            weight: 2,
            dash: '12 6',
            desc: 'God brought the Philistines from Caphtor (Amos 9:7) \u2014 widely identified with Crete/Aegean. They displaced the Avvim (Deut 2:23) and settled the coastal plain where Anakim remnants remained (Josh 11:22). The Sea Peoples invasion (~1200 BC) brought further waves. God sovereignly placed them as persistent enemies to test Israel\'s faith (Judg 3:1-4).',
            refs: 'Genesis 10:13-14; Deuteronomy 2:23; Amos 9:7; Jeremiah 47:4',
            waypoints: [
                {lat:35.3, lng:25.1, label:'Caphtor (Crete) \u2014 Philistine origin', ref:'Amos 9:7', desc:'God sovereignly moved the Philistines from Caphtor (Crete/Aegean region). They were part of the Sea Peoples migrations that reshaped the ancient Mediterranean.'},
                {lat:34.7, lng:29.0, label:'Eastern Mediterranean route', ref:'Deut 2:23', desc:'The Philistines displaced the Avvim who lived in villages as far as Gaza. This migration was part of the broader Sea Peoples movement (~1200 BC).'},
                {lat:33.0, lng:33.0, label:'Cyprus (staging area)', ref:'Gen 10:14', desc:'Cyprus served as a staging point for the Sea Peoples\' eastward push. Philistine pottery found here shows their migration path from the Aegean.'},
                {lat:31.80, lng:34.65, label:'Ashdod \u2014 Philistine Pentapolis', ref:'Josh 11:22', desc:'One of five Philistine cities. The Ark of the Covenant was placed in Dagon\'s temple here, and Dagon fell before it. Anakim remnants survived in Ashdod.'},
                {lat:31.67, lng:34.57, label:'Ashkelon \u2014 Philistine Pentapolis', ref:'Judg 14:19', desc:'Samson killed 30 men here to pay his wedding bet. Ashkelon was a major port city known for its metalworking \u2014 iron technology the Philistines monopolized.'},
                {lat:31.50, lng:34.47, label:'Gaza \u2014 Philistine Pentapolis', ref:'Josh 11:22', desc:'The southernmost Philistine city. Samson carried its gates to a hilltop and later died destroying the temple of Dagon here. Anakim remnants survived in Gaza.'},
                {lat:31.70, lng:34.85, label:'Gath \u2014 Home of Goliath & giants', ref:'1 Sam 17:4', desc:'Gath produced Goliath and four other giants (2 Sam 21). It was the city where Anakim remnants were strongest. David feigned madness here when fleeing Saul.'},
                {lat:31.78, lng:34.85, label:'Ekron \u2014 Philistine Pentapolis', ref:'1 Sam 5:10', desc:'The northern Philistine city. When the Ark arrived here, the people cried out in terror. Ekron was associated with Baal-zebub, "lord of the flies" (2 Kgs 1:2).'}
            ]
        },
        {id: 'ark_journey',
            name: 'Ark of the Covenant',
            color: '#14b8a6',
            weight: 3,
            dash: null,
            desc: 'The Ark\'s journey from Sinai through the wilderness, into Canaan, captured by the Philistines, and finally brought to Jerusalem by David. The physical throne of God among men.',
            refs: 'Exodus 25 \u2013 2 Samuel 6',
            waypoints: [
                {lat:28.54, lng:33.98, label:'Sinai (Ark constructed)', ref:'Exod 25:10-22', desc:'Built by Bezalel from acacia wood overlaid with pure gold. Inside: the tablets of the Law, Aaron\'s rod, and a jar of manna. The mercy seat was God\'s earthly throne.'},
                {lat:30.63, lng:34.40, label:'Wilderness (Kadesh)', ref:'Num 10:33', desc:'The Ark traveled before Israel to "search out a resting place." When it set out, Moses declared: "Arise, O LORD, and let your enemies be scattered."'},
                {lat:31.87, lng:35.44, label:'Jordan crossing (Jericho)', ref:'Josh 3:14-17', desc:'When the priests carrying the Ark stepped into the Jordan, the waters piled up upstream. Israel crossed on dry ground \u2014 a second Red Sea miracle.'},
                {lat:31.87, lng:35.44, label:'Jericho (walls fall)', ref:'Josh 6:6-20', desc:'The Ark was carried around Jericho for seven days. On the seventh day, at the trumpet blast and the people\'s shout, the walls collapsed. God fought for Israel.'},
                {lat:32.06, lng:35.29, label:'Shiloh (tabernacle)', ref:'Josh 18:1', desc:'The tabernacle was set up at Shiloh, and the Ark rested there for ~300 years. It became the central sanctuary for all Israel during the period of the judges.'},
                {lat:31.85, lng:35.18, label:'Ebenezer (captured!)', ref:'1 Sam 4:11', desc:'Israel brought the Ark to battle as a good-luck charm. God allowed the Philistines to capture it. Eli\'s sons were killed, and Eli died upon hearing the news. "The glory has departed from Israel."'},
                {lat:31.80, lng:34.65, label:'Ashdod (Dagon falls)', ref:'1 Sam 5:1-5', desc:'The Philistines placed the Ark in Dagon\'s temple. The next morning, Dagon was face-down before the Ark. The second morning, his head and hands were broken off. God needs no army.'},
                {lat:31.61, lng:34.85, label:'Gath (plagues)', ref:'1 Sam 5:8-9', desc:'They moved the Ark to Gath. God struck the city with tumors. Panic seized them \u2014 the Ark was too dangerous to keep.'},
                {lat:31.78, lng:34.85, label:'Ekron (cries of terror)', ref:'1 Sam 5:10', desc:'When the Ark arrived at Ekron, the people cried out: "They have brought the ark of the God of Israel to us to kill us!" Seven months of plagues convinced them to send it back.'},
                {lat:31.75, lng:34.97, label:'Beth-shemesh (returned)', ref:'1 Sam 6:12-19', desc:'The Philistines sent the Ark back on a new cart pulled by cows. Men of Beth-shemesh looked inside and God struck 70 of them \u2014 holiness cannot be trifled with.'},
                {lat:31.80, lng:35.10, label:'Kiriath-jearim (20 years)', ref:'1 Sam 7:1-2', desc:'The Ark rested in Abinadab\'s house for 20 years. Israel mourned and sought the LORD. Samuel led a revival at Mizpah, and the Philistines were subdued.'},
                {lat:31.78, lng:35.24, label:'Jerusalem (David\'s city)', ref:'2 Sam 6:12-17', desc:'David brought the Ark to Jerusalem with shouting and the sound of the horn. He danced before the LORD with all his might. The Ark found its final home.'}
            ]
        },
        {id: 'giant_slayer',
            name: 'Giant Slayer Trail (Joshua \u2192 Caleb \u2192 David)',
            color: '#fb7185',
            weight: 3,
            dash: null,
            desc: 'The progression of God\'s giant-slaying champions. Joshua cleared the Anakim from the hill country (Josh 11:21). Caleb personally took Hebron \u2014 the Anakim stronghold (Josh 14:12). David and his men killed the last five Rephaim descendants in Philistia (1 Sam 17; 2 Sam 21). All point to Christ who destroys every enemy power (1 Cor 15:25-26; Heb 2:14).',
            refs: 'Joshua 11:21-22; 14:12-15; 1 Samuel 17; 2 Samuel 21:15-22',
            waypoints: [
                {lat:31.87, lng:35.44, label:'Jericho (walls fall)', ref:'Josh 6', desc:'The first city to fall. God fought with supernatural power \u2014 walls collapsed at a shout. The conquest began not with human might but divine intervention.'},
                {lat:33.02, lng:35.57, label:'Hazor (head of kingdoms)', ref:'Josh 11:10', desc:'Joshua defeated Jabin\'s coalition. He "cut off the Anakim from the hill country" (Josh 11:21). The systematic removal of the giant clans from the land of promise.'},
                {lat:31.53, lng:35.10, label:'Hebron (Caleb drives out Anakim)', ref:'Josh 14:12-15', desc:'85-year-old Caleb claimed the giants\' stronghold: "Give me this hill country." He drove out the three sons of Anak. The faith of the minority spy, 45 years later, still burned.'},
                {lat:31.69, lng:34.96, label:'Valley of Elah (David kills Goliath)', ref:'1 Sam 17:49', desc:'Goliath \u2014 over 9 feet tall, champion of Gath. David faced him with a sling and five stones: "I come in the name of the LORD of hosts." One stone. One kill.'},
                {lat:31.70, lng:34.85, label:'Gath (four more giants killed)', ref:'2 Sam 21:15-22', desc:'David\'s warriors killed four more Rephaim descendants: Ishbi-benob, Saph, a man with six fingers and six toes, and the brother of Goliath. The giant line was finished.'},
                {lat:31.50, lng:34.47, label:'Gaza (last Anakim holdout)', ref:'Josh 11:22', desc:'Gaza, Gath, and Ashdod \u2014 the only places Anakim survived Joshua\'s purge. These Philistine cities harbored the remnant until David\'s generation completed the work.'}
            ]
        },
        {id: 'david_flight',
            name: 'David\'s Flight from Saul',
            color: '#60a5fa',
            weight: 2,
            dash: null,
            desc: 'Anointed king but hunted like an animal. David fled from Saul across the Judean wilderness for years, gathering a band of outcasts who became his mighty men. He refused to kill God\'s anointed.',
            refs: '1 Samuel 19 \u2013 30',
            waypoints: [
                {lat:31.82, lng:35.23, label:'Gibeah (flees Saul\'s spear)', ref:'1 Sam 19:10', desc:'Saul hurled a spear at David while he played the lyre. David fled into the night. The anointed king became a fugitive \u2014 a pattern Christ would also follow.'},
                {lat:31.79, lng:35.24, label:'Nob (gets Goliath\'s sword)', ref:'1 Sam 21:1-9', desc:'David went to Ahimelech the priest, ate the showbread (cited by Jesus in Matt 12:3-4), and took Goliath\'s sword. Saul later massacred the priests of Nob for helping David.'},
                {lat:31.61, lng:34.85, label:'Gath (feigns madness)', ref:'1 Sam 21:10-15', desc:'David fled to Goliath\'s own city. Recognized and afraid, he scratched on doors and let spittle run down his beard, pretending madness. The king dismissed him.'},
                {lat:31.62, lng:34.98, label:'Cave of Adullam (400 men)', ref:'1 Sam 22:1', desc:'Everyone in distress, in debt, or discontented gathered to David \u2014 about 400 men. These outcasts became his mighty warriors. Many psalms were written from this cave.'},
                {lat:31.62, lng:35.05, label:'Keilah (rescues from Philistines)', ref:'1 Sam 23:1-5', desc:'David saved Keilah from the Philistines, but God warned that the city would betray him to Saul. David moved on \u2014 even those he rescued would not shelter him.'},
                {lat:31.43, lng:35.12, label:'Wilderness of Ziph (betrayed)', ref:'1 Sam 23:14-15', desc:'The Ziphites told Saul where David was hiding. Jonathan found David and "strengthened his hand in God" \u2014 their last meeting. Saul pursued relentlessly.'},
                {lat:31.47, lng:35.39, label:'En-gedi (spares Saul)', ref:'1 Sam 24:1-22', desc:'Saul entered the very cave where David hid. David cut his robe but refused to kill him: "I will not put out my hand against the LORD\'s anointed." Radical faith in God\'s timing.'},
                {lat:31.35, lng:34.58, label:'Ziklag (Philistine base)', ref:'1 Sam 27:5-7', desc:'Achish of Gath gave David Ziklag. He operated from Philistine territory for 16 months, raiding Israel\'s enemies while Saul thought him lost. A dark but providential period.'}
            ]
        },
        {id: 'elijah',
            name: 'Elijah\'s Journey',
            color: '#d946ef',
            weight: 2,
            dash: '6 4',
            desc: 'From Gilead to Mount Carmel\'s dramatic showdown with Baal\'s prophets, then fleeing Jezebel to Beer-sheba and onward 40 days to Horeb/Sinai where God spoke in the still small voice.',
            refs: '1 Kings 17 \u2013 19',
            waypoints: [
                {lat:32.40, lng:35.78, label:'Gilead (Tishbe, home)', ref:'1 Kgs 17:1', desc:'Elijah appeared without introduction: "As the LORD the God of Israel lives, before whom I stand, there shall be no rain." One man against a nation\'s apostasy.'},
                {lat:32.00, lng:35.55, label:'Brook Cherith (ravens)', ref:'1 Kgs 17:3-6', desc:'God hid Elijah by the brook and sent ravens to feed him morning and evening with bread and meat. When the brook dried up, God moved him to the next provision.'},
                {lat:33.45, lng:35.29, label:'Zarephath (widow)', ref:'1 Kgs 17:9', desc:'A Sidonian widow, down to her last meal, fed Elijah. Her flour and oil never ran out. When her son died, Elijah raised him \u2014 the first resurrection in Scripture.'},
                {lat:32.74, lng:35.04, label:'Mount Carmel (fire falls)', ref:'1 Kgs 18:19-40', desc:'Elijah vs. 450 prophets of Baal. "How long will you go limping between two opinions?" He built an altar, soaked it with water, and fire fell from heaven consuming everything.'},
                {lat:31.25, lng:34.79, label:'Beer-sheba (fled Jezebel)', ref:'1 Kgs 19:3', desc:'After the greatest victory, Elijah\'s greatest depression. Jezebel threatened him; he ran to Beer-sheba and collapsed under a broom tree: "Take away my life."'},
                {lat:28.54, lng:33.98, label:'Horeb/Sinai (still small voice)', ref:'1 Kgs 19:8-12', desc:'Sustained by angelic food, Elijah walked 40 days to Horeb. God was not in the wind, earthquake, or fire \u2014 but in the still small voice. "What are you doing here, Elijah?"'}
            ]
        },
        {id: 'phoenician_trade',
            name: 'Phoenician Trade Route \u2014 Cursed Line Spreads',
            color: '#7c3aed',
            weight: 2,
            dash: '10 4',
            desc: 'The Phoenicians (= cursed Canaanites, Gen 9:25 + 10:15) built the greatest maritime trade network of the ancient world. Master seafarers, they established colonies across the Mediterranean, spreading both commerce and Baal worship (including child sacrifice). God sovereignly used their skills: their 22-letter alphabet (~1050 BC) became the direct ancestor of Greek, Latin, and every modern Western alphabet \u2014 the writing system God chose for His Word. Their cedar supplied His Temple. Yet everywhere they went, they carried their abominations (Lev 18:21; Deut 12:31).',
            refs: 'Gen 10:15-19; 1 Kings 5:1-12; Ezek 27 (full chapter \u2014 Tyre\'s trade catalog); Isa 23',
            waypoints: [
                {lat:34.12, lng:35.65, label:'Byblos (Gebal) \u2014 oldest city, papyrus/alphabet', ref:'1 Kings 5:18', desc:'One of the world\'s oldest continuously inhabited cities. The Phoenician alphabet was developed here \u2014 ancestor of Greek, Latin, and all Western alphabets. Gebalites helped build Solomon\'s Temple.'},
                {lat:33.56, lng:35.38, label:'Sidon \u2014 Canaan\'s firstborn', ref:'Gen 10:15', desc:'Named after Canaan\'s firstborn son (Gen 10:15). A major Phoenician port. Jezebel was a Sidonian princess who brought Baal worship to Israel. Jesus ministered in this region.'},
                {lat:33.27, lng:35.20, label:'Tyre \u2014 island fortress, purple dye capital', ref:'Ezek 27', desc:'The wealthiest city of the ancient world. Its king is addressed in Ezekiel 28 with language echoing the fall of a divine being. Hiram of Tyre supplied cedar for Solomon\'s Temple.'},
                {lat:34.68, lng:33.04, label:'Kition (Cyprus) \u2014 major colony', ref:'Ezek 27:6', desc:'A major Phoenician colony on Cyprus. Oaks from Bashan made their oars (Ezek 27:6). Cyprus was a staging point for Phoenician expansion westward.'},
                {lat:37.50, lng:15.09, label:'Syracuse (Sicily) \u2014 trading post', ref:'Ezek 27:13', desc:'Phoenicians established trading posts in Sicily. Paul later stopped at Syracuse on his voyage to Rome (Acts 28:12). Commerce and gospel both traveled these sea lanes.'},
                {lat:39.22, lng:9.11, label:'Nora (Sardinia) \u2014 Phoenician settlement', ref:'Ezek 27:12', desc:'One of the oldest Phoenician colonies in the western Mediterranean. A Phoenician inscription found here is among the earliest alphabetic texts in the West.'},
                {lat:35.90, lng:14.51, label:'Malta \u2014 strategic waypoint', ref:'Acts 28:1', desc:'A key staging point on Phoenician trade routes. Paul was later shipwrecked here (Acts 28) \u2014 God sent the gospel along the same routes the Canaanites had sailed.'},
                {lat:36.85, lng:10.32, label:'Carthage \u2014 greatest colony, child sacrifice tophet', ref:'Deut 12:31', desc:'Founded by Tyre. Became the greatest Phoenician power. Archaeological evidence confirms child sacrifice in the tophet. The curse of Canaan (Gen 9:25) spread wherever they colonized.'},
                {lat:36.53, lng:-6.30, label:'Gades (C\u00e1diz, Spain) \u2014 western terminus', ref:'Ezek 27:12 (Tarshish?)', desc:'The western limit of Phoenician trade, beyond the Pillars of Hercules. Possibly the biblical Tarshish \u2014 Jonah tried to flee to the ends of the earth to escape God\'s call.'}
            ]
        },
        {id: 'jesus_galilee',
            name: 'Jesus\' Galilean Ministry',
            color: '#2563eb',
            weight: 3,
            dash: '6 4',
            desc: 'From baptism through the major Galilean ministry \u2014 healing, teaching, calling disciples, and revealing the Kingdom of God. Jesus based His ministry in Capernaum and traveled throughout Galilee, Tyre/Sidon, and the Decapolis.',
            refs: 'Matthew 3\u201317; Mark 1\u20139; Luke 3\u20139',
            waypoints: [
                {lat:32.71, lng:35.30, label:'Nazareth \u2014 hometown, rejected', ref:'Luke 4:16-30', desc:'Jesus grew up here, then was rejected in His own synagogue after reading Isaiah 61 and claiming its fulfillment: "Today this Scripture has been fulfilled in your hearing."'},
                {lat:31.84, lng:35.55, label:'Jordan River \u2014 baptism by John', ref:'Matt 3:13-17', desc:'The heavens opened, the Spirit descended like a dove, and the Father spoke: "This is my beloved Son." A divine council moment \u2014 all three persons of the Godhead present.'},
                {lat:31.62, lng:35.45, label:'Judean Wilderness \u2014 40 days temptation', ref:'Matt 4:1-11', desc:'Satan tested Jesus three times, echoing Israel\'s 40-year wilderness failure. Where Israel failed, Jesus succeeded \u2014 quoting Deuteronomy each time.'},
                {lat:32.88, lng:35.52, label:'Capernaum \u2014 ministry headquarters', ref:'Matt 4:13', desc:'Jesus made this fishing village His base. Here He healed Peter\'s mother-in-law, the centurion\'s servant, and the paralytic lowered through the roof.'},
                {lat:32.87, lng:35.57, label:'Sea of Galilee \u2014 calling of disciples', ref:'Matt 4:18-22', desc:'Jesus called Peter, Andrew, James, and John from their fishing nets: "Follow me, and I will make you fishers of men." Later He walked on these waters.'},
                {lat:32.63, lng:35.35, label:'Nain \u2014 widow\'s son raised', ref:'Luke 7:11-17', desc:'Jesus raised the widow\'s only son from the dead. The crowd proclaimed: "A great prophet has arisen among us! God has visited his people!"'},
                {lat:32.91, lng:35.63, label:'Bethsaida \u2014 feeding of 5,000', ref:'Luke 9:10-17', desc:'Near here Jesus fed 5,000 with five loaves and two fish. The twelve baskets of leftovers signify the twelve tribes of Israel being fed by their Messiah.'},
                {lat:33.27, lng:35.22, label:'Tyre & Sidon \u2014 Gentile ministry', ref:'Matt 15:21-28', desc:'A Canaanite woman\'s faith moved Jesus: "O woman, great is your faith!" He healed her daughter, showing the Kingdom extends beyond Israel\'s borders.'},
                {lat:33.25, lng:35.69, label:'Caesarea Philippi \u2014 Peter\'s confession', ref:'Matt 16:13-20', desc:'At the Gates of Hades (Pan\'s grotto), Peter declared "You are the Christ, the Son of the living God." Jesus announced He would build His church against the gates of Hades.'},
                {lat:33.42, lng:35.86, label:'Mount Hermon \u2014 Transfiguration', ref:'Matt 17:1-8', desc:'Jesus was transfigured \u2014 face shining like the sun. Moses and Elijah appeared. The Father\'s voice: "This is my beloved Son; listen to him." A divine council throne-room vision.'}
            ]
        },
        {id: 'jesus_final_week',
            name: 'Jesus\' Final Week \u2014 Jerusalem',
            color: '#dc2626',
            weight: 4,
            dash: null,
            desc: 'The last week of Jesus\' earthly ministry in Jerusalem \u2014 from the Triumphal Entry through the crucifixion and resurrection. Every location carries immense theological weight.',
            refs: 'Matthew 21\u201328; Mark 11\u201316; Luke 19\u201324; John 12\u201321',
            waypoints: [
                {lat:31.771, lng:35.244, label:'Bethphage/Bethany \u2014 Triumphal Entry begins', ref:'Matt 21:1-11', desc:'Jesus rode a donkey into Jerusalem, fulfilling Zechariah 9:9. The crowds cried "Hosanna to the Son of David!" \u2014 a royal messianic claim.'},
                {lat:31.778, lng:35.236, label:'Temple \u2014 cleansing and teaching', ref:'Matt 21:12-13', desc:'Jesus drove out the money-changers: "My house shall be called a house of prayer." He then taught daily in the Temple courts, clashing with religious leaders.'},
                {lat:31.779, lng:35.230, label:'Upper Room \u2014 Last Supper', ref:'Matt 26:17-30', desc:'Jesus instituted the Lord\'s Supper, washing the disciples\' feet. "This is my blood of the covenant, poured out for many for the forgiveness of sins."'},
                {lat:31.779, lng:35.241, label:'Gethsemane \u2014 agony and arrest', ref:'Matt 26:36-56', desc:'"My soul is very sorrowful, even to death." Jesus sweat drops of blood, then was betrayed by Judas with a kiss and arrested by the Temple guard.'},
                {lat:31.775, lng:35.229, label:'House of Caiaphas \u2014 Jewish trial', ref:'Matt 26:57-68', desc:'The high priest asked: "Are you the Christ, the Son of the Blessed?" Jesus replied: "I am, and you will see the Son of Man seated at the right hand of Power." They condemned Him for blasphemy.'},
                {lat:31.778, lng:35.228, label:'Pilate\'s Praetorium \u2014 Roman trial', ref:'Matt 27:11-26', desc:'Pilate found no guilt but yielded to the crowd. "What shall I do with Jesus who is called Christ?" They cried: "Let him be crucified!"'},
                {lat:31.779, lng:35.230, label:'Golgotha \u2014 the Crucifixion', ref:'Matt 27:33-56', desc:'At the Place of the Skull, Jesus was crucified between two criminals. Darkness covered the land. "My God, my God, why have you forsaken me?" The temple veil tore from top to bottom.'},
                {lat:31.7798, lng:35.2298, label:'Garden Tomb \u2014 Resurrection', ref:'Matt 28:1-10', desc:'"He is not here, for he has risen." The angel rolled away the stone \u2014 not to let Jesus out, but to let the witnesses in. The resurrection is the vindication of the Son of God.'}
            ]
        },
        {id: 'paul_journey1',
            name: 'Paul\'s 1st Missionary Journey',
            color: '#16a34a',
            weight: 3,
            dash: '10 5',
            desc: 'The first organized Gentile mission. Paul and Barnabas, sent by the Holy Spirit from Antioch, traveled through Cyprus and southern Asia Minor. This journey established the pattern: synagogue first, then Gentiles.',
            refs: 'Acts 13\u201314',
            waypoints: [
                {lat:36.20, lng:36.16, label:'Antioch (Syria) \u2014 sent by the Holy Spirit', ref:'Acts 13:1-3', desc:'The church at Antioch fasted and prayed. The Holy Spirit said: "Set apart for me Barnabas and Saul for the work to which I have called them."'},
                {lat:36.12, lng:35.92, label:'Seleucia \u2014 port of departure', ref:'Acts 13:4', desc:'The seaport of Antioch. Paul and Barnabas, accompanied by John Mark, sailed from here to Cyprus.'},
                {lat:35.18, lng:33.89, label:'Salamis (Cyprus) \u2014 synagogue preaching', ref:'Acts 13:5', desc:'They proclaimed the word of God in the synagogues of the Jews. This was Paul\'s consistent pattern: to the Jew first.'},
                {lat:34.76, lng:32.41, label:'Paphos \u2014 Bar-Jesus blinded', ref:'Acts 13:6-12', desc:'The sorcerer Bar-Jesus opposed them before the proconsul Sergius Paulus. Paul struck him blind. The proconsul believed, astonished at the teaching of the Lord.'},
                {lat:36.93, lng:30.64, label:'Perga \u2014 John Mark departs', ref:'Acts 13:13', desc:'John Mark left and returned to Jerusalem \u2014 a decision that later caused Paul and Barnabas to separate (Acts 15:37-39).'},
                {lat:38.30, lng:30.53, label:'Pisidian Antioch \u2014 Paul\'s first major sermon', ref:'Acts 13:14-52', desc:'In the synagogue, Paul preached Israel\'s history culminating in Jesus. "Through this man forgiveness of sins is proclaimed to you." The Gentiles begged to hear more.'},
                {lat:37.68, lng:31.87, label:'Iconium \u2014 believed and opposed', ref:'Acts 14:1-7', desc:'A great number of both Jews and Greeks believed, but the city was divided. When they learned of a plot to stone them, Paul and Barnabas fled to Lycaonia.'},
                {lat:37.87, lng:32.49, label:'Lystra \u2014 healed lame man, then stoned', ref:'Acts 14:8-20', desc:'After healing a lame man, the crowd called them Zeus and Hermes. Paul barely stopped them from sacrificing. Then Jews arrived and stoned Paul, leaving him for dead.'},
                {lat:37.35, lng:33.25, label:'Derbe \u2014 many disciples made', ref:'Acts 14:20-21', desc:'Paul and Barnabas preached and made many disciples. Then they courageously retraced their steps through the hostile cities to strengthen the new believers.'},
                {lat:36.20, lng:36.16, label:'Return to Antioch \u2014 mission report', ref:'Acts 14:26-28', desc:'They gathered the church and declared all that God had done with them, and how He had opened a door of faith to the Gentiles.'}
            ]
        },
        {id: 'paul_journey2',
            name: 'Paul\'s 2nd Missionary Journey',
            color: '#9333ea',
            weight: 3,
            dash: '6 3 2 3',
            desc: 'The gospel enters Europe. Paul (now with Silas) revisited Asian churches, then crossed into Macedonia by divine vision. This journey produced 1 & 2 Thessalonians and established churches in Philippi, Thessalonica, and Corinth.',
            refs: 'Acts 15:36 \u2013 18:22',
            waypoints: [
                {lat:36.20, lng:36.16, label:'Antioch (Syria) \u2014 departure with Silas', ref:'Acts 15:40', desc:'After the Jerusalem Council resolved the Gentile question, Paul chose Silas and departed, commended by the brothers to the grace of the Lord.'},
                {lat:37.35, lng:33.25, label:'Derbe & Lystra \u2014 Timothy joins', ref:'Acts 16:1-5', desc:'Paul recruited young Timothy, son of a Jewish mother and Greek father. He circumcised Timothy because of the Jews in those areas \u2014 a pastoral decision, not a doctrinal one.'},
                {lat:39.74, lng:26.14, label:'Troas \u2014 Macedonian vision', ref:'Acts 16:8-10', desc:'A man from Macedonia appeared in a vision: "Come over and help us." Luke joins the team here (note the shift to "we"). The gospel heads to Europe.'},
                {lat:41.01, lng:24.30, label:'Philippi \u2014 Lydia, prison, earthquake', ref:'Acts 16:11-40', desc:'First European convert: Lydia, a dealer in purple cloth. Paul and Silas were beaten and imprisoned, but sang hymns at midnight. An earthquake freed them; the jailer believed.'},
                {lat:40.63, lng:22.94, label:'Thessalonica \u2014 "turned the world upside down"', ref:'Acts 17:1-9', desc:'Paul reasoned from Scripture that Christ had to suffer and rise. Many believed, but opponents accused them of turning the world upside down.'},
                {lat:40.51, lng:22.35, label:'Berea \u2014 "more noble" searchers', ref:'Acts 17:10-15', desc:'The Bereans received the word with all eagerness, examining the Scriptures daily. They became the model for careful Bible study.'},
                {lat:37.97, lng:23.72, label:'Athens \u2014 Mars Hill sermon', ref:'Acts 17:16-34', desc:'Paul stood before the Areopagus: "The God who made the world does not live in temples made by man." He quoted Greek poets and proclaimed the resurrection.'},
                {lat:37.94, lng:22.93, label:'Corinth \u2014 18 months of ministry', ref:'Acts 18:1-17', desc:'Paul worked as a tentmaker with Aquila and Priscilla. The Lord spoke: "Do not be afraid; I have many people in this city." He stayed 18 months, writing 1 & 2 Thessalonians.'},
                {lat:37.94, lng:27.34, label:'Ephesus \u2014 brief visit, promises return', ref:'Acts 18:19-21', desc:'Paul stopped briefly at Ephesus, reasoning in the synagogue. He promised to return if God wills \u2014 and he would, for over two years on his third journey.'},
                {lat:32.49, lng:34.89, label:'Caesarea Maritima \u2014 landing', ref:'Acts 18:22', desc:'Paul landed at Caesarea and went up to greet the church, then returned to Antioch, completing the second missionary circuit.'},
                {lat:31.78, lng:35.24, label:'Jerusalem \u2014 greeted the church', ref:'Acts 18:22', desc:'A brief visit to the Jerusalem church, maintaining the connection between the Gentile mission and the mother church.'},
                {lat:36.20, lng:36.16, label:'Return to Antioch \u2014 journey complete', ref:'Acts 18:22', desc:'Paul returned to Antioch, completing the second circuit. The gospel had now reached Europe and major Roman cities.'}
            ]
        },
        {id: 'paul_journey3',
            name: 'Paul\'s 3rd Missionary Journey',
            color: '#0d9488',
            weight: 3,
            dash: '12 4 4 4',
            desc: 'Paul\'s longest journey, centered on a 2+ year ministry in Ephesus. He wrote 1 Corinthians from Ephesus, then traveled through Macedonia to Corinth (writing Romans), and returned via Troas to Miletus for a tearful farewell to the Ephesian elders.',
            refs: 'Acts 18:23 \u2013 21:17',
            waypoints: [
                {lat:36.20, lng:36.16, label:'Antioch \u2014 third departure', ref:'Acts 18:23', desc:'Paul departed again, going from place to place through the region of Galatia and Phrygia, strengthening all the disciples.'},
                {lat:38.70, lng:34.80, label:'Galatia & Phrygia \u2014 strengthening churches', ref:'Acts 18:23', desc:'Paul revisited the inland churches he had planted, strengthening the believers. These were the communities he would later address in his letter to the Galatians.'},
                {lat:37.94, lng:27.34, label:'Ephesus \u2014 2+ years of ministry', ref:'Acts 19:1-41', desc:'Paul\'s longest stay in one city. All the residents of Asia heard the word. Extraordinary miracles, burning of magic books, and the riot of the silversmiths. He wrote 1 Corinthians from here.'},
                {lat:41.01, lng:24.30, label:'Macedonia \u2014 encouragement tour', ref:'Acts 20:1-2', desc:'Paul traveled through Macedonia, encouraging the churches in Philippi, Thessalonica, and Berea. He likely wrote 2 Corinthians during this leg.'},
                {lat:37.94, lng:22.93, label:'Corinth \u2014 3 months, wrote Romans', ref:'Acts 20:2-3', desc:'Paul spent three winter months in Corinth. Here he wrote Romans \u2014 his magnum opus \u2014 laying out the gospel systematically before his planned visit to Rome.'},
                {lat:39.74, lng:26.14, label:'Troas \u2014 Eutychus falls from window', ref:'Acts 20:6-12', desc:'Paul preached until midnight. Young Eutychus fell asleep and tumbled from a third-story window. Paul embraced him: "His life is in him." He was taken away alive.'},
                {lat:37.54, lng:27.26, label:'Miletus \u2014 farewell to Ephesian elders', ref:'Acts 20:17-38', desc:'Paul summoned the elders for a tearful farewell: "I know that none of you will see my face again." He warned of wolves entering the flock and commended them to God.'},
                {lat:36.40, lng:28.22, label:'Cos & Rhodes \u2014 island stops', ref:'Acts 21:1', desc:'Brief stops at the islands of Cos and Rhodes as Paul sailed southeast toward the Levant, determined to reach Jerusalem by Pentecost.'},
                {lat:34.43, lng:35.84, label:'Tyre \u2014 warned not to go to Jerusalem', ref:'Acts 21:3-6', desc:'The disciples at Tyre, through the Spirit, told Paul not to go to Jerusalem. But Paul was resolved. They all knelt on the beach and prayed before parting.'},
                {lat:32.49, lng:34.89, label:'Caesarea \u2014 Agabus\' prophecy', ref:'Acts 21:8-14', desc:'The prophet Agabus bound his own hands with Paul\'s belt: "The Jews at Jerusalem will bind the owner." Paul replied: "I am ready to die for the name of the Lord Jesus."'},
                {lat:31.78, lng:35.24, label:'Jerusalem \u2014 arrival and arrest', ref:'Acts 21:15-17', desc:'Paul arrived bearing the Gentile churches\' financial gift. Within days he would be arrested in the Temple, beginning his long journey to Rome as a prisoner.'}
            ]
        },
        {id: 'ron_wyatt',
            name: 'Ron Wyatt Archaeological Discoveries',
            color: '#e63946',
            weight: 4,
            dash: '10 6',
            desc: 'Ron Wyatt (1933–1999) was an American nurse anesthetist and amateur archaeologist who claimed to have discovered numerous significant biblical sites between the 1970s and 1990s. His findings — including Noah\'s Ark, the Red Sea crossing site, the real Mount Sinai, and the Ark of the Covenant — remain highly controversial among professional archaeologists and are rejected by mainstream academia. Nevertheless, several of the physical sites he identified are real geological and archaeological features that continue to attract serious independent investigation. This journey traces his claimed discoveries in rough biblical-chronological order, from the Flood to the Exodus to the destruction of Sodom, and finally to Jerusalem.',
            refs: 'Gen 6–8; Gen 19; Ex 14–17; Ex 19; 2 Chr 35:3; Jer 3:16; Matt 27:33; Gal 4:25',
            waypoints: [
                {lat:39.4397, lng:44.2340, label:'Durupınar Site — Claimed Noah\'s Ark', ref:'Genesis 8:4', desc:'A boat-shaped geological formation on the slopes of Mount Tendürek near Doğubayazıt, Turkey, at approximately 6,300 feet elevation. The formation measures roughly 515 feet (157 m) in length — close to the biblical 300 cubits — and exhibits a symmetrical hull-like profile with a raised midship section. Wyatt first visited in 1977 and conducted multiple expeditions claiming to find petrified wood, metal fittings, and a ballast stone inside the structure. The Turkish government designated the site an official national park and archaeological site in 1987. Mainstream geologists attribute the shape to a laccolithic intrusion deformed by landslide activity. Genesis 8:4 states the ark rested "on the mountains of Ararat," and this formation lies within the ancient region of Urartu (biblical Ararat), roughly 18 miles south of Mount Ararat proper.'},
                {lat:39.70, lng:43.90, label:'Anchor Stones near Kazan Village', ref:'Genesis 8:4', desc:'Several large standing stones scattered across the highland plateau near the villages of Kazan and Arzap, roughly 15–20 miles northwest of the Durupınar site. The stones are drogue-stone shaped — tall, rectangular, with a hole near the top — and range from 8 to 18 feet in height. Several bear carved cross symbols, which Wyatt interpreted as later Christian markings added by pilgrims who venerated them as relics from Noah\'s voyage. He identified them as sea anchors (drogue stones) that ancient sailors used to stabilize vessels in rough water, arguing that Noah\'s family carved the crosses after the Flood as a memorial. Drogue stones of similar design are attested in ancient Mediterranean seafaring contexts. The cross carvings remain unexplained by conventional archaeology.'},
                {lat:29.0333, lng:34.6500, label:'Nuweiba Beach — Red Sea Crossing', ref:'Exodus 14:21–22', desc:'A wide sandy beach on the Gulf of Aqaba at Nuweiba, Sinai Peninsula, Egypt. Wyatt proposed this location as the Israelite crossing point based on its geography: the beach is unusually large (roughly 3 miles wide), capable of accommodating a large population, and directly faces the Saudi Arabian coastline across a 12-mile-wide strait. A natural underwater land bridge — a gradual slope rather than an abrupt chasm — connects the two coastlines at this point at a depth of approximately 800 feet. Wyatt claimed this gradual gradient was precisely what would be required for a miraculous crossing of chariots and masses of people on foot. The traditional Exodus route through the northern Sinai is also attested, and scholars dispute both geography and the historicity of the Exodus itself, but the underwater topography at Nuweiba is a documented geological feature.'},
                {lat:28.90, lng:34.70, label:'Underwater Chariot Wheels — Gulf of Aqaba', ref:'Exodus 14:23–28', desc:'In the waters of the Gulf of Aqaba between Nuweiba and the Saudi Arabian coast, Wyatt claimed to have found coral-encrusted chariot wheels, axle components, and skeletal remains of horses and humans on the seabed. He reportedly retrieved a four-spoked gold-veneer chariot wheel consistent in design with New Kingdom Egyptian chariotry (18th Dynasty). Photographs attributed to Wyatt\'s expeditions have circulated widely but have not been independently verified by peer-reviewed marine archaeology. The Egyptian military chariot wheel design he described — including the distinctive four-spoke configuration — is indeed attested archaeologically from the period of Ramesses II and Thutmose III. Exodus 14:25 records that "he clogged their chariot wheels so that they drove heavily," and v.28 describes the waters returning over the chariots and horsemen.'},
                {lat:28.6553, lng:35.3094, label:'Jebel al-Lawz — Proposed Mount Sinai in Arabia', ref:'Exodus 19:18; Galatians 4:25', desc:'A 8,465-foot granite peak in the Tabuk region of northwestern Saudi Arabia (ancient Midian), proposed by Wyatt and later independently by Bob Cornuke and Larry Williams as the true location of biblical Mount Sinai. Galatians 4:25 explicitly states "Sinai is a mountain in Arabia," which Paul distinguishes from the Sinai Peninsula. Features cited in support include: (1) the summit and upper slopes are strikingly blackened — consistent with Exodus 19:18 ("the whole mountain trembled greatly" and was covered in smoke and fire); (2) a large flat plain at the base suitable for encampment of the Israelites; (3) a boundary perimeter of stones; (4) an altar-like stone structure at the base; and (5) petroglyphs of bovine animals nearby, potentially connected to the golden calf episode of Exodus 32. Saudi authorities have restricted access to the site. Traditional scholarship places Sinai at Jebel Musa in the Sinai Peninsula (St. Catherine\'s Monastery tradition), though this identification dates only to the 4th century AD.'},
                {lat:28.73, lng:35.24, label:'Split Rock at Horeb', ref:'Exodus 17:6', desc:'A massive split granite boulder in the vicinity of Jebel al-Lawz, standing approximately 60 feet tall and split cleanly down the center. The rock sits atop a raised platform and shows clear signs of water erosion — smooth channels and scoured surfaces — extending outward from the split in a pattern consistent with a large outflow of water. Wyatt identified this as the rock Moses struck at Horeb (Rephidim) from which water flowed for the Israelites. Exodus 17:6 records God\'s command: "Behold, I will stand before you there on the rock at Horeb, and you shall strike the rock, and water shall come out of it." The erosion channels are visible in photographs taken by Cornuke and Williams, who visited independently of Wyatt. The rock\'s location on a raised natural pedestal is consistent with the text\'s implication of a public, visible event before assembled Israel.'},
                {lat:28.50, lng:35.40, label:'Elim — Twelve Springs and Seventy Palms', ref:'Exodus 15:27', desc:'A site in the general region southeast of Jebel al-Lawz featuring springs and palm trees, proposed as Elim, the Israelites\' encampment after the bitter waters of Marah. Exodus 15:27 records: "Then they came to Elim, where there were twelve springs of water and seventy palm trees, and they encamped there by the water." The broader Tabuk region of northwestern Saudi Arabia (ancient Midian/Hejaz) contains numerous oasis sites with springs and date palms — a stark contrast to the traditional Sinai Peninsula route, which offers fewer such features between the Reed Sea and Jebel Musa. The precise identification remains speculative but fits within the overall Arabia hypothesis for the Exodus route. The traditional Sinai route also has candidate sites for Elim, most commonly Wadi Ghurundel.'},
                {lat:31.30, lng:35.37, label:'Sodom & Gomorrah — Sulfur Ball Sites near Masada', ref:'Genesis 19:24–25', desc:'Several sites along the western shore of the Dead Sea, primarily in the area south of Masada and extending toward Ghor es-Safi (ancient Zoar), where Wyatt and others have documented an unusual phenomenon: white, ash-like formations containing embedded spheres of nearly pure elemental sulfur. These "sulfur balls" are 95–98% pure sulfur — far higher than volcanic sulfur deposits, which typically run 40–60% — and range from marble-sized to golf-ball-sized. The surrounding material has the consistency and appearance of compacted ash. Genesis 19:24 records that "the LORD rained on Sodom and Gomorrah sulfur and fire from the LORD out of heaven." The candidate cities are debated: traditional archaeology places Sodom at Tell el-Hammam (Jordan River valley, northeast Dead Sea) or at sites along the southeastern plain. The sulfur ball formations are real and documented by researchers including Wyatt and independently by Jonathan Gray. The unusual purity of the sulfur remains unexplained by conventional geology.'},
                {lat:31.10, lng:35.35, label:'Lot\'s Wife Pillar', ref:'Genesis 19:26', desc:'A solitary salt pillar formation near the southern end of the Dead Sea, in the vicinity of Mount Sodom (Har Sedom) — a 5-mile-long ridge composed almost entirely of halite (rock salt) that rises on the southwestern shore of the Dead Sea. Wyatt identified a particular formation as Lot\'s wife, who "looked back" and "became a pillar of salt" (Genesis 19:26). Mount Sodom naturally produces distinctive salt columns through dissolution and collapse of its halite mass, and several have received names from local tradition over the centuries. Josephus (Antiquities 1.11.4) claimed to have seen the pillar himself, and early church visitors reported it as well. While the specific formation erodes and reforms over geological time, the area\'s salt pillar topography is a genuine feature of the landscape and has been associated with this account since antiquity.'},
                {lat:31.7839, lng:35.2297, label:'Garden Tomb / Gordon\'s Calvary — Claimed Ark of the Covenant Site', ref:'Jeremiah 3:16; Matthew 27:33', desc:'Wyatt\'s most extraordinary and most contested claim: that the Ark of the Covenant lies hidden in a cave system beneath Gordon\'s Calvary (Skull Hill) and the adjacent Garden Tomb in Jerusalem, and that at the moment of Christ\'s crucifixion, an earthquake (Matthew 27:51) opened a crack in the rock through which Christ\'s blood dripped down onto the mercy seat of the Ark — a theological convergence of the sacrifice and the atonement symbol. Wyatt claimed to have entered the cave system in 1982, found the Ark in a chamber, and been prohibited by angelic figures from removing or photographing it. He said he took a sample of dried blood from the crack, which when rehydrated reportedly showed only 24 chromosomes — 23 from Mary and one Y chromosome from the Father — a claim with no scientific documentation or independent verification. Jeremiah 3:16 prophesies that the Ark "shall not come to mind" and "shall not be made again" in the messianic age, which some interpret as implying it was hidden rather than destroyed. The Garden Tomb itself is a genuine 1st-century tomb, proposed as an alternative to the Church of the Holy Sepulchre as the burial site of Christ.'},
                {lat:31.7785, lng:35.2340, label:'Zedekiah\'s Cave — Solomon\'s Quarries', ref:'2 Chronicles 35:3; Jeremiah 3:16', desc:'A massive underground quarry stretching approximately 330 feet beneath the Muslim Quarter of Jerusalem\'s Old City, with an entrance at the base of the northern city wall near the Damascus Gate. The cave runs some 750 feet into the hill and covers an area of roughly 5 acres. It is composed of meleke limestone, the same stone used in Second Temple construction, and shows extensive ancient quarrying marks. It is traditionally associated with Freemason lore as "Solomon\'s Quarries." In the context of Wyatt\'s Ark claim, the cave system is relevant because it connects to the broader underground network beneath the Old City. 2 Chronicles 35:3 records Josiah commanding the Levites to return the Ark to the Temple — implying it had been removed — and many scholars believe Josiah or Jeremiah hid the Ark before the Babylonian invasion of 586 BC. Jeremiah\'s Grotto, a traditional site of Jeremiah\'s imprisonment, is located directly adjacent to Gordon\'s Calvary and the Garden Tomb, lending circumstantial geographical coherence to Wyatt\'s hypothesis about the Ark\'s concealment location.'}
            ]
        }
    ];

    // ── 33rd Degree Reference Lines ──
    var PARALLEL_LINES = {
        greenwich_33E: { lat: null, lng: 33.0, label: '33\u00B0E Greenwich', color: '#5a9a6a', dash: '8 4' },
        paris_33E: { lat: null, lng: 35.3372, label: '33\u00B0E Paris Meridian', color: '#b07a50', dash: '12 6' },
        greenwich_meridian: { lat: null, lng: 0, label: 'Greenwich Meridian (0\u00B0)', color: '#5a9a6a', dash: '4 8' },
        paris_meridian: { lat: null, lng: 2.3372, label: 'Paris Meridian (2.34\u00B0E)', color: '#b07a50', dash: '4 8' },
        lat_33: { lat: 33.0, lng: null, label: '33\u00B0N Parallel', color: '#b0a060', dash: '8 4' },
        lat_33_33: { lat: 33.33, lng: null, label: '33.33\u00B0N Parallel', color: '#9a5a68', dash: '12 4 4 4' },
        paris_33_33E: { lat: null, lng: 35.6672, label: '33.33\u00B0E Paris Meridian', color: '#9a5a68', dash: '12 4 4 4' }
    };

    var mapLayerGroups = {};
    var mapBaseLayers = {};
    var mapOverlayLayers = {};
    var mapLayerControl = null;

    // ── BOOK-TO-JOURNEYS MAPPING ─────────────────────────────
    var BOOK_TO_JOURNEYS = {
        'genesis': ['watcher_descent', 'nimrod_expansion', 'abraham', 'abrahams_war', 'isaac', 'jacob', 'joseph', 'ron_wyatt'],
        'exodus': ['moses_life', 'exodus', 'ark_journey', 'ron_wyatt'],
        'leviticus': ['exodus', 'wilderness'],
        'numbers': ['spies_route', 'balaam', 'wilderness', 'watcher_descent'],
        'deuteronomy': ['wilderness', 'conquest'],
        'joshua': ['conquest', 'ark_journey', 'giant_slayer', 'watcher_descent'],
        'judges': ['conquest', 'philistine_migration', 'ark_journey'],
        'ruth': ['conquest'],
        '1samuel': ['ark_journey', 'giant_slayer', 'david_flight', 'philistine_migration'],
        '2samuel': ['david_flight', 'giant_slayer', 'ark_journey'],
        '1kings': ['elijah', 'ark_journey'],
        '2kings': ['elijah', 'nimrod_expansion'],
        '1chronicles': ['david_flight', 'giant_slayer', 'ark_journey'],
        '2chronicles': ['elijah', 'nimrod_expansion'],
        'psalms': ['david_flight', 'conquest', 'ark_journey', 'wilderness', 'exodus'],
        'job': ['watcher_descent'],
        'proverbs': [],
        'ecclesiastes': [],
        'songofsolomon': [],
        'isaiah': ['nimrod_expansion', 'exodus'],
        'jeremiah': ['nimrod_expansion'],
        'ezekiel': ['nimrod_expansion', 'watcher_descent'],
        'daniel': ['nimrod_expansion'],
        'hosea': ['exodus', 'conquest'],
        'joel': ['conquest'],
        'amos': ['nimrod_expansion', 'philistine_migration', 'conquest'],
        'obadiah': ['conquest'],
        'jonah': ['nimrod_expansion'],
        'micah': ['nimrod_expansion', 'conquest'],
        'nahum': ['nimrod_expansion'],
        'habakkuk': ['nimrod_expansion'],
        'zephaniah': ['nimrod_expansion'],
        'haggai': ['nimrod_expansion'],
        'zechariah': ['nimrod_expansion', 'conquest', 'jesus_final_week'],
        'malachi': ['elijah'],
        'lamentations': ['nimrod_expansion'],
        'ezra': ['nimrod_expansion'],
        'nehemiah': ['nimrod_expansion'],
        'esther': ['nimrod_expansion'],
        'matthew': ['jesus_galilee', 'jesus_final_week', 'exodus'],
        'mark': ['jesus_galilee', 'jesus_final_week'],
        'luke': ['jesus_galilee', 'jesus_final_week'],
        'john': ['jesus_galilee', 'jesus_final_week', 'conquest'],
        'acts': ['paul_journey1', 'paul_journey2', 'paul_journey3', 'jesus_final_week'],
        'romans': ['paul_journey3'],
        '1corinthians': ['paul_journey2', 'paul_journey3'],
        '2corinthians': ['paul_journey2', 'paul_journey3'],
        'galatians': ['paul_journey1', 'paul_journey3'],
        'ephesians': ['paul_journey3'],
        'philippians': ['paul_journey2'],
        'colossians': ['paul_journey3'],
        '1thessalonians': ['paul_journey2'],
        '2thessalonians': ['paul_journey2'],
        '1timothy': ['paul_journey3'],
        '2timothy': ['paul_journey3'],
        'titus': ['paul_journey3'],
        'philemon': ['paul_journey3'],
        'hebrews': ['exodus', 'wilderness', 'conquest', 'ark_journey', 'moses_life', 'abraham', 'elijah'],
        'james': ['jesus_galilee', 'jesus_final_week'],
        '1peter': ['paul_journey3', 'exodus'],
        '2peter': ['paul_journey3', 'watcher_descent'],
        '1john': ['jesus_galilee', 'jesus_final_week'],
        '2john': ['jesus_galilee'],
        '3john': ['paul_journey3'],
        'jude': ['watcher_descent', 'exodus', 'wilderness'],
        'revelation': ['jesus_final_week', 'paul_journey3', 'nimrod_expansion', 'watcher_descent'],
        '1enoch': ['watcher_descent'],
        'giants': ['watcher_descent', 'conquest'],
        'jubilees': ['watcher_descent', 'abraham', 'exodus', 'moses_life'],
        'jasher': ['abraham', 'jacob', 'joseph', 'exodus', 'conquest'],
        'genesis_apocryphon': ['abraham', 'watcher_descent'],
        'dss_sectarian': ['conquest', 'wilderness'],
        'josephus': ['jesus_final_week', 'nimrod_expansion'],
        'heavenly_court': ['watcher_descent', 'conquest'],
        'messianic_thread': ['abraham', 'exodus', 'david_flight', 'jesus_final_week'],
        'nephilim_giants': ['watcher_descent', 'giant_slayer', 'conquest', 'nimrod_expansion'],
        'three_rebellions': ['watcher_descent', 'nimrod_expansion', 'conquest']
    };

    function openMapForBook(textId) {
        openMap();
        // Wait for map initialization then filter
        var checkMap = setInterval(function() {
            if (mapInstance && Object.keys(mapOverlayLayers).length > 0) {
                clearInterval(checkMap);
                filterMapForBook(textId);
            }
        }, 100);
        // Safety timeout
        setTimeout(function() { clearInterval(checkMap); }, 5000);
    }

    function filterMapForBook(textId) {
        var bookJourneys = BOOK_TO_JOURNEYS[textId] || [];
        if (bookJourneys.length === 0) return; // Show all if no mapping

        // Remove all journey layers first
        MAP_JOURNEYS.forEach(function(journey) {
            var layerKey = '\ud83d\uddfaï¸ ' + journey.name;
            var layer = mapOverlayLayers[layerKey];
            if (layer && mapInstance.hasLayer(layer)) {
                mapInstance.removeLayer(layer);
            }
        });

        // Add only relevant journeys and collect bounds
        var allCoords = [];
        MAP_JOURNEYS.forEach(function(journey) {
            if (bookJourneys.indexOf(journey.id) !== -1) {
                var layerKey = '\ud83d\uddfaï¸ ' + journey.name;
                var layer = mapOverlayLayers[layerKey];
                if (layer) {
                    layer.addTo(mapInstance);
                    journey.waypoints.forEach(function(wp) {
                        allCoords.push([wp.lat, wp.lng]);
                    });
                }
            }
        });

        // Fit map bounds to the visible journeys
        if (allCoords.length > 1) {
            var bounds = L.latLngBounds(allCoords);
            mapInstance.fitBounds(bounds.pad(0.15));
        } else if (allCoords.length === 1) {
            mapInstance.setView(allCoords[0], 8);
        }
    }

    // ── LEARN HEBREW ──────────────────────────────────────────
    function openHebrew() {
        document.getElementById('hebrewOverlay').classList.add('open');
        renderHebrewTab('alphabet');
    }
    function closeHebrew() {
        document.getElementById('hebrewOverlay').classList.remove('open');
    }

    var HEBREW_ALPHABET = [
        {l:'\u05D0', name:'Aleph', sound:'silent / glottal stop', val:1, note:'First letter. Silent carrier for vowels.'},
        {l:'\u05D1', name:'Bet / Vet', sound:'b (with dagesh) / v', val:2, note:'With dot (dagesh): B. Without: V.'},
        {l:'\u05D2', name:'Gimel', sound:'g (as in "go")', val:3, note:'Always hard G sound.'},
        {l:'\u05D3', name:'Dalet', sound:'d', val:4, note:'Like English D.'},
        {l:'\u05D4', name:'He', sound:'h', val:5, note:'Soft H. At end of word often silent.'},
        {l:'\u05D5', name:'Vav', sound:'v / o / u', val:6, note:'Consonant V. Also vowel marker: \u05D5\u05B9 = "o", \u05D5\u05BC = "u".'},
        {l:'\u05D6', name:'Zayin', sound:'z', val:7, note:'Like English Z.'},
        {l:'\u05D7', name:'Chet', sound:'ch (as in "Bach")', val:8, note:'Guttural. Like Scottish "loch."'},
        {l:'\u05D8', name:'Tet', sound:'t', val:9, note:'Emphatic T. Same sound as Tav in modern Hebrew.'},
        {l:'\u05D9', name:'Yod', sound:'y / i', val:10, note:'Smallest letter. Also vowel marker for "i" and "ei".'},
        {l:'\u05DB', name:'Kaf / Khaf', sound:'k / kh', val:20, note:'With dagesh: K. Without: KH (like Chet). Final: \u05DA'},
        {l:'\u05DC', name:'Lamed', sound:'l', val:30, note:'Like English L. Tallest letter.'},
        {l:'\u05DE', name:'Mem', sound:'m', val:40, note:'Like English M. Final form: \u05DD (closed square).'},
        {l:'\u05E0', name:'Nun', sound:'n', val:50, note:'Like English N. Final form: \u05DF (descends below line).'},
        {l:'\u05E1', name:'Samekh', sound:'s', val:60, note:'Like English S.'},
        {l:'\u05E2', name:'Ayin', sound:'silent / guttural', val:70, note:'Originally a voiced pharyngeal. Now silent in most traditions.'},
        {l:'\u05E4', name:'Pe / Fe', sound:'p / f', val:80, note:'With dagesh: P. Without: F. Final: \u05E3'},
        {l:'\u05E6', name:'Tsade', sound:'ts', val:90, note:'Like "ts" in "bits". Final: \u05E5'},
        {l:'\u05E7', name:'Qof', sound:'q / k', val:100, note:'Back-of-throat K. Deeper than Kaf.'},
        {l:'\u05E8', name:'Resh', sound:'r', val:200, note:'Rolled or uvular R (varies by tradition).'},
        {l:'\u05E9', name:'Shin / Sin', sound:'sh / s', val:300, note:'\u05E9\u05C1 (dot right) = SH. \u05E9\u05C2 (dot left) = S.'},
        {l:'\u05EA', name:'Tav', sound:'t', val:400, note:'Like English T. Last letter of the alphabet.'}
    ];

    var HEBREW_VOWELS = [
        {v:'\u05B7', name:'Patach', sound:'a (as in "father")', type:'short', ex:'\u05D3\u05B7\u05D1\u05B8\u05E8'},
        {v:'\u05B8', name:'Qamats', sound:'a (as in "father")', type:'long', ex:'\u05D3\u05B8\u05D1\u05B8\u05E8'},
        {v:'\u05B6', name:'Segol', sound:'e (as in "bed")', type:'short', ex:'\u05DE\u05B6\u05DC\u05B6\u05DA'},
        {v:'\u05B5', name:'Tsere', sound:'ei (as in "they")', type:'long', ex:'\u05D1\u05B5\u05D9\u05EA'},
        {v:'\u05B4', name:'Chiriq', sound:'i (as in "machine")', type:'short/long', ex:'\u05DE\u05B4\u05D3\u05B0\u05D1\u05B8\u05E8'},
        {v:'\u05D5\u05B9', name:'Cholem (vav)', sound:'o (as in "role")', type:'long', ex:'\u05E9\u05C1\u05D5\u05B9\u05DC\u05D5\u05B9\u05DD'},
        {v:'\u05B9', name:'Cholem', sound:'o (as in "role")', type:'long', ex:'\u05E7\u05B9\u05D3\u05B6\u05E9\u05C1'},
        {v:'\u05BB', name:'Qubbuts', sound:'u (as in "flute")', type:'short', ex:'\u05D7\u05BB\u05E7\u05B8\u05BC\u05D4'},
        {v:'\u05D5\u05BC', name:'Shureq', sound:'u (as in "flute")', type:'long', ex:'\u05E8\u05D5\u05BC\u05D7\u05B7'},
        {v:'\u05B0', name:'Sheva', sound:'quick "e" or silent', type:'reduced', ex:'\u05D1\u05B0\u05E8\u05B5\u05D0\u05E9\u05C1\u05B4\u05D9\u05EA'},
        {v:'\u05B2', name:'Chataf Patach', sound:'quick "a"', type:'reduced', ex:'\u05D0\u05B2\u05E0\u05B4\u05D9'},
        {v:'\u05B1', name:'Chataf Segol', sound:'quick "e"', type:'reduced', ex:'\u05D0\u05B1\u05DC\u05B9\u05D4\u05B4\u05D9\u05DD'},
        {v:'\u05B3', name:'Chataf Qamats', sound:'quick "o"', type:'reduced', ex:'\u05D7\u05B3\u05DC\u05B4\u05D9'}
    ];

    var HEBREW_PRACTICE = [
        {heb:'\u05D1\u05B0\u05E8\u05B5\u05D0\u05E9\u05C1\u05B4\u05D9\u05EA', translit:'b\u0259r\u0113\u02BEsh\u012Bt', gloss:'In the beginning', ref:'Genesis 1:1', breakdown:'b\u0259- (in) + r\u0113\u02BEsh\u012Bt (beginning)'},
        {heb:'\u05D0\u05B1\u05DC\u05B9\u05D4\u05B4\u05D9\u05DD', translit:'\u02BEel\u014Dh\u012Bm', gloss:'God (plural of majesty)', ref:'Genesis 1:1', breakdown:'\u02BEel\u014D\u0101h (god) + -\u012Bm (plural)'},
        {heb:'\u05E9\u05C1\u05B8\u05DE\u05B7\u05D9\u05B4\u05DD', translit:'sh\u0101mayim', gloss:'heavens / sky', ref:'Genesis 1:1', breakdown:'Dual form: two heavens (visible + invisible)'},
        {heb:'\u05D0\u05B8\u05E8\u05B6\u05E5', translit:'\u02BE\u0101rets', gloss:'earth / land', ref:'Genesis 1:1', breakdown:'The physical world, contrasted with sh\u0101mayim'},
        {heb:'\u05D0\u05B8\u05D3\u05B8\u05DD', translit:'\u02BE\u0101d\u0101m', gloss:'man / humanity', ref:'Genesis 1:26', breakdown:'From \u02BEad\u0101m\u0101h (ground/soil) \u2014 earthling'},
        {heb:'\u05EA\u05BC\u05D5\u05B9\u05E8\u05B8\u05D4', translit:'t\u014Dr\u0101h', gloss:'instruction / law / Torah', ref:'Deuteronomy 1:5', breakdown:'From y\u0101r\u0101h (to throw/shoot/instruct)'},
        {heb:'\u05E9\u05C1\u05B8\u05DC\u05D5\u05B9\u05DD', translit:'sh\u0101l\u014Dm', gloss:'peace / wholeness / completeness', ref:'Judges 6:24', breakdown:'From sh\u0101l\u0113m (to be complete)'},
        {heb:'\u05D9\u05B0\u05D4\u05D5\u05B8\u05D4', translit:'YHWH (Yahweh)', gloss:'The LORD (the Name)', ref:'Exodus 3:14', breakdown:'From h\u0101y\u0101h (to be) \u2014 "I AM WHO I AM"'},
        {heb:'\u05DE\u05B7\u05DC\u05B0\u05D0\u05B8\u05DA\u05B0', translit:'mal\u02BE\u0101k', gloss:'messenger / angel', ref:'Genesis 16:7', breakdown:'From l\u02BE\u0101k (to send) \u2014 one who is sent'},
        {heb:'\u05E7\u05B8\u05D3\u05D5\u05B9\u05E9\u05C1', translit:'q\u0101d\u014Dsh', gloss:'holy / set apart', ref:'Leviticus 19:2', breakdown:'From q\u0101dash (to be set apart/consecrated)'},
        {heb:'\u05D1\u05B0\u05E0\u05B5\u05D9 \u05D4\u05B8\u05D0\u05B1\u05DC\u05B9\u05D4\u05B4\u05D9\u05DD', translit:'b\u0259n\u0113y h\u0101\u02BEel\u014Dh\u012Bm', gloss:'sons of God', ref:'Genesis 6:2', breakdown:'b\u0259n\u0113y (sons of) + h\u0101- (the) + \u02BEel\u014Dh\u012Bm (God)'},
        {heb:'\u05E0\u05B0\u05E4\u05B4\u05D9\u05DC\u05B4\u05D9\u05DD', translit:'n\u0259phil\u012Bm', gloss:'Nephilim / fallen ones / giants', ref:'Genesis 6:4', breakdown:'From n\u0101phal (to fall) \u2014 the fallen ones'}
    ];

    function renderHebrewTab(tab) {
        var el = document.getElementById('hebrewLearnContent');
        if (tab === 'alphabet') {
            var html = '<h3>The Hebrew Alphabet (Aleph-Bet)</h3>';
            html += '<p>Hebrew has 22 consonant letters. It reads <strong>right to left</strong>. Vowels are shown as dots and dashes (niqqud) above and below the letters. The alphabet is also a number system \u2014 each letter has a numeric value.</p>';
            html += '<div class="hl-tip"><strong>Key concept:</strong> Hebrew was originally written without vowels. The niqqud (vowel points) were added by the Masoretes around 600-1000 AD to preserve the correct pronunciation. Ancient scrolls and modern Israeli Hebrew are written without vowels.</div>';
            html += '<div class="hl-letter-grid">';
            HEBREW_ALPHABET.forEach(function(lt) {
                html += '<div class="hl-letter-card">' +
                    '<div class="hl-letter-big">' + lt.l + '</div>' +
                    '<div class="hl-letter-name">' + lt.name + '</div>' +
                    '<div class="hl-letter-sound">' + lt.sound + '</div>' +
                    '<div class="hl-letter-value">Value: ' + lt.val + '</div>' +
                    '</div>';
            });
            html += '</div>';

            html += '<h3>Final Forms (Sofit)</h3>';
            html += '<p>Five letters change shape when they appear at the end of a word:</p>';
            html += '<div class="hl-letter-grid">';
            [{n:'Kaf',r:'\u05DB',f:'\u05DA'},{n:'Mem',r:'\u05DE',f:'\u05DD'},{n:'Nun',r:'\u05E0',f:'\u05DF'},{n:'Pe',r:'\u05E4',f:'\u05E3'},{n:'Tsade',r:'\u05E6',f:'\u05E5'}].forEach(function(sf) {
                html += '<div class="hl-letter-card"><div class="hl-letter-big">' + sf.r + ' \u2192 ' + sf.f + '</div><div class="hl-letter-name">' + sf.n + ' \u2192 ' + sf.n + ' Sofit</div><div class="hl-letter-sound">Same sound, end-of-word form</div></div>';
            });
            html += '</div>';

            html += '<h3>Begadkefat Letters</h3>';
            html += '<p>Six letters have two pronunciations depending on whether they have a <strong>dagesh</strong> (dot inside). Remember the mnemonic: <strong>BeGaD KeFaT</strong>.</p>';
            html += '<div class="hl-letter-grid">';
            [{l:'\u05D1\u05BC',h:'B',l2:'\u05D1',s:'V'},{l:'\u05D2\u05BC',h:'G (hard)',l2:'\u05D2',s:'Gh (soft)'},{l:'\u05D3\u05BC',h:'D',l2:'\u05D3',s:'Dh'},{l:'\u05DB\u05BC',h:'K',l2:'\u05DB',s:'Kh'},{l:'\u05E4\u05BC',h:'P',l2:'\u05E4',s:'F'},{l:'\u05EA\u05BC',h:'T (hard)',l2:'\u05EA',s:'Th (soft)'}].forEach(function(bg) {
                html += '<div class="hl-letter-card"><div class="hl-letter-big">' + bg.l + ' / ' + bg.l2 + '</div><div class="hl-letter-name">' + bg.h + ' / ' + bg.s + '</div><div class="hl-letter-sound">With dagesh / Without</div></div>';
            });
            html += '</div>';
            html += '<div class="hl-tip"><strong>Modern Hebrew:</strong> In practice, only Bet/Vet (\u05D1\u05BC/\u05D1), Kaf/Khaf (\u05DB\u05BC/\u05DB), and Pe/Fe (\u05E4\u05BC/\u05E4) still have distinct pronunciations. The other three pairs sound the same in modern speech.</div>';
            el.innerHTML = html;

        } else if (tab === 'vowels') {
            var html = '<h3>Hebrew Vowel Points (Niqqud)</h3>';
            html += '<p>Vowels appear as dots and lines <strong>below</strong> (sometimes above) the consonant they follow. Each consonant + vowel combination creates a syllable. The consonant \u05D1 (Bet) is used below to show placement.</p>';
            html += '<div class="hl-tip"><strong>Reading order:</strong> Read the consonant first, then the vowel attached to it. \u05D1\u05B8 = consonant B + vowel A = "ba". Go right to left, one consonant-vowel pair at a time.</div>';
            html += '<h3>Full Vowels</h3>';
            html += '<div class="hl-vowel-grid">';
            HEBREW_VOWELS.filter(function(v){return v.type !== 'reduced';}).forEach(function(vw) {
                html += '<div class="hl-vowel-card">' +
                    '<div class="hl-vowel-big">\u05D1' + vw.v + '</div>' +
                    '<div class="hl-vowel-name">' + vw.name + '</div>' +
                    '<div class="hl-vowel-sound">' + vw.sound + ' (' + vw.type + ')</div>' +
                    '</div>';
            });
            html += '</div>';
            html += '<h3>Reduced Vowels (Chataf)</h3>';
            html += '<p>These are "half vowels" \u2014 very quick, unstressed sounds. They appear under gutturals (\u05D0, \u05D4, \u05D7, \u05E2) which cannot take a regular sheva.</p>';
            html += '<div class="hl-vowel-grid">';
            HEBREW_VOWELS.filter(function(v){return v.type === 'reduced';}).forEach(function(vw) {
                html += '<div class="hl-vowel-card">' +
                    '<div class="hl-vowel-big">\u05D0' + vw.v + '</div>' +
                    '<div class="hl-vowel-name">' + vw.name + '</div>' +
                    '<div class="hl-vowel-sound">' + vw.sound + '</div>' +
                    '</div>';
            });
            html += '</div>';
            html += '<h3>The Dagesh</h3>';
            html += '<p>A dot inside a consonant. Two types:</p>';
            html += '<div class="hl-tip"><strong>Dagesh Lene</strong> (light): In BeGaD KeFaT letters, hardens the sound (V\u2192B, F\u2192P, Kh\u2192K).<br><strong>Dagesh Forte</strong> (strong): In any letter, doubles the consonant. \u05E9\u05C1\u05B7\u05D1\u05B8\u05BC\u05EA = shab-b\u0101t (the B is doubled).</div>';
            el.innerHTML = html;

        } else if (tab === 'reading') {
            var html = '<h3>How to Read Biblical Hebrew</h3>';
            html += '<h3>Step 1: Direction</h3>';
            html += '<p>Hebrew reads <strong>right to left</strong>. In the interlinear pane of this app, each Hebrew word is displayed right-to-left, but the word order follows the verse sequence.</p>';
            html += '<h3>Step 2: Consonant + Vowel Pairs</h3>';
            html += '<p>Each consonant is paired with the vowel <strong>underneath</strong> (or above/beside) it. Read one pair at a time, moving right to left within each word.</p>';
            html += '<div class="hl-example"><div class="hl-example-heb">\u05D1\u05B8\u05E8\u05B8\u05D0</div><div class="hl-example-info"><div class="hl-example-translit">b\u0101r\u0101\u02BE</div><div class="hl-example-gloss">"he created"</div><div class="hl-example-breakdown">\u05D1\u05B8 (ba) + \u05E8\u05B8 (ra) + \u05D0 (\u02BE, silent aleph) = bara\u02BE</div></div></div>';
            html += '<h3>Step 3: Syllable Rules</h3>';
            html += '<div class="hl-tip"><strong>Open syllable:</strong> ends with a vowel (ba-, ra-)<br><strong>Closed syllable:</strong> ends with a consonant (bar-, sham-)<br><strong>Sheva rule:</strong> Sheva (\u05B0) at the start of a word or after a closed syllable is <em>vocal</em> (pronounced "e"). After an open syllable it is <em>silent</em> (closes the syllable).</div>';
            html += '<h3>Step 4: Word Examples from Genesis 1:1</h3>';
            html += '<div class="hl-example"><div class="hl-example-heb">\u05D1\u05B0\u05E8\u05B5\u05D0\u05E9\u05C1\u05B4\u05D9\u05EA</div><div class="hl-example-info"><div class="hl-example-translit">b\u0259r\u0113\u02BEsh\u012Bt</div><div class="hl-example-gloss">"In the beginning"</div><div class="hl-example-breakdown">\u05D1\u05B0 (b\u0259) + \u05E8\u05B5 (r\u0113) + \u05D0 (\u02BE) + \u05E9\u05C1\u05B4 (shi) + \u05D9\u05EA (t) = "In-beginning"</div></div></div>';
            html += '<div class="hl-example"><div class="hl-example-heb">\u05D0\u05B5\u05EA \u05D4\u05B7\u05E9\u05C1\u05B8\u05DE\u05B7\u05D9\u05B4\u05DD</div><div class="hl-example-info"><div class="hl-example-translit">\u02BE\u0113t hash\u0101mayim</div><div class="hl-example-gloss">"(marker) the heavens"</div><div class="hl-example-breakdown">\u05D0\u05B5\u05EA = \u02BEet (direct object marker, untranslatable) | \u05D4\u05B7 (ha-) = "the" + \u05E9\u05C1\u05B8\u05DE\u05B7\u05D9\u05B4\u05DD = sh\u0101mayim = "heavens"</div></div></div>';
            html += '<div class="hl-example"><div class="hl-example-heb">\u05D5\u05B0\u05D0\u05B5\u05EA \u05D4\u05B8\u05D0\u05B8\u05E8\u05B6\u05E5</div><div class="hl-example-info"><div class="hl-example-translit">w\u0259\u02BEet h\u0101\u02BE\u0101rets</div><div class="hl-example-gloss">"and (marker) the earth"</div><div class="hl-example-breakdown">\u05D5\u05B0 (w\u0259-) = "and" + \u05D0\u05B5\u05EA = object marker | \u05D4\u05B8 (h\u0101-) = "the" + \u05D0\u05B8\u05E8\u05B6\u05E5 = \u02BEarets = "earth"</div></div></div>';
            html += '<h3>Step 5: The Definite Article</h3>';
            html += '<p>Hebrew has no indefinite article ("a/an"). The definite article ("the") is the prefix <strong>\u05D4\u05B7</strong> (ha-) attached directly to the noun:</p>';
            html += '<div class="hl-example"><div class="hl-example-heb">\u05D0\u05B8\u05D3\u05B8\u05DD \u2192 \u05D4\u05B8\u05D0\u05B8\u05D3\u05B8\u05DD</div><div class="hl-example-info"><div class="hl-example-gloss">"man" \u2192 "the man"</div><div class="hl-example-breakdown">\u02BEadam \u2192 ha\u02BEadam. Just add ha- (\u05D4\u05B7) to the front.</div></div></div>';
            html += '<h3>Step 6: Conjunction Vav</h3>';
            html += '<p>The most common word in the Hebrew Bible is <strong>\u05D5\u05B0</strong> (w\u0259-) meaning "and." It attaches as a prefix: \u05D0\u05B8\u05E8\u05B6\u05E5 (\u02BEarets) \u2192 \u05D5\u05B0\u05D0\u05B8\u05E8\u05B6\u05E5 (w\u0259\u02BEarets = "and-earth").</p>';
            html += '<h3>Using the Interlinear Pane</h3>';
            html += '<div class="hl-tip"><strong>In this app:</strong> Open the interlinear reading pane (toggle on the right side). Each Hebrew word shows: the Hebrew text, transliteration, morphology code, Strong\'s number, and English gloss. Click any word for more details. Use the book selector dropdown to switch between Genesis, Exodus, Leviticus, Numbers, Deuteronomy, and Joshua.</div>';
            el.innerHTML = html;

        } else if (tab === 'roots') {
            var html = '<h3>The Hebrew Root System</h3>';
            html += '<p>Almost every Hebrew word is built from a <strong>three-letter root</strong> (called a <em>shoresh</em>, \u05E9\u05C1\u05B9\u05E8\u05B6\u05E9\u05C1). The root carries the core meaning, and different patterns (vowels, prefixes, suffixes) create related words.</p>';
            html += '<div class="hl-tip"><strong>Why this matters:</strong> When you learn ONE root, you instantly understand dozens of related words. This is the key to unlocking Hebrew vocabulary rapidly.</div>';

            html += '<h3>Example: \u05DE\u05DC\u05DA (m-l-k) \u2014 King/Rule</h3>';
            html += '<table class="hl-root-table"><tr><th>Hebrew</th><th>Transliteration</th><th>Meaning</th><th>Pattern</th></tr>';
            html += '<tr><td>\u05DE\u05B6\u05DC\u05B6\u05DA\u05B0</td><td>melek</td><td>king</td><td>noun (agent)</td></tr>';
            html += '<tr><td>\u05DE\u05B7\u05DC\u05B0\u05DB\u05B8\u05BC\u05D4</td><td>malk\u0101h</td><td>queen</td><td>feminine noun</td></tr>';
            html += '<tr><td>\u05DE\u05B7\u05DE\u05B0\u05DC\u05B8\u05DB\u05B8\u05D4</td><td>maml\u0101k\u0101h</td><td>kingdom</td><td>abstract noun</td></tr>';
            html += '<tr><td>\u05DE\u05B8\u05DC\u05B7\u05DA\u05B0</td><td>m\u0101lak</td><td>he reigned</td><td>Qal perfect</td></tr>';
            html += '<tr><td>\u05D4\u05B4\u05DE\u05B0\u05DC\u05B4\u05D9\u05DA\u05B0</td><td>himl\u012Bk</td><td>he made king</td><td>Hiphil (causative)</td></tr>';
            html += '</table>';

            html += '<h3>Key Biblical Roots</h3>';
            html += '<table class="hl-root-table"><tr><th>Root</th><th>Letters</th><th>Core Meaning</th><th>Key Words</th></tr>';
            html += '<tr><td>\u05D1\u05E8\u05D0</td><td>b-r-\u02BE</td><td>create (divine)</td><td>bar\u0101\u02BE (he created), b\u0259r\u012B\u02BE\u0101h (creation)</td></tr>';
            html += '<tr><td>\u05D3\u05D1\u05E8</td><td>d-b-r</td><td>word/speak</td><td>d\u0101b\u0101r (word/thing), dibb\u0113r (he spoke), midbar (wilderness)</td></tr>';
            html += '<tr><td>\u05E7\u05D3\u05E9</td><td>q-d-sh</td><td>holy/set apart</td><td>q\u0101d\u014Dsh (holy), miqdash (sanctuary), qiddesh (sanctified)</td></tr>';
            html += '<tr><td>\u05E9\u05C1\u05DE\u05E8</td><td>sh-m-r</td><td>guard/keep</td><td>sh\u0101mar (he kept), mismeret (charge/duty), shomer (guardian)</td></tr>';
            html += '<tr><td>\u05D9\u05E8\u05D0</td><td>y-r-\u02BE</td><td>fear/awe</td><td>y\u0101r\u0113\u02BE (he feared), yir\u02BE\u0101h (fear/reverence), n\u014Dr\u0101\u02BE (awesome)</td></tr>';
            html += '<tr><td>\u05E2\u05D1\u05D3</td><td>\u02BF-b-d</td><td>serve/work</td><td>\u02BF\u0101bad (he served), \u02BFebed (servant), \u02BFab\u014Dd\u0101h (service/worship)</td></tr>';
            html += '<tr><td>\u05DB\u05EA\u05D1</td><td>k-t-b</td><td>write</td><td>k\u0101tab (he wrote), k\u0259t\u0101b (writing), mikt\u0101b (letter)</td></tr>';
            html += '<tr><td>\u05E9\u05C1\u05DC\u05DD</td><td>sh-l-m</td><td>complete/peace</td><td>sh\u0101l\u014Dm (peace), shalem (complete), shillem (he repaid)</td></tr>';
            html += '<tr><td>\u05D9\u05E9\u05C1\u05E2</td><td>y-sh-\u02BF</td><td>save/deliver</td><td>y\u0101sha\u02BF (he saved), y\u0259sh\u016B\u02BF\u0101h (salvation), m\u014Dsh\u012B\u02BFa (savior)</td></tr>';
            html += '<tr><td>\u05E0\u05E4\u05DC</td><td>n-p-l</td><td>fall</td><td>n\u0101phal (he fell), n\u0259phil\u012Bm (Nephilim/fallen ones), mapp\u0113l\u0101h (ruin)</td></tr>';
            html += '</table>';

            html += '<h3>The Seven Verb Stems (Binyanim)</h3>';
            html += '<p>Hebrew verbs have seven patterns (binyanim) that modify the root meaning:</p>';
            html += '<table class="hl-root-table"><tr><th>Stem</th><th>Pattern</th><th>Function</th><th>Example (\u05E9\u05C1\u05DE\u05E8)</th></tr>';
            html += '<tr><td>Qal</td><td>simple</td><td>Simple active</td><td>sh\u0101mar = "he guarded"</td></tr>';
            html += '<tr><td>Niphal</td><td>ni-</td><td>Passive / Reflexive</td><td>nishmar = "he was guarded"</td></tr>';
            html += '<tr><td>Piel</td><td>intensive</td><td>Intensive active</td><td>shimm\u0113r = "he guarded carefully"</td></tr>';
            html += '<tr><td>Pual</td><td>intensive passive</td><td>Intensive passive</td><td>shummar = "he was carefully guarded"</td></tr>';
            html += '<tr><td>Hiphil</td><td>hi-</td><td>Causative active</td><td>hishm\u012Br = "he caused to guard"</td></tr>';
            html += '<tr><td>Hophal</td><td>hu-</td><td>Causative passive</td><td>hoshmar = "he was made to guard"</td></tr>';
            html += '<tr><td>Hithpael</td><td>hit-</td><td>Reflexive</td><td>hishtamm\u0113r = "he guarded himself"</td></tr>';
            html += '</table>';
            html += '<div class="hl-tip"><strong>Don\'t panic:</strong> You do NOT need to memorize all seven stems to start reading. The interlinear pane shows the stem (Q, N, Pi, Pu, Hi, Ho, Ht) in the morphology code. Start with Qal \u2014 it accounts for ~70% of biblical verbs.</div>';
            el.innerHTML = html;

        } else if (tab === 'practice') {
            var html = '<h3>Practice: Key Biblical Words</h3>';
            html += '<p>Try to sound out each word before revealing the answer. These are among the most important words in the Hebrew Bible.</p>';
            HEBREW_PRACTICE.forEach(function(pw, i) {
                html += '<div class="hl-practice-word">' +
                    '<div class="hl-practice-heb">' + pw.heb + '</div>' +
                    '<button class="hl-practice-reveal" onclick="this.nextElementSibling.classList.toggle(\'show\');this.textContent=this.textContent===\'Reveal\'?\'Hide\':\'Reveal\'">Reveal</button>' +
                    '<div class="hl-practice-answer">' +
                    '<div class="hl-example-translit">' + pw.translit + '</div>' +
                    '<div class="hl-example-gloss">' + pw.gloss + '</div>' +
                    '<div class="hl-example-breakdown">' + pw.breakdown + '</div>' +
                    '<div style="color:var(--text-muted);font-size:0.8rem;margin-top:4px">' + pw.ref + '</div>' +
                    '</div></div>';
            });
            html += '<h3>Reading Genesis 1:1</h3>';
            html += '<p>Put it all together \u2014 the first verse of the Bible, word by word:</p>';
            html += '<div class="hl-example" style="flex-direction:column;text-align:center">';
            html += '<div class="hl-example-heb" style="font-size:2.4rem;letter-spacing:4px">\u05D1\u05B0\u05E8\u05B5\u05D0\u05E9\u05C1\u05B4\u05D9\u05EA \u05D1\u05B8\u05E8\u05B8\u05D0 \u05D0\u05B1\u05DC\u05B9\u05D4\u05B4\u05D9\u05DD \u05D0\u05B5\u05EA \u05D4\u05B7\u05E9\u05C1\u05B8\u05DE\u05B7\u05D9\u05B4\u05DD \u05D5\u05B0\u05D0\u05B5\u05EA \u05D4\u05B8\u05D0\u05B8\u05E8\u05B6\u05E5</div>';
            html += '<div style="margin-top:12px;font-size:1rem">';
            html += '<span class="hl-example-translit">b\u0259r\u0113\u02BEsh\u012Bt bar\u0101\u02BE \u02BEel\u014Dh\u012Bm \u02BEet hash\u0101mayim w\u0259\u02BEet h\u0101\u02BEarets</span><br>';
            html += '<span class="hl-example-gloss" style="font-size:1.1rem">"In-the-beginning created God [obj] the-heavens and-[obj] the-earth."</span>';
            html += '</div></div>';
            html += '<div class="hl-tip"><strong>Next step:</strong> Open the <strong>interlinear reading pane</strong> (right side of the app) and try reading Genesis 1 word by word. Each word shows Hebrew, transliteration, grammar, Strong\'s number, and English gloss. You\'re now equipped to start!</div>';
            el.innerHTML = html;
        }
    }

    // ── MAP ─────────────────────────────────────────────────────
    function openMap() {
        logEvent('feature', 'map');
        document.getElementById('mapOverlay').classList.add('open');
        if (!mapInstance) {
            initMap();
        } else {
            setTimeout(function() { mapInstance.invalidateSize(); }, 100);
        }
    }

    function closeMap() {
        document.getElementById('mapOverlay').classList.remove('open');
    }

    function initMap() {
        mapInstance = L.map('mapContainer', {
            center: [31.5, 35.2],
            zoom: 7,
            minZoom: 2,
            maxZoom: 20,
            maxBounds: [[-85, -200], [85, 200]],
            maxBoundsViscosity: 0.8,
            zoomControl: false,
            attributionControl: false
        });

        // Zoom control top-right
        L.control.zoom({ position: 'topright' }).addTo(mapInstance);

        // Coordinate display — mouse position (GIS standard)
        var coordDisplay = L.control({ position: 'bottomleft' });
        coordDisplay.onAdd = function() {
            var div = L.DomUtil.create('div', 'map-coord-display');
            div.innerHTML = 'Lat: --  Lng: --';
            return div;
        };
        coordDisplay.addTo(mapInstance);
        mapInstance.on('mousemove', function(e) {
            var cd = document.querySelector('.map-coord-display');
            if (cd) cd.innerHTML = 'Lat: ' + e.latlng.lat.toFixed(4) + '\u00b0  Lng: ' + e.latlng.lng.toFixed(4) + '\u00b0';
        });

        // Scale bar
        L.control.scale({ position: 'bottomleft', imperial: true, metric: true }).addTo(mapInstance);

        // ── Basemap Layers ──
        // Google Satellite — highest resolution imagery available (zoom 20+)
        var googleSat = L.tileLayer('https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
            maxNativeZoom: 20, maxZoom: 20
        });
        var googleHybrid = L.tileLayer('https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', {
            maxNativeZoom: 20, maxZoom: 20
        });
        var esriSat = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
            maxNativeZoom: 18, maxZoom: 20
        });
        var esriNatGeo = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}', {
            maxNativeZoom: 16, maxZoom: 20
        });
        var darkTiles = L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
            maxNativeZoom: 18, maxZoom: 20, subdomains: 'abcd'
        });
        var streetTiles = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxNativeZoom: 19, maxZoom: 20
        });
        var topoTiles = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
            maxNativeZoom: 17, maxZoom: 20
        });

        // Default to Google Satellite — highest resolution
        googleSat.addTo(mapInstance);

        mapBaseLayers = {
            '\ud83d\udef0\ufe0f Google Satellite (Best)': googleSat,
            '\ud83d\udef0\ufe0f Google Hybrid (Labels)': googleHybrid,
            '\ud83c\udf0d ESRI Satellite': esriSat,
            '\ud83c\udf3f Nat Geo World Map': esriNatGeo,
            '\ud83c\udf11 Dark': darkTiles,
            '\ud83d\uddfa\ufe0f Street': streetTiles,
            '\u26f0\ufe0f Terrain': topoTiles
        };

        // ── Site Marker Layer Groups (one per category) ──
        Object.keys(mapCategories).forEach(function(cat) {
            mapLayerGroups[cat] = L.layerGroup();
        });

        // ── Scripture ref → text ID resolver ──
        var BOOK_TO_TEXT = {
            'genesis':'genesis','gen':'genesis','exodus':'exodus','exod':'exodus','leviticus':'leviticus','lev':'leviticus',
            'numbers':'numbers','num':'numbers','deuteronomy':'deuteronomy','deut':'deuteronomy',
            'joshua':'joshua','josh':'joshua','judges':'judges','judg':'judges','ruth':'ruth',
            '1 samuel':'1samuel','1 sam':'1samuel','2 samuel':'2samuel','2 sam':'2samuel',
            '1 kings':'1kings','1 kgs':'1kings','2 kings':'2kings','2 kgs':'2kings',
            '1 chronicles':'1chronicles','1 chr':'1chronicles','2 chronicles':'2chronicles','2 chr':'2chronicles',
            'ezra':'ezra','nehemiah':'nehemiah','neh':'nehemiah',
            'esther':'esther','job':'job','psalms':'psalms','psalm':'psalms','ps':'psalms',
            'proverbs':'proverbs','prov':'proverbs',
            'ecclesiastes':'ecclesiastes','eccl':'ecclesiastes','song of solomon':'songofsolomon',
            'isaiah':'isaiah','isa':'isaiah','jeremiah':'jeremiah','jer':'jeremiah',
            'lamentations':'lamentations','lam':'lamentations','ezekiel':'ezekiel','ezek':'ezekiel',
            'daniel':'daniel','dan':'daniel',
            'hosea':'hosea','joel':'joel','amos':'amos','obadiah':'obadiah','obad':'obadiah',
            'jonah':'jonah','micah':'micah','mic':'micah','nahum':'nahum','nah':'nahum',
            'habakkuk':'habakkuk','hab':'habakkuk','zephaniah':'zephaniah','zeph':'zephaniah',
            'haggai':'haggai','hag':'haggai','zechariah':'zechariah','zech':'zechariah','malachi':'malachi','mal':'malachi',
            'matthew':'matthew','matt':'matthew','mark':'mark','luke':'luke','john':'john','acts':'acts',
            'romans':'romans','rom':'romans','1 corinthians':'1corinthians','1 cor':'1corinthians',
            '2 corinthians':'2corinthians','2 cor':'2corinthians',
            'galatians':'galatians','gal':'galatians','ephesians':'ephesians','eph':'ephesians',
            'philippians':'philippians','phil':'philippians',
            'colossians':'colossians','col':'colossians','1 thessalonians':'1thessalonians','1 thess':'1thessalonians',
            '2 thessalonians':'2thessalonians','2 thess':'2thessalonians',
            '1 timothy':'1timothy','1 tim':'1timothy','2 timothy':'2timothy','2 tim':'2timothy',
            'titus':'titus','philemon':'philemon','phlm':'philemon',
            'hebrews':'hebrews','heb':'hebrews','james':'james','jas':'james',
            '1 peter':'1peter','1 pet':'1peter','2 peter':'2peter','2 pet':'2peter',
            '1 john':'1john','2 john':'2john','3 john':'3john','jude':'jude',
            'revelation':'revelation','rev':'revelation',
            '1 enoch':'1enoch','jubilees':'jubilees','jasher':'jasher'
        };
        function parseFirstRef(refs) {
            if (!refs) return null;
            var m = refs.match(/^([1-3]?\s?[A-Za-z]+)\s+(\d+)/);
            if (!m) return null;
            var book = m[1].trim().toLowerCase();
            var textId = BOOK_TO_TEXT[book];
            return textId ? textId : null;
        }

        // Build markers into layer groups
        MAP_SITES.forEach(function(site) {
            var popup = '<div class="map-popup-title">' + site.name + '</div>' +
                '<div class="map-popup-cat">' + (mapCategories[site.cat] || {}).label + '</div>';
            if (site.img) {
                popup += '<img class="map-popup-img" src="' + site.img + '" alt="' + site.name + '" loading="lazy" onerror="this.style.display=\'none\'">';
            }
            popup += '<div class="map-popup-desc">' + site.desc + '</div>';
            if (site.refs) popup += '<div class="map-popup-refs">\ud83d\udcdc ' + site.refs + '</div>';
            if (site.note) popup += '<div class="map-popup-note">\u26a0\ufe0f ' + site.note + '</div>';
            // "Read in App" button — auto-resolves first scripture ref to a text
            var linkTextId = parseFirstRef(site.refs);
            if (linkTextId) {
                popup += '<button class="map-popup-read-btn" data-text="' + linkTextId + '">\ud83d\udcd6 Read in App \u2192 ' + linkTextId.charAt(0).toUpperCase() + linkTextId.slice(1) + '</button>';
            }
            popup += '<div class="map-popup-coords">\ud83d\udccd ' + site.lat.toFixed(4) + '\u00b0N, ' + site.lng.toFixed(4) + '\u00b0E</div>';

            var marker = L.marker([site.lat, site.lng], {
                icon: createMarkerIcon(site.cat)
            }).bindPopup(popup, { maxWidth: 360, maxHeight: 450, className: 'map-dark-popup' });

            marker._siteData = site;
            mapMarkers.push(marker);
            if (mapLayerGroups[site.cat]) {
                mapLayerGroups[site.cat].addLayer(marker);
            }
        });

        // ── Popup "Read in App" click handler ──
        mapInstance.on('popupopen', function(e) {
            var container = e.popup._contentNode || e.popup.getElement();
            if (!container) return;
            var btn = container.querySelector('.map-popup-read-btn');
            if (btn) {
                btn.addEventListener('click', function(ev) {
                    ev.stopPropagation();
                    var tId = this.dataset.text;
                    if (tId && typeof selectText === 'function') {
                        mapInstance.closePopup();
                        document.querySelector('.map-overlay').classList.remove('open');
                        selectText(tId);
                    }
                });
            }
        });

        // Only show Biblical Sites by default; user toggles others on
        var defaultMapLayers = ['biblical'];
        Object.keys(mapLayerGroups).forEach(function(cat) {
            if (defaultMapLayers.indexOf(cat) !== -1) {
                mapLayerGroups[cat].addTo(mapInstance);
            }
        });

        // ── 33\u00b0 Reference Lines ──
        var greenwichLineGroup = L.layerGroup();
        var parisLineGroup = L.layerGroup();
        var parallelLineGroup = L.layerGroup();
        var hermonCrossGroup = L.layerGroup();

        // Helper: create labeled polyline
        function addRefLine(group, latlngs, color, dash, label) {
            var line = L.polyline(latlngs, {
                color: color, weight: 2, opacity: 0.8,
                dashArray: dash
            });
            group.addLayer(line);
            // Label at midpoint
            var mid = latlngs[Math.floor(latlngs.length / 2)];
            var labelIcon = L.divIcon({
                className: 'map-line-label',
                html: '<span style="color:' + color + ';background:rgba(12,14,20,0.85);padding:2px 6px;border-radius:3px;font-size:11px;white-space:nowrap;border:1px solid ' + color + '40">' + label + '</span>',
                iconSize: [0, 0]
            });
            group.addLayer(L.marker(mid, { icon: labelIcon, interactive: false }));
        }

        // Greenwich longitude lines
        addRefLine(greenwichLineGroup, [[-60, 0], [70, 0]], '#5a9a6a', '4 8', 'Greenwich Meridian (0\u00b0)');
        addRefLine(greenwichLineGroup, [[-60, 33], [70, 33]], '#5a9a6a', '8 4', '33\u00b0E Greenwich');

        // Paris longitude lines
        addRefLine(parisLineGroup, [[-60, 2.3372], [70, 2.3372]], '#b07a50', '4 8', 'Paris Meridian (2.34\u00b0E)');
        addRefLine(parisLineGroup, [[-60, 35.3372], [70, 35.3372]], '#b07a50', '8 4', '33\u00b0E Paris');
        addRefLine(parisLineGroup, [[-60, 35.6672], [70, 35.6672]], '#9a5a68', '12 4 4 4', '33.33\u00b0E Paris');

        // Latitude parallels
        addRefLine(parallelLineGroup, [[33, -180], [33, 180]], '#b0a060', '8 4', '33\u00b0N Parallel');
        addRefLine(parallelLineGroup, [[33.33, -180], [33.33, 180]], '#9a5a68', '12 4 4 4', '33.33\u00b0N Parallel');

        // Hermon crosshair (intersection highlight)
        var hermonCircle = L.circle([33.4167, 35.8571], {
            radius: 15000, color: '#9a5a68', weight: 2, opacity: 0.7,
            fillColor: '#9a5a68', fillOpacity: 0.1, dashArray: '6 3'
        });
        hermonCrossGroup.addLayer(hermonCircle);
        var hermonLabel = L.divIcon({
            className: 'map-line-label',
            html: '<span style="color:#9a5a68;background:rgba(12,14,20,0.9);padding:3px 8px;border-radius:4px;font-size:12px;font-weight:bold;border:1px solid #9a5a6860">\u2020 MT. HERMON \u2014 33.33\u00b0N / 33.33\u00b0E (Paris)</span>',
            iconSize: [0, 0]
        });
        hermonCrossGroup.addLayer(L.marker([33.6, 35.8571], { icon: hermonLabel, interactive: false }));

        // Add ALL reference lines to map by default
        // Reference lines off by default — user toggles them on
        // greenwichLineGroup.addTo(mapInstance);
        // parisLineGroup.addTo(mapInstance);
        // parallelLineGroup.addTo(mapInstance);
        // hermonCrossGroup.addTo(mapInstance);

        // ── Layer Control ──
        mapOverlayLayers = {};
        Object.keys(mapCategories).forEach(function(cat) {
            var c = mapCategories[cat];
            mapOverlayLayers[c.icon + ' ' + c.label] = mapLayerGroups[cat];
        });
        // ── JOURNEY LAYERS (grouped by epoch) ──
        var journeyEpochs = {
            'watcher_descent': '\u2500\u2500 PRIMEVAL \u2500\u2500',
            'abraham': '\u2500\u2500 PATRIARCHS \u2500\u2500',
            'moses_life': '\u2500\u2500 EXODUS & WILDERNESS \u2500\u2500',
            'conquest': '\u2500\u2500 CONQUEST & JUDGES \u2500\u2500',
            'giant_slayer': '\u2500\u2500 KINGDOM ERA \u2500\u2500',
            'jesus_galilee': '\u2500\u2500 JESUS\' MINISTRY \u2500\u2500',
            'paul_journey1': '\u2500\u2500 APOSTOLIC ERA \u2500\u2500',
            'ron_wyatt': '\u2500\u2500 ARCHAEOLOGICAL \u2500\u2500'
        };
        MAP_JOURNEYS.forEach(function(journey) {
            if (journeyEpochs[journey.id]) {
                mapOverlayLayers[journeyEpochs[journey.id]] = L.layerGroup(); // epoch separator
            }
            var jGroup = L.layerGroup();
            var coords = journey.waypoints.map(function(wp) { return [wp.lat, wp.lng]; });

            // Main route polyline
            var line = L.polyline(coords, {
                color: journey.color,
                weight: journey.weight || 3,
                opacity: 0.85,
                dashArray: journey.dash || null
            });
            jGroup.addLayer(line);

            // Waypoint markers (small numbered circles)
            journey.waypoints.forEach(function(wp, i) {
                var wpIcon = L.divIcon({
                    className: 'map-waypoint-icon',
                    html: '<div style="background:' + journey.color + ';color:#fff;width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:10px;font-weight:bold;border:2px solid #fff;box-shadow:0 2px 6px rgba(0,0,0,0.6);text-shadow:0 1px 2px rgba(0,0,0,0.5)">' + (i+1) + '</div>',
                    iconSize: [20, 20],
                    iconAnchor: [10, 10],
                    popupAnchor: [0, -12]
                });
                var wpPopup = '<div class="map-popup-title" style="color:' + journey.color + '">' + journey.name + '</div>' +
                    '<div style="font-weight:600;margin:4px 0">' + (i+1) + '. ' + wp.label + '</div>';
                if (wp.desc) wpPopup += '<div class="map-popup-desc" style="margin:6px 0;font-size:0.82rem">' + wp.desc + '</div>';
                wpPopup += '<div class="map-popup-refs">\ud83d\udcdc ' + wp.ref + '</div>';
                var wpTextId = wp.text || parseFirstRef(wp.ref);
                if (wpTextId) {
                    wpPopup += '<button class="map-popup-read-btn" data-text="' + wpTextId + '">\ud83d\udcd6 Read in App \u2192 ' + wpTextId.charAt(0).toUpperCase() + wpTextId.slice(1) + '</button>';
                }
                jGroup.addLayer(L.marker([wp.lat, wp.lng], { icon: wpIcon }).bindPopup(wpPopup, { maxWidth: 320, className: 'map-dark-popup' }));
            });

            // Journey title popup on the line
            var mid = coords[Math.floor(coords.length / 2)];
            line.bindPopup('<div class="map-popup-title" style="color:' + journey.color + '">' + journey.name + '</div>' +
                '<div class="map-popup-desc">' + journey.desc + '</div>' +
                '<div class="map-popup-refs">\ud83d\udcdc ' + journey.refs + '</div>' +
                '<div style="font-size:0.75rem;color:var(--text-muted);margin-top:6px">' + journey.waypoints.length + ' waypoints</div>',
                { maxWidth: 360, className: 'map-dark-popup' });

            // Journeys off by default — user toggles them on
            mapOverlayLayers['\ud83d\uddfaï¸ ' + journey.name] = jGroup;
        });

        // ── HISTORICAL EMPIRE BOUNDARIES ──
        mapOverlayLayers['\u2500\u2500 EMPIRES \u2500\u2500'] = L.layerGroup(); // separator
        var empires = [
            // ── ANCIENT MESOPOTAMIA & NEAR EAST (pre-1000 BC) ──
            {name:'Sumerian City-States (~3500-2004 BC)', color:'#c8a46e', coords:[[32.5,43.5],[33.0,44.5],[33.5,45.5],[33.0,46.5],[32.5,47.5],[31.5,48.0],[30.5,47.5],[30.0,47.0],[29.5,46.0],[29.5,45.0],[30.0,44.0],[30.5,43.5],[31.5,43.0],[32.5,43.5]]},
            {name:'Akkadian Empire (~2334-2154 BC)', color:'#d4884a', coords:[[38.0,36.5],[37.0,38.0],[36.0,40.0],[35.5,42.0],[35.0,44.0],[34.5,45.5],[33.5,46.5],[32.5,47.5],[31.0,48.0],[30.0,47.5],[29.5,46.0],[30.0,44.0],[31.0,42.0],[32.0,40.0],[33.0,38.5],[34.0,37.0],[35.0,36.0],[36.0,35.5],[37.5,36.0],[38.0,36.5]]},
            {name:'Old Kingdom Egypt (~2686-2181 BC)', color:'#c8b030', coords:[[31.5,25.0],[30.5,29.0],[30.0,31.5],[29.5,32.0],[28.0,32.5],[26.0,32.0],[24.0,32.5],[22.0,31.5],[20.0,30.5],[18.0,30.0],[22.0,27.5],[26.0,27.0],[29.0,27.0],[31.5,25.0]]},
            {name:'Middle Kingdom Egypt (~2055-1650 BC)', color:'#b89820', coords:[[31.2,25.0],[30.2,29.5],[29.8,31.8],[29.2,32.2],[27.5,32.5],[25.0,32.0],[22.5,31.0],[20.0,30.0],[17.0,29.5],[16.0,28.0],[18.0,27.0],[21.0,27.0],[24.0,26.5],[27.0,26.5],[30.0,26.5],[31.2,25.0]]},
            {name:'Hittite Empire (~1600-1178 BC)', color:'#7a9e6c', coords:[[41.5,26.0],[40.5,28.0],[39.5,30.0],[38.5,32.0],[37.5,34.0],[37.0,36.0],[36.5,37.5],[36.0,38.5],[35.0,39.0],[34.5,38.0],[35.0,36.5],[35.5,35.0],[36.0,34.0],[37.0,32.5],[37.5,30.5],[38.5,28.5],[39.5,27.0],[40.5,26.0],[41.0,27.0],[42.0,28.5],[42.5,30.0],[42.0,31.5],[41.0,32.0],[40.5,33.0],[41.0,34.0],[41.5,35.0],[40.0,36.0],[39.0,36.5],[38.5,37.5],[40.0,38.0],[41.5,37.5],[43.0,36.0],[43.5,33.0],[43.0,30.0],[42.0,28.0],[41.5,26.0]]},
            {name:'Mitanni Kingdom (~1500-1300 BC)', color:'#7abcb0', coords:[[38.0,36.5],[37.5,38.0],[37.0,40.0],[36.5,41.5],[36.0,42.5],[35.5,43.0],[35.0,42.5],[34.5,41.5],[34.5,40.0],[35.0,38.5],[35.5,37.5],[36.5,36.5],[37.0,36.0],[38.0,36.5]]},
            {name:'Elamite Kingdom (~2700-539 BC)', color:'#9a7cb0', coords:[[34.0,45.5],[34.5,46.5],[34.5,48.0],[34.0,49.5],[33.5,51.0],[33.0,52.5],[32.5,53.5],[31.5,54.0],[30.5,53.0],[30.0,51.5],[30.0,50.0],[30.5,48.5],[31.5,47.5],[32.5,46.5],[33.0,46.0],[34.0,45.5]]},
            {name:'Egyptian New Kingdom (~1550-1070 BC)', color:'#e6b422', coords:[[31.2,25],[30.0,31],[29.5,32.5],[31.0,34.5],[33.5,35.8],[35.0,36.5],[36.5,36.5],[36.5,38],[34.5,38],[31.5,35],[30,33],[24,33],[22,31],[24,28],[27,27],[31.2,25]]},
            {name:'Phoenician City-States (~1500-300 BC)', color:'#cc7a88', coords:[[36.2,36.2],[35.8,36.5],[35.2,36.2],[34.8,36.0],[34.3,35.8],[33.9,35.7],[33.5,35.5],[33.2,35.3],[33.1,35.5],[33.5,35.8],[34.0,36.0],[34.5,36.2],[35.0,36.5],[35.5,36.7],[36.0,36.6],[36.2,36.2]]},
            {name:'Philistia (~1175-604 BC)', color:'#c07840', coords:[[31.9,34.5],[31.8,34.9],[31.5,35.0],[31.2,35.0],[31.0,34.9],[30.8,34.6],[30.7,34.4],[31.0,34.2],[31.4,34.1],[31.7,34.2],[31.9,34.5]]},
            {name:'Moab (~900-600 BC)', color:'#a87858', coords:[[32.2,35.5],[32.0,35.9],[31.7,35.9],[31.3,35.8],[31.0,35.6],[31.0,35.3],[31.3,35.2],[31.7,35.3],[32.0,35.4],[32.2,35.5]]},
            {name:'Edom (~1300-600 BC)', color:'#b05040', coords:[[30.5,35.0],[30.2,35.5],[29.8,35.6],[29.4,35.5],[29.0,35.3],[28.5,35.0],[28.5,34.6],[28.8,34.3],[29.3,34.2],[29.8,34.3],[30.3,34.5],[30.5,35.0]]},
            {name:'Ammon (~1300-600 BC)', color:'#d09868', coords:[[32.5,35.8],[32.3,36.2],[32.0,36.3],[31.7,36.1],[31.5,35.9],[31.6,35.6],[31.9,35.5],[32.2,35.5],[32.5,35.8]]},
            {name:'Urartu (~860-590 BC)', color:'#7a9870', coords:[[40.0,38.0],[39.5,40.0],[39.0,42.0],[38.5,43.5],[38.0,44.5],[38.5,45.5],[39.5,46.0],[40.5,46.5],[41.5,46.5],[42.0,45.5],[43.0,44.0],[43.5,42.5],[43.5,41.0],[43.0,40.0],[42.0,39.0],[41.0,38.5],[40.0,38.0]]},
            {name:'Lydian Kingdom (~680-546 BC)', color:'#d4a860', coords:[[41.5,26.0],[41.0,28.0],[40.5,30.0],[40.0,31.5],[39.5,32.5],[39.0,33.5],[38.5,34.0],[38.0,33.5],[37.5,32.0],[37.5,30.0],[38.0,28.5],[38.5,27.5],[39.5,27.0],[40.5,26.5],[41.5,26.0]]},
            {name:'Median Empire (~678-549 BC)', color:'#6898b0', coords:[[38.0,44.5],[38.5,46.0],[38.5,48.0],[38.0,50.0],[37.5,51.5],[36.5,52.5],[35.5,53.0],[34.5,52.5],[34.0,51.0],[34.0,49.5],[34.5,48.0],[35.0,46.5],[36.0,45.5],[37.0,44.5],[38.0,44.5]]},

            // ── IRON AGE / CLASSICAL NEAR EAST ──
            {name:'Assyrian Empire (~745-612 BC)', color:'#e05540', coords:[[37.5,36],[36,38],[35,40],[34,42],[33,44],[32,46],[31,47],[30,46],[30,44],[32,42],[33,40],[34,38],[35,36],[36.5,34.5],[38,36],[39,38],[40,40],[39,42],[38,43],[37,44],[36,44.5],[35,44],[34.5,43.5],[34,42],[35,40],[36,38],[37.5,36]]},
            {name:'Babylonian Empire (~626-539 BC)', color:'#b06ce6', coords:[[33.5,35],[34,36.5],[35.5,38],[36,40],[36.5,42],[36,44],[35,45],[33.5,46],[32,47],[30.5,47.5],[29,47],[28,46],[29,44],[30,42],[30.5,40],[31,38],[31.5,36],[32,34.5],[33.5,35]]},
            {name:'Persian Empire (~550-330 BC)', color:'#4aa8e0', coords:[[41,26],[38,30],[37,32],[36,34],[34,35],[32,34],[30,33],[27,34],[23,36],[20,40],[22,44],[24,48],[25,52],[26,56],[28,60],[30,64],[32,68],[34,70],[36,68],[38,64],[40,60],[41,56],[40,52],[39,48],[38,46],[37,44],[38,42],[39,40],[40,38],[42,36],[43,34],[42,30],[41,26]]},

            // ── ISRAELITE & LEVANTINE KINGDOMS ──
            {name:'Kingdom of Israel (~1000-930 BC, United)', color:'#c9a84c', coords:[[33.3,35.5],[33.0,36.0],[32.5,35.8],[32.0,35.6],[31.5,35.5],[31.0,35.4],[30.5,35.0],[30.0,34.8],[29.8,34.5],[30.2,34.3],[30.8,34.4],[31.3,34.6],[31.8,34.8],[32.2,35.0],[32.7,35.2],[33.3,35.5]]},
            {name:'Northern Kingdom / Israel (~930-722 BC)', color:'#e0a030', coords:[[33.3,35.5],[33.0,36.0],[32.5,35.8],[32.0,35.6],[31.8,35.2],[32.0,35.0],[32.3,34.8],[32.7,35.0],[33.3,35.5]]},
            {name:'Southern Kingdom / Judah (~930-586 BC)', color:'#60aadd', coords:[[31.8,35.2],[32.0,35.6],[31.5,35.5],[31.0,35.4],[30.5,35.0],[30.0,34.8],[29.8,34.5],[30.2,34.3],[30.8,34.4],[31.3,34.6],[31.8,35.2]]},

            // ── HELLENISTIC PERIOD ──
            {name:'Alexander\'s Empire (~334-323 BC)', color:'#2dd4a8', coords:[[41,20],[40,24],[38,28],[37,32],[35,34],[33,35],[31,34],[28,33],[26,34],[23,36],[20,38],[22,44],[24,50],[26,56],[28,60],[30,65],[32,70],[34,72],[36,70],[38,66],[40,62],[41,58],[40,52],[39,48],[38,44],[39,40],[40,36],[42,32],[43,28],[42,24],[41,20]]},
            {name:'Ptolemaic Egypt (~305-30 BC)', color:'#a8c840', coords:[[31.5,25.5],[30.5,29.5],[30.0,31.5],[29.5,32.0],[28.0,32.5],[26.0,32.5],[24.0,32.5],[22.0,31.5],[20.0,30.5],[18.0,30.0],[17.0,29.0],[20.0,27.5],[24.0,27.0],[27.0,27.0],[30.0,26.5],[31.5,25.5]]},
            {name:'Seleucid Empire (~312-63 BC)', color:'#4ab8d4', coords:[[41,20],[40,24],[39,28],[38,32],[37,34],[36,36],[36,38],[35,40],[35,42],[35,44],[35.5,46],[36,48],[36,50],[36,52],[36,54],[36,56],[35,58],[33,60],[31,62],[30,64],[31,68],[33,70],[35,70],[37,68],[39,64],[40,60],[41,56],[40,52],[39,48],[38,44],[38,42],[39,40],[40,36],[42,32],[43,28],[42,24],[41,20]]},
            {name:'Hasmonean Kingdom (~140-63 BC)', color:'#40c070', coords:[[33.5,35.5],[33.2,36.2],[32.8,35.8],[32.2,35.6],[31.8,35.5],[31.2,35.4],[30.8,35.0],[30.2,34.8],[29.8,34.3],[30.5,34.2],[31.5,34.3],[32.2,34.6],[32.8,35.0],[33.5,35.5]]},
            {name:'Nabataean Kingdom (~400 BC-106 AD)', color:'#e09050', coords:[[33.5,35.5],[33.2,35.8],[32.8,36.0],[32.5,36.5],[32.0,37.0],[31.5,37.5],[30.5,37.5],[29.5,37.0],[28.5,36.5],[28.0,36.0],[27.5,36.0],[27.5,35.0],[28.0,34.5],[29.0,34.2],[30.0,34.0],[30.8,34.2],[31.5,34.5],[32.2,34.8],[32.8,35.0],[33.5,35.5]]},
            {name:'Herod\'s Kingdom (~37-4 BC)', color:'#c080e0', coords:[[33.4,35.6],[33.2,36.3],[32.9,35.9],[32.3,35.7],[31.9,35.6],[31.3,35.5],[30.5,35.1],[30.0,34.9],[29.5,34.5],[30.0,34.2],[30.8,34.3],[31.5,34.5],[32.3,34.8],[32.9,35.1],[33.4,35.6]]},

            // ── ROMAN PERIOD ──
            {name:'Roman Empire (~117 AD, max extent)', color:'#e8554a', coords:[[55,-5],[52,-10],[45,-9],[37,-8],[36,-5],[37,0],[38,5],[40,10],[45,12],[47,16],[46,20],[44,24],[42,28],[41,32],[38,36],[37,38],[36,40],[34,42],[32,40],[30,36],[28,33],[24,34],[22,31],[26,28],[32,25],[36,13],[38,10],[43,5],[47,0],[52,2],[55,-5]]},

            // ── LATE ANTIQUE / BYZANTINE ──
            {name:'Byzantine Empire (~330-1453 AD)', color:'#7855c0', coords:[[48,14],[45,18],[44,22],[42,26],[42,28],[41,30],[41,32],[40,34],[38,36],[37,38],[37,40],[36,42],[35,40],[34,38],[34,36],[35,34],[36,32],[37,30],[38,28],[38,26],[40,24],[41,22],[42,20],[43,18],[44,16],[46,14],[48,14]]},

            // ── ISLAMIC CALIPHATES ──
            {name:'Rashidun Caliphate (~632-661 AD)', color:'#38a878', coords:[[37,36],[36,38],[35,40],[34,42],[33,44],[32,46],[31,47],[30,48],[29,48],[28,46],[26,44],[24,43],[22,44],[20,43],[18,42],[17,40],[17,38],[18,36],[20,34],[22,36],[24,38],[26,40],[28,40],[29,38],[30,36],[31,34],[32,34],[33,35],[34,36],[36,36],[37,36]]},
            {name:'Umayyad Caliphate (~661-750 AD)', color:'#30c898', coords:[[43,0],[41,4],[40,8],[38,12],[37,16],[37,20],[37,24],[37,28],[37,32],[36,36],[35,40],[34,44],[33,48],[32,52],[31,56],[30,58],[28,56],[26,54],[24,50],[22,48],[20,46],[18,44],[17,40],[15,38],[15,34],[17,30],[20,28],[22,30],[24,32],[26,34],[28,36],[30,36],[32,36],[34,36],[36,34],[38,28],[39,24],[40,20],[41,16],[42,12],[43,8],[43,0]]},
            {name:'Abbasid Caliphate (~750-1258 AD)', color:'#28b0a0', coords:[[38,50],[38,54],[37,58],[36,60],[35,62],[34,64],[33,66],[32,68],[30,68],[28,66],[26,62],[24,58],[24,54],[24,50],[26,48],[28,46],[30,46],[32,46],[34,46],[36,46],[38,46],[39,48],[38,50]]},

            // ── CRUSADER & MEDIEVAL ──
            {name:'Crusader States (~1099-1291 AD)', color:'#c8c030', coords:[[37.0,36.5],[36.5,37.5],[36.0,38.0],[35.5,37.5],[35.0,37.0],[34.5,36.5],[34.0,36.2],[33.5,36.0],[33.0,35.6],[32.5,35.2],[32.0,34.9],[31.5,34.7],[31.0,35.0],[30.5,35.0],[30.0,34.8],[29.8,34.6],[30.2,34.4],[30.8,34.4],[31.5,34.4],[32.2,34.6],[33.0,35.1],[33.5,35.5],[34.0,36.0],[34.5,36.5],[35.5,37.0],[36.0,37.5],[36.5,37.0],[37.0,36.5]]},
            {name:'Mamluk Sultanate (~1250-1517 AD)', color:'#a04898', coords:[[38,22],[36,26],[35,30],[34,34],[33,36],[33,38],[33,40],[33,42],[33,44],[33,46],[32,48],[30,48],[28,46],[26,44],[24,42],[22,42],[20,42],[18,42],[17,40],[16,38],[17,36],[18,34],[20,36],[22,38],[24,40],[26,40],[28,40],[29,38],[30,36],[31,34],[32,34],[33,35],[34,36],[36,34],[37,32],[38,28],[38,22]]},
            {name:'Mongol Empire (~1206-1368 AD)', color:'#b86828', coords:[[55,12],[53,20],[51,28],[49,36],[47,40],[45,44],[43,46],[41,50],[39,54],[38,58],[37,62],[36,66],[35,70],[34,72],[34,76],[35,80],[37,84],[39,88],[41,90],[43,90],[45,88],[47,84],[49,80],[51,76],[53,72],[55,68],[57,64],[59,60],[60,56],[62,52],[64,48],[65,44],[64,40],[62,36],[60,32],[58,28],[56,24],[54,18],[55,12]]},

            // ── OTTOMAN & MODERN ──
            {name:'Ottoman Empire (~1517-1917)', color:'#d4a04a', coords:[[47,15],[42,20],[40,25],[38,28],[37,30],[36,32],[35,34],[33,36],[31,38],[28,40],[25,42],[23,44],[22,42],[20,40],[17,38],[15,36],[20,33],[24,33],[27,30],[30,28],[33,26],[36,15],[40,12],[44,14],[47,15]]},
            {name:'British Mandate Palestine (~1920-1948)', color:'#5a9ae0', coords:[[33.3,35.6],[33.1,35.9],[32.7,35.7],[32.0,35.6],[31.5,35.5],[31.0,35.5],[30.5,35.2],[29.5,35.0],[29.5,34.9],[29.5,34.3],[30.5,34.2],[31.2,34.4],[31.8,34.5],[32.5,34.7],[33.0,35.1],[33.3,35.6]]},
            {name:'Modern Israel (1949 Armistice)', color:'#44aaff', coords:[[33.3,35.6],[33.1,35.8],[32.8,35.5],[32.1,35.1],[31.8,34.8],[31.5,34.5],[31.3,34.4],[30.8,34.4],[30.0,34.5],[29.5,34.9],[29.5,34.95],[29.55,34.6],[30.5,34.3],[31.3,34.3],[31.8,34.5],[32.5,34.7],[33.0,35.1],[33.3,35.6]]}
        ];
        empires.forEach(function(emp) {
            var latlngs = emp.coords.map(function(c) { return [c[0], c[1]]; });
            var poly = L.polygon(latlngs, {
                color: emp.color, weight: 3, opacity: 0.9,
                fillColor: emp.color, fillOpacity: 0.18,
                dashArray: '6,4'
            });
            poly.bindPopup('<div class="map-popup-title" style="color:' + emp.color + '">' + emp.name + '</div>', { className: 'map-dark-popup' });
            var empGroup = L.layerGroup([poly]);
            mapOverlayLayers['\ud83c\udff0 ' + emp.name] = empGroup;
        });

        // ── NEPHILIM / REPHAIM GIANT TERRITORIES ──
        mapOverlayLayers['\u2500\u2500 GIANT TERRITORIES \u2500\u2500'] = L.layerGroup(); // separator
        var giantZones = [
            {name:'Bashan \u2014 Land of the Rephaim (Og\'s Kingdom)', color:'#cc44ff', desc:'Home of King Og, last of the Rephaim. His iron bed was 13.5 ft long (Deut 3:11). 60 fortified cities. "All Bashan is called the land of Rephaim" (Deut 3:13). Rujm el-Hiri ("Wheel of Giants") sits directly inside this territory.',
             refs:'Deut 3:1-13; Josh 12:4-5; 13:12',
             coords:[[33.5,35.6],[33.5,36.2],[33.1,36.3],[32.7,36.0],[32.7,35.6],[33.0,35.5],[33.5,35.6]]},
            {name:'Hebron / Kiriath-Arba \u2014 Anakim Stronghold', color:'#ff6090', desc:'Arba was "the greatest man among the Anakim" (Josh 14:15). The 10 spies saw Nephilim here and said "we were like grasshoppers" (Num 13:33). Caleb drove out the three sons of Anak: Sheshai, Ahiman, and Talmai (Josh 15:14).',
             refs:'Num 13:22,33; Josh 14:12-15; 15:13-14',
             coords:[[31.65,34.95],[31.65,35.20],[31.40,35.20],[31.40,34.95],[31.65,34.95]]},
            {name:'Philistine Plain \u2014 Last Anakim Survivors (Gaza, Gath, Ashdod)', color:'#ff8844', desc:'"There were no Anakim left in the land of Israel; only in Gaza, Gath, and Ashdod some remained" (Josh 11:22). Goliath of Gath and his four giant relatives came from here (2 Sam 21:15-22). David killed Goliath; his men killed the other four.',
             refs:'Josh 11:22; 1 Sam 17:4; 2 Sam 21:15-22',
             coords:[[31.85,34.45],[31.85,34.90],[31.55,34.90],[31.10,34.50],[31.10,34.40],[31.55,34.40],[31.85,34.45]]},
            {name:'Valley of Rephaim (near Jerusalem)', color:'#ee55cc', desc:'Named after the Rephaim giants. David fought the Philistines here twice (2 Sam 5:18-25). Located southwest of Jerusalem between Bethlehem and the city.',
             refs:'Josh 15:8; 18:16; 2 Sam 5:18-25',
             coords:[[31.78,35.14],[31.78,35.22],[31.73,35.22],[31.73,35.14],[31.78,35.14]]},
            {name:'Moab \u2014 Emim Territory', color:'#aa66ff', desc:'The Emim ("terrors/frightening ones") lived in Moab before God dispossessed them for Lot\'s descendants. "A people as great, numerous, and tall as the Anakim \u2014 they are also regarded as Rephaim" (Deut 2:10-11).',
             refs:'Deut 2:10-11; Gen 14:5',
             coords:[[31.8,35.5],[31.8,35.9],[31.2,35.9],[31.0,35.6],[31.0,35.5],[31.5,35.4],[31.8,35.5]]},
            {name:'Ammon \u2014 Zamzummim Territory', color:'#77bbff', desc:'The Zamzummim ("whisperers/plotters") inhabited the territory God later gave to the Ammonites. "A people as great, numerous, and tall as the Anakim, but the LORD destroyed them" (Deut 2:20-21). Og\'s iron bed was preserved in Rabbah of Ammon.',
             refs:'Deut 2:20-21; 3:11',
             coords:[[32.3,35.8],[32.3,36.2],[31.9,36.2],[31.9,35.8],[32.3,35.8]]}
        ];
        giantZones.forEach(function(gz) {
            var latlngs = gz.coords.map(function(c) { return [c[0], c[1]]; });
            var poly = L.polygon(latlngs, {
                color: gz.color, weight: 3, opacity: 0.9,
                fillColor: gz.color, fillOpacity: 0.25,
                dashArray: '4,4'
            });
            var popupHtml = '<div class="map-popup-title" style="color:' + gz.color + '">' + gz.name + '</div>' +
                '<div class="map-popup-desc">' + gz.desc + '</div>' +
                '<div class="map-popup-refs">\ud83d\udcdc ' + gz.refs + '</div>';
            poly.bindPopup(popupHtml, { maxWidth: 380, className: 'map-dark-popup' });
            var gzGroup = L.layerGroup([poly]);
            mapOverlayLayers['\ud83d\udc79 ' + gz.name] = gzGroup;
        });

        // ── PHOENICIAN / CANAANITE COASTAL TERRITORY ──
        mapOverlayLayers['\u2500\u2500 TERRITORIES \u2500\u2500'] = L.layerGroup(); // separator
        var territories = [
            {name:'Phoenician / Canaanite Coast (~1200-332 BC)', color:'#dd66aa',
             desc:'The cursed Canaanite survivors (Gen 9:25 + 10:15-19) who thrived on the northern coast because Israel never fully obeyed the command to drive them out (Josh 13:2-6). They called themselves Canaanites; "Phoenician" is a Greek exonym from phoinix ("purple"). Direct cultural descendants of Bronze Age Canaanites. God sovereignly used their maritime genius, trade empire, and alphabet for His purposes (Temple cedar, Scripture\'s writing system) while judging their pride and idolatry exactly as prophesied (Ezek 26-28). Their cities were epicenters of Baal worship, child sacrifice (tophets), and sacred prostitution. Baalbek in their heartland contains the largest megaliths on earth.',
             refs:'Gen 9:25; 10:15-19; Josh 13:2-6; 1 Kings 5; Ezek 26-28; Judg 3:1-4',
             coords:[[34.90,35.80],[34.85,35.86],[34.12,35.65],[33.56,35.38],[33.27,35.20],[33.05,35.07],[33.05,35.40],[33.27,35.55],[33.56,35.70],[34.12,35.90],[34.85,36.10],[34.90,35.80]]},
            {name:'Nimrod\'s Empire \u2014 Babel to Assyria (~post-Flood)', color:'#a07a4a',
             desc:'Nimrod ("rebel"), son of Cush, son of Ham \u2014 the first post-Flood "mighty one" (gibbor, the same term used for Nephilim in Gen 6:4). "A mighty hunter before the LORD" (Gen 10:9) implies opposition to God. His kingdom began at Babel (center of unified rebellion, Gen 11:1-9) and expanded to build Nineveh and the great cities of Assyria. Nimrod embodies post-Flood pride: Babel\'s tower was a counterfeit heavenly access point. God scattered that rebellion via language confusion (Gen 11:8-9). Arabic legends claim Nimrod sent giants to rebuild Baalbek as an extension of Babel\'s project.',
             refs:'Gen 10:8-12; Gen 11:1-9; Micah 5:6',
             coords:[[32.0,43.5],[32.5,44.4],[33.0,44.0],[33.5,43.5],[34.5,43.0],[35.5,43.0],[36.5,43.5],[37.0,43.0],[36.5,42.0],[36.0,41.0],[35.0,40.0],[34.0,39.0],[33.5,38.0],[33.0,37.0],[32.5,38.0],[31.5,40.0],[31.0,42.0],[31.0,44.0],[31.5,45.0],[32.0,46.0],[32.5,47.0],[33.0,46.5],[33.5,45.5],[33.5,44.5],[32.0,43.5]]}
        ];
        territories.forEach(function(terr) {
            var latlngs = terr.coords.map(function(c) { return [c[0], c[1]]; });
            var poly = L.polygon(latlngs, {
                color: terr.color, weight: 2, opacity: 0.7,
                fillColor: terr.color, fillOpacity: 0.15,
                dashArray: '8,4'
            });
            var popupHtml = '<div class="map-popup-title" style="color:' + terr.color + '">' + terr.name + '</div>' +
                '<div class="map-popup-desc">' + terr.desc + '</div>' +
                '<div class="map-popup-refs">\ud83d\udcdc ' + terr.refs + '</div>';
            poly.bindPopup(popupHtml, { maxWidth: 400, className: 'map-dark-popup' });
            var tGroup = L.layerGroup([poly]);
            mapOverlayLayers['\ud83d\uddfa\ufe0f ' + terr.name] = tGroup;
        });

        // ── Nimrod-to-Baalbek Connection Line ──
        var nimrodBaalbekGroup = L.layerGroup();
        var nbLine = L.polyline([[32.54, 44.42], [34.00, 42.00], [35.00, 40.00], [34.50, 38.00], [34.01, 36.20]], {
            color: '#a07a4a', weight: 2, opacity: 0.6, dashArray: '12 6 4 6'
        });
        nimrodBaalbekGroup.addLayer(nbLine);
        var nbLabel = L.divIcon({
            className: 'map-line-label',
            html: '<span style="color:#a07a4a;background:rgba(12,14,20,0.9);padding:2px 6px;border-radius:3px;font-size:11px;border:1px solid #a07a4a40">Nimrod \u2192 Baalbek (legend)</span>',
            iconSize: [0, 0]
        });
        nimrodBaalbekGroup.addLayer(L.marker([34.50, 38.00], { icon: nbLabel, interactive: false }));
        mapOverlayLayers['\ud83d\udd25 Nimrod \u2192 Baalbek Connection'] = nimrodBaalbekGroup;

        mapOverlayLayers['\u2500\u2500 REFERENCE LINES \u2500\u2500'] = L.layerGroup(); // separator
        mapOverlayLayers['\ud83d\udfe2 Greenwich Lines (0\u00b0 + 33\u00b0E)'] = greenwichLineGroup;
        mapOverlayLayers['\ud83d\udfe0 Paris Lines (2.34\u00b0 + 33\u00b0E + 33.33\u00b0E)'] = parisLineGroup;
        mapOverlayLayers['\ud83d\udfe1 33\u00b0N + 33.33\u00b0N Parallels'] = parallelLineGroup;
        mapOverlayLayers['\u2720 Mt. Hermon Crosshair'] = hermonCrossGroup;

        // ── MODERN REFERENCE OVERLAYS (transparent tile layers) ──
        mapOverlayLayers['\u2500\u2500 MODERN REFERENCE \u2500\u2500'] = L.layerGroup(); // separator

        var cartoLabels = L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_only_labels/{z}/{x}/{y}{r}.png', {
            maxNativeZoom: 18, maxZoom: 20, subdomains: 'abcd', opacity: 0.9
        });
        mapOverlayLayers['\ud83c\udff7\ufe0f Modern Labels (Cities/Countries)'] = cartoLabels;

        var esriBoundaries = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer/tile/{z}/{y}/{x}', {
            maxNativeZoom: 18, maxZoom: 20, opacity: 0.85
        });
        mapOverlayLayers['\ud83c\udf10 Political Borders & Places'] = esriBoundaries;

        var esriTransport = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Transportation/MapServer/tile/{z}/{y}/{x}', {
            maxNativeZoom: 18, maxZoom: 20, opacity: 0.7
        });
        mapOverlayLayers['\ud83d\udee3\ufe0f Modern Roads'] = esriTransport;

        mapLayerControl = L.control.layers(mapBaseLayers, mapOverlayLayers, {
            position: 'topleft',
            collapsed: true,
            sortLayers: false
        }).addTo(mapInstance);

        // ── Enhance layer control: add close button + convert separators to group headers ──
        (function enhanceLayerControl() {
            var container = mapLayerControl.getContainer();
            if (!container) return;

            // Add a close button at the top of the expanded layer list
            var layersList = container.querySelector('.leaflet-control-layers-list');
            if (layersList) {
                var closeBtn = document.createElement('div');
                closeBtn.className = 'map-layers-close-btn';
                closeBtn.innerHTML = '\u2715 Close Layers';
                closeBtn.style.cssText = 'text-align:right;padding:4px 8px 6px;cursor:pointer;color:var(--gold);font-size:0.78rem;font-weight:600;border-bottom:1px solid var(--border);margin-bottom:4px;user-select:none';
                closeBtn.addEventListener('click', function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    mapLayerControl.collapse();
                });
                layersList.insertBefore(closeBtn, layersList.firstChild);
            }

            // Convert separator entries into styled group headers
            var labels = container.querySelectorAll('.leaflet-control-layers-overlays label');
            labels.forEach(function(label) {
                var span = label.querySelector('span');
                if (!span) return;
                var text = span.textContent.trim();
                // Detect separator entries like "── JOURNEYS ──"
                if (text.match(/^\u2500\u2500\s*.+\s*\u2500\u2500$/)) {
                    var groupName = text.replace(/\u2500/g, '').trim();
                    label.classList.add('map-layer-group-header');
                    label.innerHTML = '<span class="map-layer-group-toggle">\u25BC</span> ' + groupName;
                    // Hide the checkbox for separator entries
                    var input = label.querySelector('input');
                    if (input) input.style.display = 'none';

                    // Collapsible: click header to toggle next siblings until next header
                    label.style.cursor = 'pointer';
                    label.addEventListener('click', function(e) {
                        e.preventDefault();
                        e.stopPropagation();
                        var toggle = this.querySelector('.map-layer-group-toggle');
                        var collapsed = toggle.textContent === '\u25B6';
                        toggle.textContent = collapsed ? '\u25BC' : '\u25B6';
                        var sibling = this.nextElementSibling;
                        while (sibling && !sibling.classList.contains('map-layer-group-header')) {
                            sibling.style.display = collapsed ? '' : 'none';
                            sibling = sibling.nextElementSibling;
                        }
                    });
                }
            });
        })();

        // ── Coordinates display ──
        var coordDiv = L.DomUtil.create('div', 'map-coords-display');
        coordDiv.style.cssText = 'position:absolute;bottom:8px;left:8px;z-index:1000;background:rgba(12,14,20,0.85);color:#c9a84c;padding:4px 10px;border-radius:4px;font-size:12px;font-family:monospace;border:1px solid #c9a84c30;pointer-events:none';
        coordDiv.innerHTML = 'Move mouse over map';
        document.getElementById('mapContainer').appendChild(coordDiv);
        mapInstance.on('mousemove', function(e) {
            var gLng = e.latlng.lng;
            var pLng = gLng - 2.3372;
            coordDiv.innerHTML = e.latlng.lat.toFixed(4) + '\u00b0N, ' + gLng.toFixed(4) + '\u00b0E (Greenwich) | ' + pLng.toFixed(4) + '\u00b0E (Paris)';
        });

        // ── Scale bar ──
        L.control.scale({ position: 'bottomright', imperial: true, metric: true }).addTo(mapInstance);

        // Remove old filter bar (replaced by layer control)
        var oldFilter = document.getElementById('mapFilterBar');
        if (oldFilter) oldFilter.style.display = 'none';

        // ── Map Search ──
        var mapSearchInput = document.getElementById('mapSearchInput');
        var mapSearchResults = document.getElementById('mapSearchResults');

        if (mapSearchInput) {
            // Build searchable items list: sites + empires + journeys + giant zones
            var searchableItems = [];
            MAP_SITES.forEach(function(s) {
                searchableItems.push({ name: s.name, cat: (mapCategories[s.cat] || {}).label || s.cat, type: 'site', lat: s.lat, lng: s.lng, data: s });
            });
            empires.forEach(function(emp) {
                var center = emp.coords.reduce(function(a, c) { return [a[0] + c[0], a[1] + c[1]]; }, [0, 0]);
                center = [center[0] / emp.coords.length, center[1] / emp.coords.length];
                searchableItems.push({ name: emp.name, cat: 'Empire', type: 'empire', lat: center[0], lng: center[1] });
            });
            MAP_JOURNEYS.forEach(function(j) {
                var mid = j.waypoints[Math.floor(j.waypoints.length / 2)];
                searchableItems.push({ name: j.name, cat: 'Journey', type: 'journey', lat: mid.lat, lng: mid.lng });
            });
            giantZones.forEach(function(gz) {
                var center = gz.coords.reduce(function(a, c) { return [a[0] + c[0], a[1] + c[1]]; }, [0, 0]);
                center = [center[0] / gz.coords.length, center[1] / gz.coords.length];
                searchableItems.push({ name: gz.name, cat: 'Giant Territory', type: 'giant', lat: center[0], lng: center[1] });
            });

            mapSearchInput.addEventListener('input', function() {
                var q = this.value.toLowerCase().trim();
                if (q.length < 2) { mapSearchResults.classList.remove('open'); return; }
                var matches = searchableItems.filter(function(item) {
                    return item.name.toLowerCase().indexOf(q) !== -1 || item.cat.toLowerCase().indexOf(q) !== -1;
                }).slice(0, 12);
                if (matches.length === 0) {
                    mapSearchResults.innerHTML = '<div class="map-search-no-results">No results for "' + q + '"</div>';
                } else {
                    mapSearchResults.innerHTML = matches.map(function(m) {
                        return '<div class="map-search-result" data-lat="' + m.lat + '" data-lng="' + m.lng + '" data-type="' + m.type + '">' +
                            '<div class="map-search-result-name">' + m.name + '</div>' +
                            '<div class="map-search-result-cat">' + m.cat + '</div></div>';
                    }).join('');
                }
                mapSearchResults.classList.add('open');
            });

            mapSearchResults.addEventListener('click', function(e) {
                var item = e.target.closest('.map-search-result');
                if (!item) return;
                var lat = parseFloat(item.dataset.lat);
                var lng = parseFloat(item.dataset.lng);
                mapInstance.setView([lat, lng], 10, { animate: true });
                mapSearchResults.classList.remove('open');
                mapSearchInput.value = '';
                // Open popup if it's a site marker
                if (item.dataset.type === 'site') {
                    var name = item.querySelector('.map-search-result-name').textContent;
                    mapMarkers.forEach(function(marker) {
                        if (marker._siteData && marker._siteData.name === name) {
                            // Ensure the layer is visible
                            var cat = marker._siteData.cat;
                            if (mapLayerGroups[cat] && !mapInstance.hasLayer(mapLayerGroups[cat])) {
                                mapLayerGroups[cat].addTo(mapInstance);
                            }
                            marker.openPopup();
                        }
                    });
                }
            });

            // Close search on click outside
            document.addEventListener('click', function(e) {
                if (!e.target.closest('.map-search-box')) {
                    mapSearchResults.classList.remove('open');
                }
            });

            // Close search on Escape
            mapSearchInput.addEventListener('keydown', function(e) {
                if (e.key === 'Escape') {
                    mapSearchResults.classList.remove('open');
                    mapSearchInput.value = '';
                    mapSearchInput.blur();
                }
            });
        }

        setTimeout(function() { mapInstance.invalidateSize(); }, 200);
    }

    function createMarkerIcon(cat) {
        var c = mapCategories[cat] || mapCategories['biblical'];
        return L.divIcon({
            className: 'map-marker-icon',
            html: '<div style="background:' + c.color + ';width:30px;height:30px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:15px;border:2px solid rgba(255,255,255,0.4);box-shadow:0 2px 10px rgba(0,0,0,0.5);cursor:pointer;transition:transform 0.15s">' + c.icon + '</div>',
            iconSize: [30, 30],
            iconAnchor: [15, 15],
            popupAnchor: [0, -18]
        });
    }

    // Legacy stubs (replaced by layer control)
    function addMapMarkers() {}
    function updateMapMarkers() {}

    // ── Bible Truth Matrix ──────────────────────────────────
    var matrixOverlay = document.getElementById('matrixOverlay');
    var matrixSelectedDoctrine = 'god';
    var matrixSelectedCat = 'all';

    function openMatrix() {
        logEvent('feature', 'bible_truth_matrix');
        renderMatrix();
        matrixOverlay.classList.add('open');
    }
    function closeMatrix() { matrixOverlay.classList.remove('open'); }

    function renderMatrix() {
        var content = document.getElementById('matrixContent');
        var html = '';

        // Doctrine tabs
        html += '<div class="matrix-doctrine-tabs">';
        DOCTRINE_KEYS.forEach(function(key) {
            var active = key === matrixSelectedDoctrine ? ' active' : '';
            html += '<button class="matrix-tab' + active + '" data-doctrine="' + key + '">' + BIBLE_TEACHES[key].label + '</button>';
        });
        html += '</div>';

        var bt = BIBLE_TEACHES[matrixSelectedDoctrine];

        // Bible teaches banner
        html += '<div class="matrix-bible-teaches">';
        html += '<div class="matrix-bible-header"><span class="matrix-bible-icon">\u2727</span> What the Bible Teaches</div>';
        html += '<p>' + esc(bt.teaching) + '</p>';
        html += '<div class="matrix-bible-refs">' + bt.scriptures.map(function(s) { return '<span class="matrix-ref">' + esc(s) + '</span>'; }).join('') + '</div>';
        html += '</div>';

        // Legend
        html += '<div class="matrix-legend">';
        Object.keys(ALIGNMENT_INFO).forEach(function(k) {
            var a = ALIGNMENT_INFO[k];
            html += '<span class="matrix-legend-item"><span class="matrix-dot" style="background:' + a.color + '"></span>' + a.label + '</span>';
        });
        html += '</div>';

        // Category filter
        html += '<div class="matrix-cat-filter">';
        html += '<button class="matrix-cat-btn' + (matrixSelectedCat === 'all' ? ' active' : '') + '" data-cat="all">All</button>';
        Object.keys(RELIGION_CATEGORIES).forEach(function(k) {
            var active = matrixSelectedCat === k ? ' active' : '';
            html += '<button class="matrix-cat-btn' + active + '" data-cat="' + k + '">' + RELIGION_CATEGORIES[k].icon + ' ' + RELIGION_CATEGORIES[k].label + '</button>';
        });
        html += '</div>';

        // Religion cards — sorted by alignment (most aligned first)
        var ALIGN_SCORE = { full: 5, mostly: 4, parallel: 3, partial: 2, divergent: 1 };
        function getOverallScore(r) {
            var total = 0;
            DOCTRINE_KEYS.forEach(function(k) { total += (ALIGN_SCORE[r.d[k]] || 1); });
            return total;
        }
        var filtered = matrixSelectedCat === 'all' ? RELIGIONS_DATA.slice() : RELIGIONS_DATA.filter(function(r) { return r.cat === matrixSelectedCat; });
        filtered.sort(function(a, b) {
            // Primary: selected doctrine alignment
            var da = ALIGN_SCORE[a.d[matrixSelectedDoctrine]] || 1;
            var db = ALIGN_SCORE[b.d[matrixSelectedDoctrine]] || 1;
            if (db !== da) return db - da;
            // Secondary: overall alignment score
            return getOverallScore(b) - getOverallScore(a);
        });
        html += '<div class="matrix-grid">';
        filtered.forEach(function(r) {
            var alignment = r.d[matrixSelectedDoctrine] || 'divergent';
            var ai = ALIGNMENT_INFO[alignment];
            var catInfo = RELIGION_CATEGORIES[r.cat] || {};
            var overallPct = Math.round((getOverallScore(r) / (DOCTRINE_KEYS.length * 5)) * 100);
            var pctColor = overallPct >= 80 ? '#22c55e' : overallPct >= 60 ? '#3b82f6' : overallPct >= 40 ? '#f59e0b' : '#ef4444';
            html += '<div class="matrix-card" style="border-left-color:' + ai.color + ';cursor:pointer" data-religion="' + r.id + '" title="Click to explore ' + esc(r.name) + '">';
            html += '<div class="matrix-card-header">';
            html += '<div class="matrix-card-name">' + esc(r.name) + '</div>';
            html += '<div class="matrix-card-meta">' + (catInfo.icon || '') + ' ' + esc(r.founded) + ' \u00B7 ' + esc(r.adherents) + '</div>';
            html += '</div>';
            html += '<div class="matrix-alignment" style="color:' + ai.color + '">';
            html += '<span class="matrix-dot" style="background:' + ai.color + '"></span>' + ai.label;
            html += '<span class="matrix-pct" style="color:' + pctColor + '">' + overallPct + '% overall</span>';
            html += '</div>';
            html += '<div class="matrix-card-explore">Tap to explore \u2192</div>';
            html += '</div>';
        });
        html += '</div>';

        // Heatmap summary table
        html += '<div class="matrix-heatmap-section"><h3>Full Alignment Heatmap</h3>';
        html += '<div class="matrix-heatmap-scroll"><table class="matrix-heatmap"><thead><tr><th>Religion</th>';
        DOCTRINE_KEYS.forEach(function(k) {
            html += '<th title="' + BIBLE_TEACHES[k].label + '">' + k.charAt(0).toUpperCase() + k.slice(0,3) + '</th>';
        });
        html += '<th>Score</th></tr></thead><tbody>';
        filtered.forEach(function(r) {
            var overallPct = Math.round((getOverallScore(r) / (DOCTRINE_KEYS.length * 5)) * 100);
            var pctColor = overallPct >= 80 ? '#22c55e' : overallPct >= 60 ? '#3b82f6' : overallPct >= 40 ? '#f59e0b' : '#ef4444';
            html += '<tr style="cursor:pointer" data-religion="' + r.id + '">';
            html += '<td class="matrix-hm-name">' + esc(r.name) + '</td>';
            DOCTRINE_KEYS.forEach(function(k) {
                var al = r.d[k] || 'divergent';
                var ai = ALIGNMENT_INFO[al];
                html += '<td><span class="matrix-hm-cell" style="background:' + ai.color + '" title="' + ai.label + '"></span></td>';
            });
            html += '<td style="font-size:0.72rem;font-weight:700;color:' + pctColor + ';text-align:center">' + overallPct + '%</td>';
            html += '</tr>';
        });
        html += '</tbody></table></div></div>';

        content.innerHTML = html;

        // Event listeners for tabs
        content.querySelectorAll('.matrix-tab').forEach(function(btn) {
            btn.addEventListener('click', function() {
                matrixSelectedDoctrine = this.dataset.doctrine;
                renderMatrix();
            });
        });
        content.querySelectorAll('.matrix-cat-btn').forEach(function(btn) {
            btn.addEventListener('click', function() {
                matrixSelectedCat = this.dataset.cat;
                renderMatrix();
            });
        });
        // Click handlers for religion cards
        content.querySelectorAll('.matrix-card[data-religion]').forEach(function(card) {
            card.addEventListener('click', function() {
                showReligionDetail(this.dataset.religion);
            });
        });
        // Click handlers for heatmap rows
        content.querySelectorAll('.matrix-heatmap tbody tr[data-religion]').forEach(function(row) {
            row.addEventListener('click', function() {
                showReligionDetail(this.dataset.religion);
            });
        });
    }

    // ── Religion Detail Overlay ────────────────────────────────
    var religionDetailOverlay = document.getElementById('religionDetailOverlay');

    function showReligionDetail(religionId) {
        logEvent('feature', 'religion_detail_' + religionId);
        var detail = RELIGIONS_DETAIL[religionId];
        if (!detail) { return; }

        var catInfo = RELIGION_CATEGORIES[detail.category] || {};
        var titleEl = document.getElementById('religionDetailTitle');
        var contentEl = document.getElementById('religionDetailContent');

        // Count alignments
        var counts = { full: 0, mostly: 0, parallel: 0, partial: 0, divergent: 0 };
        DOCTRINE_KEYS.forEach(function(k) {
            var al = detail.doctrines[k] ? detail.doctrines[k].alignment : 'divergent';
            counts[al] = (counts[al] || 0) + 1;
        });

        // Title
        titleEl.innerHTML = '<h2>' + (catInfo.icon || '') + ' ' + esc(detail.name) + '</h2>' +
            '<div class="religion-detail-meta">' +
            '<span class="religion-meta-item"><strong>Founded:</strong> ' + esc(detail.founded) + '</span>' +
            (detail.founder ? '<span class="religion-meta-item"><strong>Founder:</strong> ' + esc(detail.founder) + '</span>' : '') +
            '<span class="religion-meta-item"><strong>Adherents:</strong> ' + esc(detail.adherents) + '</span>' +
            '</div>';

        var html = '';

        // Alignment summary bar
        html += '<div class="religion-alignment-summary">';
        Object.keys(ALIGNMENT_INFO).forEach(function(k) {
            if (counts[k] > 0) {
                var ai = ALIGNMENT_INFO[k];
                html += '<span class="religion-summary-badge" style="background:' + ai.color + '20;color:' + ai.color + ';border:1px solid ' + ai.color + '40">';
                html += counts[k] + ' ' + ai.label;
                html += '</span>';
            }
        });
        html += '</div>';

        // Doctrine comparison cards
        html += '<div class="religion-doctrines-grid">';
        DOCTRINE_KEYS.forEach(function(k) {
            var bt = BIBLE_TEACHES[k];
            var rd = detail.doctrines[k] || { position: 'No information available.', alignment: 'divergent' };
            var ai = ALIGNMENT_INFO[rd.alignment] || ALIGNMENT_INFO.divergent;

            html += '<div class="religion-doctrine-card">';
            html += '<div class="religion-doctrine-header">';
            html += '<span class="religion-doctrine-label">' + esc(bt.label) + '</span>';
            html += '<span class="religion-doctrine-badge" style="background:' + ai.color + '20;color:' + ai.color + ';border:1px solid ' + ai.color + '40">' + ai.label + '</span>';
            html += '</div>';

            // Bible teaches
            html += '<div class="religion-doctrine-bible">';
            html += '<div class="religion-doctrine-source">\u2727 Bible Teaches</div>';
            html += '<p>' + esc(bt.teaching) + '</p>';
            html += '</div>';

            // Religion's position
            html += '<div class="religion-doctrine-position" style="border-left-color:' + ai.color + '">';
            html += '<div class="religion-doctrine-source">' + (catInfo.icon || '') + ' ' + esc(detail.name) + '</div>';
            html += '<p>' + esc(rd.position) + '</p>';
            html += '</div>';

            html += '</div>';
        });
        html += '</div>';

        contentEl.innerHTML = html;
        religionDetailOverlay.classList.add('open');
    }

    function closeReligionDetail() {
        religionDetailOverlay.classList.remove('open');
    }

    if (document.getElementById('religionDetailClose')) {
        document.getElementById('religionDetailClose').addEventListener('click', closeReligionDetail);
    }
    if (religionDetailOverlay) {
        religionDetailOverlay.addEventListener('click', function(e) {
            if (e.target === religionDetailOverlay) closeReligionDetail();
        });
    }

    // ── Patriarch Ages Chart (Genesis 5 & 11) ────────────────
    var patriarchChartOverlay = document.getElementById('patriarchChartOverlay');

    // Genesis 5 — Adam to Noah (pre-flood)
    var PATRIARCH_PREFLOOD = [
        { name: 'Adam',       heb: '\u05D0\u05B8\u05D3\u05B8\u05DD',     born: 0,    age: 930, color: '#c9a84c',
          meaning: 'Man', root: 'From \u02BEadam\u0101h (\u05D0\u05B2\u05D3\u05B8\u05DE\u05B8\u05D4, ground/earth). Humanity formed from the dust.' },
        { name: 'Seth',       heb: '\u05E9\u05C1\u05B5\u05EA',         born: 130,  age: 912, color: '#d4a843',
          meaning: 'Appointed', root: 'From sh\u012Bth (\u05E9\u05C1\u05B4\u05D9\u05EA, to set/appoint). Gen 4:25 \u2014 "God has appointed for me another offspring."' },
        { name: 'Enosh',      heb: '\u05D0\u05B1\u05E0\u05D5\u05B9\u05E9\u05C1', born: 235,  age: 905, color: '#c9963c',
          meaning: 'Mortal', root: 'From \u02BEanash (\u05D0\u05B8\u05E0\u05B7\u05E9\u05C1, to be weak/frail). The recognition of human mortality and need for God.' },
        { name: 'Kenan',      heb: '\u05E7\u05B5\u05D9\u05E0\u05B8\u05DF',   born: 325,  age: 910, color: '#b8893a',
          meaning: 'Sorrow', root: 'From q\u012Bn\u0101h (\u05E7\u05B4\u05D9\u05E0\u05B8\u05D4, lamentation/dirge). The human condition of grief after the Fall.' },
        { name: 'Mahalalel',  heb: '\u05DE\u05B7\u05D4\u05B2\u05DC\u05B7\u05DC\u05B0\u05D0\u05B5\u05DC', born: 395, age: 895, color: '#a67d38',
          meaning: 'Praise of God', root: 'Compound: mahal\u0101l (\u05DE\u05B7\u05D4\u05B2\u05DC\u05B8\u05DC, praise) + \u02BEEl (\u05D0\u05B5\u05DC, God). The Blessed God is worthy of praise.' },
        { name: 'Jared',      heb: '\u05D9\u05B6\u05E8\u05B6\u05D3',       born: 460,  age: 962, color: '#947136',
          meaning: 'Shall Come Down', root: 'From y\u0101rad (\u05D9\u05B8\u05E8\u05B7\u05D3, to descend). 1 Enoch tradition: the Watchers descended in Jared\u2019s days.' },
        { name: 'Enoch',      heb: '\u05D7\u05B2\u05E0\u05D5\u05B9\u05DA\u05B0',  born: 622,  age: 365, color: '#6aab73',
          meaning: 'Teaching / Dedicated', root: 'From ch\u0101nak (\u05D7\u05B8\u05E0\u05B7\u05DA, to train up/dedicate). He walked with God and was taken (Gen 5:24).' },
        { name: 'Methuselah', heb: '\u05DE\u05B0\u05EA\u05D5\u05BC\u05E9\u05C1\u05B6\u05DC\u05B7\u05D7', born: 687, age: 969, color: '#5b8dbf',
          meaning: 'His Death Shall Bring', root: 'Compound: m\u0115t\u016B (\u05DE\u05B5\u05EA\u05D5\u05BC, his death) + sh\u0101lach (\u05E9\u05C1\u05B8\u05DC\u05B7\u05D7, to send). The year he died, the Flood came.' },
        { name: 'Lamech',     heb: '\u05DC\u05B6\u05DE\u05B6\u05DA\u05B0',   born: 874,  age: 777, color: '#9b7ec8',
          meaning: 'The Despairing', root: 'Possibly from m\u016Bk (\u05DE\u05D5\u05BC\u05DA, to be brought low). His life of 777 years \u2014 divine perfection tripled.' },
        { name: 'Noah',       heb: '\u05E0\u05B9\u05D7\u05B7',         born: 1056, age: 950, color: '#2d9a8f',
          meaning: 'Rest / Comfort', root: 'From n\u016Bach (\u05E0\u05D5\u05BC\u05D7\u05B7, to rest). Gen 5:29 \u2014 "This one shall comfort us from the cursed ground."' }
    ];

    // Genesis 11 — Shem to Abraham (post-flood)
    var PATRIARCH_POSTFLOOD = [
        { name: 'Shem',       heb: '\u05E9\u05C1\u05B5\u05DD',         born: 1558, age: 600, color: '#c9a84c',
          meaning: 'Name / Renown', root: 'Sh\u0113m (\u05E9\u05C1\u05B5\u05DD, name/fame). The line through which YHWH\u2019s Name would be known to the world.' },
        { name: 'Arpachshad', heb: '\u05D0\u05B7\u05E8\u05B0\u05E4\u05B7\u05DB\u05B0\u05E9\u05C1\u05B7\u05D3', born: 1658, age: 438, color: '#b8a04c',
          meaning: 'Healer / Boundary', root: 'Uncertain. Possibly "healer from Chaldea" or "stronghold of the boundary." First born after the Flood (Gen 11:10).' },
        { name: 'Shelah',     heb: '\u05E9\u05C1\u05B6\u05DC\u05B7\u05D7',     born: 1693, age: 433, color: '#a89940',
          meaning: 'Sent Forth', root: 'From sh\u0101lach (\u05E9\u05C1\u05B8\u05DC\u05B7\u05D7, to send). A sprout sent out \u2014 the line is being purposefully directed.' },
        { name: 'Eber',       heb: '\u05E2\u05B5\u05D1\u05B6\u05E8',       born: 1723, age: 464, color: '#988f38',
          meaning: 'One Who Crosses Over', root: 'From \u02BEavar (\u05E2\u05B8\u05D1\u05B7\u05E8, to cross/pass through). Root of "Hebrew" (\u02BEivr\u012B). The people who cross boundaries.' },
        { name: 'Peleg',      heb: '\u05E4\u05B6\u05BC\u05DC\u05B6\u05D2',     born: 1757, age: 239, color: '#887e30',
          meaning: 'Division', root: 'From p\u0101lag (\u05E4\u05B8\u05BC\u05DC\u05B7\u05D2, to divide). Gen 10:25 \u2014 "in his days the earth was divided." Tower of Babel event.' },
        { name: 'Reu',        heb: '\u05E8\u05B0\u05E2\u05D5\u05BC',       born: 1787, age: 239, color: '#786e28',
          meaning: 'Friend / Shepherd', root: 'From r\u0101\u02BE\u0101h (\u05E8\u05B8\u05E2\u05B8\u05D4, to tend/associate with). Friendship and shepherding \u2014 relational faithfulness.' },
        { name: 'Serug',      heb: '\u05E9\u05C2\u05B0\u05E8\u05D5\u05BC\u05D2',   born: 1819, age: 230, color: '#685e20',
          meaning: 'Branch / Tendril', root: 'From s\u0101rag (\u05E9\u05C2\u05B8\u05E8\u05B7\u05D2, to intertwine). A branch growing, intertwining with God\u2019s plan.' },
        { name: 'Nahor',      heb: '\u05E0\u05B8\u05D7\u05D5\u05B9\u05E8',     born: 1849, age: 148, color: '#585018',
          meaning: 'Snorting / Ardent', root: 'From n\u0101char (\u05E0\u05B8\u05D7\u05B7\u05E8, to snort/be zealous). Burning desire \u2014 anticipation building toward the promise.' },
        { name: 'Terah',      heb: '\u05EA\u05B6\u05BC\u05E8\u05B7\u05D7',     born: 1878, age: 205, color: '#484010',
          meaning: 'Wanderer / Delay', root: 'Possibly from t\u0101rach (to wander/delay). An idolater in Ur (Josh 24:2) \u2014 but God calls his son out.' },
        { name: 'Abraham',    heb: '\u05D0\u05B7\u05D1\u05B0\u05E8\u05B8\u05D4\u05B8\u05DD', born: 1948, age: 175, color: '#c9a84c',
          meaning: 'Father of Multitudes', root: 'Originally Abram (\u05D0\u05B7\u05D1\u05B0\u05E8\u05B8\u05DD, exalted father). God renames him (Gen 17:5) \u2014 from one man to all nations.' }
    ];

    var PATRIARCH_DATA = PATRIARCH_PREFLOOD.concat(PATRIARCH_POSTFLOOD);
    var FLOOD_YEAR = 1656; // AM (Anno Mundi) — Genesis 7:6, Noah was 600

    function openPatriarchChart() {
        logEvent('feature', 'patriarch_chart');
        renderPatriarchChart();
        patriarchChartOverlay.classList.add('open');
    }
    function closePatriarchChart() { patriarchChartOverlay.classList.remove('open'); }

    function renderPatriarchChart() {
        var content = document.getElementById('patriarchChartContent');
        if (!content) return;

        var maxYear = 2200; // chart extent (Abraham dies 2123 AM)
        var chartWidth = 100; // percentage-based

        var html = '<div class="pc-container">';

        // Legend
        html += '<div class="pc-legend">' +
            '<div class="pc-legend-item"><div class="pc-legend-swatch" style="background:#6aab73"></div> Taken by God (Enoch)</div>' +
            '<div class="pc-legend-item"><div class="pc-legend-swatch" style="background:rgba(91,141,191,0.6)"></div> The Flood (1656 AM)</div>' +
            '<div class="pc-legend-item"><div class="pc-legend-swatch" style="background:rgba(180,80,60,0.6)"></div> Babel / Division (~1757 AM)</div>' +
            '<div class="pc-legend-item">Hover/tap bars for name meanings &amp; details</div>' +
            '</div>';

        // ════════════════════════════════════════════════════════
        // THE GOSPEL HIDDEN IN THE NAMES — Genesis 5
        // ════════════════════════════════════════════════════════
        html += '<div class="pc-gospel-message">' +
            '<h4>\u2721 The Gospel Hidden in the Names \u2014 Genesis 5</h4>' +
            '<div class="pc-gospel-text">' +
            '<span class="pc-gm-name">Adam</span> <span class="pc-gm-word">Man</span> ' +
            '<span class="pc-gm-name">Seth</span> <span class="pc-gm-word">(is) appointed</span> ' +
            '<span class="pc-gm-name">Enosh</span> <span class="pc-gm-word">mortal</span> ' +
            '<span class="pc-gm-name">Kenan</span> <span class="pc-gm-word">sorrow;</span> ' +
            '<span class="pc-gm-name">Mahalalel</span> <span class="pc-gm-word">(but) the Blessed God</span> ' +
            '<span class="pc-gm-name">Jared</span> <span class="pc-gm-word">shall come down,</span> ' +
            '<span class="pc-gm-name">Enoch</span> <span class="pc-gm-word">teaching</span> ' +
            '<span class="pc-gm-name">Methuselah</span> <span class="pc-gm-word">(that) His death shall bring</span> ' +
            '<span class="pc-gm-name">Lamech</span> <span class="pc-gm-word">(the) despairing</span> ' +
            '<span class="pc-gm-name">Noah</span> <span class="pc-gm-word">rest.</span>' +
            '</div>' +
            '<div class="pc-gospel-note">Read the name meanings in sequence: the entire plan of redemption \u2014 ' +
            'from the Fall to the coming of Christ \u2014 is encoded in the genealogy of Genesis 5. ' +
            'This is not eisegesis; each meaning is derived from the Hebrew root given in Scripture itself.</div>' +
            '</div>';

        // ════════════════════════════════════════════════════════
        // PRE-FLOOD: Genesis 5 (Adam → Noah)
        // ════════════════════════════════════════════════════════
        html += '<div class="pc-section-header"><h4>\u05D1\u05B0\u05BC\u05E8\u05B5\u05D0\u05E9\u05C1\u05B4\u05D9\u05EA &nbsp; Genesis 5 \u2014 Adam to Noah (Pre-Flood)</h4></div>';

        // Year axis
        html += '<div class="pc-axis">';
        for (var y = 0; y <= 2200; y += 200) {
            html += '<span class="pc-axis-label">' + y + '</span>';
        }
        html += '</div>';

        // Chart area with flood line
        html += '<div style="position:relative">';

        // Flood line
        var floodFraction = (FLOOD_YEAR / maxYear).toFixed(4);
        html += '<div class="pc-flood-line" style="left:calc(140px + (100% - 140px) * ' + floodFraction + ')">' +
            '<div class="pc-flood-label">\uD83C\uDF0A Flood (1656 AM)</div></div>';

        // Babel line
        var babelFraction = (1757 / maxYear).toFixed(4);
        html += '<div class="pc-flood-line" style="left:calc(140px + (100% - 140px) * ' + babelFraction + ');background:rgba(180,80,60,0.5)">' +
            '<div class="pc-flood-label" style="color:#b4503c">\uD83D\uDDFC Babel (~1757 AM)</div></div>';

        // Pre-flood patriarch rows
        PATRIARCH_PREFLOOD.forEach(function(p) {
            var startPct = (p.born / maxYear * 100).toFixed(2);
            var widthPct = (p.age / maxYear * 100).toFixed(2);
            var deathYear = p.born + p.age;
            var labelText = p.age + ' yrs';
            var opacity = p.name === 'Enoch' ? '0.8' : '1';

            html += '<div class="pc-row">' +
                '<div class="pc-name">' + p.name +
                '<span class="pc-name-meaning">\u201C' + p.meaning + '\u201D</span>' +
                '<span class="pc-name-heb">' + p.heb + '</span></div>' +
                '<div class="pc-bar-track">' +
                '<div class="pc-bar" style="left:' + startPct + '%;width:' + widthPct + '%;background:' + p.color + ';opacity:' + opacity + '"' +
                ' data-patriarch="' + p.name + '"' +
                ' data-born="' + p.born + '"' +
                ' data-age="' + p.age + '"' +
                ' data-death="' + deathYear + '"' +
                ' data-heb="' + p.heb + '"' +
                ' data-meaning="' + p.meaning + '"' +
                ' data-root="' + (p.root || '').replace(/"/g, '&quot;') + '">' +
                '<span class="pc-bar-label">' + labelText + '</span>' +
                '</div></div></div>';
        });

        html += '</div>'; // end pre-flood chart area

        // ════════════════════════════════════════════════════════
        // POST-FLOOD: Genesis 11 (Shem → Abraham)
        // ════════════════════════════════════════════════════════
        html += '<div class="pc-section-header" style="margin-top:var(--space-lg)"><h4>\u05EA\u05D5\u05B9\u05DC\u05B0\u05D3\u05D5\u05B9\u05EA &nbsp; Genesis 11 \u2014 Shem to Abraham (Post-Flood)</h4></div>';

        // Post-flood year axis
        html += '<div class="pc-axis">';
        for (var y2 = 0; y2 <= 2200; y2 += 200) {
            html += '<span class="pc-axis-label">' + y2 + '</span>';
        }
        html += '</div>';

        // Post-flood chart area
        html += '<div style="position:relative">';

        // Flood + Babel lines (re-draw for context)
        html += '<div class="pc-flood-line" style="left:calc(140px + (100% - 140px) * ' + floodFraction + ')">' +
            '<div class="pc-flood-label">\uD83C\uDF0A Flood</div></div>';
        html += '<div class="pc-flood-line" style="left:calc(140px + (100% - 140px) * ' + babelFraction + ');background:rgba(180,80,60,0.5)">' +
            '<div class="pc-flood-label" style="color:#b4503c">\uD83D\uDDFC Babel</div></div>';

        // Post-flood patriarch rows
        PATRIARCH_POSTFLOOD.forEach(function(p) {
            var startPct = (p.born / maxYear * 100).toFixed(2);
            var widthPct = (p.age / maxYear * 100).toFixed(2);
            var deathYear = p.born + p.age;
            var labelText = p.age + ' yrs';

            html += '<div class="pc-row">' +
                '<div class="pc-name">' + p.name +
                '<span class="pc-name-meaning">\u201C' + p.meaning + '\u201D</span>' +
                '<span class="pc-name-heb">' + p.heb + '</span></div>' +
                '<div class="pc-bar-track">' +
                '<div class="pc-bar" style="left:' + startPct + '%;width:' + widthPct + '%;background:' + p.color + '"' +
                ' data-patriarch="' + p.name + '"' +
                ' data-born="' + p.born + '"' +
                ' data-age="' + p.age + '"' +
                ' data-death="' + deathYear + '"' +
                ' data-heb="' + p.heb + '"' +
                ' data-meaning="' + p.meaning + '"' +
                ' data-root="' + (p.root || '').replace(/"/g, '&quot;') + '">' +
                '<span class="pc-bar-label">' + labelText + '</span>' +
                '</div></div></div>';
        });

        html += '</div>'; // end post-flood chart area

        // ════════════════════════════════════════════════════════
        // KEY OBSERVATIONS
        // ════════════════════════════════════════════════════════
        html += '<div class="pc-stats">' +
            '<h4>Key Observations</h4>' +
            '<div class="pc-stats-grid">' +
            '<div class="pc-stat-item"><div class="pc-stat-label">Longest Life</div>Methuselah \u2014 969 years</div>' +
            '<div class="pc-stat-item"><div class="pc-stat-label">Shortest Life (pre-flood)</div>Enoch \u2014 365 years (taken by God)</div>' +
            '<div class="pc-stat-item"><div class="pc-stat-label">Methuselah\u2019s Death</div>Year 1656 AM \u2014 the exact year of the Flood</div>' +
            '<div class="pc-stat-item"><div class="pc-stat-label">Adam \u2192 Lamech Overlap</div>Adam died when Lamech was 56 \u2014 only 2 oral links from Eden to the Ark</div>' +
            '<div class="pc-stat-item"><div class="pc-stat-label">Shem Outlives Abraham</div>Shem died in 2158 AM \u2014 Abraham died in 2123 AM. Shem survived 35 years longer!</div>' +
            '<div class="pc-stat-item"><div class="pc-stat-label">Dramatic Lifespan Drop</div>Pre-flood average: ~858 yrs. Post-flood drops from 600 (Shem) to 175 (Abraham) \u2014 exponential decay</div>' +
            '<div class="pc-stat-item"><div class="pc-stat-label">Enoch\u2019s 365 Years</div>Matches days in a solar year \u2014 calendrical symbolism; walked with God</div>' +
            '<div class="pc-stat-item"><div class="pc-stat-label">Lamech\u2019s 777 Years</div>The number of divine perfection tripled \u2014 contrast with Lamech of Cain\u2019s line (Gen 4:24)</div>' +
            '<div class="pc-stat-item"><div class="pc-stat-label">Peleg \u2014 Division</div>Named for the division of the earth (Gen 10:25) \u2014 the Tower of Babel and Deut 32:8 allotment of nations</div>' +
            '<div class="pc-stat-item"><div class="pc-stat-label">Eber \u2192 Hebrew</div>The root of \u201CHebrew\u201D (\u02BEivr\u012B) \u2014 \u201Cone who crosses over.\u201D The identity of God\u2019s people as boundary-crossers</div>' +
            '<div class="pc-stat-item"><div class="pc-stat-label">Name Change: Abram \u2192 Abraham</div>God inserts the \u05D4 (heh) from His own name into Abram\u2019s \u2014 \u201Cexalted father\u201D becomes \u201Cfather of multitudes\u201D (Gen 17:5)</div>' +
            '<div class="pc-stat-item"><div class="pc-stat-label">Noah \u2192 Abraham Continuity</div>Noah was still alive when Abraham was born (Noah died 2006, Abraham born 1948). The covenant chain is unbroken.</div>' +
            '</div></div>';

        html += '</div>'; // end container

        content.innerHTML = html;

        // Tooltip
        var tooltip = document.createElement('div');
        tooltip.className = 'pc-tooltip';
        document.body.appendChild(tooltip);

        content.addEventListener('mouseover', function(e) {
            var bar = e.target.closest('.pc-bar');
            if (!bar) { tooltip.classList.remove('visible'); return; }
            var name = bar.dataset.patriarch;
            var born = parseInt(bar.dataset.born);
            var age = parseInt(bar.dataset.age);
            var death = parseInt(bar.dataset.death);
            var heb = bar.dataset.heb;

            // Find who was alive when this person was born
            var contemporaries = [];
            PATRIARCH_DATA.forEach(function(p) {
                if (p.name === name) return;
                if (p.born < death && (p.born + p.age) > born) {
                    contemporaries.push(p.name);
                }
            });

            var beforeFlood = death <= FLOOD_YEAR ? 'Died before the Flood' :
                (born < FLOOD_YEAR ? 'Survived the Flood' : 'Born after the Flood');
            if (name === 'Enoch') beforeFlood = 'Taken by God (Gen 5:24)';

            var meaning = bar.dataset.meaning || '';
            var root = bar.dataset.root || '';

            tooltip.innerHTML = '<div class="pc-tooltip-name">' + heb + ' ' + name + '</div>' +
                (meaning ? '<div class="pc-tooltip-meaning">\u201C' + meaning + '\u201D</div>' : '') +
                (root ? '<div class="pc-tooltip-root">' + root + '</div>' : '') +
                '<div class="pc-tooltip-detail">' +
                'Born: ' + born + ' AM<br>' +
                (name === 'Enoch' ? 'Taken: ' : 'Died: ') + death + ' AM<br>' +
                'Lifespan: ' + age + ' years<br>' +
                beforeFlood + '<br>' +
                (contemporaries.length > 0 ? 'Contemporaries: ' + contemporaries.join(', ') : '') +
                '</div>';
            tooltip.classList.add('visible');
        });

        content.addEventListener('mousemove', function(e) {
            if (tooltip.classList.contains('visible')) {
                tooltip.style.left = (e.clientX + 15) + 'px';
                tooltip.style.top = (e.clientY - 10) + 'px';
            }
        });

        content.addEventListener('mouseout', function(e) {
            if (!e.target.closest('.pc-bar')) tooltip.classList.remove('visible');
        });

        // Touch support
        content.addEventListener('click', function(e) {
            var bar = e.target.closest('.pc-bar');
            if (bar) {
                var event = new MouseEvent('mouseover', { clientX: e.clientX, clientY: e.clientY, bubbles: true });
                bar.dispatchEvent(event);
            }
        });

        // Cleanup tooltip on overlay close
        patriarchChartOverlay.addEventListener('click', function handler(e) {
            if (e.target === patriarchChartOverlay) {
                tooltip.classList.remove('visible');
            }
        });
    }

    // ── Biblical + World History Timeline ─────────────────────
    var timelineOverlay = document.getElementById('timelineOverlay');
    var timelineFilter = 'all';
    var timelineEraFilter = 'all';

    function openTimeline() {
        logEvent('feature', 'timeline');
        renderTimeline();
        timelineOverlay.classList.add('open');
    }
    function closeTimeline() { timelineOverlay.classList.remove('open'); }

    function renderTimeline() {
        var content = document.getElementById('timelineContent');
        var html = '';

        // Filter buttons
        html += '<div class="tl-filters">';
        html += '<div class="tl-filter-group">';
        html += '<button class="tl-filter-btn' + (timelineFilter === 'all' ? ' active' : '') + '" data-filter="all">All Events</button>';
        html += '<button class="tl-filter-btn' + (timelineFilter === 'bible' ? ' active' : '') + '" data-filter="bible">\u2727 Biblical</button>';
        html += '<button class="tl-filter-btn' + (timelineFilter === 'world' ? ' active' : '') + '" data-filter="world">\uD83C\uDF0D World History</button>';
        html += '</div>';
        html += '<div class="tl-era-group">';
        html += '<button class="tl-era-btn' + (timelineEraFilter === 'all' ? ' active' : '') + '" data-era="all">All Eras</button>';
        Object.keys(TIMELINE_ERAS).forEach(function(k) {
            var e = TIMELINE_ERAS[k];
            var active = timelineEraFilter === k ? ' active' : '';
            html += '<button class="tl-era-btn' + active + '" data-era="' + k + '" style="--era-color:' + e.color + '">' + e.label + '</button>';
        });
        html += '</div></div>';

        // Filter events
        var events = TIMELINE_DATA.filter(function(ev) {
            if (timelineFilter !== 'all' && ev.cat !== timelineFilter) return false;
            if (timelineEraFilter !== 'all' && ev.era !== timelineEraFilter) return false;
            return true;
        });

        // Sort by year
        events.sort(function(a, b) { return a.year - b.year; });

        // Stats
        var biblicalCount = events.filter(function(e) { return e.cat === 'bible'; }).length;
        var worldCount = events.filter(function(e) { return e.cat === 'world'; }).length;
        html += '<div class="tl-stats">';
        html += '<span class="tl-stat">\u2727 ' + biblicalCount + ' Biblical</span>';
        html += '<span class="tl-stat">\uD83C\uDF0D ' + worldCount + ' World History</span>';
        html += '<span class="tl-stat">Total: ' + events.length + ' events</span>';
        html += '</div>';

        // Timeline
        html += '<div class="tl-track">';
        var lastEra = '';
        events.forEach(function(ev, i) {
            var eraInfo = TIMELINE_ERAS[ev.era] || { color: '#666', label: '' };

            // Era separator
            if (ev.era !== lastEra) {
                html += '<div class="tl-era-divider" style="border-color:' + eraInfo.color + '">';
                html += '<span class="tl-era-label" style="background:' + eraInfo.color + '">' + eraInfo.label + '</span>';
                html += '</div>';
                lastEra = ev.era;
            }

            var isBible = ev.cat === 'bible';
            var side = i % 2 === 0 ? 'left' : 'right';
            var yearStr = ev.year < 0 ? Math.abs(ev.year) + ' BC' : ev.year + ' AD';
            if (ev.end && ev.end !== ev.year) {
                yearStr += ' \u2013 ' + (ev.end < 0 ? Math.abs(ev.end) + ' BC' : ev.end + ' AD');
            }

            html += '<div class="tl-event tl-' + side + (isBible ? ' tl-bible' : ' tl-world') + '" style="--event-color:' + eraInfo.color + '">';
            html += '<div class="tl-marker" style="background:' + eraInfo.color + '">' + (isBible ? '\u2727' : '\uD83C\uDF0D') + '</div>';
            html += '<div class="tl-card">';
            html += '<div class="tl-year">' + yearStr + '</div>';
            html += '<div class="tl-title">' + esc(ev.label) + '</div>';
            html += '<div class="tl-desc">' + esc(ev.desc) + '</div>';
            if (ev.ref) {
                html += '<div class="tl-ref">' + esc(ev.ref) + '</div>';
            }
            html += '</div></div>';
        });
        html += '</div>';

        content.innerHTML = html;

        // Filter listeners
        content.querySelectorAll('.tl-filter-btn').forEach(function(btn) {
            btn.addEventListener('click', function() {
                timelineFilter = this.dataset.filter;
                renderTimeline();
            });
        });
        content.querySelectorAll('.tl-era-btn').forEach(function(btn) {
            btn.addEventListener('click', function() {
                timelineEraFilter = this.dataset.era;
                renderTimeline();
            });
        });
    }

    // ── Developer Progress Page ──────────────────────────────
    var progressOverlay = document.getElementById('progressOverlay');

    function openProgress() {
        renderProgress();
        progressOverlay.classList.add('open');
    }

    function closeProgress() {
        progressOverlay.classList.remove('open');
    }

    function renderProgress() {
        var content = document.getElementById('progressContent');

        // Release mode: show reading progress + about for end users
        if (typeof IS_RELEASE !== 'undefined' && IS_RELEASE) {
            var ilWords = countInterlinearWords();

            // Calculate overall reading progress
            var totalRead = 0, totalChAll = 0;
            texts.forEach(function(t) {
                var rc = getTextReadCount(t.id);
                totalRead += rc.read;
                totalChAll += rc.total;
            });
            var pctRead = totalChAll > 0 ? Math.round((totalRead / totalChAll) * 100) : 0;

            var html = '<div class="progress-stats">' +
                '<div class="progress-stat"><div class="stat-value">' + totalRead + '/' + totalChAll + '</div><div class="stat-label">Chapters Read</div></div>' +
                '<div class="progress-stat"><div class="stat-value">' + pctRead + '%</div><div class="stat-label">Overall Progress</div></div>' +
                '<div class="progress-stat"><div class="stat-value">' + texts.length + '</div><div class="stat-label">Sacred Texts</div></div>' +
                '<div class="progress-stat"><div class="stat-value">' + Object.keys(GLOSSARY).length + '</div><div class="stat-label">Glossary Terms</div></div>' +
                '</div>';

            // Per-text reading progress bars
            html += '<div class="progress-section"><h3>Reading Progress</h3>';
            var hasProgress = false;
            texts.forEach(function(t) {
                var rc = getTextReadCount(t.id);
                if (rc.total === 0) return;
                var pct = Math.round((rc.read / rc.total) * 100);
                if (rc.read > 0) hasProgress = true;
                if (rc.read === 0) return; // Only show texts with some progress
                html += '<div class="progress-bar-row">' +
                    '<div class="progress-bar-label">' + t.name + ' <span class="progress-bar-count">' + rc.read + '/' + rc.total + '</span></div>' +
                    '<div class="progress-bar-track"><div class="progress-bar-fill' + (pct === 100 ? ' bar-complete' : '') + '" style="width:' + pct + '%"></div></div>' +
                    '</div>';
            });
            if (!hasProgress) {
                html += '<p style="color:var(--text-muted);font-size:0.85rem;font-style:italic">No chapters read yet. Open a text and check the box on any chapter to start tracking.</p>';
            }
            html += '</div>';

            // About section (condensed)
            html += '<div class="progress-section">' +
                '<h3>About</h3>' +
                '<p style="color:var(--text-secondary);line-height:1.7">' +
                '<strong style="color:var(--gold)">Texts:</strong> 39 OT + 27 NT + 8 Second Temple<br>' +
                '<strong style="color:var(--gold)">Interlinear:</strong> ' + ilWords + ' original language words<br>' +
                '<strong style="color:var(--gold)">Version:</strong> ' + (MANIFEST.version || '3.1') +
                '</p></div>';
            html += renderAnalyticsPanel();
            content.innerHTML = html;
            var exportBtn = document.getElementById('exportAnalyticsBtn');
            if (exportBtn) exportBtn.addEventListener('click', exportAnalytics);
            var clearBtn = document.getElementById('clearAnalyticsBtn');
            if (clearBtn) clearBtn.addEventListener('click', function() {
                if (confirm('Clear all usage data? This cannot be undone.')) {
                    analyticsLog = [];
                    localStorage.removeItem(ANALYTICS_KEY);
                    renderProgress();
                }
            });
            return;
        }

        // Calculate stats
        var totalChapters = 0, totalInserts = 0, totalDSS = 0;
        var textStats = {};

        texts.forEach(function(t) { textStats[t.id] = { chapters: 0, inserts: 0, dss: 0 }; });

        MANIFEST.eras.forEach(function(era) {
            var chapters = ERA_DATA[era.id] || [];
            chapters.forEach(function(ch) {
                var s = textStats[era.text] || { chapters: 0, inserts: 0, dss: 0 };
                if (ch.type === 'historical_insert') { s.inserts++; totalInserts++; }
                else { s.chapters++; totalChapters++; }
                (ch.cross_refs || []).forEach(function(xr) {
                    if (xr.type === 'dss') { s.dss++; totalDSS++; }
                });
                textStats[era.text] = s;
            });
        });

        var glossaryCount = Object.keys(GLOSSARY).length;
        var totalIL = 0;
        texts.forEach(function(t) {
            totalIL += Object.keys(getTextInterlinear(t.id)).length;
        });

        var html = '';

        // Overall stats
        var ilWordCount = countInterlinearWords();
        html += '<div class="progress-stats">' +
            '<div class="progress-stat"><div class="stat-value">' + totalChapters + '</div><div class="stat-label">Study Chapters</div></div>' +
            '<div class="progress-stat"><div class="stat-value">' + totalIL + '</div><div class="stat-label">Interlinear Chapters</div></div>' +
            '<div class="progress-stat"><div class="stat-value">' + ilWordCount + '</div><div class="stat-label">Interlinear Words</div></div>' +
            '<div class="progress-stat"><div class="stat-value">' + glossaryCount + '</div><div class="stat-label">Glossary Terms</div></div>' +
            '<div class="progress-stat"><div class="stat-value">' + texts.length + '</div><div class="stat-label">Texts in Library</div></div>' +
            '<div class="progress-stat"><div class="stat-value">' + MANIFEST.eras.length + '</div><div class="stat-label">Study Eras</div></div>' +
            '</div>';

        // Per-text progress — computed dynamically from actual data
        html += '<div class="progress-section"><h3>Text Completion</h3>';

        texts.forEach(function(t) {
            var s = textStats[t.id] || { chapters: 0, inserts: 0, dss: 0 };
            var studyCh = s.chapters;
            var ilData = getTextInterlinear(t.id);
            var ilChapters = Object.keys(ilData).length;
            var biblicalCh = t.chapters || 0;

            // Skip texts with zero content
            if (studyCh === 0 && ilChapters === 0) return;

            // Study content: show chapters found
            var studyLabel = studyCh + ' study chapters';
            var studyPct = studyCh > 0 ? 100 : 0;
            html += makeProgressBar(t.name + ' \u2014 Study Content', studyLabel, studyPct, 'bar-blue');

            // Interlinear: compare against biblical chapter count
            if (ilChapters > 0 || biblicalCh > 0) {
                var ilPct = biblicalCh > 0 ? Math.min(Math.round((ilChapters / biblicalCh) * 100), 100) : (ilChapters > 0 ? 100 : 0);
                var ilLabel = ilChapters + (biblicalCh > 0 ? '/' + biblicalCh : '') + ' chapters';
                if (ilPct === 100) ilLabel += ' \u2014 COMPLETE';
                html += makeProgressBar(t.name + ' \u2014 Interlinear', ilLabel, ilPct, 'bar-gold');
            }
        });

        html += '</div>';

        // Features
        html += '<div class="progress-section"><h3>Features</h3><ul class="feature-list">';

        var features = [
            {name: 'Multi-text library (74 texts: 39 OT + 27 NT + 8 Second Temple)', status: 'done'},
            {name: 'Category badges (Canon/DSS/Deuterocanon/Pseudepigrapha)', status: 'done'},
            {name: 'Library grid landing page', status: 'done'},
            {name: 'Hebrew interlinear — all 39 OT books (OSHB + Strong\'s)', status: 'done'},
            {name: 'Greek interlinear — all 27 NT books (MorphGNT + Strong\'s)', status: 'done'},
            {name: 'Word-by-word popup with morphology', status: 'done'},
            {name: 'Flow translations — all 66 biblical books (31,101 verses)', status: 'done'},
            {name: 'Multi-language glossary (553 terms)', status: 'done'},
            {name: 'Cross-reference drawer (5,932 refs, OT/NT/ANE/DSS)', status: 'done'},
            {name: 'Second Temple sources with non-canonical badges', status: 'done'},
            {name: 'Full-text search across all texts + flow verses', status: 'done'},
            {name: 'Ancient World Map with 60+ overlays & journey routes', status: 'done'},
            {name: 'Bookmarks with localStorage persistence', status: 'done'},
            {name: 'Reading progress tracker (per-chapter checkboxes)', status: 'done'},
            {name: 'Resizable 3-column layout with drag handles', status: 'done'},
            {name: 'Keyboard shortcuts (Alt+H/F/L, Ctrl+K)', status: 'done'},
            {name: 'Expand/fullscreen reading mode (Alt+F)', status: 'done'},
            {name: 'Font size controls for reading pane', status: 'done'},
            {name: 'Collapsible interlinear notes toggle', status: 'done'},
            {name: 'Copy to clipboard (verse/chapter/study content)', status: 'done'},
            {name: 'Dark theme with print stylesheet', status: 'done'},
            {name: 'Build profiles (--profile sons-of-god)', status: 'done'},
            {name: 'The Heavenly Court thematic study (23 chapters)', status: 'done'},
            {name: 'THC \u2194 Library cross-references', status: 'done'},
            {name: 'Glossary terms clickable in grammar boxes', status: 'done'},
            {name: 'Electron desktop app with Windows installer', status: 'done'},
            {name: 'Josephus excerpts (25 chapters)', status: 'done'},
            {name: 'DSS Sectarian texts study content', status: 'done'},
            {name: 'Genesis Apocryphon study content', status: 'done'},
            {name: '1 Enoch study content (expanding — 61/108 chapters)', status: 'wip'},
            {name: 'Jubilees study content (expanding — 34/50 chapters)', status: 'wip'},
            {name: 'Book of Jasher study content (expanding — 49/91 chapters)', status: 'wip'},
            {name: 'NT era depth (38 texts with thin eras)', status: 'wip'},
            {name: 'Bible Truth Matrix (30+ worldviews, 13 doctrines)', status: 'done'},
            {name: 'Biblical + World History Timeline (80+ events)', status: 'done'},
            {name: 'Study notes export (PDF/Markdown)', status: 'planned'},
            {name: 'Verse highlighting & annotations', status: 'planned'},
        ];

        features.forEach(function(f) {
            var check = f.status === 'done' ? '\u2713' : f.status === 'wip' ? '\u25CB' : '\u2012';
            html += '<li class="feature-item">' +
                '<span class="feature-check ' + f.status + '">' + check + '</span>' +
                '<span class="feature-name">' + f.name + '</span>' +
                '<span class="feature-status ' + f.status + '">' +
                (f.status === 'done' ? 'Complete' : f.status === 'wip' ? 'In Progress' : 'Planned') +
                '</span></li>';
        });

        html += '</ul></div>';

        // Build info
        html += '<div class="progress-section"><h3>Build Information</h3>' +
            '<div style="font-size:0.82rem;color:var(--text-secondary);line-height:1.8">' +
            'Build date: ' + (MANIFEST.build_date || 'unknown') + '<br>' +
            'Version: ' + (MANIFEST.version || '3.0') + '<br>' +
            'Total eras: ' + MANIFEST.eras.length + '<br>' +
            'Historical inserts: ' + totalInserts + '<br>' +
            'Interlinear words: ' + countInterlinearWords() +
            '</div></div>';

        // Usage analytics section
        html += renderAnalyticsPanel();

        content.innerHTML = html;

        // Wire up analytics buttons
        var exportBtn = document.getElementById('exportAnalyticsBtn');
        if (exportBtn) exportBtn.addEventListener('click', exportAnalytics);
        var clearBtn = document.getElementById('clearAnalyticsBtn');
        if (clearBtn) clearBtn.addEventListener('click', function() {
            if (confirm('Clear all usage data? This cannot be undone.')) {
                analyticsLog = [];
                localStorage.removeItem(ANALYTICS_KEY);
                renderProgress();
            }
        });
    }

    function makeProgressBar(name, detail, pct, barClass) {
        return '<div class="progress-bar-container">' +
            '<div class="progress-bar-label">' +
            '<span class="progress-name">' + name + ' <span style="font-weight:400;font-size:0.75rem;color:var(--text-muted)">(' + detail + ')</span></span>' +
            '<span class="progress-pct">' + pct + '%</span></div>' +
            '<div class="progress-bar"><div class="progress-bar-fill ' + barClass + '" style="width:' + pct + '%"></div></div></div>';
    }

    function countInterlinearWords() {
        var count = 0;
        texts.forEach(function(t) {
            var ilData = getTextInterlinear(t.id);
            Object.values(ilData).forEach(function(ch) {
                if (ch && ch.verses) ch.verses.forEach(function(v) { count += v.words.length; });
            });
        });
        return count.toLocaleString();
    }

    // ── HTML Escaping ─────────────────────────────────────────
    function esc(str) {
        var d = document.createElement('div');
        d.textContent = str;
        return d.innerHTML;
    }

    function escAttr(str) {
        if (!str) return '';
        return String(str).replace(/&/g, '&amp;').replace(/"/g, '&quot;')
                  .replace(/</g, '&lt;').replace(/>/g, '&gt;');
    }

    // Normalize a cross-ref entry — handles both string ("Job 1:6") and object ({ref, note, type}) formats
    function normXref(xr) {
        if (typeof xr === 'string') return { ref: xr, note: xr, type: 'ot' };
        return { ref: xr.ref || '', note: xr.note || xr.ref || '', type: xr.type || 'ot' };
    }

    // ══════════════════════════════════════════════════════════
    //  USAGE ANALYTICS — Anonymous usage logging for refinement
    //  Stores locally in localStorage. User can export as JSON.
    // ══════════════════════════════════════════════════════════

    var ANALYTICS_KEY = 'atl-usage-log';
    var ANALYTICS_SESSION_KEY = 'atl-session-id';
    var analyticsLog = JSON.parse(localStorage.getItem(ANALYTICS_KEY) || '[]');
    var analyticsSessionId = sessionStorage.getItem(ANALYTICS_SESSION_KEY);
    if (!analyticsSessionId) {
        analyticsSessionId = 'ses_' + Date.now().toString(36) + Math.random().toString(36).slice(2, 6);
        sessionStorage.setItem(ANALYTICS_SESSION_KEY, analyticsSessionId);
    }
    var analyticsSessionStart = Date.now();

    function logEvent(type, data) {
        var entry = {
            t: Date.now(),
            s: analyticsSessionId,
            type: type
        };
        if (data) entry.data = data;
        analyticsLog.push(entry);
        // Cap at 5000 events to avoid filling storage
        if (analyticsLog.length > 5000) analyticsLog = analyticsLog.slice(-4000);
        try { localStorage.setItem(ANALYTICS_KEY, JSON.stringify(analyticsLog)); } catch(e) {}
    }

    function getAnalyticsSummary() {
        var sessions = {};
        var textViews = {};
        var chapterViews = {};
        var searches = [];
        var features = {};
        var totalTime = 0;

        analyticsLog.forEach(function(e) {
            if (!sessions[e.s]) sessions[e.s] = { start: e.t, end: e.t, events: 0 };
            sessions[e.s].end = e.t;
            sessions[e.s].events++;

            if (e.type === 'text_view' && e.data) {
                textViews[e.data] = (textViews[e.data] || 0) + 1;
            }
            if (e.type === 'chapter_view' && e.data) {
                chapterViews[e.data] = (chapterViews[e.data] || 0) + 1;
            }
            if (e.type === 'search' && e.data) {
                searches.push(e.data);
            }
            if (e.type === 'feature') {
                features[e.data] = (features[e.data] || 0) + 1;
            }
        });

        Object.values(sessions).forEach(function(s) {
            totalTime += (s.end - s.start);
        });

        return {
            version: MANIFEST.version || '3.0',
            exportDate: new Date().toISOString(),
            totalSessions: Object.keys(sessions).length,
            totalEvents: analyticsLog.length,
            totalMinutes: Math.round(totalTime / 60000),
            topTexts: Object.entries(textViews).sort(function(a,b) { return b[1]-a[1]; }).slice(0,20),
            topChapters: Object.entries(chapterViews).sort(function(a,b) { return b[1]-a[1]; }).slice(0,30),
            recentSearches: searches.slice(-50),
            featureUsage: features,
            rawLog: analyticsLog
        };
    }

    function exportAnalytics() {
        var summary = getAnalyticsSummary();
        var json = JSON.stringify(summary, null, 2);
        var blob = new Blob([json], { type: 'application/json' });
        var url = URL.createObjectURL(blob);
        var a = document.createElement('a');
        a.href = url;
        a.download = 'ancient-texts-usage-' + new Date().toISOString().slice(0,10) + '.json';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    }

    function renderAnalyticsPanel() {
        var s = getAnalyticsSummary();
        var html = '<div class="analytics-panel">';
        html += '<h3>Your Usage Summary</h3>';
        html += '<div class="analytics-stats">';
        html += '<div class="progress-stat"><div class="stat-value">' + s.totalSessions + '</div><div class="stat-label">Sessions</div></div>';
        html += '<div class="progress-stat"><div class="stat-value">' + s.totalEvents + '</div><div class="stat-label">Events Logged</div></div>';
        html += '<div class="progress-stat"><div class="stat-value">' + s.totalMinutes + '</div><div class="stat-label">Minutes Spent</div></div>';
        html += '</div>';
        if (s.topTexts.length > 0) {
            html += '<h4>Most Viewed Texts</h4><div class="analytics-list">';
            s.topTexts.slice(0,10).forEach(function(t) {
                var textDef = getTextDef(t[0]);
                var name = textDef ? textDef.name : t[0];
                html += '<div class="analytics-row"><span>' + esc(name) + '</span><span class="analytics-count">' + t[1] + '</span></div>';
            });
            html += '</div>';
        }
        if (Object.keys(s.featureUsage).length > 0) {
            html += '<h4>Features Used</h4><div class="analytics-list">';
            Object.entries(s.featureUsage).sort(function(a,b) { return b[1]-a[1]; }).forEach(function(f) {
                html += '<div class="analytics-row"><span>' + esc(f[0]) + '</span><span class="analytics-count">' + f[1] + '</span></div>';
            });
            html += '</div>';
        }
        html += '<div style="margin-top:16px;display:flex;gap:8px;flex-wrap:wrap">';
        html += '<button class="matrix-cat-btn" id="exportAnalyticsBtn">Export Usage Data (JSON)</button>';
        html += '<button class="matrix-cat-btn" id="clearAnalyticsBtn" style="color:#ef4444;border-color:#ef4444">Clear All Data</button>';
        html += '</div>';
        html += '<p style="font-size:0.7rem;color:var(--text-muted);margin-top:8px">Usage data is stored locally on your device. Export and send the JSON file to help improve the app.</p>';
        html += '</div>';
        return html;
    }

    // Log session start
    logEvent('session_start');

    // ══════════════════════════════════════════════════════════
    //  HALLELUJAH AI — Bible-Bound Chat Module
    //  Local AI chat powered by Ollama with transparent,
    //  Scripture-derived guidelines. No hidden rules.
    // ══════════════════════════════════════════════════════════

    var HAI_API = 'http://127.0.0.1:8741';
    var haiChatHistory = JSON.parse(localStorage.getItem('hai-chat-history') || '[]');
    var haiConnected = false;
    var haiCurrentModel = localStorage.getItem('hai-model') || '';
    var haiModels = [];
    var haiStreaming = false;
    var haiBibleBound = localStorage.getItem('hai-bible-bound') !== 'false';
    var haiShowAudit = localStorage.getItem('hai-show-audit') === 'true';

    function saveHaiState() {
        try {
            // Keep last 50 messages max to avoid filling localStorage
            var toSave = haiChatHistory.slice(-50);
            localStorage.setItem('hai-chat-history', JSON.stringify(toSave));
        } catch (e) { /* storage full — silently fail */ }
    }
    var haiPolicyCache = null;
    var haiPolicyEditorOpen = false;

    function initHallelujahChat() {
        createChatDOM();
        bindChatEvents();
        restoreChatHistory();
        checkHaiConnection();
        // Re-check connection every 30s
        setInterval(checkHaiConnection, 30000);
    }

    function restoreChatHistory() {
        if (haiChatHistory.length === 0) return;
        var messages = document.getElementById('haiMessages');
        // Remove welcome message
        var welcome = messages.querySelector('.hai-welcome');
        if (welcome) welcome.remove();

        // Render saved messages
        haiChatHistory.forEach(function(msg) {
            addHaiMessage(msg.role, msg.content);
        });

        // Restore toggle states
        document.getElementById('haiBibleBoundToggle').checked = haiBibleBound;
        document.getElementById('haiAuditToggle').checked = haiShowAudit;
    }

    function createChatDOM() {
        // Chat toggle button (fixed position)
        var toggleBtn = document.createElement('button');
        toggleBtn.id = 'haiToggle';
        toggleBtn.className = 'hai-toggle';
        toggleBtn.title = 'Hallelujah AI (Alt+A)';
        toggleBtn.innerHTML = '<span class="hai-toggle-icon">&#x2726;</span>' +
            '<span class="hai-toggle-label">Hallelujah AI</span>' +
            '<span class="hai-status-dot" id="haiStatusDot"></span>';
        document.body.appendChild(toggleBtn);

        // Chat panel
        var panel = document.createElement('div');
        panel.id = 'haiPanel';
        panel.className = 'hai-panel';
        panel.innerHTML =
            '<div class="hai-header">' +
                '<div class="hai-header-left">' +
                    '<h3 class="hai-title">Hallelujah AI</h3>' +
                    '<span class="hai-connection" id="haiConnectionBadge">Checking...</span>' +
                '</div>' +
                '<div class="hai-header-right">' +
                    '<button class="hai-header-btn" id="haiFullChatBtn" title="Open full-screen chat">Full Chat</button>' +
                    '<button class="hai-header-btn" id="haiPolicyBtn" title="View/Edit Policies">Policy</button>' +
                    '<button class="hai-header-btn" id="haiClearBtn" title="Clear chat">Clear</button>' +
                    '<button class="hai-close" id="haiClose">&times;</button>' +
                '</div>' +
            '</div>' +
            '<div class="hai-toolbar">' +
                '<select class="hai-model-select" id="haiModelSelect" title="Select model">' +
                    '<option value="">No models</option>' +
                '</select>' +
                '<label class="hai-toggle-switch" title="Bible-Bound Mode">' +
                    '<input type="checkbox" id="haiBibleBoundToggle" checked>' +
                    '<span class="hai-switch-label">Bible-Bound</span>' +
                '</label>' +
                '<label class="hai-toggle-switch" title="Show audit trail">' +
                    '<input type="checkbox" id="haiAuditToggle">' +
                    '<span class="hai-switch-label">Audit</span>' +
                '</label>' +
            '</div>' +
            '<div class="hai-messages" id="haiMessages">' +
                '<div class="hai-welcome">' +
                    '<div class="hai-welcome-icon">&#x2726;</div>' +
                    '<h4>Hallelujah AI</h4>' +
                    '<p>Bible-bound study assistant powered by local AI.</p>' +
                    '<p class="hai-welcome-sub">Every guideline is transparent and editable.<br>' +
                    'Scripture interprets Scripture. No hidden rules.</p>' +
                '</div>' +
            '</div>' +
            '<div class="hai-policy-editor" id="haiPolicyEditor">' +
                '<div class="hai-policy-header">' +
                    '<h4>Policy Files</h4>' +
                    '<button class="hai-policy-close" id="haiPolicyClose">&times;</button>' +
                '</div>' +
                '<div class="hai-policy-tabs" id="haiPolicyTabs"></div>' +
                '<textarea class="hai-policy-textarea" id="haiPolicyTextarea" spellcheck="false"></textarea>' +
                '<div class="hai-policy-actions">' +
                    '<button class="hai-policy-save" id="haiPolicySave">Save Changes</button>' +
                '</div>' +
            '</div>' +
            '<div class="hai-input-area">' +
                '<button class="hai-context-btn" id="haiContextBtn" title="Ask about current chapter">' +
                    'Ask about this chapter' +
                '</button>' +
                '<div class="hai-input-row">' +
                    '<textarea class="hai-input" id="haiInput" placeholder="Ask anything... (Scripture is the authority)" rows="1"></textarea>' +
                    '<button class="hai-send" id="haiSend" title="Send (Enter)">&#x27A4;</button>' +
                '</div>' +
            '</div>';
        document.body.appendChild(panel);
    }

    function bindChatEvents() {
        // Toggle panel
        var toggle = document.getElementById('haiToggle');
        var panel = document.getElementById('haiPanel');
        var closeBtn = document.getElementById('haiClose');

        toggle.addEventListener('click', function() {
            panel.classList.toggle('open');
            if (panel.classList.contains('open')) {
                document.getElementById('haiInput').focus();
            }
        });
        closeBtn.addEventListener('click', function() {
            panel.classList.remove('open');
        });

        // Keyboard shortcut Alt+A
        document.addEventListener('keydown', function(e) {
            if (e.altKey && e.key === 'a') {
                e.preventDefault();
                panel.classList.toggle('open');
                if (panel.classList.contains('open')) {
                    document.getElementById('haiInput').focus();
                }
            }
        });

        // Send message
        var sendBtn = document.getElementById('haiSend');
        var input = document.getElementById('haiInput');

        sendBtn.addEventListener('click', function() { haiSendMessage(); });
        input.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                haiSendMessage();
            }
        });

        // Auto-resize textarea
        input.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = Math.min(this.scrollHeight, 120) + 'px';
        });

        // Full Chat — navigate to full-screen chat
        document.getElementById('haiFullChatBtn').addEventListener('click', function() {
            if (window.pywebview && window.pywebview.api) {
                window.pywebview.api.navigate('chat');
            } else {
                window.location.href = 'http://127.0.0.1:8741/chat';
            }
        });

        // Clear chat
        document.getElementById('haiClearBtn').addEventListener('click', function() {
            haiChatHistory = [];
            saveHaiState();
            var messages = document.getElementById('haiMessages');
            messages.innerHTML =
                '<div class="hai-welcome">' +
                    '<div class="hai-welcome-icon">&#x2726;</div>' +
                    '<h4>Chat cleared</h4>' +
                    '<p>Ready for a new conversation.</p>' +
                '</div>';
        });

        // Bible-Bound toggle
        document.getElementById('haiBibleBoundToggle').addEventListener('change', function() {
            haiBibleBound = this.checked;
            localStorage.setItem('hai-bible-bound', this.checked);
        });

        // Audit toggle
        document.getElementById('haiAuditToggle').addEventListener('change', function() {
            haiShowAudit = this.checked;
            localStorage.setItem('hai-show-audit', this.checked);
            // Show/hide existing audit sections
            var audits = document.querySelectorAll('.hai-audit');
            audits.forEach(function(a) {
                a.style.display = haiShowAudit ? 'block' : 'none';
            });
        });

        // Context button — inject current study context
        document.getElementById('haiContextBtn').addEventListener('click', function() {
            var ctx = gatherStudyContext();
            if (ctx) {
                var input = document.getElementById('haiInput');
                input.value = 'Tell me about this chapter — what are the key insights, original language highlights, and canonical connections?';
                input.focus();
            }
        });

        // Model selector
        document.getElementById('haiModelSelect').addEventListener('change', function() {
            haiCurrentModel = this.value;
            localStorage.setItem('hai-model', this.value);
        });

        // Policy editor
        document.getElementById('haiPolicyBtn').addEventListener('click', function() {
            togglePolicyEditor(true);
        });
        document.getElementById('haiPolicyClose').addEventListener('click', function() {
            togglePolicyEditor(false);
        });
        document.getElementById('haiPolicySave').addEventListener('click', savePolicyEdit);
    }

    function checkHaiConnection() {
        var dot = document.getElementById('haiStatusDot');
        var badge = document.getElementById('haiConnectionBadge');
        var select = document.getElementById('haiModelSelect');

        fetch(HAI_API + '/health')
            .then(function(r) { return r.json(); })
            .then(function(data) {
                var ollamaOk = data.ollama && data.ollama.status === 'connected';
                haiConnected = ollamaOk;

                if (ollamaOk) {
                    dot.className = 'hai-status-dot connected';
                    haiModels = data.ollama.models || [];
                    haiCurrentModel = haiModels[0] || '';
                    badge.textContent = 'Connected: ' + haiCurrentModel;
                    badge.className = 'hai-connection connected';

                    // Populate model selector
                    select.innerHTML = '';
                    haiModels.forEach(function(m) {
                        var opt = document.createElement('option');
                        opt.value = m;
                        opt.textContent = m;
                        select.appendChild(opt);
                    });
                } else {
                    dot.className = 'hai-status-dot offline';
                    badge.textContent = 'Ollama offline';
                    badge.className = 'hai-connection offline';
                }
            })
            .catch(function() {
                haiConnected = false;
                dot.className = 'hai-status-dot offline';
                badge.textContent = 'Server offline';
                badge.className = 'hai-connection offline';
            });
    }

    function gatherStudyContext() {
        if (!currentText || !currentEra) return null;

        var textDef = MANIFEST.texts.find(function(t) { return t.id === currentText; });
        var eraDef = MANIFEST.eras.find(function(e) { return e.id === currentEra; });
        var chapters = ERA_DATA[currentEra] || [];

        var ctx = {
            text_name: textDef ? textDef.name : currentText,
            era_name: eraDef ? eraDef.name : currentEra,
            chapter_title: '',
            chapter_ref: '',
            key_verse: '',
            chapter_content: '',
            hebrew_terms: [],
            cross_refs: []
        };

        // Get first chapter data as primary context
        if (chapters.length > 0) {
            var ch = chapters[0];
            ctx.chapter_title = ch.title || '';
            ctx.chapter_ref = ch.ref || '';
            ctx.hebrew_terms = ch.hebrew_terms || [];
            ctx.cross_refs = (ch.cross_refs || []).map(function(x) {
                return { ref: x.ref || '', note: x.note || '' };
            });

            if (ch.key_verse) {
                ctx.key_verse = (ch.key_verse.ref || '') + ' — ' + (ch.key_verse.text || '');
            }

            // Build content from sections
            var parts = [];
            (ch.sections || []).forEach(function(s) {
                if (s.heading) parts.push('### ' + s.heading);
                if (s.body) {
                    // Strip HTML
                    var tmp = document.createElement('div');
                    tmp.innerHTML = s.body;
                    parts.push(tmp.textContent);
                }
            });
            ctx.chapter_content = parts.join('\n\n').substring(0, 8000);
        }

        return ctx;
    }

    function haiSendMessage() {
        var input = document.getElementById('haiInput');
        var text = input.value.trim();
        if (!text || haiStreaming) return;

        if (!haiConnected) {
            addHaiMessage('system', 'Hallelujah AI is not connected. Make sure Ollama is running (ollama serve) and the backend server is started.');
            return;
        }

        // Add user message to UI
        addHaiMessage('user', text);
        input.value = '';
        input.style.height = 'auto';

        // Add to history
        haiChatHistory.push({ role: 'user', content: text });
        saveHaiState();

        // Build request
        var studyCtx = gatherStudyContext();
        var reqBody = {
            message: text,
            history: haiChatHistory.slice(0, -1), // Everything except the current message
            model: haiCurrentModel,
            temperature: 0.7,
            bible_bound: haiBibleBound,
            study_context: studyCtx
        };

        // Stream the response
        haiStreaming = true;
        var msgEl = addHaiMessage('assistant', '');
        var contentEl = msgEl.querySelector('.hai-msg-content');

        fetch(HAI_API + '/chat/stream', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(reqBody)
        })
        .then(function(response) {
            var reader = response.body.getReader();
            var decoder = new TextDecoder();
            var fullText = '';
            var buffer = '';

            function readChunk() {
                reader.read().then(function(result) {
                    if (result.done) {
                        haiStreaming = false;
                        haiChatHistory.push({ role: 'assistant', content: fullText });
                        saveHaiState();
                        return;
                    }

                    buffer += decoder.decode(result.value, { stream: true });
                    var lines = buffer.split('\n');
                    buffer = lines.pop(); // Keep incomplete line in buffer

                    lines.forEach(function(line) {
                        if (line.startsWith('data: ')) {
                            try {
                                var data = JSON.parse(line.substring(6));
                                if (data.token) {
                                    fullText += data.token;
                                    contentEl.innerHTML = renderMarkdown(fullText);
                                    scrollChatToBottom();
                                }
                                if (data.done) {
                                    haiStreaming = false;
                                    haiChatHistory.push({ role: 'assistant', content: fullText });
                                    saveHaiState();
                                    contentEl.innerHTML = renderMarkdown(fullText);
                                    if (data.audit) {
                                        renderAudit(msgEl, data.audit);
                                    }
                                }
                                if (data.error) {
                                    contentEl.innerHTML = '<span class="hai-error">Error: ' + esc(data.error) + '</span>';
                                    haiStreaming = false;
                                }
                            } catch (e) { /* skip malformed */ }
                        }
                    });

                    readChunk();
                }).catch(function(err) {
                    contentEl.innerHTML += '<span class="hai-error"><br>Stream error: ' + esc(err.message) + '</span>';
                    haiStreaming = false;
                });
            }

            readChunk();
        })
        .catch(function(err) {
            contentEl.innerHTML = '<span class="hai-error">Connection error: ' + esc(err.message) + '</span>';
            haiStreaming = false;
        });
    }

    function addHaiMessage(role, content) {
        var messages = document.getElementById('haiMessages');
        // Remove welcome message if present
        var welcome = messages.querySelector('.hai-welcome');
        if (welcome) welcome.remove();

        var msg = document.createElement('div');
        msg.className = 'hai-msg hai-msg-' + role;

        var label = role === 'user' ? 'You' : role === 'assistant' ? 'Hallelujah AI' : 'System';
        var icon = role === 'user' ? '&#x1F464;' : role === 'assistant' ? '&#x2726;' : '&#x26A0;';

        msg.innerHTML =
            '<div class="hai-msg-header">' +
                '<span class="hai-msg-icon">' + icon + '</span>' +
                '<span class="hai-msg-label">' + label + '</span>' +
            '</div>' +
            '<div class="hai-msg-content">' + (content ? renderMarkdown(content) : '<span class="hai-typing">Thinking...</span>') + '</div>';

        messages.appendChild(msg);
        scrollChatToBottom();
        return msg;
    }

    function renderAudit(msgEl, audit) {
        if (!audit) return;
        var auditEl = document.createElement('div');
        auditEl.className = 'hai-audit';
        auditEl.style.display = haiShowAudit ? 'block' : 'none';

        var labels = audit.labels || {};
        var flags = audit.flags || [];
        var sections = audit.sections_found || [];
        var score = audit.score || 0;

        var html = '<div class="hai-audit-header" onclick="this.parentElement.classList.toggle(\'expanded\')">' +
            '<span>Audit Trail</span>' +
            '<span class="hai-audit-score">Score: ' + score + '/100</span>' +
            '</div>' +
            '<div class="hai-audit-body">' +
            '<div class="hai-audit-labels">' +
                '<span class="hai-label-a">[A] ' + (labels.A || 0) + '</span>' +
                '<span class="hai-label-b">[B] ' + (labels.B || 0) + '</span>' +
                '<span class="hai-label-c">[C] ' + (labels.C || 0) + '</span>' +
                '<span class="hai-label-u">[U] ' + (labels.U || 0) + '</span>' +
            '</div>' +
            '<div class="hai-audit-verses">Verse citations: ' + (audit.verse_citations || 0) + '</div>' +
            '<div class="hai-audit-sections">Sections: ' + sections.join(', ') + '</div>';

        if (flags.length > 0) {
            html += '<div class="hai-audit-flags">';
            flags.forEach(function(f) {
                html += '<div class="hai-audit-flag">&#x26A0; ' + esc(f) + '</div>';
            });
            html += '</div>';
        }

        html += '</div>';
        auditEl.innerHTML = html;
        msgEl.appendChild(auditEl);
    }

    function renderMarkdown(text) {
        if (!text) return '';
        // Simple markdown rendering
        var html = esc(text);

        // Headers
        html = html.replace(/^### (.+)$/gm, '<h5 class="hai-h3">$1</h5>');
        html = html.replace(/^## (.+)$/gm, '<h4 class="hai-h2">$1</h4>');

        // Bold and italic
        html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
        html = html.replace(/\*(.+?)\*/g, '<em>$1</em>');

        // Claim labels — colorize
        html = html.replace(/\[A\]/g, '<span class="hai-label-a">[A]</span>');
        html = html.replace(/\[B\]/g, '<span class="hai-label-b">[B]</span>');
        html = html.replace(/\[C\]/g, '<span class="hai-label-c">[C]</span>');
        html = html.replace(/\[U\]/g, '<span class="hai-label-u">[U]</span>');

        // Bullet lists
        html = html.replace(/^- (.+)$/gm, '<li>$1</li>');
        html = html.replace(/(<li>.*<\/li>)/s, '<ul>$1</ul>');

        // Code blocks
        html = html.replace(/```(\w*)\n([\s\S]*?)```/g, '<pre class="hai-code"><code>$2</code></pre>');
        html = html.replace(/`([^`]+)`/g, '<code class="hai-inline-code">$1</code>');

        // Line breaks
        html = html.replace(/\n\n/g, '</p><p>');
        html = html.replace(/\n/g, '<br>');

        return '<p>' + html + '</p>';
    }

    function scrollChatToBottom() {
        var messages = document.getElementById('haiMessages');
        messages.scrollTop = messages.scrollHeight;
    }

    // Policy Editor
    var activePolicyFile = null;

    function togglePolicyEditor(show) {
        var editor = document.getElementById('haiPolicyEditor');
        var messages = document.getElementById('haiMessages');
        haiPolicyEditorOpen = show;

        if (show) {
            editor.style.display = 'flex';
            messages.style.display = 'none';
            loadPolicies();
        } else {
            editor.style.display = 'none';
            messages.style.display = 'flex';
        }
    }

    function loadPolicies() {
        fetch(HAI_API + '/policy')
            .then(function(r) { return r.json(); })
            .then(function(data) {
                haiPolicyCache = data.policies || {};
                var tabs = document.getElementById('haiPolicyTabs');
                tabs.innerHTML = '';
                var files = Object.keys(haiPolicyCache);
                files.forEach(function(fname, i) {
                    var tab = document.createElement('button');
                    tab.className = 'hai-policy-tab' + (i === 0 ? ' active' : '');
                    tab.textContent = fname.replace('.yaml', '');
                    tab.addEventListener('click', function() {
                        document.querySelectorAll('.hai-policy-tab').forEach(function(t) { t.classList.remove('active'); });
                        tab.classList.add('active');
                        activePolicyFile = fname;
                        document.getElementById('haiPolicyTextarea').value = haiPolicyCache[fname] || '';
                    });
                    tabs.appendChild(tab);
                });
                // Load first file
                if (files.length > 0) {
                    activePolicyFile = files[0];
                    document.getElementById('haiPolicyTextarea').value = haiPolicyCache[files[0]] || '';
                }
            })
            .catch(function() {
                document.getElementById('haiPolicyTextarea').value = '# Could not load policies.\n# Make sure the Hallelujah AI server is running.';
            });
    }

    function savePolicyEdit() {
        if (!activePolicyFile) return;
        var content = document.getElementById('haiPolicyTextarea').value;

        fetch(HAI_API + '/policy', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ filename: activePolicyFile, content: content })
        })
        .then(function(r) { return r.json(); })
        .then(function(data) {
            if (data.status === 'saved') {
                haiPolicyCache[activePolicyFile] = content;
                var btn = document.getElementById('haiPolicySave');
                btn.textContent = 'Saved!';
                setTimeout(function() { btn.textContent = 'Save Changes'; }, 2000);
            }
        })
        .catch(function(err) {
            alert('Error saving policy: ' + err.message);
        });
    }

    // ── Firebase Auth & Cloud Sync ─────────────────────────
    var authCurrentUser = null;
    var firestoreDb = null;
    var authReady = false;
    var SYNC_KEYS = ['genesis-study-bookmarks', 'atl-read-chapters', 'atl-user-mode', 'atl-il-rows', 'atl-reading-mode', 'atl-study-notes'];

    function initFirebaseAuth() {
        if (typeof firebase === 'undefined' || !firebase.apps) return;
        if (!firebase.apps.length) {
            firebase.initializeApp(window.__FIREBASE_CONFIG || {});
        }
        firestoreDb = firebase.firestore();

        firebase.auth().onAuthStateChanged(function(user) {
            authCurrentUser = user;
            authReady = true;
            updateAuthUI();
            if (user) {
                hideAuthOverlay();
                pullFromCloud();
            }
        });
    }

    function showAuthOverlay() {
        var ov = document.getElementById('authOverlay');
        if (ov) { ov.classList.remove('auth-hidden'); ov.style.display = 'flex'; }
    }

    function hideAuthOverlay() {
        var ov = document.getElementById('authOverlay');
        if (ov) { ov.classList.add('auth-hidden'); setTimeout(function() { ov.style.display = 'none'; }, 400); }
    }

    function updateAuthUI() {
        var badge = document.getElementById('authUserBadge');
        if (!badge) return;
        if (authCurrentUser) {
            var email = authCurrentUser.email || 'User';
            var initial = email.charAt(0).toUpperCase();
            badge.innerHTML = '<span class="auth-user-icon">' + initial + '</span>' +
                '<span class="auth-user-email">' + email + '</span>' +
                '<span class="auth-sync-dot"></span>' +
                '<span class="auth-signout" id="authSignOut">Sign out</span>';
            badge.style.display = 'flex';
            var so = document.getElementById('authSignOut');
            if (so) so.addEventListener('click', function() {
                firebase.auth().signOut();
                authCurrentUser = null;
                updateAuthUI();
            });
        } else {
            badge.innerHTML = '<span class="auth-signout" id="authSignIn" style="color:var(--color-gold);cursor:pointer;font-size:0.8rem;">Sign in to sync progress</span>';
            badge.style.display = 'flex';
            var si = document.getElementById('authSignIn');
            if (si) si.addEventListener('click', showAuthOverlay);
        }
    }

    function handleAuthSubmit(isSignUp) {
        var email = document.getElementById('authEmail').value.trim();
        var pass = document.getElementById('authPass').value;
        var errEl = document.getElementById('authError');
        if (!email || !pass) { errEl.textContent = 'Email and password required.'; return; }
        if (pass.length < 6) { errEl.textContent = 'Password must be at least 6 characters.'; return; }
        errEl.textContent = '';
        var btn = document.getElementById('authSubmitBtn');
        btn.disabled = true;
        btn.textContent = isSignUp ? 'Creating account...' : 'Signing in...';

        var authPromise = isSignUp
            ? firebase.auth().createUserWithEmailAndPassword(email, pass)
            : firebase.auth().signInWithEmailAndPassword(email, pass);

        authPromise.then(function() {
            btn.disabled = false;
            btn.textContent = isSignUp ? 'Create Account' : 'Sign In';
            hideAuthOverlay();
            pushToCloud();
        }).catch(function(err) {
            btn.disabled = false;
            btn.textContent = isSignUp ? 'Create Account' : 'Sign In';
            var msg = err.message || 'Authentication failed.';
            if (err.code === 'auth/email-already-in-use') msg = 'An account with this email already exists.';
            if (err.code === 'auth/user-not-found') msg = 'No account found with this email.';
            if (err.code === 'auth/wrong-password') msg = 'Incorrect password.';
            if (err.code === 'auth/invalid-email') msg = 'Invalid email address.';
            if (err.code === 'auth/invalid-credential') msg = 'Invalid email or password.';
            errEl.textContent = msg;
        });
    }

    function bindAuthEvents() {
        var overlay = document.getElementById('authOverlay');
        if (!overlay) return;

        var submitBtn = document.getElementById('authSubmitBtn');
        var guestBtn = document.getElementById('authGuestBtn');
        var toggleLink = document.getElementById('authToggleLink');
        var isSignUp = false;

        if (submitBtn) submitBtn.addEventListener('click', function() {
            handleAuthSubmit(isSignUp);
        });

        if (guestBtn) guestBtn.addEventListener('click', function() {
            hideAuthOverlay();
        });

        if (toggleLink) toggleLink.addEventListener('click', function(e) {
            e.preventDefault();
            isSignUp = !isSignUp;
            submitBtn.textContent = isSignUp ? 'Create Account' : 'Sign In';
            document.getElementById('authToggleText').textContent =
                isSignUp ? 'Already have an account? ' : "Don't have an account? ";
            toggleLink.textContent = isSignUp ? 'Sign in' : 'Sign up';
            document.getElementById('authError').textContent = '';
        });

        // Enter key submits
        var passInput = document.getElementById('authPass');
        if (passInput) passInput.addEventListener('keydown', function(e) {
            if (e.key === 'Enter') handleAuthSubmit(isSignUp);
        });
    }

    // ── Cloud Sync (Firestore) ──────────────────────────────
    function pushToCloud() {
        if (!authCurrentUser || !firestoreDb) return;
        var data = {};
        SYNC_KEYS.forEach(function(key) {
            var val = localStorage.getItem(key);
            if (val !== null) data[key] = val;
        });
        data.updatedAt = firebase.firestore.FieldValue.serverTimestamp();
        setSyncDot(true);
        firestoreDb.collection('users').doc(authCurrentUser.uid).set(data, { merge: true })
            .then(function() { setSyncDot(false); })
            .catch(function() { setSyncDot(false); });
    }

    function pullFromCloud() {
        if (!authCurrentUser || !firestoreDb) return;
        setSyncDot(true);
        firestoreDb.collection('users').doc(authCurrentUser.uid).get()
            .then(function(doc) {
                setSyncDot(false);
                if (!doc.exists) { pushToCloud(); return; }
                var data = doc.data();
                SYNC_KEYS.forEach(function(key) {
                    if (data[key] !== undefined && data[key] !== null) {
                        localStorage.setItem(key, data[key]);
                    }
                });
                // Refresh in-memory state from updated localStorage
                bookmarks = JSON.parse(localStorage.getItem('genesis-study-bookmarks') || '[]');
                readChapters = JSON.parse(localStorage.getItem('atl-read-chapters') || '{}');
                userMode = localStorage.getItem('atl-user-mode') || 'scholar';
                ilRows = JSON.parse(localStorage.getItem('atl-il-rows') || 'null') || USER_MODES[userMode];
                renderBookmarks();
                if (typeof updateProgressDisplay === 'function') updateProgressDisplay();
            })
            .catch(function() { setSyncDot(false); });
    }

    function syncAfterChange() {
        if (authCurrentUser && firestoreDb) {
            clearTimeout(window._syncDebounce);
            window._syncDebounce = setTimeout(pushToCloud, 2000);
        }
    }

    function setSyncDot(syncing) {
        var dots = document.querySelectorAll('.auth-sync-dot');
        dots.forEach(function(d) { d.classList.toggle('syncing', syncing); });
    }

    // ── Launch ──────────────────────────────────────────────
    // Note: On large inline scripts, DOMContentLoaded may fire before the
    // script finishes parsing, so we check readyState as a fallback.
    function startApp() {
        init();
        bindAuthEvents();
        initFirebaseAuth();

        // Show auth overlay only on first visit (no user seen before)
        var hasSeenAuth = localStorage.getItem('atl-auth-seen');
        if (!hasSeenAuth && typeof firebase !== 'undefined') {
            // Brief delay to let Firebase check for existing session
            setTimeout(function() {
                if (!authCurrentUser) showAuthOverlay();
                localStorage.setItem('atl-auth-seen', '1');
            }, 800);
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', startApp);
    } else {
        startApp();
    }

})();
