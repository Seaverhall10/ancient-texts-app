# Ancient Texts Study App — Current Status
*Last updated: 2026-03-12*

---

## WHAT IS COMPLETE

### Core App — Two Versions
- [x] **PC Version**: Single-file HTML app (`build.py → output/AncientTextsStudy.html`, ~68 MB dev / ~65 MB release)
- [x] **Mobile Version**: Progressive Web App (`build_mobile.py → output/mobile/`, 0.7 MB shell + on-demand data)
- [x] Both versions contain identical content (74 texts, all interlinear, all features)
- [x] **Electron desktop app** (Windows installer, `electron/` folder)
- [x] Release system packages both into `PC/` + `Mobile/` folders with launchers

### Build & Release System
- [x] `BUILD_ALL.bat` — one-click build of desktop + release + mobile
- [x] `LAUNCH.bat` — 8-option menu (browser, Electron, AI, build, build all, sync, council, exit)
- [x] `release.py` — versioned ZIP packaging with `PC/` and `Mobile/` folders
- [x] `LAUNCH-MOBILE.bat` — auto-detects local IP, starts server for phone access
- [x] Current version: **3.3.0**
- [x] Release ZIP: ~40 MB (includes both PC + Mobile)

### Content (74 texts total)
- [x] **74 texts** in manifest (39 OT + 27 NT + 8 Apocryphal/Second Temple)
- [x] **206 eras** (study chapter groupings)
- [x] **955 study chapters** across all texts
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
- [x] Bible Truth Matrix — 52 worldviews × 13 doctrines, heatmap
- [x] Biblical + World History Timeline — 91 events, 8 eras
- [x] Study Trails — 6 curated paths (Divine Council, Messianic, Nephilim, Covenant, Adam-to-Jesus, Cosmic Geography)
- [x] **Hidden Treasures Discovery** — 8 lesser-known texts surfaced in Library (War Scroll, 1 Enoch, Book of Giants, etc.)
- [x] Ancient World Map — 60+ overlays, CartoDB labels, ESRI borders/roads
- [x] Learn Hebrew module (Aleph-Bet, vowels, roots, practice)
- [x] **Study Notes Export** — Markdown download per chapter
- [x] Usage Analytics — localStorage logging, JSON export, 5K cap
- [x] Reverse cross-references, bookmarks, breadcrumbs, prev/next nav
- [x] CSS design system (tokens, 42 component files, 6-tier responsive breakpoints, clamp())
- [x] Resizable 3-column layout with keyboard shortcuts

### Apocryphal / Second Temple Texts (eras only, no flow/interlinear)
1 Enoch, Book of Giants, Jubilees, Jasher, Genesis Apocryphon,
DSS Sectarian, Josephus, Heavenly Court

---

## WHAT IS MISSING

### TIER 1 — Content Enrichment
1. **NT Era Depth (remaining)** — 4 single-chapter books have 1 era (2 John, 3 John, Philemon, Jude) — appropriate for their length; 17 other thin-era texts still need depth
2. **Apocryphal Flow Translations** — none of the 8 non-canonical texts have verse-level translations

### TIER 2 — Features
3. **YouTube / Resource Links** — video sources embedded throughout study content
4. **PDF Export** — export study content as formatted PDF (Markdown export already done)

---

## APP STATISTICS (v3.3.0)

| Metric | Value |
|--------|-------|
| Total texts | **74** |
| Total eras | **206** |
| Study chapters | **955** |
| Flow translations | **66/74 texts** (all 39 OT + all 27 NT) |
| Flow verses | **31,101** |
| Interlinear words (OT) | **306,506** |
| Interlinear words (NT) | **137,833** |
| **Total interlinear** | **444,339** |
| Cross-references | **6,392** |
| Unique passages cited | **3,992** |
| Glossary terms | **556** |
| Build output (dev) | ~68 MB HTML |
| Build output (release) | ~65 MB HTML |
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
- 42 CSS component files (added reading-modes.css, hidden-treasures.css)

---

## KEY FILES

| File | Purpose |
|------|---------|
| `build.py` | Build desktop app — run after any change |
| `build.py --release` | Build release version (no HAI) |
| `build_mobile.py` | Build mobile PWA (requires release build) |
| `BUILD_ALL.bat` | One-click: desktop → release → mobile |
| `LAUNCH.bat` | Main menu launcher (8 options) |
| `release.py` | Package versioned release ZIP (PC + Mobile) |
| `manifest.json` | Master text/era registry |
| `CONTENT_MAP.json` | AI navigation index (auto-built) |
| `pipeline/bible_bound.py` | HAI system prompt builder |
| `policy/linguistics.yaml` | Ancient linguistics reference data |
| `Modelfile` | Ollama model configuration |
| `app.py` | HAI server (FastAPI + pywebview) |
| `data/generate_ot_flow.py` | OT flow generator (Claude Sonnet API) |
| `data/generate_nt_flow.py` | NT flow generator (Claude API) |
| `VERSION` | Current version (3.3.0) |
| `STATUS.md` | THIS FILE |
