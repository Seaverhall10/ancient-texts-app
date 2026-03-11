# Ancient Texts Study App — v4.0 Roadmap

**Created:** 2026-03-11
**Target:** 2 weeks (10 working sessions)
**Goal:** Professionally polished, restructured for stability and growth

---

## Phase Overview

| Phase | Days | Focus | Sessions |
|-------|------|-------|----------|
| **A** | 1-2 | JS Module Split (app.js → 25 modules) | 2 |
| **B** | 3-4 | Mobile UX Overhaul (single-chapter view, swipe) | 2 |
| **C** | 5-6 | Feature Polish (Matrix, filters, glossary, Selah) | 2 |
| **D** | 7-8 | Build System Consolidation + Launch Experience | 2 |
| **E** | 9-10 | Full QA Crawl + Deploy v4.0 | 2 |

---

## Phase A: JS Module Split (Days 1-2)

**Problem:** `app.js` is 6,793 lines — one monolithic IIFE. Hard to maintain, debug, or extend. Past bugs (tools popup, search index) stem from this complexity.

**Action:** Split into ~20 focused modules in `src/js/modules/`, concatenated by build.py in dependency order (like CSS build-order).

### Module Map

```
src/js/
├── build-order.txt          ← concatenation order
├── modules/
│   ├── 00-iife-open.js      ← (function() { 'use strict';
│   ├── 01-config.js         ← constants, design tokens, feature flags
│   ├── 02-state.js          ← state variables, localStorage, readChapters
│   ├── 03-data.js           ← MANIFEST, ERA_DATA, GLOSSARY, etc. (placeholders)
│   ├── 04-utils.js          ← esc(), escAttr(), debounce(), helpers
│   ├── 05-analytics.js      ← logEvent(), renderAnalyticsPanel(), export
│   ├── 06-library.js        ← renderLibraryMain(), category sections, recent texts
│   ├── 07-text-view.js      ← selectText(), loadTextContent(), renderChapter()
│   ├── 08-text-intro.js     ← renderTextIntro(), renderIntroSection()
│   ├── 09-sidebar.js        ← buildTextSidebar(), buildLibrarySidebar()
│   ├── 10-search.js         ← buildSearchIndex(), performSearch()
│   ├── 11-interlinear.js    ← renderInterlinear(), word popups, pane controls
│   ├── 12-crossrefs.js      ← openXrefDrawer(), getReverseCitations()
│   ├── 13-glossary.js       ← openGlossary(), renderGlossaryEntries()
│   ├── 14-matrix.js         ← openMatrix(), renderMatrix(), showReligionDetail()
│   ├── 15-timeline.js       ← openTimeline(), renderTimeline()
│   ├── 16-map.js            ← openMap(), Leaflet integration
│   ├── 17-hebrew.js         ← openHebrew(), letter grid
│   ├── 18-progress.js       ← openProgress(), renderProgress()
│   ├── 19-prophecy.js       ← showProphecyTracker(), showCoreBeliefs()
│   ├── 20-trails.js         ← renderStudyTrail(), trail navigation
│   ├── 21-bookmarks.js      ← toggleBookmark(), renderBookmarks()
│   ├── 22-keyboard.js       ← keyboard shortcuts, Ctrl+K, ESC
│   ├── 23-events.js         ← all event listeners, click delegation
│   ├── 24-init.js           ← DOMContentLoaded, hash routing, startup
│   └── 99-iife-close.js     ← })();
```

### Build Changes
- Update `build.py` to read `src/js/build-order.txt` and concatenate JS modules (same pattern as CSS)
- Update `build_mobile.py` to work with concatenated JS
- All `var` declarations at module level stay in IIFE scope (no leakage)
- Each module is a section comment block, not an ES module (keeps IIFE pattern)

### Verification
- Desktop build produces identical functionality
- Mobile build works (all patches still apply via string replacement)
- Agent crawl: 95 tests still pass

---

## Phase B: Mobile UX Overhaul (Days 3-4)

### B1. Single-Chapter View with Swipe Navigation

**Problem:** Genesis renders 53 chapters in a 325,820px scroll (401 screens). Users can't find content, can't track position, get lost.

**Solution:** Show one chapter at a time on mobile. Swipe left/right or tap arrows to navigate.

```
┌─────────────────────────┐
│ ≡  Old Testament > Gen  │  ← breadcrumb (sticky)
├─────────────────────────┤
│ ◀  Chapter 3 of 53  ▶  │  ← floating chapter nav
├─────────────────────────┤
│                         │
│  GENESIS 1:26–28        │
│  The Imago Dei          │
│                         │
│  [synopsis text]        │
│                         │
│  [scripture block]      │
│                         │
│  [hebrew terms]         │
│                         │
│  [ANE context]          │
│                         │
│  ○ Mark as Read  ☆ Save │
│                         │
├─────────────────────────┤
│  ◀ Previous    Next ▶   │
├─────────────────────────┤
│ 🏠  🔍  ⚙  📖  ★      │  ← bottom nav
└─────────────────────────┘
```

**Implementation:**
- New `renderSingleChapter(textId, chapterIndex)` function
- Chapter index stored in state: `currentChapterIndex`
- Touch swipe detection (touchstart/touchmove/touchend)
- Floating chapter indicator: "Chapter 3 of 53" with left/right arrows
- Sidebar chapter list still works for jump-to navigation
- Era headers shown inline above the first chapter of each era
- Option: "Show All Chapters" toggle at bottom for users who prefer scroll view
- Prev/Next buttons already exist — make them primary navigation

### B2. Dedicated Bookmarks Overlay

**Problem:** "SAVED" bottom nav button opens the sidebar instead of showing bookmarks.

**Solution:** Create a proper full-screen bookmarks overlay (like Glossary).

### B3. Better Search Experience

**Problem:** "SEARCH" opens the sidebar.

**Solution:** Full-screen search overlay with:
- Large search input
- Recent searches
- Results with book/chapter context
- Tap result → navigates to that chapter in single-chapter view

### B4. Auto-Hide Study Controls

**Problem:** Hebrew/ANE/2ndTemple/Council/Xrefs pills always visible, even on library home.

**Solution:** Only show when viewing a text. Hide on library home, tools, overlays.

### B5. Fix Hebrew Toggle

**Problem:** Hebrew filter toggle targets `.terms-section` which doesn't exist in DOM.

**Solution:** Either:
- (a) Wrap `renderTermsGrid()` output in `<div class="terms-section">` so the toggle works
- (b) Remove Hebrew toggle until content exists

Recommendation: (a) — add the wrapper class. The Hebrew terms grid IS rendered, just not wrapped in `.terms-section`.

---

## Phase C: Feature Polish (Days 5-6)

### C1. Truth Matrix Enhancements

Current: 52 religion cards in a grid, click for detail.

**Add:**
- **Summary stats bar**: "12 Full Match | 8 Mostly | 15 Partial | 17 Divergent"
- **Sort options**: By alignment score, alphabetical, by founding date
- **Compare mode**: Select 2-3 religions, see side-by-side doctrine comparison
- **Heatmap view**: Toggle between card view and doctrine heatmap grid
  - Rows = religions, columns = 13 doctrines
  - Color-coded cells (green → red for alignment)
  - Click cell → detail popup

```
                    Trinity  Atonement  Scripture  Afterlife  ...
  ─────────────────────────────────────────────────────────────
  Roman Catholic    ██████   ██████     ██████     ██████
  Eastern Orthodox  ██████   █████░     ██████     █████░
  Islam             ░░░░░░   ░░░░░░     ░░░░░░     █████░
  Buddhism          ░░░░░░   ░░░░░░     ░░░░░░     ░░░░░░
```

### C2. Fix "Prophecy Matrix" Naming

**Action:** Rename Tools popup button from "Prophecy Matrix" to "Truth Matrix" in `build_mobile.py`.

### C3. Add "Selah" to Glossary

**Add to `data/glossary.py`:**
```python
"selah": {
    "term": "Selah",
    "hebrew": "סֶלָה",
    "transliteration": "selah",
    "strongs": "H5542",
    "definition": "A liturgical or musical notation in the Psalms...",
    "usage": "Appears 71 times in Psalms and 3 times in Habakkuk...",
    "theological_significance": "...",
    "related_terms": ["tehillah", "mizmor", "shir"]
}
```

### C4. Auto-Link Glossary Terms in Content

- Scan chapter content for first occurrence of each glossary term
- Wrap in `<span class="glossary-link" data-term="selah">Selah</span>`
- On tap: show inline tooltip with definition, "See full entry" link
- Only first occurrence per chapter (avoid clutter)

### C5. Study Trail Progress

- Track completed trail stops (localStorage)
- Show "3/9 stops completed" on trail cards
- "Continue" vs "Begin" CTA based on progress

---

## Phase D: Build System + Launch Experience (Days 7-8)

### D1. Simplified Launch

**Problem:** LAUNCH.bat has 8 options. Too many for a casual user.

**Create `START.bat`** — single obvious entry point:
```batch
@echo off
echo.
echo  ╔═══════════════════════════════════════╗
echo  ║   Ancient Texts Study App  v4.0       ║
echo  ╠═══════════════════════════════════════╣
echo  ║                                       ║
echo  ║   [1] Open App (Browser)              ║
echo  ║   [2] Open App (Desktop)              ║
echo  ║   [3] Developer Tools                 ║
echo  ║                                       ║
echo  ╚═══════════════════════════════════════╝
echo.
```

Option 3 opens LAUNCH.bat with the full 8 options for developers.

### D2. Build Consolidation

- Ensure `BUILD_ALL.bat` handles all error cases
- Add version bump prompt to DEPLOY.bat
- Add build timestamp to output HTML
- Ensure `release.py` works cleanly with v4.0

### D3. File Organization Cleanup

```
Before:                          After:
├── LAUNCH.bat (8 options)       ├── START.bat (3 options, user-facing)
├── BUILD_ALL.bat                ├── LAUNCH.bat (developer menu, renamed)
├── DEPLOY.bat                   ├── BUILD_ALL.bat (unchanged)
├── build.py                     ├── DEPLOY.bat (unchanged)
├── build_mobile.py              ├── build.py
├── release.py                   ├── build_mobile.py
├── manifest.json                ├── release.py
├── CONTENT_MAP.json             ├── manifest.json
├── VERSION                      ├── CONTENT_MAP.json
├── requirements.txt             ├── VERSION
├── CLAUDE.md                    ├── requirements.txt
├── CHANGELOG.md                 ├── CLAUDE.md
├── STATUS.md                    ├── CHANGELOG.md
├── PROJECT.md                   ├── PROJECT.md (updated)
├── ROADMAP.md (this file)       ├── ROADMAP.md
├── CLAUDE_CONTEXT/              ├── docs/ (consolidated)
├── docs/                        │   ├── STATUS.md
├── agents/                      │   ├── research/
├── hai/                         │   ├── vision/
├── tools/                       │   └── handoffs/
├── tests/                       ├── agents/
├── archive/                     ├── hai/
└── electron/                    ├── tools/
                                 ├── tests/
                                 └── electron/
```

Key changes:
- **`START.bat`** — the ONE file users double-click
- **STATUS.md** → `docs/STATUS.md` (reduce root clutter)
- **CLAUDE_CONTEXT/** — contents merged into `.claude/` memory
- **archive/** — verify empty, remove if so

### D4. Service Worker Improvements

- Add cache versioning tied to build timestamp
- Proper cache invalidation on new deploy
- Offline fallback page
- Update notification ("New version available, tap to refresh")

---

## Phase E: Full QA + Deploy v4.0 (Days 9-10)

### E1. Agent Crawl — Full Suite

Run all 8 crawl suites against both targets:
- Desktop (port 8079): Suites 1-6, 8
- Mobile (port 8080): All 8 suites including Suite 7

**Target: 95/95 PASS (100%)**

Fix any regressions from Phase A-D changes.

### E2. Vision Crawl

Visual/UX audit of every screen:
- Library home (condensed hero, recent texts, trails, categories)
- Single-chapter view (swipe, navigation, action bar)
- All overlays (Glossary, Matrix, Timeline, Map, Hebrew, Progress)
- Interlinear pane
- Search overlay
- Bookmarks overlay

### E3. Performance Audit

- Page load time (target: <3s desktop, <5s mobile)
- Memory usage (target: <100MB after 10 text navigations)
- Search index build time (target: <1s)
- Chapter render time (target: <200ms)

### E4. Version Bump + Release

1. Update `VERSION` to `4.0.0`
2. Update `CHANGELOG.md`
3. Run `BUILD_ALL.bat`
4. Run `release.py --version 4.0.0`
5. Test release package (PC + Mobile folders)
6. `DEPLOY.bat` — push to main + deploy gh-pages
7. Verify live at https://seaverhall10.github.io/ancient-texts-app/

### E5. Update Documentation

- Update `PROJECT.md` with new module structure
- Update `CLAUDE.md` with new patterns
- Update memory files for future sessions

---

## Quick Wins (Can Do Anytime)

These are small fixes that can be done in any session:

- [ ] Add "Selah" to glossary.py
- [ ] Rename "Prophecy Matrix" → "Truth Matrix" in tools popup
- [ ] Wrap Hebrew terms grid in `.terms-section` class
- [ ] Hide study controls bar on library home page
- [ ] Add scroll progress indicator on mobile
- [ ] Fix ayin (ע) button discoverability (add tooltip)

---

## What NOT to Change

- **Data module pattern** — Python files with `CHAPTERS`, `FLOW_*`, `INTERLINEAR_*` exports work well
- **CSS component architecture** — 39 files + build-order.txt is clean
- **Agent system** — 5-agent council pipeline is solid
- **Build profiles** — sons-of-god, canon-only, etc. stay
- **Theological stance** — divine council, Deut 32:8 DSS/LXX, Gen 6 supernatural view
- **Desktop single-HTML** — 65MB monolith is the correct architecture for offline use
- **Mobile on-demand loading** — shell + JSON chunks is the right pattern

---

## Success Criteria for v4.0

1. **User opens `START.bat` → app launches in 2 clicks**
2. **Mobile: single-chapter view with swipe navigation**
3. **Mobile: 95/95 crawl tests pass**
4. **JS split into ~20 modules** (no more 6,800-line monolith)
5. **All overlays work on mobile** (Matrix detail, Glossary, Timeline, etc.)
6. **Reading progress visible** (chapter counts, progress bars, trails)
7. **Search works on mobile** (index rebuilds after data load)
8. **Truth Matrix has heatmap view** option
9. **Zero console errors** on both targets
10. **Clean git history** — each phase is one commit

---

## Session Instructions

Each Claude session should:
1. Read `ROADMAP.md` (this file) first
2. Check which phase is current
3. Read `CLAUDE.md` + memory files for context
4. Work on the current phase
5. Run agent crawl after changes
6. Commit with descriptive message
7. Update this file's checkboxes

**Current Phase:** A (JS Module Split)
**Last Completed:** Pre-v4.0 UX improvements (commit 4aadf34)
