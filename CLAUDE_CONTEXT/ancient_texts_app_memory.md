# Ancient Texts Study App — Project Memory
*Updated: March 12, 2026 (Session 4)*

## Location
- **Working dir**: `C:\Users\User\Desktop\ANCIENT_TEXTS Study App\`
- **Google Drive**: `G:\My Drive\ANCIENT_TEXTS Study App\` (OUTDATED as of March 7 — needs full sync)
- **Sync**: `LAUNCH.bat → option 6` or `SYNC.bat`

## What It Is
Two-version study app for deep scripture research with original languages:
- **PC Version**: Single 65.5 MB HTML file (release without HAI)
- **Mobile Version**: Progressive Web App (0.7 MB shell + on-demand data, ~102 MB total)
- **77 texts**: 39 OT + 27 NT + 5 DSS/Second Temple + 1 Pseudepigrapha + 1 Historical + 4 Thematic
- **230 eras**, **978 study chapters**, **444,339 interlinear words**, 567 glossary terms
- **31,101 flow verses** across all 66 biblical books (0 gaps)
- **6,863 cross-references**
- Dark gold-accent design (#0c0e14 bg, #c9a84c gold)
- Current version: **3.3.0**

## Build System
| Command | What it does |
|---------|-------------|
| `python build.py` | Desktop dev build (with HAI) → `output/AncientTextsStudy.html` |
| `python build.py --release` | Release build (no HAI) → `output/AncientTextsStudy-Release.html` |
| `python build_mobile.py` | Mobile PWA → `output/mobile/` (needs release build first) |
| `BUILD_ALL.bat` | One-click: desktop → release → mobile |
| `python release.py` | Package versioned ZIP with `PC/` + `Mobile/` folders |
| `LAUNCH.bat` | Main menu (8 options: browser, Electron, AI, build, build all, sync, council, exit) |
| `DEPLOY.bat` | **One-click**: build all → commit → push main → deploy gh-pages |

Build order: `build.py` → `build.py --release` → `build_mobile.py`

## GitHub Deployment
- **Repo**: `Seaverhall10/ancient-texts-app`
- **main branch**: Source code (Python data, JS, CSS, build scripts)
- **gh-pages branch**: Mobile PWA only (deployed from `output/mobile/`)
- **Live URL**: https://seaverhall10.github.io/ancient-texts-app/
- **Deploy method**: `DEPLOY.bat` (or manually: temp dir → `git init` → copy `output/mobile/*` → orphan push)
- **NEVER** use `git subtree` or `git checkout --orphan` in the working directory — it will try to add ALL files
- **ALWAYS** deploy gh-pages from a temp directory to avoid polluting the source tree

## Mobile PWA Architecture
- `build_mobile.py` generates `output/mobile/` from the release HTML
- Splits data into per-text JSON chunks: `data/eras/{book}.json`, `data/interlinear/{book}.json`
- App shell is ~0.7 MB, data loads per-text on demand
- Service worker: network-first for data, cache-first for shell
- **Critical**: data loader must be INSIDE the existing IIFE (not wrapped in outer)
- **Critical**: `texts` and `categories` re-populated in `mobileBootstrap()` after loading MANIFEST
- **All 6 tool buttons verified working**: Timeline, Map, Matrix, Prophecy, Hebrew, Glossary
- `LAUNCH-MOBILE.bat` auto-detects local IP for phone access via `ipconfig`

## Hallelujah AI (HAI) — Local Ollama
- Base model: Qwen 2.5 7B (`Modelfile` → `ollama create hallelujah -f Modelfile`)
- Server: `app.py` (FastAPI + pywebview on port 8741)
- Prompt builder: `pipeline/bible_bound.py` (compact ~3K + full ~10K chars)
- **Linguistics baked into ALL modes by default** — not a separate selectable mode
  - Pictographic/Proto-Sinaitic Hebrew, gematria, theophoric elements
  - Root families, name change theology, number symbolism
  - Adam→Noah genealogy gospel
  - Reference data in `policy/linguistics.yaml`
- 4 modes: General, Bible Study, Berean, Dev
- Only in dev build (stripped from release + mobile)

## Release System (`release.py`)
- Packages into `releases/AncientTextsStudy-vX.Y.Z/`:
  - `PC/` — AncientTextsStudy.html + LAUNCH.bat + LAUNCH.command
  - `Mobile/` — PWA files + LAUNCH-MOBILE.bat + LAUNCH-MOBILE.command
  - README.txt (documents both versions), CHANGELOG.txt, FEEDBACK.txt, VERSION.txt
- ZIP archive: ~40 MB compressed
- Commands: `python release.py`, `--version X.Y.Z`, `--skip-build`

## What's Complete
- All 39 OT: info + eras + flow + Hebrew interlinear (OSHB)
- All 27 NT: flow + Greek interlinear + eras
- 8 Apocryphal: eras only
- 4 Thematic deep dives: Nephilim & Giants, Messianic Thread, Heavenly Court, **Jesus & the Gentiles** (9 chapters)
- Full-text search, cross-ref navigation, reading progress, bookmarks
- **Bible Truth Matrix** — 52+ religions, sorted by alignment, % scores (color-coded)
- Timeline, Study Trails (6 trails), Analytics, Map, Learn Hebrew
- Electron desktop app with Windows installer
- CSS design system (45 component files), responsive breakpoints, keyboard shortcuts
- **Mobile bottom nav**: Home | Search | Tools | Glossary | Saved
- **Mobile tools**: All 6 buttons working (Prophecy async patched)
- Reading Mode Toggle (Scripture / Study / Interlinear)
- Firebase Auth + Cloud Sync (Firestore)
- Cross-reference preview tooltips
- Study Notes Markdown export
- Hidden Treasures Discovery feature

## What's Missing
1. **Minor Prophets depth** — 12 books at 25-40% of Genesis depth
2. **NT era expansion** — Matthew/Luke/John/Acts only 2 eras each
3. **DSS/1 Enoch/Jasher hebrew_terms** — many chapters at 0%
4. **Study Trail conversions** — Covenant Arc, Adam-to-Jesus, Cosmic Geography, DSS Connection still old format
5. **YouTube/resource links** — video sources throughout
6. **PDF export** — Markdown done, PDF needed
7. **Apocryphal flow translations** — none
8. **JS module split** (Phase 2) — 7,907-line app.js

## Key Technical Patterns
- **Flow files**: `data/flow/flow_{book_id}.py` → exports `FLOW_{BOOK}` + `NOTES_{BOOK}` dicts
- **Build filter**: `flow_file.count("_") == 1` — only loads combined files
- **NT interlinear fallback**: build.py checks `INTERLINEAR_NT_{BOOK}` after `INTERLINEAR_{BOOK}`
- **Era files**: `data/{text_id}/era_*.py` → exports `CHAPTERS` list
- **Era chapter format**: Each chapter dict MUST have: `id`, `ref`, `chapter_num`, `title` (NOT `heading`!), `era`, `type`, `synopsis`, `key_verse` (object with ref/text/translation), `hebrew_terms` (array of objects), `ane_backdrop` (string), `second_temple` (array of objects with source/summary/relevance), `cross_refs` (array of objects with ref/note/type), `divine_council_note` (string or None), `sections` (array of objects with **heading**/body)
- **1 Enoch**: manifest `data_dir: "enoch1"` → files in `data/enoch1/`
- **Genesis interlinear**: `data/genesis/interlinear.py` (subdirectory)
- **Religions data**: `data/religions_data.py` → `RELIGIONS_DETAIL` dict (52 religions × 13 doctrines)
- **Mobile tool overlays**: z-index 110 on mobile (sidebar is 100, bottom nav is 9999)
- **Mobile async data loading**: Functions that render mobile data MUST be `async` with `await loadX()` before accessing data that starts as `{}`

## Builder's Council (5 Agents)
1. ORACLE — planning  2. SCRIBE — content  3. ARBITER — theology
4. LECTOR — languages  5. ARCHITECT — infrastructure
Keys in `agents/config.py`. Runner: `python agents/run_council.py`

## Lessons Learned
1. NEVER use robocopy /MIR in Git Bash — use PowerShell
2. NEVER create flow partials without combining after
3. NEVER ignore `data_dir` in manifest (1 Enoch = `data/enoch1/`)
4. Build filter: `flow_file.count("_") == 1`
5. Preview tools CANNOT handle 67 MB HTML — test in real browser
6. `key_verse` can be None — use `(ch.get('key_verse') or {}).get('ref', '')`
7. Mobile IIFE scope: inject code inside existing IIFE, not wrap in new one
8. Mobile bootstrap: must re-assign `texts` and `categories` after MANIFEST loads
9. **gh-pages deploy**: ALWAYS use a temp directory. NEVER `git checkout --orphan` in the working tree
10. **Overlay z-index on mobile**: Sidebar is z-index 100, overlay was 40 → fixed to 110
11. **const → var on mobile**: `const` interlinear vars can't be reassigned by `eval()` in mobile data loader
12. **CRITICAL: build_mobile.py must replace ALL placeholders from app.js** — any `__*_DATA__` left unreplaced causes ReferenceError that kills the entire IIFE silently
13. **Debugging mobile IIFE crashes**: Console won't show errors from IIFE-time ReferenceErrors. Fix: inject `<script>` tag BEFORE main script with `window.addEventListener('error', ...)`
14. **Service worker cache busting**: Cache name must include build timestamp, not just version string
15. **After adding ANY new data placeholder**: MUST update BOTH `build.py` AND `build_mobile.py`
16. **Era file chapter title**: Use `"title"` key at chapter level, `"heading"` key at section level. Mixing them up causes "undefined" rendering.
17. **Mobile async pattern**: Any function rendering data that starts as `{}` on mobile must be patched to `async` with `await loadX()` in build_mobile.py. Example: `showProphecyMatrix()` → `async function showProphecyMatrix() { await loadProphecy(); ... }`
18. **cross_refs format**: Must be array of objects `[{ref, note, type}]` — NOT plain strings
19. **second_temple format**: Must be array of objects `[{source, summary, relevance}]` — NOT plain string

## Protocol: Making Changes
1. Edit source files in `src/js/app.js`, `src/css/*.css`, `data/`, `build.py`, `build_mobile.py`
2. Run `python build.py` to test desktop
3. Run `python build.py --release && python build_mobile.py` to build mobile
4. Commit: `git add <specific files> && git commit -m "message"`
5. Push: `git push origin main`
6. Deploy mobile: use `DEPLOY.bat` or manual temp-dir method
7. **NEVER** `git add -A` or `git add .` — always add specific files
8. **NEVER** modify git config or use `--force` on main
9. Keep `.gitignore` updated when adding new file types

## Theological Stance (NON-NEGOTIABLE)
- Christ IS the promised Messiah and King
- Divine council = real heavenly administration (Ps 82, Deut 32:8-9)
- Gen 6:1-4 = divine/angelic beings (NOT Sethite view)
- Deut 32:8 = DSS/LXX "sons of God" (NOT MT "sons of Israel")
- Non-canonical: "According to 1 Enoch..." NEVER "the Bible says..."
- Evidence tiers: [A] Direct Scripture / [B] Valid inference / [C] Ancient parallels
