# Ancient Texts Study App — Current Status
*Last updated: 2026-03-12 (Session 4)*

---

## WHAT IS COMPLETE

### Core App — Two Versions
- [x] **PC Version**: Single-file HTML app (`build.py → output/AncientTextsStudy.html`, ~68 MB dev / ~65.5 MB release)
- [x] **Mobile Version**: Progressive Web App (`build_mobile.py → output/mobile/`, 0.7 MB shell + on-demand data)
- [x] Both versions contain identical content (77 texts, all interlinear, all features)
- [x] **Electron desktop app** (Windows installer, `electron/` folder)
- [x] Release system packages both into `PC/` + `Mobile/` folders with launchers

### Build & Release System
- [x] `BUILD_ALL.bat` — one-click build of desktop + release + mobile
- [x] `LAUNCH.bat` — 8-option menu (browser, Electron, AI, build, build all, sync, council, exit)
- [x] `release.py` — versioned ZIP packaging with `PC/` and `Mobile/` folders
- [x] `LAUNCH-MOBILE.bat` — auto-detects local IP, starts server for phone access
- [x] `DEPLOY.bat` — one-click build all + commit + push + deploy gh-pages
- [x] Current version: **3.3.0**
- [x] Release ZIP: ~40 MB (includes both PC + Mobile)

### Content (77 texts total)
- [x] **77 texts** in manifest (39 OT + 27 NT + 5 DSS/Second Temple + 1 Pseudepigrapha + 1 Historical + 4 Thematic)
- [x] **230 eras** (study chapter groupings)
- [x] **978 study chapters** across all texts
- [x] CONTENT_MAP.json — master AI navigation index (auto-rebuilt on every build)

### Flow Translations (verse-by-verse English prose)
**ALL 66 biblical books have flow translations — 31,101 total verses.**

**OT — all 39 books complete** | **NT — all 27 books complete**

### Interlinear Data (click any word → original language popup)
- [x] **ALL 39 OT books** — 306,506 Hebrew words (from OSHB, CC BY 4.0)
- [x] **ALL 27 NT books** — 137,833 Greek words
- [x] **GRAND TOTAL: 444,339 interlinear words across 66 biblical books**

### Hallelujah AI (Local Ollama Chat)
- [x] Qwen 2.5 7B base model, custom `Modelfile`
- [x] Full prompt builder (`pipeline/bible_bound.py`) — compact + expanded modes
- [x] **Ancient linguistics baked into ALL modes by default** (not a separate mode)
  - Pictographic/Proto-Sinaitic Hebrew letter meanings
  - Gematria (Hebrew/Greek numerical values)
  - Theophoric name elements (El, Yah, YHWH, Baal)
  - Root family analysis (ישע, שלם, קדש, ברך, אמן)
  - Name change theology, number symbolism
  - Adam→Noah genealogy gospel
- [x] Policy files: `policy/linguistics.yaml`, `policy/bible_bound.yaml`, `policy/security.yaml`
- [x] 4 modes: General, Bible Study, Berean, Dev
- [x] Included in dev build only (stripped from release/mobile)
- [x] RAG context from app study data

### App Features
- [x] Full-text search across era content + 31,101 flow verses
- [x] Cross-reference navigation — "→ Go" links for biblical refs
- [x] **Cross-reference preview tooltips** — hover/tap to see connection note without navigating
- [x] Reading progress tracker — per-chapter checkboxes, localStorage
- [x] **Reading Mode Toggle** — Scripture / Study / Interlinear per chapter (CSS-driven)
- [x] **Firebase Auth + Cloud Sync** — email/password login, Firestore cloud sync
- [x] **Bible Truth Matrix** — 52 worldviews × 13 doctrines, heatmap, **sorted by alignment** with % scores
- [x] Biblical + World History Timeline — 91 events, 8 eras
- [x] Study Trails — 6 curated paths (Divine Council, Messianic, Nephilim, Covenant, Adam-to-Jesus, Cosmic Geography)
- [x] **Hidden Treasures Discovery** — 8 lesser-known texts surfaced in Library
- [x] Ancient World Map — 60+ overlays, CartoDB labels, ESRI borders/roads
- [x] Learn Hebrew module (Aleph-Bet, vowels, roots, practice)
- [x] **Study Notes Export** — Markdown download per chapter
- [x] **Prophecy Matrix** — 59 prophecies with fulfillment tracking
- [x] Usage Analytics — localStorage logging, JSON export, 5K cap
- [x] Reverse cross-references, bookmarks, breadcrumbs, prev/next nav
- [x] CSS design system (tokens, 45 component files, 6-tier responsive breakpoints, clamp())
- [x] Resizable 3-column layout with keyboard shortcuts
- [x] **All 6 mobile Study Tool buttons verified working** (Timeline, Map, Matrix, Prophecy, Hebrew, Glossary)

### Thematic Deep Dives
- [x] **Nephilim & Giants** — multi-era study
- [x] **Messianic Thread** — prophecy-to-fulfillment trail
- [x] **Heavenly Court** — divine council deep dive
- [x] **Jesus & the Gentiles** — 9 chapters: parables, wedding invitation theme, faith vs. theology (NEW)

### Apocryphal / Second Temple Texts (eras only, no flow/interlinear)
1 Enoch, Book of Giants, Jubilees, Jasher, Genesis Apocryphon,
DSS Sectarian, Josephus, Heavenly Court

---

## WHAT IS MISSING

### TIER 1 — Content Depth (Major Gaps)
1. **Minor Prophets section depth** — All 12 books at 25-40% of Genesis depth (51/55 chapters flagged)
2. **NT era expansion** — Matthew, Luke, John, Acts have only 2 eras each (thin for 20-28 chapter books)
3. **DSS Sectarian hebrew_terms** — 26 chapters at 0% coverage
4. **1 Enoch hebrew_terms** — 55/73 chapters empty (75%)
5. **Jasher hebrew_terms** — 43/49 chapters empty (88%)

### TIER 2 — Study Trail Conversions
6. **Covenant Arc** — still old step-by-step format, needs article conversion
7. **Adam to Jesus** — still old step-by-step format
8. **Cosmic Geography** — still old step-by-step format
9. **Dead Sea Scrolls Connection** — still old step-by-step format

### TIER 3 — Features
10. **YouTube / Resource Links** — video sources embedded throughout study content
11. **PDF Export** — export study content as formatted PDF (Markdown export already done)

### TIER 4 — Architecture (Restructuring Plan)
12. **Phase 2**: JS module split (~25 files from 7,907-line app.js)
13. **Phase 3**: Build consolidation + data registry
14. **Phase 4**: Testing + CI/CD

### TIER 5 — Content (Nice to Have)
15. **Apocryphal flow translations** — none of the 8 non-canonical texts have verse-level translations
16. **Psalms, Isaiah, Jeremiah, Ezekiel** — large books with relatively few eras compared to chapter count

---

## APP STATISTICS (v3.3.0)

| Metric | Value |
|--------|-------|
| Total texts | **77** |
| Total eras | **230** |
| Study chapters | **978** |
| Flow translations | **66/77 texts** (all 39 OT + all 27 NT) |
| Flow verses | **31,101** |
| Interlinear words (OT) | **306,506** |
| Interlinear words (NT) | **137,833** |
| **Total interlinear** | **444,339** |
| Cross-references | **6,863** |
| Glossary terms | **567** |
| Religions in Truth Matrix | **52** |
| CSS component files | **45** |
| app.js lines | **7,907** |
| Build output (dev) | ~68 MB HTML |
| Build output (release) | ~65.5 MB HTML |
| Mobile shell | ~0.7 MB |
| Release ZIP | ~40 MB (PC + Mobile) |
| Current version | **3.3.0** |

---

## RECENT CHANGES (2026-03-12)

### Session 1 — Firebase + NT Depth + Reading Modes
- Firebase Auth with email/password login and Firestore cloud sync
- Reading Mode Toggle: Scripture / Study / Interlinear per chapter
- 14 new NT era files (42 study chapters across 11 books)

### Session 2 — Features + More NT Depth
- 6 more NT era files (18 study chapters): 1 John, 1 Timothy, 2 Peter, 2 Thessalonians, 2 Timothy, Titus
- Hidden Treasures Discovery feature (8 lesser-known texts in Library)
- Cross-reference preview tooltips (hover to see connection notes)
- Study notes Markdown export (download per chapter)
- 45 CSS component files

### Session 3 — DSS Text Grouping, Study Notes, Study Trails inline scripture
- DSS texts grouped into thematic category in sidebar
- Study Notes system with cloud sync
- Study Trails updated with inline scripture rendering

### Session 4 — Mobile Fixes, Truth Matrix Sort, Jesus & the Gentiles
- Fixed all 6 mobile Study Tool buttons (Prophecy async loading, correct function names)
- Truth Matrix sorted by alignment — most aligned first + overall % scores (color-coded)
- **"Jesus & the Gentiles" deep dive** — 9 chapters across 3 eras:
  - Part I: Why Did Jesus Speak in Parables? (Matt 13, Gentile faith, Pharisee blindness)
  - Part II: The Wedding Invitation (Wisdom's feast, wedding banquet parables, ten virgins)
  - Part III: Simple Faith vs. Theological Steps (Sermon on Mount, thief on cross, apostolic theology)
- Full biblical accuracy verification of all 9 chapters
- Fixed Chapter 4 title key bug (`heading` → `title`)
- Commits: cd97133, 946bc85, 35423ec, bdfb1ed

---

## KEY FILES

| File | Purpose |
|------|---------|
| `build.py` | Build desktop app — run after any change |
| `build.py --release` | Build release version (no HAI) |
| `build_mobile.py` | Build mobile PWA (requires release build) |
| `BUILD_ALL.bat` | One-click: desktop → release → mobile |
| `DEPLOY.bat` | One-click: build all → commit → push → deploy gh-pages |
| `LAUNCH.bat` | Main menu launcher (8 options) |
| `release.py` | Package versioned release ZIP (PC + Mobile) |
| `manifest.json` | Master text/era registry (77 texts, 230 eras) |
| `CONTENT_MAP.json` | AI navigation index (auto-built) |
| `pipeline/bible_bound.py` | HAI system prompt builder |
| `policy/linguistics.yaml` | Ancient linguistics reference data |
| `Modelfile` | Ollama model configuration |
| `app.py` | HAI server (FastAPI + pywebview) |
| `data/generate_ot_flow.py` | OT flow generator (Claude Sonnet API) |
| `data/generate_nt_flow.py` | NT flow generator (Claude API) |
| `VERSION` | Current version (3.3.0) |
| `STATUS.md` | THIS FILE |
