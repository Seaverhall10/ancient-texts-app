// ═══════════════════════════════════════════════════════════════
// state.js — Centralized state management & localStorage abstraction
// ═══════════════════════════════════════════════════════════════
// Replaces 30+ scattered globals with a single AppState object.
// All localStorage access goes through the Storage wrapper.
// Legacy genesis-* keys are auto-migrated on first load.

// ── Storage abstraction ──────────────────────────────────────
// When a backend is added, only this object needs to change.
var Storage = {
    PREFIX: 'atl-',

    /** Get raw string value */
    get: function(key) {
        try { return localStorage.getItem(this.PREFIX + key); }
        catch(e) { return null; }
    },

    /** Set value (objects are auto-serialized) */
    set: function(key, val) {
        try {
            localStorage.setItem(
                this.PREFIX + key,
                typeof val === 'object' ? JSON.stringify(val) : String(val)
            );
        } catch(e) {
            console.warn('[Storage] Failed to save ' + key + ':', e);
        }
    },

    /** Get parsed JSON value */
    getJSON: function(key) {
        try { return JSON.parse(this.get(key)); }
        catch(e) { return null; }
    },

    /** Remove a key */
    remove: function(key) {
        try { localStorage.removeItem(this.PREFIX + key); }
        catch(e) { /* ignore */ }
    },

    /** Get boolean (treats 'true' as true, everything else as false) */
    getBool: function(key, defaultVal) {
        var v = this.get(key);
        if (v === null) return !!defaultVal;
        return v === 'true';
    },

    /** Get float with fallback */
    getFloat: function(key, defaultVal) {
        var v = parseFloat(this.get(key));
        return isNaN(v) ? (defaultVal || 0) : v;
    }
};


// ── Legacy key migration ─────────────────────────────────────
// Moves genesis-* keys to atl-* prefix (one-time, non-destructive).
var LEGACY_KEY_MAP = {
    'genesis-study-bookmarks': 'bookmarks',
    'genesis-reading-pane':    'reading-pane-open',
    'genesis-reading-mode':    'reading-pane-mode',
    'genesis-il-font-scale':   'il-font-scale'
};

function migrateLegacyKeys() {
    var migrated = 0;
    for (var oldKey in LEGACY_KEY_MAP) {
        if (!LEGACY_KEY_MAP.hasOwnProperty(oldKey)) continue;
        var newKey = Storage.PREFIX + LEGACY_KEY_MAP[oldKey];
        var oldVal = localStorage.getItem(oldKey);
        if (oldVal !== null && localStorage.getItem(newKey) === null) {
            localStorage.setItem(newKey, oldVal);
            migrated++;
        }
    }
    if (migrated > 0) {
        console.log('[state] Migrated ' + migrated + ' legacy genesis-* keys to atl-* prefix');
    }
}


// ── User mode presets ────────────────────────────────────────
var USER_MODES = {
    reader:  { translit: false, morph: false, strongs: false, gloss: true,  flow: true,  notes: false },
    student: { translit: true,  morph: false, strongs: true,  gloss: true,  flow: true,  notes: false },
    scholar: { translit: true,  morph: true,  strongs: true,  gloss: true,  flow: true,  notes: false }
};


// ── AppState: single source of truth ─────────────────────────
// Persisted keys are marked with [P]. Runtime-only keys with [R].
var AppState = {
    // Navigation [P]
    currentText:     null,
    currentEra:      null,
    libraryMode:     true,

    // Reading pane [P]
    readingPaneOpen: true,
    readingPaneMode: 'full',

    // Interlinear [P partial]
    currentILBook:    'genesis',
    currentILChapter: null,        // [R]
    ilFontScale:      1.0,
    sourceReadingMode: false,      // [R]

    // User preferences [P]
    userMode:     'scholar',
    ilRows:       { translit: true, morph: true, strongs: true, gloss: true, flow: true, notes: false },
    highContrast: false,

    // User data [P]
    bookmarks:    [],
    readChapters: {},

    // Search [R]
    searchIndex:     null,
    flowSearchIndex: null,

    // UI state [R] — per-session, not persisted
    textContentCache:   {},
    reverseXrefIndex:   {},
    activeResourceFilter: 'all',

    // Matrix/Timeline filters [R]
    matrixSelectedDoctrine: 'god',
    matrixSelectedCat:      'all',
    timelineFilter:         'all',
    timelineEraFilter:      'all',

    // Layout [P]
    layout:       null,
    colWidth:     null,
    studyToggles: null
};


// ── loadState: read all persisted keys into AppState ─────────
function loadState() {
    // Migrate legacy keys first
    migrateLegacyKeys();

    // Navigation
    AppState.currentText = Storage.get('current-text') || null;
    AppState.libraryMode = !AppState.currentText;

    // Reading pane
    AppState.readingPaneOpen = Storage.get('reading-pane-open') !== 'false';
    AppState.readingPaneMode = Storage.get('reading-pane-mode') || 'full';

    // Interlinear
    AppState.ilFontScale = Storage.getFloat('il-font-scale', 1.0);

    // User preferences
    AppState.userMode     = Storage.get('user-mode') || 'scholar';
    AppState.ilRows       = Storage.getJSON('il-rows') || USER_MODES[AppState.userMode] ||
                            USER_MODES.scholar;
    AppState.highContrast  = Storage.getBool('high-contrast', false);

    // User data
    AppState.bookmarks    = Storage.getJSON('bookmarks') || [];
    AppState.readChapters = Storage.getJSON('read-chapters') || {};

    // Layout
    AppState.layout       = Storage.get('layout');
    AppState.colWidth     = Storage.get('col-width');
    AppState.studyToggles = Storage.getJSON('study-toggles');
}


// ── saveState: persist a single key (or all persisted keys) ──
// Usage: saveState('bookmarks')  or  saveState() for all
var STATE_PERSIST_MAP = {
    'currentText':     { key: 'current-text',      type: 'string' },
    'readingPaneOpen': { key: 'reading-pane-open',  type: 'string' },
    'readingPaneMode': { key: 'reading-pane-mode',  type: 'string' },
    'ilFontScale':     { key: 'il-font-scale',      type: 'string' },
    'userMode':        { key: 'user-mode',          type: 'string' },
    'ilRows':          { key: 'il-rows',            type: 'json' },
    'highContrast':    { key: 'high-contrast',      type: 'string' },
    'bookmarks':       { key: 'bookmarks',          type: 'json' },
    'readChapters':    { key: 'read-chapters',      type: 'json' },
    'layout':          { key: 'layout',             type: 'string' },
    'colWidth':        { key: 'col-width',          type: 'string' },
    'studyToggles':    { key: 'study-toggles',      type: 'json' }
};

function saveState(stateKey) {
    if (stateKey) {
        // Save a single key
        var mapping = STATE_PERSIST_MAP[stateKey];
        if (!mapping) { console.warn('[state] Unknown persist key:', stateKey); return; }
        var val = AppState[stateKey];
        if (val === null || val === undefined) {
            Storage.remove(mapping.key);
        } else {
            Storage.set(mapping.key, val);
        }
    } else {
        // Save all persisted keys
        for (var k in STATE_PERSIST_MAP) {
            if (STATE_PERSIST_MAP.hasOwnProperty(k)) {
                saveState(k);
            }
        }
    }
}
