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

    // ── User Mode & Row Visibility State ──────────────────
    var USER_MODES = {
        reader:  { translit: false, morph: false, strongs: false, gloss: false, flow: true, notes: false },
        student: { translit: true,  morph: false, strongs: false, gloss: true,  flow: true, notes: false },
        scholar: { translit: true,  morph: true,  strongs: true,  gloss: true,  flow: true, notes: false }
    };
    var userMode = localStorage.getItem('atl-user-mode') || 'scholar';
    var ilRows = JSON.parse(localStorage.getItem('atl-il-rows') || 'null') || USER_MODES[userMode];
    var highContrast = localStorage.getItem('atl-high-contrast') === 'true';

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
                ch.cross_refs.forEach(function(xr) {
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
            name: 'The Divine Council',
            icon: '\u2727',
            color: '#c9a84c',
            desc: 'Trace the heavenly court from creation through the New Testament \u2014 how God governs through a council of divine beings.',
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
        }
    ];

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

        // Check hash — only navigate to a text if URL hash points to one
        var hash = location.hash.slice(1);
        if (hash && hash !== 'library') {
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
        libraryMode = true;
        currentText = null;
        document.body.classList.remove('text-selected');
        localStorage.removeItem('atl-current-text');
        location.hash = '';
        setReadingPane(false);
        buildLibrarySidebar();
        renderLibraryMain();
    }

    function showProphecyMatrix() {
        libraryMode = true;
        currentText = null;
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
        document.body.classList.remove('text-selected');
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
        document.body.classList.remove('text-selected');
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
            '<span class="library-badge-count">' + PROPHECY_MATRIX.length + '</span>' +
            '</div>' +
            '<div class="library-text-link" data-action="prophecy-tracker">' +
            '<span class="library-dot" style="background:#5a7a9e"></span>' +
            '<span class="library-text-name">Prophecy Tracker</span>' +
            '<span class="library-badge-count">' + Object.keys(BOOK_PROPHECIES).length + ' books</span>' +
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
            html += '<div class="trail-step" data-nav-text="' + (textId || '') + '" data-nav-chapter="' + (step.chId || '') + '">' +
                '<div class="trail-step-number">' + (i + 1) + '</div>' +
                '<div class="trail-step-content">' +
                '<div class="trail-step-label">' + step.label + '</div>' +
                '<div class="trail-step-why">' + step.why + '</div>' +
                '</div>' +
                '<span class="trail-step-go">\u2192</span>' +
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

        // Recent texts section (continue reading)
        var recentTexts = JSON.parse(localStorage.getItem('atl-recent-texts') || '[]');
        if (recentTexts.length > 0) {
            html += '<div class="library-recent-section">' +
                '<h2 class="library-recent-heading">Continue Reading</h2>' +
                '<div class="library-recent-grid">';
            recentTexts.slice(0, 4).forEach(function(rid) {
                var rt = getTextDef(rid);
                if (!rt) return;
                var rcat = getCategoryDef(rt.category);
                var rcounts = getTextReadCount(rid);
                html += '<div class="library-recent-card" data-text="' + rid + '" style="--card-color:' + (rt.color || rcat.color) + '">' +
                    '<span class="canon-badge badge-small" style="background:' + rcat.color + '20;color:' + rcat.color + ';border-color:' + rcat.color + '40">' + rcat.badge + '</span>' +
                    '<h3 class="library-recent-title">' + rt.name + '</h3>' +
                    '<span class="library-recent-progress">' + rcounts.read + '/' + rcounts.total + ' read</span>' +
                    '</div>';
            });
            html += '</div></div>';
        }

        // Featured study card
        html += '<div class="library-featured">' +
            '<div class="library-featured-card" data-text="heavenly_court">' +
            '<div class="library-featured-label">FEATURED STUDY</div>' +
            '<h3 class="library-featured-title">The Heavenly Court</h3>' +
            '<p class="library-featured-desc">Deep dive into the divine council worldview that unifies the entire biblical narrative.</p>' +
            '<span class="library-featured-cta">Begin the Study &rarr;</span>' +
            '</div>' +
            '</div>';

        // Study Trails section
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

        categories.forEach(function(cat) {
            var catTexts = texts.filter(function(t) { return t.category === cat.id; });
            var isEmpty = catTexts.length === 0;
            // Large sections (OT, NT) start collapsed; smaller ones start open
            var startCollapsed = catTexts.length > 6;

            // Section header for each category (clickable to toggle)
            html += '<div class="library-section' + (startCollapsed ? ' collapsed' : '') + '" data-category="' + cat.id + '">' +
                '<div class="library-section-header" data-toggle="section">' +
                '<h2 class="library-section-title" style="color:' + cat.color + '">' +
                '<span class="library-section-badge" style="background:' + cat.color + '18;color:' + cat.color + ';border:1px solid ' + cat.color + '40">' + cat.badge + '</span>' +
                cat.name +
                '</h2>' +
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
                    var chCount = 0;
                    eras.forEach(function(era) {
                        var chapters = ERA_DATA[era.id] || [];
                        chapters.forEach(function(ch) {
                            if (ch.type === 'chapter') chCount++;
                        });
                    });
                    var hasContent = eras.length > 0;
                    var il = getTextInterlinear(t.id);
                    var ilCount = Object.keys(il).length;

                    html += '<div class="library-card' + (hasContent ? '' : ' library-card-empty') + '" data-text="' + t.id + '" style="--card-color:' + (t.color || cat.color) + '">' +
                        '<div class="library-card-top">' +
                        '<span class="canon-badge" style="background:' + cat.color + '20;color:' + cat.color + ';border-color:' + cat.color + '40">' + cat.badge + '</span>' +
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
                html += '</div></div>';
            }

            html += '</div>';
        });

        mainContent.innerHTML = html;

        // Stagger-animate library cards
        var cards = mainContent.querySelectorAll('.library-card');
        cards.forEach(function(card, i) {
            card.classList.add('stagger-in');
            card.style.animationDelay = (i * 30) + 'ms';
        });
    }

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

            libraryMode = false;
            currentText = textId;
            document.body.classList.add('text-selected');
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

    function loadTextContent(textId) {
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

            // Render text introduction panel if available
            html += renderTextIntro(textId);

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

        // Eras start collapsed — user expands what they want
        setupIntersectionObserver();
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

        var html = '<div class="chapter-card' + (isRead ? ' chapter-read' : '') + '" id="' + ch.id + '" style="--era-color:' + era.color + '">' +
            '<div style="position:absolute;top:0;left:0;right:0;height:3px;background:' + era.color + ';border-radius:6px 6px 0 0"></div>' +
            '<label class="read-check-label" title="Mark as read"><input type="checkbox" class="read-check" data-id="' + ch.id + '"' + (isRead ? ' checked' : '') + '></label>' +
            '<button class="chapter-copy-btn" data-id="' + ch.id + '" title="Copy study content">&#x1F4CB;</button>' +
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

        // Key verse
        if (ch.key_verse) {
            html += '<div class="scripture-block">' +
                '<div class="verse-ref">' + ch.key_verse.ref + '</div>' +
                '<div class="verse-text">' + ch.key_verse.text + '</div>' +
                '<div class="verse-translation">' + ch.key_verse.translation + '</div>' +
                '</div>';
        }

        // Hebrew terms
        if (ch.hebrew_terms && ch.hebrew_terms.length > 0) {
            html += renderTermsGrid(ch.hebrew_terms);
        }

        // ANE backdrop
        if (ch.ane_backdrop) {
            html += '<div class="ane-callout">' +
                '<div class="callout-label">Ancient Near Eastern Context</div>' +
                '<div class="callout-body">' + ch.ane_backdrop + '</div></div>';
        }

        // Second Temple sources
        if (ch.second_temple && ch.second_temple.length > 0) {
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
                html += '<span class="cross-ref-pill type-' + xr.type + '"' +
                    ' data-chapter="' + ch.id + '" data-index="' + i + '"' +
                    ' title="' + escAttr(xr.note) + '">' + xr.ref + '</span>';
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

        // Sections
        if (ch.sections && ch.sections.length > 0) {
            html += '<div class="chapter-sections">';
            ch.sections.forEach(function(sec) {
                html += '<div class="section-block">' +
                    '<h4>' + sec.heading + '</h4>' +
                    '<div class="section-body">' + sec.body + '</div></div>';
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

        // Mobile-friendly action bar at bottom of card
        html += '<div class="chapter-action-bar">' +
            '<button class="chapter-action-read' + (isRead ? ' is-read' : '') + '" data-id="' + ch.id + '">' +
            (isRead ? '\u2714 Read' : '\u25CB Mark as Read') + '</button>' +
            '<button class="chapter-action-bookmark' + (isBookmarked ? ' is-bookmarked' : '') + '" data-id="' + ch.id + '">' +
            (isBookmarked ? '\u2605 Saved' : '\u2606 Save') + '</button>' +
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
                html += '<span class="cross-ref-pill type-' + xr.type + '"' +
                    ' data-chapter="' + ch.id + '" data-index="' + i + '"' +
                    ' title="' + escAttr(xr.note) + '">' + xr.ref + '</span>';
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

            // Recent text card — open text
            var recentCard = e.target.closest('.library-recent-card');
            if (recentCard && recentCard.dataset.text) {
                selectText(recentCard.dataset.text);
                return;
            }

            var featured = e.target.closest('.library-featured-card');
            if (featured && featured.dataset.text) {
                selectText(featured.dataset.text);
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

            // Study trail card — open trail detail view
            var trailCard = e.target.closest('.study-trail-card');
            if (trailCard && trailCard.dataset.trail) {
                renderStudyTrail(trailCard.dataset.trail);
                window.scrollTo(0, 0);
                return;
            }

            var card = e.target.closest('.library-card');
            if (card && !card.classList.contains('library-card-empty')) {
                selectText(card.dataset.text);
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

            // Study trail step navigation
            var trailStep = e.target.closest('.trail-step');
            if (trailStep && trailStep.dataset.navText) {
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

        // Search
        var searchTimer = null;
        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimer);
            searchTimer = setTimeout(function() { performSearch(searchInput.value.trim()); }, 200);
        });

        searchInput.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                searchInput.value = '';
                searchResults.classList.remove('visible');
            }
        });

        // Keyboard shortcuts
        document.addEventListener('keydown', function(e) {
            if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
                e.preventDefault();
                searchInput.focus();
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
        var el = document.getElementById(id);
        if (el) {
            el.scrollIntoView({ behavior: 'smooth', block: 'start' });
            el.classList.add('flash');
            setTimeout(function() { el.classList.remove('flash'); }, 1000);
        }
    }

    function handleHash() {
        var hash = location.hash.slice(1);

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

    // ── Search ──────────────────────────────────────────────
    var flowSearchIndex = null;

    function buildSearchIndex(force) {
        if (searchIndex && !force) return;
        searchIndex = [];

        MANIFEST.eras.forEach(function(era) {
            var chapters = ERA_DATA[era.id] || [];
            chapters.forEach(function(ch) {
                var text = [ch.title, ch.synopsis || ''];

                if (ch.type === 'html_fragment' && ch.html) {
                    text.push(ch.html.replace(/<[^>]+>/g, ' '));
                }

                if (ch.sections) {
                    ch.sections.forEach(function(s) {
                        text.push(s.heading);
                        text.push(s.body);
                    });
                }
                if (ch.ane_backdrop) text.push(ch.ane_backdrop);
                if (ch.divine_council_note) text.push(ch.divine_council_note);
                if (ch.second_temple) {
                    ch.second_temple.forEach(function(s) {
                        text.push(s.source);
                        text.push(s.summary);
                    });
                }

                searchIndex.push({
                    id: ch.id,
                    era: era.id,
                    textId: era.text,
                    ref: ch.ref || ch.title,
                    title: ch.title,
                    type: ch.type,
                    text: text.join(' ')
                });
            });
        });
    }

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
                        textId: t.id,
                        bookName: bookName,
                        ch: chNum,
                        v: verse.num,
                        flow: verse.flow,
                        note: verse.note || ''
                    });
                });
            });
        });
    }

    function performSearch(query) {
        if (!query || query.length < 2) {
            searchResults.classList.remove('visible');
            return;
        }
        logEvent('search', query);

        buildSearchIndex();
        var lower = query.toLowerCase();
        var results = [];

        // Search study chapters (era content)
        searchIndex.forEach(function(entry) {
            var score = 0;
            if (entry.title.toLowerCase().includes(lower)) score += 10;
            if (entry.ref.toLowerCase().includes(lower)) score += 8;
            if (entry.text.toLowerCase().includes(lower)) score += 3;
            if (score > 0) {
                var textLower = entry.text.toLowerCase();
                var idx = textLower.indexOf(lower);
                var context = '';
                if (idx >= 0) {
                    var start = Math.max(0, idx - 40);
                    var end = Math.min(entry.text.length, idx + query.length + 60);
                    context = (start > 0 ? '...' : '') +
                              entry.text.substring(start, end) +
                              (end < entry.text.length ? '...' : '');
                }
                results.push({ id: entry.id, era: entry.era, textId: entry.textId,
                    ref: entry.ref, title: entry.title, score: score, context: context,
                    isVerse: false });
            }
        });

        // Search flow translations (verse text)
        buildFlowSearchIndex();
        flowSearchIndex.forEach(function(entry) {
            var flowLower = entry.flow.toLowerCase();
            var noteLower = entry.note.toLowerCase();
            var idx = flowLower.indexOf(lower);
            var noteIdx = noteLower.indexOf(lower);
            if (idx >= 0 || noteIdx >= 0) {
                var source = idx >= 0 ? entry.flow : entry.note;
                var srcIdx = idx >= 0 ? idx : noteIdx;
                var start = Math.max(0, srcIdx - 30);
                var end = Math.min(source.length, srcIdx + query.length + 50);
                var context = (start > 0 ? '...' : '') +
                              source.substring(start, end) +
                              (end < source.length ? '...' : '');
                results.push({
                    id: null,
                    textId: entry.textId,
                    ref: entry.bookName + ' ' + entry.ch + ':' + entry.v,
                    title: entry.bookName + ' ' + entry.ch + ':' + entry.v,
                    score: idx >= 0 ? 5 : 2,
                    context: context,
                    isVerse: true,
                    ch: entry.ch
                });
            }
        });

        results.sort(function(a, b) { return b.score - a.score; });
        var top = results.slice(0, 15);

        if (top.length === 0) {
            searchResults.innerHTML = '<div class="search-result-item"><span class="result-context">No results found</span></div>';
        } else {
            var re = new RegExp('(' + query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi');
            searchResults.innerHTML = top.map(function(r) {
                var textName = getTextName(r.textId);
                var badge = r.isVerse ? '<span class="result-badge">verse</span>' : '';
                return '<div class="search-result-item" data-id="' + (r.id || '') + '" data-text="' + r.textId + '" data-ch="' + (r.ch || '') + '" data-verse="' + (r.isVerse ? '1' : '') + '">' +
                    '<div class="result-ref">' + badge + textName + ' \u2014 ' + r.ref + '</div>' +
                    '<div class="result-context">' + r.context.replace(re, '<mark>$1</mark>') + '</div></div>';
            }).join('');

            searchResults.querySelectorAll('.search-result-item').forEach(function(item) {
                item.addEventListener('click', function() {
                    searchResults.classList.remove('visible');
                    searchInput.value = '';
                    var textId = item.dataset.text;
                    var isVerse = item.dataset.verse === '1';
                    var chNum = parseInt(item.dataset.ch);

                    if (isVerse && textId && chNum) {
                        // Navigate to the book + chapter in interlinear reading pane
                        if (textId !== currentText) selectText(textId, true);
                        currentILBook = textId;
                        renderInterlinear(chNum);
                        setReadingPane(true);
                    } else {
                        if (textId && textId !== currentText) {
                            selectText(textId, true);
                        }
                        requestAnimationFrame(function() {
                            location.hash = item.dataset.id;
                        });
                    }
                });
            });
        }

        searchResults.classList.add('visible');
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
        chapterData.cross_refs.forEach(function(xr, i) {
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
            activeChapter.cross_refs.forEach(function(xr) {
                html += '<div class="source-reading-xref">' +
                    '<span class="source-reading-xref-ref">' + xr.ref + '</span>';
                if (xr.note) html += '<span class="source-reading-xref-note"> \u2014 ' + xr.note + '</span>';
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

    // ── Ancient World Map ────────────────────────────────────
    var mapInstance = null;
    var mapMarkers = [];
    var mapCategories = {
        'biblical':   { color: '#c9a84c', label: 'Biblical Sites',      icon: '\u2721' },
        'typology':   { color: '#b5564a', label: 'Christ Typology',     icon: '\u2670' },
        'watcher':    { color: '#9b7ec8', label: 'Watcher Geography',   icon: '\u2604' },
        'megalith':   { color: '#b07050', label: 'Megaliths & Anomalies', icon: '\u25B2' },
        'pyramid':    { color: '#d4a853', label: 'Global Pyramids',     icon: '\u25B3' },
        'dss':        { color: '#5b8dbf', label: 'Dead Sea Scroll Sites', icon: '\u2720' },
        'cultural':   { color: '#2d9a8f', label: 'Cultural Parallels',  icon: '\u2735' }
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
         refs:'Genesis 11:1-9; Deuteronomy 32:8'},
        {cat:'biblical', name:'Ur of the Chaldeans', lat:30.96, lng:46.1,
         desc:'Abraham\'s birthplace. Excavated by Leonard Woolley (1922-34), revealing a sophisticated Sumerian city with the Royal Tombs and ziggurat of Nanna.',
         refs:'Genesis 11:31; Acts 7:2-4'},
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
         refs:'Genesis 19; Jude 1:7'},
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
         note:'The 33.33\u00B0 latitude (Paris Meridian) connection: Before the 1884 Greenwich switch, Paris was the prime meridian. Mt. Hermon sits at exactly 33\u00B033\' on that system. The number 33 recurs in esoteric traditions (33 degrees of Freemasonry, Jesus crucified at 33, 33 vertebrae in the spine). Coincidence or pattern?'},
        {cat:'watcher', name:'Azazel\'s Desert Prison', lat:31.0, lng:35.3,
         desc:'The wilderness of Dudael where Azazel was bound. The scapegoat ritual (Leviticus 16) sends a goat "for Azazel" into the desert\u2014a ritual acknowledgment of the imprisoned Watcher.',
         refs:'1 Enoch 10:4-6; Leviticus 16:8-10'},
        {cat:'watcher', name:'Dan / Caesarea Philippi', lat:33.25, lng:35.69,
         desc:'At the base of Mt. Hermon. The "Gates of Hades" cave where pagan worship occurred. Jesus deliberately chose THIS location to declare "the gates of Hades shall not prevail."',
         refs:'Matthew 16:13-18; Judges 18'},
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
         refs:'1 Enoch 8:3 (astronomical knowledge)'},
        {cat:'megalith', name:'Sacsayhuaman, Peru', lat:-13.5092, lng:-71.9822,
         desc:'Massive stones (up to 200 tons) fitted together with sub-millimeter precision\u2014no mortar. Zigzag walls of enormous blocks. The Inca said THEY didn\'t build it\u2014it was built by "giants" who came before.',
         refs:'Numbers 13:33 (Nephilim in the land)',
         note:'Local tradition attributes construction to giants or supernatural beings. The precision fitting exceeds modern engineering without laser-cut tools.'},
        {cat:'megalith', name:'Puma Punku, Bolivia', lat:-16.5616, lng:-68.6795,
         desc:'H-shaped blocks weighing up to 130 tons, precision-cut from diorite (one of the hardest stones). Interlocking joints without mortar. At 12,800 ft altitude. The Aymara say it was built "in a single night by the gods."',
         refs:'1 Enoch 7-8 (Watcher-taught arts)'},
        {cat:'megalith', name:'Easter Island (Rapa Nui)', lat:-27.1127, lng:-109.3497,
         desc:'The moai statues (up to 82 tons) carved and transported across the island. Local legends say they "walked" into place through mana (spiritual power). 887 statues on a remote Pacific island.',
         refs:'Genesis 6:4 (heroes of old, men of renown)'},

        // ── GLOBAL PYRAMIDS ──
        {cat:'pyramid', name:'Great Pyramid of Giza', lat:29.9792, lng:31.1342,
         desc:'2.3 million blocks averaging 2.5 tons. Built in ~20 years = 1 block every 2-5 minutes, 24/7, no breaks. The math doesn\'t work with copper tools and ramps. Aligned to true north within 3/60th of a degree. Internal chambers contain granite transported 500 miles from Aswan.',
         refs:'Job 38:4-7 (foundations of the earth)',
         note:'Timeline problem: Mainstream = ~2560 BC by Khufu with 20,000-30,000 workers. But: 2.3M blocks \u00F7 20 years \u00F7 365 days = 315 blocks/day = 1 every 4.5 minutes. Including quarrying, transporting, and precision-placing multi-ton blocks. With copper tools. At altitude. With perfect astronomical alignment. Something doesn\'t add up.', img:'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Kheops-Pyramid.jpg/320px-Kheops-Pyramid.jpg'},
        {cat:'pyramid', name:'Pyramid of the Sun, Teotihuacan', lat:19.6925, lng:-98.8431,
         desc:'Third-largest pyramid on Earth. Base perimeter nearly identical to the Great Pyramid. Built ~100 AD. Teotihuacan means "the place where men became gods"\u2014or more literally, "birthplace of the gods." Builders unknown.',
         refs:'Genesis 6:4; Deuteronomy 32:8 (divine allotment of nations)', img:'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Teotihuac%C3%A1n_-_Sonnenpyramide.jpg/320px-Teotihuac%C3%A1n_-_Sonnenpyramide.jpg'},
        {cat:'pyramid', name:'Borobudur, Indonesia', lat:-7.6079, lng:110.2038,
         desc:'Largest Buddhist temple in the world. 2 million stone blocks. 72 bell-shaped stupas. Built ~800 AD but on a much older foundation. Indonesia\'s Ring of Fire parallels other anomalous sites.'},
        {cat:'pyramid', name:'White Pyramid of Xi\'an, China', lat:34.3381, lng:108.5694,
         desc:'Over 40 pyramids in Shaanxi province. The largest rivals Giza in base area. Chinese government restricts access. Built 2000+ years ago. Aligned to cardinal directions like Giza and Teotihuacan.'},
        {cat:'pyramid', name:'Gunung Padang, Indonesia', lat:-6.9944, lng:107.0564,
         desc:'Controversial site. Core samples suggest construction may date to 20,000-27,000 BP, which would make it the oldest pyramid structure on Earth. If confirmed, this predates the end of the Ice Age and all known civilizations.',
         note:'Geological dating is disputed. But even conservative estimates put it at 5000+ BC\u2014older than Giza.'},
        {cat:'pyramid', name:'Antarctica Ice Anomalies', lat:-79.98, lng:-81.96,
         desc:'Satellite imagery reveals symmetrical, pyramid-shaped mountains in the Ellsworth range. Natural formation or remnant of pre-Ice-Age construction? Antarctica was ice-free until ~34 million years ago\u2014but the Piri Reis map (1513) shows accurate Antarctic coastline.',
         note:'Speculative but persistent. The Piri Reis map, drawn from older source maps, depicts Antarctica without ice. Combined with the global pyramid distribution pattern, Antarctica remains an open question.'},

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
         note:'The Templar-Freemason-Solomon connection. Knights Templar excavated the Temple Mount (1119-1128 AD). What did they find? Solomon\'s Temple contained the Ark, the mercy seat\u2014the physical throne of God\'s council.'},
        {cat:'cultural', name:'Giza-Orion Alignment', lat:29.9773, lng:31.1325,
         desc:'Robert Bauval\'s Orion Correlation Theory: the three Giza pyramids mirror the three stars of Orion\'s Belt. The shaft in the King\'s Chamber points directly to Orion (Osiris) and Sirius (Isis). Astronomical encoding in stone.',
         note:'If the Watchers "taught the signs of the sun, moon, and stars" (1 Enoch 8:3), astronomical encoding in megalithic architecture is exactly what we\'d expect.'},
        {cat:'cultural', name:'Derinkuyu Underground City, Turkey', lat:38.3735, lng:34.7348,
         desc:'Underground city for 20,000 people, extending 18 stories deep. Built by unknown civilization. Could be sealed from the inside. A place to hide from... what? The flood? The Nephilim?',
         note:'Multiple underground cities in Cappadocia suggest a civilization that needed to go underground for extended periods. The scale exceeds mere defense.'},
        {cat:'cultural', name:'Shroud of Turin, Italy', lat:45.0735, lng:7.6860,
         desc:'Cathedral of St. John the Baptist houses the most studied artifact in history. 14.3 x 3.6 ft linen cloth bearing the image of a crucified man. No pigment \u2014 image affects only outermost 200-600nm of fiber. 3D information encoded (VP8 analyzer, 1977). Blood type AB+, applied BEFORE image formed. 2019 WAXS dating: ~55 CE.',
         refs:'Matthew 27:59; Mark 15:46; John 19:40',
         note:'The 1988 C-14 dating (medieval) used a repaired corner. The 2019 Wide Angle X-ray Scattering method dates it to the 1st century. The Sudarium of Oviedo (Spain) has 124 matching blood stains and the same AB blood type.'},
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
         note:'Carthage proves that wherever the cursed Canaanite line spread, they took their abominations with them. The tophet excavations found urns containing charred infant bones \u2014 exactly what Leviticus 18:21 and Deuteronomy 12:31 condemn. God\'s judgment on Canaan was not arbitrary \u2014 it was justice.'},
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
        {cat:'biblical', name:'Hebron (Kiriath-Arba)', lat:31.5326, lng:35.0998,
         desc:'Ancient name Kiriath-Arba means "City of Arba" \u2014 Arba was "the greatest man among the Anakim" (Joshua 14:15). The Anakim were the post-flood Nephilim clan. Caleb drove them out (Joshua 15:13-14). Also the burial site of Abraham, Isaac, and Jacob.',
         refs:'Joshua 14:15; Numbers 13:22; Genesis 23:2'},
        {cat:'biblical', name:'Gath of the Philistines', lat:31.6103, lng:34.8489,
         desc:'Home of Goliath and his four giant relatives (2 Samuel 21:15-22). After Joshua cleared most Anakim, survivors remained in Gaza, Gath, and Ashdod (Joshua 11:22). Tell es-Safi excavations found a potsherd with names etymologically related to "Goliath."',
         refs:'1 Samuel 17:4; 2 Samuel 21:15-22; Joshua 11:22'},
        {cat:'biblical', name:'Bashan / Golan Heights', lat:32.95, lng:35.80,
         desc:'Kingdom of Og, last of the Rephaim. His bed was 13.5 feet long (Deuteronomy 3:11). Bashan was considered a gateway to the underworld in Ugaritic and Israelite tradition. Psalm 22:12: "Strong bulls of Bashan encircle me."',
         refs:'Deuteronomy 3:1-11; Psalm 22:12; Amos 4:1'},
        {cat:'watcher', name:'Raphael\'s Binding Site (Dudael)', lat:31.7, lng:35.4,
         desc:'1 Enoch 10:4-6: Raphael binds Azazel "hand and foot, and cast him into the darkness: and make an opening in the desert \u2014 which is in Dudael \u2014 and cast him therein." Traditionally located in the Judean wilderness near the Dead Sea.',
         refs:'1 Enoch 10:4-6; Leviticus 16:10'},
        {cat:'megalith', name:'Carnac Stones, France', lat:47.5916, lng:-3.0744,
         desc:'Over 3,000 standing stones arranged in parallel alignments stretching 4 kilometers. Erected ~4500-3300 BC. The largest stones (up to 350 tons, now fallen) are at the western end. Local Breton legend says they are Roman soldiers turned to stone by Merlin.',
         note:'Pre-Celtic, pre-Roman. Like Gobekli Tepe, this was built by people who shouldn\'t have had the organization or technology for monumental construction. The alignment patterns suggest astronomical knowledge.'},
        {cat:'megalith', name:'Newgrange, Ireland', lat:53.6947, lng:-6.4754,
         desc:'Built ~3200 BC \u2014 older than both Stonehenge and the Giza pyramids. The passage tomb is precisely aligned so that on the winter solstice, sunlight floods the inner chamber through a roof box. Engineering of this precision by "primitive" Neolithic Irish is unexplained.',
         refs:'1 Enoch 8:3 (astronomical knowledge taught by Watchers)'},
        {cat:'megalith', name:'Rujm el-Hiri (Gilgal Refaim)', lat:32.9932, lng:35.8175,
         desc:'A massive megalithic monument in the Golan Heights \u2014 five concentric stone circles with a central cairn. ~5000 BC. Hebrew name means "Wheel of the Giants" (Rephaim). Over 42,000 basalt rocks, weighing ~40,000 tons total. Visible only from the air. Connected to the Rephaim/Nephilim tradition \u2014 the giants of Bashan (Deut 3:11, Og\'s iron bed).',
         refs:'Deuteronomy 3:11,13; Joshua 12:4; 2 Samuel 5:18 (Valley of Rephaim)',
         note:'Located in biblical Bashan, territory of Og the giant king. The name "Gilgal Refaim" (Wheel of the Rephaim) directly connects this to the Nephilim tradition. No known builder civilization.'},
        {cat:'megalith', name:'Dolmen Field, Golan Heights', lat:32.85, lng:35.78,
         desc:'The Golan Heights contain the highest concentration of dolmens in the Middle East \u2014 over 5,000 stone burial chambers. Many weigh 20-50 tons. Dated ~4500-3000 BC. Traditionally associated with the Rephaim/giants who inhabited Bashan.',
         refs:'Deuteronomy 3:13; Joshua 13:12'},
        {cat:'megalith', name:'Karnak Temple, Egypt', lat:25.7188, lng:32.6573,
         desc:'The largest ancient religious complex in the world. The Hypostyle Hall has 134 columns up to 24m tall, each weighing ~70 tons. The largest obelisk (by Hatshepsut) weighs 323 tons of solid granite. How these were quarried, transported, and erected remains debated.',
         refs:'Exodus 1:11 (built by forced labor)',
         note:'The scale of stone construction at Karnak exceeds anything achievable with the tools attributed to ancient Egyptians. The precision of the column placement suggests mathematical knowledge.'},
        {cat:'megalith', name:'Aswan Unfinished Obelisk', lat:24.0776, lng:32.8977,
         desc:'A partially carved obelisk still lying in its quarry at Aswan. If completed, it would be 42m tall and weigh ~1,200 tons \u2014 the heaviest single stone ever attempted by ancient civilizations. Abandoned due to a crack. Provides unique evidence of quarrying methods.',
         note:'1,200 tons of solid granite. Modern cranes max out at ~300 tons. No satisfactory explanation for how ancient Egyptians planned to move this.'},
        {cat:'megalith', name:'Ollantaytambo, Peru', lat:-13.2588, lng:-72.2636,
         desc:'Inca fortress with six massive rose-granite monoliths (each ~50 tons) fitted without mortar at the summit. The stone was quarried across a valley and up a mountain. The precision of the stonework rivals any ancient civilization. Local legend attributes it to giants.',
         note:'The "tired stones" (piedras cansadas) scattered along the route are explained by local tradition as stones abandoned by giants who grew weary.'},
        {cat:'megalith', name:'Trilithon, Baalbek', lat:34.0069, lng:36.2040,
         desc:'Three stones (the Trilithon) each weighing ~800 tons, precisely placed 7m above ground in the foundation of the Temple of Jupiter. The nearby "Stone of the Pregnant Woman" (~1,000 tons) and the even larger "Stone of the South" (~1,242 tons) remain in the quarry. These are the largest hewn stones in the world.',
         note:'Attributed to pre-Roman, possibly pre-Phoenician builders. Roman engineers used these existing megaliths as foundations. The logistics of quarrying, transporting, and placing 800-ton stones remain unexplained.'},
        {cat:'megalith', name:'Jiroft / Konar Sandal, Iran', lat:28.4977, lng:57.7327,
         desc:'A Bronze Age civilization (~3000 BC) discovered in 2001 in southeastern Iran. Massive ziggurats, sophisticated chlorite vessels, and evidence of advanced metallurgy. Some scholars connect this to the "Land of Aratta" mentioned in Sumerian texts. Evidence of a "lost" advanced civilization.',
         refs:'Genesis 10:22 (Elam, sons of Shem)'},
        {cat:'megalith', name:'Adam\'s Calendar, South Africa', lat:-25.8842, lng:30.5003,
         desc:'A stone circle in Mpumalanga, South Africa. Claims of extreme antiquity (75,000+ years) are controversial, but the site does show careful astronomical alignment. Some researchers connect it to ancient gold mining in the region.',
         note:'If the dating claims are accurate, this would be the oldest man-made structure. Mainstream archaeology disputes the extreme dates, but the stone arrangement is undeniably deliberate.'},
        {cat:'megalith', name:'Yonaguni Monument, Japan', lat:24.4351, lng:122.9994,
         desc:'An underwater rock formation off Yonaguni Island that appears to show stepped pyramidal structures, channels, and right angles. Discovered 1987. Debate continues whether this is natural erosion or a submerged ancient monument (~10,000+ years old if man-made).',
         note:'If artificial, this predates all known civilizations and would have been built during the last Ice Age when sea levels were lower.'},
        {cat:'megalith', name:'Gunung Padang, Indonesia', lat:-6.9946, lng:107.0563,
         desc:'A megalithic site on a volcanic hill in Java. Core drilling in 2023 revealed buried construction layers potentially dating to 25,000+ BC, which would make it the oldest known pyramid. Five terraces of columnar basalt arranged with clear human purpose.',
         note:'If the deep-layer dating holds, this rewrites human history. Published in Archaeological Prospection (2023). Fierce academic debate ongoing.'},
        {cat:'megalith', name:'Malta Temples (Ggantija)', lat:36.0475, lng:14.2690,
         desc:'The Ggantija temples on Gozo (~3600 BC) are among the oldest free-standing structures on Earth \u2014 older than Stonehenge and the pyramids. Stones up to 50 tons. Built by a Neolithic island culture with no metal tools. Local Maltese legend says they were built by giants.',
         refs:'Genesis 6:4 (giants)',
         note:'"Ggantija" literally means "Giant\'s Tower" in Maltese. The temple builders vanished ~2500 BC with no clear successor.'},
        {cat:'megalith', name:'Moai (Rano Raraku), Easter Island', lat:-27.1213, lng:-109.2863,
         desc:'The quarry where ~95% of the 887 moai statues were carved from compressed volcanic ash (tuff). The largest unfinished moai is 21m tall and would weigh ~270 tons. The Rapanui oral tradition says the moai "walked" to their platforms through mana (spiritual power).',
         note:'The islanders\' own explanation is supernatural. Modern experiments show they CAN be moved by rocking/walking with ropes, but the logistics of the largest ones (80+ tons) remain impressive.'},
        // ── GROK MEGALITHIC EXPANSION ──
        {cat:'megalith', name:'Karahan Tepe', lat:37.41, lng:39.05,
         desc:'Sister site to G\u00f6bekli Tepe in Turkey. Similar T-shaped pillars with phallic and animal carvings. Human head carved from bedrock. Possibly older than G\u00f6bekli. Suggests a widespread pre-agricultural temple-building culture in southeastern Turkey.',
         note:'If these sites are pre-agricultural, it means organized religion preceded farming \u2014 the opposite of what secular archaeology predicted. Pre-Flood knowledge (Gen 4:20-22) carried through Babel?'},
        {cat:'megalith', name:'Derinkuyu Underground City', lat:38.375, lng:34.734,
         desc:'18-level underground city carved from soft volcanic tuff in Cappadocia, Turkey. Could house 20,000 people with livestock. Massive stone doors, ventilation shafts, and wells. Connected to other underground cities by tunnels.',
         note:'Built to hide from what? Who needed to shelter 20,000 people underground? Local tradition says it was built to escape giants/enemies. The engineering implies advanced knowledge of geology and ventilation.'},
        {cat:'megalith', name:'Nabta Playa Stone Circle', lat:22.5, lng:30.7,
         desc:'Ancient stone circle in the Nubian Desert of Egypt, ~7000-6500 BC. Aligned with summer solstice and several bright stars. Predates Stonehenge by ~2,000 years. Built when the Sahara was green.',
         refs:'1 Enoch 8:3 (Baraqiel taught astrology)',
         note:'Astronomical knowledge this early challenges the timeline of civilization. The builders understood stellar precession \u2014 knowledge attributed to the Watchers in 1 Enoch.'},
        {cat:'megalith', name:'Senegambian Stone Circles', lat:13.69, lng:-15.53,
         desc:'Over 1,000 stone circles and tumuli scattered across Gambia and Senegal, comprising 28,000+ individual stones. UNESCO World Heritage site. Erected ~300 BC to 1600 AD. Each circle contains 8-14 standing stones up to 2.5m tall.',
         note:'West Africa\'s most extensive megalithic landscape. Evidence that the impulse to build stone circles is truly global, not limited to Europe or the Near East.'},
        {cat:'megalith', name:'Avebury Henge', lat:51.4285, lng:-1.8530,
         desc:'The largest stone circle in Europe, enclosing 28.5 acres. The outer circle has ~98 standing stones (originally), surrounded by a massive ditch 10m deep. Three times the diameter of Stonehenge. Much of it was deliberately destroyed in the Middle Ages by Christians.',
         note:'Medieval Christians smashed the stones because they believed them to be pagan \u2014 confirming that even in the 1300s, people associated these sites with spiritual power.'},
        {cat:'megalith', name:'Hagar Qim & Mnajdra', lat:35.827, lng:14.442,
         desc:'Neolithic temple complex on Malta\'s southern coast, ~3600-3200 BC. Mnajdra has precise equinox/solstice alignments. Hagar Qim contains the largest single stone in Maltese temples (~20 tons). Female fertility figurines found throughout.',
         note:'Same culture as Ggantija ("Giant\'s Tower"). These tiny islands have the densest concentration of megalithic temples anywhere on Earth. Who were these island builders?'},
        {cat:'megalith', name:'Ring of Brodgar', lat:59.001, lng:-3.230,
         desc:'A massive Neolithic henge and stone circle on Orkney, Scotland. Originally 60 stones in a perfect circle 104m in diameter, surrounded by a deep ditch cut from solid bedrock. ~2500-2000 BC.',
         note:'On a tiny subarctic island with brutal winters, someone cut a ditch through solid rock and erected 60 massive stones in a perfect circle. Why here?'},
        {cat:'megalith', name:'Callanish Stones', lat:58.197, lng:-6.745,
         desc:'A cruciform stone setting on the Isle of Lewis, Scotland, ~2900-2600 BC. 13 stones in a circle with avenue and radiating stone rows forming a cross shape. Aligned with the lunar standstill cycle (every 18.6 years).',
         note:'Understanding the 18.6-year lunar standstill cycle requires generations of observation. This is advanced astronomical knowledge on a remote Scottish island.'},
        {cat:'megalith', name:'Machu Picchu', lat:-13.1631, lng:-72.5450,
         desc:'Inca citadel at 2,430m elevation, built ~1450 AD. Precision dry-stone walls with polygonal blocks fitted without mortar. The Intihuatana stone is an astronomical observatory. Built on earthquake-fault geology yet survives because of the precision engineering.',
         note:'Anti-seismic construction that outperforms modern buildings. Polygonal masonry defies simple tools. The two construction styles (rough upper, precision lower) may indicate different builders/periods.'},
        {cat:'megalith', name:'Teotihuacan', lat:19.6925, lng:-98.8438,
         desc:'Ancient Mesoamerican city in Mexico, peak ~100-450 AD, population 125,000+. Pyramid of the Sun (third largest pyramid on Earth) aligned to astronomical events. Street grid at 15.5\u00b0 east of north. Mica sheets found in construction (imported from 3,000 miles away).',
         note:'Mica has no decorative purpose \u2014 it is used in modern electronics as an insulator. Why import it 3,000 miles and embed it in a pyramid? The name means "birthplace of the gods" in Nahuatl, but the actual builders are UNKNOWN.'},
        {cat:'megalith', name:'Nan Madol', lat:6.85, lng:158.33,
         desc:'A ruined city of 92 artificial islands in a lagoon in Pohnpei, Micronesia. Built from massive basalt "logs" (columnar basalt) weighing up to 50 tons each. The logistics of transporting these across open water are staggering.',
         refs:'Genesis 11:8-9 (dispersed to islands)',
         note:'Local legend says the city was built by twin sorcerers who made the stones fly using magic. "Venice of the Pacific" built by people with no metal tools, no pulleys, no wheels \u2014 on a tiny Pacific island.'},
        {cat:'megalith', name:'Zorats Karer (Carahunge)', lat:39.552, lng:45.510,
         desc:'A stone circle in Armenia with ~223 stones, some with smooth holes drilled through them. Possibly aligned with astronomical events. Sometimes called "Armenia\'s Stonehenge." Dated to ~5500 BC or earlier by some researchers.',
         note:'The drilled holes may be astronomical sighting tubes \u2014 telescope precursors. If the early dating holds, this predates Near Eastern urban civilization.'},
        {cat:'megalith', name:'Almendres Cromlech', lat:38.558, lng:-8.061,
         desc:'The largest cromlech (stone circle) on the Iberian Peninsula, with ~95 standing stones near \u00c9vora, Portugal. Dated to ~6000-4000 BC. The stones are arranged in an ellipse with clear astronomical alignments.',
         note:'One of the oldest megalithic sites in Western Europe. Evidence that megalith-building was already sophisticated before the major European stone ages.'},
        {cat:'megalith', name:'Coral Castle', lat:25.5003, lng:-80.4444,
         desc:'A structure in Florida built single-handedly by Latvian immigrant Edward Leedskalnin (~1923-1951). Over 1,100 tons of oolitic limestone, cut and moved by one man alone. Includes a 9-ton gate that opens with a finger push, perfectly balanced.',
         note:'Leedskalnin claimed to know the secrets of the pyramids. He worked only at night, refusing witnesses. When asked how, he said "I understand the laws of weight and leverage." No one has definitively explained his methods.'},
        {cat:'megalith', name:'Osirion (Abydos)', lat:26.185, lng:31.919,
         desc:'A mysterious subterranean structure behind the Temple of Seti I at Abydos, Egypt. Built from enormous red granite blocks in a style completely different from the temple. Some researchers argue it predates dynastic Egypt.',
         note:'The construction technique (massive megalithic blocks, no decoration) resembles the Valley Temple at Giza more than any New Kingdom work. If pre-dynastic, who built it?'},
        {cat:'megalith', name:'Sardinian Nuraghi', lat:39.843, lng:9.024,
         desc:'Over 7,000 stone towers (nuraghi) dot the island of Sardinia, built ~1900-730 BC. Some are massive multi-tower complexes. The Nuragic civilization also produced mysterious bronze statuettes of warriors, priests, and "giant" figures. Local tradition: "the island of giants."',
         note:'7,000 towers on one island. The logistics suggest a highly organized civilization. Sardinian legends speak of giants. Giant bone discoveries (disputed) have been reported. The bronze figurines show supernatural beings.'},
        {cat:'pyramid', name:'Cholula, Mexico', lat:19.0578, lng:-98.3017,
         desc:'The Great Pyramid of Cholula is the LARGEST pyramid by volume in the world \u2014 bigger than Giza. 4.45 million cubic meters. Aztec name: Tlachihualtepetl ("man-made mountain"). Now has a church on top. Multiple construction phases spanning 2,000 years.',
         note:'The Spanish built a church directly on top of the pagan pyramid \u2014 the same pattern as Christianity building on top of pagan sacred sites across Europe. The largest pyramid on Earth, and most people have never heard of it.'},

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
        {cat:'biblical', name:'Jericho', lat:31.8711, lng:35.4444,
         desc:'First city conquered in Canaan. The walls "fell flat" after Israel marched 7 days. Rahab the prostitute was saved. Everything was cherem (devoted to destruction). The oldest known walled city (~8000 BC).',
         refs:'Joshua 6; Hebrews 11:30-31'},
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
         refs:'Revelation 16:16; Judges 5:19; 2 Kings 23:29'},
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
         refs:'Psalm 82 (cf. KTU 1.2); Psalm 29 (cf. KTU 1.4)'},
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
         note:'The Sea Peoples invasion (~1200 BC) brought further waves of Aegean peoples to this coast. Egyptian inscriptions at Medinet Habu record Ramesses III repelling them. The Peleset (Philistines) settled in Canaan. Strictly C-level archaeological context \u2014 but Scripture confirms God orchestrates all migrations (Acts 17:26).'}
    ];

    // ── BIBLICAL JOURNEYS ──
    var MAP_JOURNEYS = [
        {
            id: 'abraham',
            name: 'Abraham\'s Journey',
            color: '#c9a84c',
            weight: 3,
            dash: '10 6',
            desc: 'From Ur of the Chaldeans through Haran to the Promised Land. God called Abram to leave everything and go to a land "I will show you" (Gen 12:1).',
            refs: 'Genesis 11:31 \u2013 23:19',
            waypoints: [
                {lat:30.96, lng:46.10, label:'Ur of the Chaldeans', ref:'Gen 11:31'},
                {lat:36.87, lng:39.03, label:'Haran', ref:'Gen 11:31-12:4'},
                {lat:32.21, lng:35.28, label:'Shechem', ref:'Gen 12:6'},
                {lat:31.93, lng:35.22, label:'Bethel', ref:'Gen 12:8'},
                {lat:30.05, lng:31.23, label:'Egypt (famine)', ref:'Gen 12:10'},
                {lat:31.93, lng:35.22, label:'Return to Bethel', ref:'Gen 13:3'},
                {lat:31.53, lng:35.10, label:'Hebron / Mamre', ref:'Gen 13:18'},
                {lat:33.25, lng:35.69, label:'Dan (pursuit of kings)', ref:'Gen 14:14'},
                {lat:31.53, lng:35.10, label:'Hebron', ref:'Gen 14:13'},
                {lat:31.25, lng:34.79, label:'Beer-sheba', ref:'Gen 21:31'},
                {lat:31.78, lng:35.24, label:'Mount Moriah (Aqedah)', ref:'Gen 22:2'},
                {lat:31.53, lng:35.10, label:'Hebron (Sarah\'s burial)', ref:'Gen 23:19'}
            ]
        },
        {
            id: 'jacob',
            name: 'Jacob\'s Journey',
            color: '#5a9a6a',
            weight: 3,
            dash: '8 4',
            desc: 'From Beer-sheba to Haran (fleeing Esau), back through Peniel (wrestling God), to Shechem and finally Hebron and Egypt.',
            refs: 'Genesis 28 \u2013 46',
            waypoints: [
                {lat:31.25, lng:34.79, label:'Beer-sheba', ref:'Gen 28:10'},
                {lat:31.93, lng:35.22, label:'Bethel (ladder vision)', ref:'Gen 28:19'},
                {lat:36.87, lng:39.03, label:'Haran (Laban, 20 years)', ref:'Gen 29:4'},
                {lat:32.33, lng:35.73, label:'Mahanaim (angels)', ref:'Gen 32:1-2'},
                {lat:32.19, lng:35.62, label:'Peniel (wrestles God)', ref:'Gen 32:30'},
                {lat:32.21, lng:35.28, label:'Shechem (Dinah)', ref:'Gen 33:18'},
                {lat:31.93, lng:35.22, label:'Bethel (return)', ref:'Gen 35:1'},
                {lat:31.53, lng:35.10, label:'Hebron (reunites with Isaac)', ref:'Gen 35:27'},
                {lat:30.78, lng:31.77, label:'Goshen, Egypt', ref:'Gen 46:28-29'}
            ]
        },
        {
            id: 'exodus',
            name: 'The Exodus',
            color: '#b5564a',
            weight: 4,
            dash: null,
            desc: 'Israel\'s liberation from Egypt through the Red Sea to Mount Sinai. The greatest act of divine intervention in the Old Testament.',
            refs: 'Exodus 12 \u2013 19',
            waypoints: [
                {lat:30.79, lng:31.83, label:'Rameses (departure)', ref:'Exod 12:37'},
                {lat:30.55, lng:32.10, label:'Succoth', ref:'Exod 12:37'},
                {lat:30.30, lng:32.35, label:'Etham', ref:'Exod 13:20'},
                {lat:29.92, lng:32.55, label:'Pi-hahiroth (Red Sea)', ref:'Exod 14:2'},
                {lat:29.27, lng:33.08, label:'Marah (bitter water)', ref:'Exod 15:23'},
                {lat:28.83, lng:33.18, label:'Elim (12 springs, 70 palms)', ref:'Exod 15:27'},
                {lat:28.68, lng:33.68, label:'Rephidim (rock, Amalek)', ref:'Exod 17:1'},
                {lat:28.54, lng:33.98, label:'Mount Sinai', ref:'Exod 19:1'}
            ]
        },
        {
            id: 'wilderness',
            name: 'Wilderness Wandering',
            color: '#b09050',
            weight: 3,
            dash: '6 4',
            desc: 'The 40-year journey from Sinai through the wilderness to the Plains of Moab. A generation died because they refused to enter the land.',
            refs: 'Numbers 10 \u2013 36',
            waypoints: [
                {lat:28.54, lng:33.98, label:'Mount Sinai (departure)', ref:'Num 10:11'},
                {lat:30.63, lng:34.40, label:'Kadesh-barnea (spies)', ref:'Num 13:26'},
                {lat:30.63, lng:34.40, label:'40 years near Kadesh', ref:'Num 14:33-34'},
                {lat:30.32, lng:35.40, label:'Edom border (refused passage)', ref:'Num 20:14-21'},
                {lat:29.83, lng:35.23, label:'Punon (bronze serpent)', ref:'Num 21:4-9'},
                {lat:31.38, lng:35.70, label:'Arnon crossing', ref:'Num 21:13'},
                {lat:31.86, lng:35.56, label:'Plains of Moab', ref:'Num 22:1'},
                {lat:31.77, lng:35.73, label:'Mount Nebo (Moses\' death)', ref:'Deut 34:1'}
            ]
        },
        {
            id: 'conquest',
            name: 'Conquest of Canaan',
            color: '#8a7aaa',
            weight: 3,
            dash: '4 4',
            desc: 'Joshua leads Israel across the Jordan to take the Promised Land. The giant clans (Anakim, Rephaim) are driven out.',
            refs: 'Joshua 1 \u2013 12',
            waypoints: [
                {lat:31.86, lng:35.56, label:'Plains of Moab (staging)', ref:'Josh 1:1'},
                {lat:31.87, lng:35.44, label:'Jericho (walls fall)', ref:'Josh 6'},
                {lat:31.92, lng:35.26, label:'Ai (second assault)', ref:'Josh 8'},
                {lat:31.85, lng:35.18, label:'Gibeon (sun stands still)', ref:'Josh 10:12'},
                {lat:31.61, lng:34.85, label:'Gath (Anakim remnant)', ref:'Josh 11:22'},
                {lat:31.53, lng:35.10, label:'Hebron (Caleb takes it)', ref:'Josh 14:12-15'},
                {lat:33.02, lng:35.57, label:'Hazor (head of kingdoms)', ref:'Josh 11:10'},
                {lat:32.21, lng:35.28, label:'Shechem (covenant renewal)', ref:'Josh 24'}
            ]
        },
        {
            id: 'watcher_descent',
            name: 'Watcher Descent & Nephilim Spread',
            color: '#9b7ec8',
            weight: 3,
            dash: '12 4 4 4',
            desc: 'The 200 Watchers descend on Mount Hermon and their giant offspring spread across the ancient world. After the Flood, remnant Nephilim clans appear in Canaan.',
            refs: '1 Enoch 6\u201316; Genesis 6:1-4; Numbers 13:33',
            waypoints: [
                {lat:33.42, lng:35.86, label:'Mount Hermon (descent)', ref:'1 Enoch 6:6'},
                {lat:34.01, lng:36.20, label:'Baalbek (giant construction)', ref:'Book of Giants'},
                {lat:32.95, lng:35.80, label:'Bashan (Og\'s kingdom)', ref:'Deut 3:11'},
                {lat:33.25, lng:35.69, label:'Dan / Gates of Hades', ref:'Matt 16:18'},
                {lat:31.53, lng:35.10, label:'Hebron (Anakim)', ref:'Num 13:22'},
                {lat:31.61, lng:34.85, label:'Gath (Goliath)', ref:'1 Sam 17:4'},
                {lat:31.10, lng:34.40, label:'Gaza (Anakim survivors)', ref:'Josh 11:22'}
            ]
        },
        {
            id: 'joseph',
            name: 'Joseph\'s Journey',
            color: '#b09050',
            weight: 2,
            dash: '8 6',
            desc: 'Sold by his brothers, carried to Egypt by Ishmaelite traders. From slave to prisoner to vizier of all Egypt. Joseph\'s journey is the prototype of suffering producing salvation for many (Gen 50:20).',
            refs: 'Genesis 37 \u2013 50',
            waypoints: [
                {lat:31.53, lng:35.10, label:'Hebron (father\'s home)', ref:'Gen 37:14'},
                {lat:32.21, lng:35.28, label:'Shechem (sent to brothers)', ref:'Gen 37:12-14'},
                {lat:32.41, lng:35.23, label:'Dothan (sold to traders)', ref:'Gen 37:17-28'},
                {lat:30.60, lng:32.30, label:'Trade route through Sinai', ref:'Gen 37:25'},
                {lat:29.85, lng:31.25, label:'Potiphar\'s house (Memphis)', ref:'Gen 39:1'},
                {lat:29.85, lng:31.28, label:'Prison', ref:'Gen 39:20'},
                {lat:30.05, lng:31.23, label:'Pharaoh\'s court (vizier)', ref:'Gen 41:39-45'},
                {lat:30.78, lng:31.77, label:'Goshen (family settled)', ref:'Gen 47:6'}
            ]
        },
        {
            id: 'moses_life',
            name: 'Moses\' Life Journey',
            color: '#a05a54',
            weight: 3,
            dash: '12 4',
            desc: 'Born under a death sentence in Egypt, raised in Pharaoh\'s palace, exiled to Midian, called at the burning bush, led Israel through the Red Sea and wilderness to the edge of the Promised Land.',
            refs: 'Exodus 2 \u2013 Deuteronomy 34',
            waypoints: [
                {lat:30.78, lng:31.77, label:'Goshen (born in slavery)', ref:'Exod 2:1-2'},
                {lat:30.45, lng:31.20, label:'Nile (basket in reeds)', ref:'Exod 2:3'},
                {lat:30.05, lng:31.23, label:'Pharaoh\'s Palace (raised)', ref:'Exod 2:10'},
                {lat:28.50, lng:35.00, label:'Midian (40 years exile)', ref:'Exod 2:15'},
                {lat:28.54, lng:33.98, label:'Mount Horeb (burning bush)', ref:'Exod 3:1-4'},
                {lat:30.79, lng:31.83, label:'Egypt (plagues & Exodus)', ref:'Exod 7-12'},
                {lat:29.92, lng:32.55, label:'Red Sea crossing', ref:'Exod 14:21-22'},
                {lat:28.54, lng:33.98, label:'Mount Sinai (Torah given)', ref:'Exod 19-20'},
                {lat:30.63, lng:34.40, label:'Kadesh-barnea', ref:'Num 13:26'},
                {lat:31.77, lng:35.73, label:'Mount Nebo (death)', ref:'Deut 34:1-5'}
            ]
        },
        {
            id: 'balaam',
            name: 'Balaam\'s Journey',
            color: '#8a7aaa',
            weight: 2,
            dash: null,
            desc: 'The pagan diviner Balaam, summoned by Balak to curse Israel, found himself compelled by God to bless them instead. His donkey saw the angel of the LORD blocking the road before Balaam did.',
            refs: 'Numbers 22 \u2013 24',
            waypoints: [
                {lat:36.23, lng:38.17, label:'Pethor (Mesopotamia)', ref:'Num 22:5'},
                {lat:34.00, lng:37.00, label:'En route through Syria', ref:'Num 22:21'},
                {lat:32.50, lng:36.20, label:'Donkey sees angel', ref:'Num 22:22-35'},
                {lat:31.86, lng:35.56, label:'Plains of Moab (Balak)', ref:'Num 22:36'},
                {lat:31.77, lng:35.74, label:'Mount Pisgah (blesses Israel)', ref:'Num 23:14'}
            ]
        },
        {
            id: 'spies_route',
            name: 'Spies\' Route',
            color: '#4a8a96',
            weight: 2,
            dash: '4 4',
            desc: 'The 12 spies sent from Kadesh-barnea to scout the Promised Land. They went through the Negev to Hebron, cut grapes at Eshcol, and returned after 40 days. Ten gave a bad report; only Caleb and Joshua trusted God.',
            refs: 'Numbers 13 \u2013 14',
            waypoints: [
                {lat:30.63, lng:34.40, label:'Kadesh-barnea (sent out)', ref:'Num 13:3'},
                {lat:30.85, lng:34.60, label:'Negev (entered from south)', ref:'Num 13:17'},
                {lat:31.25, lng:34.79, label:'Beer-sheba region', ref:'Num 13:17'},
                {lat:31.53, lng:35.10, label:'Hebron (saw the Anakim)', ref:'Num 13:22'},
                {lat:31.55, lng:35.08, label:'Valley of Eshcol (grapes)', ref:'Num 13:23'},
                {lat:33.02, lng:35.57, label:'Lebo-hamath (northern extent)', ref:'Num 13:21'},
                {lat:31.55, lng:35.08, label:'Return via Eshcol', ref:'Num 13:24-25'},
                {lat:30.63, lng:34.40, label:'Kadesh-barnea (report)', ref:'Num 13:26'}
            ]
        },
        {
            id: 'ark_journey',
            name: 'Ark of the Covenant',
            color: '#c9a84c',
            weight: 3,
            dash: null,
            desc: 'The Ark\'s journey from Sinai through the wilderness, into Canaan, captured by the Philistines, and finally brought to Jerusalem by David. The physical throne of God among men.',
            refs: 'Exodus 25 \u2013 2 Samuel 6',
            waypoints: [
                {lat:28.54, lng:33.98, label:'Sinai (Ark constructed)', ref:'Exod 25:10-22'},
                {lat:30.63, lng:34.40, label:'Wilderness (Kadesh)', ref:'Num 10:33'},
                {lat:31.87, lng:35.44, label:'Jordan crossing (Jericho)', ref:'Josh 3:14-17'},
                {lat:31.87, lng:35.44, label:'Jericho (walls fall)', ref:'Josh 6:6-20'},
                {lat:32.06, lng:35.29, label:'Shiloh (tabernacle)', ref:'Josh 18:1'},
                {lat:31.85, lng:35.18, label:'Ebenezer (captured!)', ref:'1 Sam 4:11'},
                {lat:31.80, lng:34.65, label:'Ashdod (Dagon falls)', ref:'1 Sam 5:1-5'},
                {lat:31.61, lng:34.85, label:'Gath (plagues)', ref:'1 Sam 5:8-9'},
                {lat:31.78, lng:34.85, label:'Ekron (cries of terror)', ref:'1 Sam 5:10'},
                {lat:31.75, lng:34.97, label:'Beth-shemesh (returned)', ref:'1 Sam 6:12-19'},
                {lat:31.80, lng:35.10, label:'Kiriath-jearim (20 years)', ref:'1 Sam 7:1-2'},
                {lat:31.78, lng:35.24, label:'Jerusalem (David\'s city)', ref:'2 Sam 6:12-17'}
            ]
        },
        {
            id: 'abrahams_war',
            name: 'Abraham\'s War (Rescue of Lot)',
            color: '#5a9a70',
            weight: 2,
            dash: null,
            desc: 'When four Mesopotamian kings captured Lot at Sodom, Abraham armed 318 trained servants, pursued them north past Dan to Hobah near Damascus, defeated them at night, and recovered everything. Met Melchizedek on return.',
            refs: 'Genesis 14',
            waypoints: [
                {lat:31.53, lng:35.10, label:'Hebron (Mamre, news arrives)', ref:'Gen 14:13'},
                {lat:31.25, lng:35.53, label:'Sodom region (Lot captured)', ref:'Gen 14:11-12'},
                {lat:32.21, lng:35.28, label:'Shechem (northward pursuit)', ref:'Gen 14:14'},
                {lat:33.25, lng:35.69, label:'Dan (caught up to kings)', ref:'Gen 14:14'},
                {lat:33.55, lng:36.25, label:'Hobah near Damascus (victory)', ref:'Gen 14:15'},
                {lat:31.78, lng:35.24, label:'Salem (meets Melchizedek)', ref:'Gen 14:18'},
                {lat:31.53, lng:35.10, label:'Hebron (returns home)', ref:'Gen 14:13'}
            ]
        },
        {
            id: 'elijah',
            name: 'Elijah\'s Journey',
            color: '#a07a4a',
            weight: 2,
            dash: '6 4',
            desc: 'From Gilead to Mount Carmel\'s dramatic showdown with Baal\'s prophets, then fleeing Jezebel to Beer-sheba and onward 40 days to Horeb/Sinai where God spoke in the still small voice.',
            refs: '1 Kings 17 \u2013 19',
            waypoints: [
                {lat:32.40, lng:35.78, label:'Gilead (Tishbe, home)', ref:'1 Kgs 17:1'},
                {lat:32.00, lng:35.55, label:'Brook Cherith (ravens)', ref:'1 Kgs 17:3-6'},
                {lat:33.45, lng:35.29, label:'Zarephath (widow)', ref:'1 Kgs 17:9'},
                {lat:32.74, lng:35.04, label:'Mount Carmel (fire falls)', ref:'1 Kgs 18:19-40'},
                {lat:31.25, lng:34.79, label:'Beer-sheba (fled Jezebel)', ref:'1 Kgs 19:3'},
                {lat:28.54, lng:33.98, label:'Horeb/Sinai (still small voice)', ref:'1 Kgs 19:8-12'}
            ]
        },
        {
            id: 'david_flight',
            name: 'David\'s Flight from Saul',
            color: '#5a7a9a',
            weight: 2,
            dash: null,
            desc: 'Anointed king but hunted like an animal. David fled from Saul across the Judean wilderness for years, gathering a band of outcasts who became his mighty men. He refused to kill God\'s anointed.',
            refs: '1 Samuel 19 \u2013 30',
            waypoints: [
                {lat:31.82, lng:35.23, label:'Gibeah (flees Saul\'s spear)', ref:'1 Sam 19:10'},
                {lat:31.79, lng:35.24, label:'Nob (gets Goliath\'s sword)', ref:'1 Sam 21:1-9'},
                {lat:31.61, lng:34.85, label:'Gath (feigns madness)', ref:'1 Sam 21:10-15'},
                {lat:31.62, lng:34.98, label:'Cave of Adullam (400 men)', ref:'1 Sam 22:1'},
                {lat:31.62, lng:35.05, label:'Keilah (rescues from Philistines)', ref:'1 Sam 23:1-5'},
                {lat:31.43, lng:35.12, label:'Wilderness of Ziph (betrayed)', ref:'1 Sam 23:14-15'},
                {lat:31.47, lng:35.39, label:'En-gedi (spares Saul)', ref:'1 Sam 24:1-22'},
                {lat:31.35, lng:34.58, label:'Ziklag (Philistine base)', ref:'1 Sam 27:5-7'}
            ]
        },
        {
            id: 'philistine_migration',
            name: 'Philistine / Sea Peoples Migration from Caphtor',
            color: '#4a8a96',
            weight: 2,
            dash: '12 6',
            desc: 'God brought the Philistines from Caphtor (Amos 9:7) \u2014 widely identified with Crete/Aegean. They displaced the Avvim (Deut 2:23) and settled the coastal plain where Anakim remnants remained (Josh 11:22). The Sea Peoples invasion (~1200 BC) brought further waves. God sovereignly placed them as persistent enemies to test Israel\'s faith (Judg 3:1-4).',
            refs: 'Genesis 10:13-14; Deuteronomy 2:23; Amos 9:7; Jeremiah 47:4',
            waypoints: [
                {lat:35.3, lng:25.1, label:'Caphtor (Crete) \u2014 Philistine origin', ref:'Amos 9:7'},
                {lat:34.7, lng:29.0, label:'Eastern Mediterranean route', ref:'Deut 2:23'},
                {lat:33.0, lng:33.0, label:'Cyprus (staging area)', ref:'Gen 10:14'},
                {lat:31.80, lng:34.65, label:'Ashdod \u2014 Philistine Pentapolis', ref:'Josh 11:22'},
                {lat:31.67, lng:34.57, label:'Ashkelon \u2014 Philistine Pentapolis', ref:'Judg 14:19'},
                {lat:31.50, lng:34.47, label:'Gaza \u2014 Philistine Pentapolis', ref:'Josh 11:22'},
                {lat:31.70, lng:34.85, label:'Gath \u2014 Home of Goliath & giants', ref:'1 Sam 17:4'},
                {lat:31.78, lng:34.85, label:'Ekron \u2014 Philistine Pentapolis', ref:'1 Sam 5:10'}
            ]
        },
        {
            id: 'giant_slayer',
            name: 'Giant Slayer Trail (Joshua \u2192 Caleb \u2192 David)',
            color: '#b5564a',
            weight: 3,
            dash: null,
            desc: 'The progression of God\'s giant-slaying champions. Joshua cleared the Anakim from the hill country (Josh 11:21). Caleb personally took Hebron \u2014 the Anakim stronghold (Josh 14:12). David and his men killed the last five Rephaim descendants in Philistia (1 Sam 17; 2 Sam 21). All point to Christ who destroys every enemy power (1 Cor 15:25-26; Heb 2:14).',
            refs: 'Joshua 11:21-22; 14:12-15; 1 Samuel 17; 2 Samuel 21:15-22',
            waypoints: [
                {lat:31.87, lng:35.44, label:'Jordan Crossing (conquest begins)', ref:'Josh 3:14-17'},
                {lat:31.87, lng:35.44, label:'Jericho (walls fall)', ref:'Josh 6'},
                {lat:33.02, lng:35.57, label:'Hazor (head of kingdoms)', ref:'Josh 11:10'},
                {lat:31.53, lng:35.10, label:'Hebron (Caleb drives out Anakim)', ref:'Josh 14:12-15'},
                {lat:31.69, lng:34.96, label:'Valley of Elah (David kills Goliath)', ref:'1 Sam 17:49'},
                {lat:31.70, lng:34.85, label:'Gath (four more giants killed)', ref:'2 Sam 21:15-22'},
                {lat:31.50, lng:34.47, label:'Gaza (last Anakim holdout)', ref:'Josh 11:22'}
            ]
        },
        {
            id: 'phoenician_trade',
            name: 'Phoenician Trade Route \u2014 Cursed Line Spreads',
            color: '#7a5a96',
            weight: 2,
            dash: '10 4',
            desc: 'The Phoenicians (= cursed Canaanites, Gen 9:25 + 10:15) built the greatest maritime trade network of the ancient world. Master seafarers, they established colonies across the Mediterranean, spreading both commerce and Baal worship (including child sacrifice). God sovereignly used their skills: their 22-letter alphabet (~1050 BC) became the direct ancestor of Greek, Latin, and every modern Western alphabet \u2014 the writing system God chose for His Word. Their cedar supplied His Temple. Yet everywhere they went, they carried their abominations (Lev 18:21; Deut 12:31).',
            refs: 'Gen 10:15-19; 1 Kings 5:1-12; Ezek 27 (full chapter \u2014 Tyre\'s trade catalog); Isa 23',
            waypoints: [
                {lat:34.12, lng:35.65, label:'Byblos (Gebal) \u2014 oldest city, papyrus/alphabet', ref:'1 Kings 5:18'},
                {lat:33.56, lng:35.38, label:'Sidon \u2014 Canaan\'s firstborn', ref:'Gen 10:15'},
                {lat:33.27, lng:35.20, label:'Tyre \u2014 island fortress, purple dye capital', ref:'Ezek 27'},
                {lat:34.68, lng:33.04, label:'Kition (Cyprus) \u2014 major colony', ref:'Ezek 27:6'},
                {lat:37.50, lng:15.09, label:'Syracuse (Sicily) \u2014 trading post', ref:'Ezek 27:13'},
                {lat:39.22, lng:9.11, label:'Nora (Sardinia) \u2014 Phoenician settlement', ref:'Ezek 27:12'},
                {lat:35.90, lng:14.51, label:'Malta \u2014 strategic waypoint', ref:'Acts 28:1'},
                {lat:36.85, lng:10.32, label:'Carthage \u2014 greatest colony, child sacrifice tophet', ref:'Deut 12:31'},
                {lat:36.53, lng:-6.30, label:'Gades (C\u00e1diz, Spain) \u2014 western terminus', ref:'Ezek 27:12 (Tarshish?)'}
            ]
        },
        {
            id: 'nimrod_expansion',
            name: 'Nimrod\'s Empire \u2014 Babel to Assyria',
            color: '#a07a4a',
            weight: 3,
            dash: '8 4 4 4',
            desc: 'The first post-Flood kingdom-builder. Nimrod (gibbor \u2014 "mighty one," the same term for Nephilim in Gen 6:4) began at Babel in Shinar, then expanded northward into Assyria, building Nineveh, Rehoboth-Ir, Calah, and Resen. His Babel was the center of unified rebellion against God\'s command to fill the earth (Gen 9:1). God scattered it via language confusion (Gen 11:8-9). Arabic legends extend his reach to Baalbek, where he allegedly sent giants to build the megalithic fortress. Nimrod is the prototype of human pride opposing God \u2014 all later proud kingdoms (Assyria, Babylon, Rome) echo his rebellion.',
            refs: 'Gen 10:8-12; Gen 11:1-9; Micah 5:6',
            waypoints: [
                {lat:32.54, lng:44.42, label:'Babel / Babylon (Shinar) \u2014 tower & rebellion', ref:'Gen 11:1-9'},
                {lat:31.32, lng:45.64, label:'Erech (Uruk) \u2014 Gilgamesh\'s city', ref:'Gen 10:10'},
                {lat:32.78, lng:44.00, label:'Accad \u2014 Nimrod\'s domain', ref:'Gen 10:10'},
                {lat:34.50, lng:43.50, label:'Calah \u2014 built by Nimrod in Assyria', ref:'Gen 10:11-12'},
                {lat:36.36, lng:43.15, label:'Nineveh \u2014 "the great city"', ref:'Gen 10:11'},
                {lat:34.01, lng:36.20, label:'Baalbek \u2014 giants rebuild (C-level legend)', ref:'Arabic traditions; Gen 6:4'}
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
            maxZoom: 20,
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
        // ── JOURNEY LAYERS ──
        mapOverlayLayers['\u2500\u2500 JOURNEYS \u2500\u2500'] = L.layerGroup(); // separator
        MAP_JOURNEYS.forEach(function(journey) {
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
                    html: '<div style="background:' + journey.color + ';color:#0c0e14;width:20px;height:20px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:10px;font-weight:bold;border:1px solid rgba(255,255,255,0.5);box-shadow:0 1px 4px rgba(0,0,0,0.5)">' + (i+1) + '</div>',
                    iconSize: [20, 20],
                    iconAnchor: [10, 10],
                    popupAnchor: [0, -12]
                });
                var wpPopup = '<div class="map-popup-title" style="color:' + journey.color + '">' + journey.name + '</div>' +
                    '<div style="font-weight:600;margin:4px 0">' + (i+1) + '. ' + wp.label + '</div>' +
                    '<div class="map-popup-refs">\ud83d\udcdc ' + wp.ref + '</div>';
                jGroup.addLayer(L.marker([wp.lat, wp.lng], { icon: wpIcon }).bindPopup(wpPopup, { maxWidth: 300, className: 'map-dark-popup' }));
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
            {name:'Egyptian New Kingdom (~1550-1070 BC)', color:'#e6b422', coords:[[31.2,25],[30.0,31],[29.5,32.5],[31.0,34.5],[33.5,35.8],[35.0,36.5],[36.5,36.5],[36.5,38],[34.5,38],[31.5,35],[30,33],[24,33],[22,31],[24,28],[27,27],[31.2,25]]},
            {name:'Assyrian Empire (~745-612 BC)', color:'#e05540', coords:[[37.5,36],[36,38],[35,40],[34,42],[33,44],[32,46],[31,47],[30,46],[30,44],[32,42],[33,40],[34,38],[35,36],[36.5,34.5],[38,36],[39,38],[40,40],[39,42],[38,43],[37,44],[36,44.5],[35,44],[34.5,43.5],[34,42],[35,40],[36,38],[37.5,36]]},
            {name:'Babylonian Empire (~626-539 BC)', color:'#b06ce6', coords:[[33.5,35],[34,36.5],[35.5,38],[36,40],[36.5,42],[36,44],[35,45],[33.5,46],[32,47],[30.5,47.5],[29,47],[28,46],[29,44],[30,42],[30.5,40],[31,38],[31.5,36],[32,34.5],[33.5,35]]},
            {name:'Persian Empire (~550-330 BC)', color:'#4aa8e0', coords:[[41,26],[38,30],[37,32],[36,34],[34,35],[32,34],[30,33],[27,34],[23,36],[20,40],[22,44],[24,48],[25,52],[26,56],[28,60],[30,64],[32,68],[34,70],[36,68],[38,64],[40,60],[41,56],[40,52],[39,48],[38,46],[37,44],[38,42],[39,40],[40,38],[42,36],[43,34],[42,30],[41,26]]},
            {name:'Alexander\'s Empire (~334-323 BC)', color:'#2dd4a8', coords:[[41,20],[40,24],[38,28],[37,32],[35,34],[33,35],[31,34],[28,33],[26,34],[23,36],[20,38],[22,44],[24,50],[26,56],[28,60],[30,65],[32,70],[34,72],[36,70],[38,66],[40,62],[41,58],[40,52],[39,48],[38,44],[39,40],[40,36],[42,32],[43,28],[42,24],[41,20]]},
            {name:'Roman Empire (~117 AD, max extent)', color:'#e8554a', coords:[[55,-5],[52,-10],[45,-9],[37,-8],[36,-5],[37,0],[38,5],[40,10],[45,12],[47,16],[46,20],[44,24],[42,28],[41,32],[38,36],[37,38],[36,40],[34,42],[32,40],[30,36],[28,33],[24,34],[22,31],[26,28],[32,25],[36,13],[38,10],[43,5],[47,0],[52,2],[55,-5]]},
            {name:'Kingdom of Israel (~1000-930 BC, United)', color:'#c9a84c', coords:[[33.3,35.5],[33.0,36.0],[32.5,35.8],[32.0,35.6],[31.5,35.5],[31.0,35.4],[30.5,35.0],[30.0,34.8],[29.8,34.5],[30.2,34.3],[30.8,34.4],[31.3,34.6],[31.8,34.8],[32.2,35.0],[32.7,35.2],[33.3,35.5]]},
            {name:'Northern Kingdom / Israel (~930-722 BC)', color:'#e0a030', coords:[[33.3,35.5],[33.0,36.0],[32.5,35.8],[32.0,35.6],[31.8,35.2],[32.0,35.0],[32.3,34.8],[32.7,35.0],[33.3,35.5]]},
            {name:'Southern Kingdom / Judah (~930-586 BC)', color:'#60aadd', coords:[[31.8,35.2],[32.0,35.6],[31.5,35.5],[31.0,35.4],[30.5,35.0],[30.0,34.8],[29.8,34.5],[30.2,34.3],[30.8,34.4],[31.3,34.6],[31.8,35.2]]},
            {name:'Hasmonean Kingdom (~140-63 BC)', color:'#40c070', coords:[[33.5,35.5],[33.2,36.2],[32.8,35.8],[32.2,35.6],[31.8,35.5],[31.2,35.4],[30.8,35.0],[30.2,34.8],[29.8,34.3],[30.5,34.2],[31.5,34.3],[32.2,34.6],[32.8,35.0],[33.5,35.5]]},
            {name:'Herod\'s Kingdom (~37-4 BC)', color:'#c080e0', coords:[[33.4,35.6],[33.2,36.3],[32.9,35.9],[32.3,35.7],[31.9,35.6],[31.3,35.5],[30.5,35.1],[30.0,34.9],[29.5,34.5],[30.0,34.2],[30.8,34.3],[31.5,34.5],[32.3,34.8],[32.9,35.1],[33.4,35.6]]},
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

        // Religion cards
        var filtered = matrixSelectedCat === 'all' ? RELIGIONS_DATA : RELIGIONS_DATA.filter(function(r) { return r.cat === matrixSelectedCat; });
        html += '<div class="matrix-grid">';
        filtered.forEach(function(r) {
            var alignment = r.d[matrixSelectedDoctrine] || 'divergent';
            var ai = ALIGNMENT_INFO[alignment];
            var catInfo = RELIGION_CATEGORIES[r.cat] || {};
            html += '<div class="matrix-card" style="border-left-color:' + ai.color + ';cursor:pointer" data-religion="' + r.id + '" title="Click to explore ' + esc(r.name) + '">';
            html += '<div class="matrix-card-header">';
            html += '<div class="matrix-card-name">' + esc(r.name) + '</div>';
            html += '<div class="matrix-card-meta">' + (catInfo.icon || '') + ' ' + esc(r.founded) + ' \u00B7 ' + esc(r.adherents) + '</div>';
            html += '</div>';
            html += '<div class="matrix-alignment" style="color:' + ai.color + '">';
            html += '<span class="matrix-dot" style="background:' + ai.color + '"></span>' + ai.label;
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
        html += '</tr></thead><tbody>';
        filtered.forEach(function(r) {
            html += '<tr style="cursor:pointer" data-religion="' + r.id + '">';
            html += '<td class="matrix-hm-name">' + esc(r.name) + '</td>';
            DOCTRINE_KEYS.forEach(function(k) {
                var al = r.d[k] || 'divergent';
                var ai = ALIGNMENT_INFO[al];
                html += '<td><span class="matrix-hm-cell" style="background:' + ai.color + '" title="' + ai.label + '"></span></td>';
            });
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
        return str.replace(/&/g, '&amp;').replace(/"/g, '&quot;')
                  .replace(/</g, '&lt;').replace(/>/g, '&gt;');
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

    // ── Launch ──────────────────────────────────────────────
    // Note: On large inline scripts, DOMContentLoaded may fire before the
    // script finishes parsing, so we check readyState as a fallback.
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();
