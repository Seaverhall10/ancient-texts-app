# Ancient Texts Study App — Project Memory
*Updated: March 7, 2026*

## Location
- **Working dir**: `C:\Users\User\Desktop\ANCIENT_TEXTS Study App\`
- **Google Drive**: `E:\My Drive\ANCIENT_TEXTS Study App\`
- **Sync**: `LAUNCH.bat → option 6` or `SYNC.bat`

## What It Is
Two-version study app for deep scripture research with original languages:
- **PC Version**: Single 67 MB HTML file (dev) / 64 MB (release without HAI)
- **Mobile Version**: Progressive Web App (0.6 MB shell + on-demand data, ~102 MB total)
- **74 texts**: 39 OT + 27 NT + 8 Apocryphal/Second Temple
- **186 eras**, **895 study chapters**, **444,339 interlinear words**, 553 glossary terms
- **31,101 flow verses** across all 66 biblical books (0 gaps)
- **5,932 cross-references**, 3,843 unique passages cited
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

Build order: `build.py` → `build.py --release` → `build_mobile.py`

## Mobile PWA Architecture
- `build_mobile.py` generates `output/mobile/` from the release HTML
- Splits data into per-text JSON chunks: `data/eras/{book}.json`, `data/interlinear/{book}.json`
- App shell is ~0.6 MB, data loads per-text on demand
- Service worker: network-first for data, cache-first for shell
- **Critical**: data loader must be INSIDE the existing IIFE (not wrapped in outer)
- **Critical**: `texts` and `categories` re-populated in `mobileBootstrap()` after loading MANIFEST
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
- Full-text search, cross-ref navigation, reading progress, bookmarks
- Bible Truth Matrix, Timeline, Study Trails, Analytics, Map, Learn Hebrew
- Electron desktop app with Windows installer
- CSS design system, responsive breakpoints, keyboard shortcuts

## What's Missing
1. **NT era depth** — 38 texts with <2 eras (most NT books have only 1)
2. **Apocryphal flow translations** — none
3. **Export** — study notes as PDF/Markdown
4. **YouTube/resource links** — video sources throughout

## Key Technical Patterns
- **Flow files**: `data/flow/flow_{book_id}.py` → exports `FLOW_{BOOK}` + `NOTES_{BOOK}` dicts
- **Build filter**: `flow_file.count("_") == 1` — only loads combined files
- **NT interlinear fallback**: build.py checks `INTERLINEAR_NT_{BOOK}` after `INTERLINEAR_{BOOK}`
- **Era files**: `data/{text_id}/era_*.py` → exports `CHAPTERS` list
- **1 Enoch**: manifest `data_dir: "enoch1"` → files in `data/enoch1/`
- **Genesis interlinear**: `data/genesis/interlinear.py` (subdirectory)
- **OT flow generator**: `data/generate_ot_flow.py` (Claude Sonnet, formal equivalence)

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

## Theological Stance (NON-NEGOTIABLE)
- Christ IS the promised Messiah and King
- Divine council = real heavenly administration (Ps 82, Deut 32:8-9)
- Gen 6:1-4 = divine/angelic beings (NOT Sethite view)
- Deut 32:8 = DSS/LXX "sons of God" (NOT MT "sons of Israel")
- Non-canonical: "According to 1 Enoch..." NEVER "the Bible says..."
- Evidence tiers: [A] Direct Scripture / [B] Valid inference / [C] Ancient parallels
