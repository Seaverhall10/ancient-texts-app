# Ancient Texts Study App — Project Manifest

**Version:** 3.3.0
**Author:** Seaver Hall
**Repository:** https://github.com/Seaverhall10/ancient-texts-app
**Live (Mobile):** https://seaverhall10.github.io/ancient-texts-app/

---

## What This Is

A deep scripture study application with original-language interlinear, cross-references, divine council theology, and Second Temple Jewish context. Built as a single-page app from Python data files.

**By the numbers:**
- 74 texts (39 OT + 27 NT + 8 Apocryphal/Second Temple)
- 186 study eras, 895 chapters
- 444,339 interlinear words (Hebrew + Greek)
- 31,101 flow verse translations
- 5,932 cross-references
- 553 glossary terms
- 52+ world religions in Bible Truth Matrix

**Two build targets:**
- **Desktop** — single 65 MB HTML file (everything embedded)
- **Mobile PWA** — 0.6 MB app shell + on-demand data (~102 MB total)

---

## Directory Structure

```
ANCIENT_TEXTS Study App/
│
├── build.py                 # Desktop build (dev + release)
├── build_mobile.py          # Mobile PWA build
├── release.py               # Package releases (PC + Mobile ZIP)
├── manifest.json            # Master text manifest (74 texts, eras, metadata)
├── CONTENT_MAP.json         # Auto-generated content index (cross-refs, gaps)
├── requirements.txt         # Python dependencies
├── VERSION                  # Semver version string
│
├── LAUNCH.bat               # One-click launcher (build, run, HAI, council)
├── BUILD_ALL.bat             # Build all targets (desktop + release + mobile)
├── DEPLOY.bat                # Build + commit + push + deploy gh-pages
│
├── CLAUDE.md                # Claude Code session instructions
├── CHANGELOG.md             # Version history
├── STATUS.md                # Current project status & priorities
├── .gitignore               # Git exclusions
│
├── src/                     # ── SOURCE CODE ──────────────────────────
│   ├── css/                 # Component CSS files (39 files)
│   │   ├── build-order.txt  #   Concatenation order for build
│   │   ├── _tokens.css      #   Design tokens (:root custom properties)
│   │   ├── _reset.css       #   CSS reset + base typography
│   │   ├── layout.css       #   App container grid
│   │   ├── sidebar.css      #   Sidebar navigation
│   │   ├── main-content.css #   Era headers, chapter cards
│   │   ├── interlinear.css  #   Reading pane, word cards, grammar colors
│   │   ├── library.css      #   Library grid, text cards, badges
│   │   ├── mobile.css       #   Mobile PWA overrides + bottom nav
│   │   ├── ...              #   (35 more component files)
│   │   └── styles.css       #   Legacy monolith (fallback only)
│   │
│   └── js/                  # JavaScript source
│       ├── app.js           #   Main application (6,677 lines — Phase 2 split)
│       └── state.js         #   State management module (ready for Phase 2)
│
├── data/                    # ── CONTENT DATA ─────────────────────────
│   ├── *.py                 #   Top-level shared era files (Genesis eras 1-16)
│   ├── generate_nt_flow.py  #   NT flow translation generator
│   ├── build_interlinear.py #   OT interlinear builder
│   ├── build_nt_interlinear.py # NT interlinear builder
│   ├── core_beliefs.py      #   Core beliefs data
│   │
│   ├── genesis/             #   Per-text folders (76 total):
│   │   ├── info.py          #     Text metadata
│   │   ├── era_*.py         #     Study eras (thematic chapters)
│   │   ├── interlinear.py   #     Hebrew/Greek interlinear data
│   │   └── flow.py          #     Verse-by-verse flow translations
│   ├── exodus/              #   Same pattern for all 74 texts
│   ├── ...                  #   (+ enoch1, jubilees, jasher, etc.)
│   └── flow/                #   Combined flow files (one per book)
│       └── flow_*.py        #     e.g. flow_genesis.py, flow_romans.py
│
├── agents/                  # ── BUILDER'S COUNCIL (5 AI Agents) ──────
│   ├── oracle.py            #   Planning & priorities
│   ├── scribe.py            #   Content generation
│   ├── arbiter.py           #   Theological accuracy
│   ├── lector.py            #   Language, glossary, interlinear
│   ├── architect.py         #   Build & infrastructure
│   ├── reader.py            #   QA & testing agent
│   ├── run_council.py       #   Full council pipeline runner
│   ├── run_trinity.py       #   Quick 3-agent run
│   ├── build_content_map.py #   CONTENT_MAP.json generator
│   ├── config.py            #   API keys (gitignored)
│   ├── reports/             #   Generated audit reports (gitignored)
│   └── tasks/               #   Task queue (pending/in_progress/completed)
│
├── hai/                     # ── HALLELUJAH AI (Dev-only Chat) ────────
│   ├── app.py               #   PyWebView launcher
│   ├── Modelfile            #   Ollama model definition
│   ├── HALLELUJAH_AI_*.md   #   Vision, protocols, constitution, intel
│   ├── ui/                  #   Chat & launcher HTML/CSS/JS
│   ├── pipeline/            #   Prompt builder (bible_bound.py)
│   ├── server/              #   FastAPI backend + RAG
│   │   ├── main.py          #     API server
│   │   ├── config.py        #     Server config
│   │   ├── providers/       #     Ollama/LlamaCPP providers
│   │   └── rag/             #     RAG indexer + search
│   ├── policy/              #   YAML policy files (boundaries, security)
│   └── tests/               #   HAI-specific tests
│
├── electron/                # ── DESKTOP APP (Electron) ───────────────
│   ├── main.js              #   Electron main process
│   ├── package.json         #   Electron dependencies
│   └── ...                  #   Electron config files
│
├── docs/                    # ── DOCUMENTATION & REFERENCE ────────────
│   ├── WHATS_LEFT.md        #   Remaining work backlog
│   ├── SETUP.md             #   Developer setup guide
│   ├── personal_INDEX.md    #   Personal reference index
│   ├── vision/              #   Design documents
│   │   └── CORE_BELIEFS_DESIGN.md
│   ├── research/            #   Theological research notes
│   │   ├── 01_three_rebellions.md
│   │   ├── 02_nephilim_taxonomy.md
│   │   ├── 03_nt_passages.md
│   │   ├── 04_theodicy_already_not_yet.md
│   │   ├── 05_ot_deep_dives.md
│   │   ├── 06_cosmic_prophecies.md
│   │   └── grok-map/        #   Ancient World Map data (Grok-generated)
│   ├── handoffs/            #   AI handoff documents
│   │   ├── GROK_HANDOFF/    #     Grok session handoffs
│   │   └── SONNET_HANDOFF/  #     Sonnet session handoffs
│   └── comms/               #   Session status updates & TODOs
│
├── tools/                   # ── UTILITY SCRIPTS (one-off) ────────────
│   ├── add_missing_ot_to_manifest.py
│   ├── check_syntax.py
│   ├── fix_encoding.py
│   ├── fix_manifest_eras.py
│   ├── fix_quotes.py
│   ├── merge_expansions.py
│   └── split_css.py
│
├── CLAUDE_CONTEXT/          # ── CLAUDE SESSION MEMORY ────────────────
│   └── ancient_texts_app_memory.md
│
├── archive/                 # Old/deprecated files (gitignored)
├── output/                  # Build output (gitignored)
├── releases/                # Packaged releases (gitignored)
├── dist/                    # Electron installer (gitignored)
└── venv/                    # Python virtualenv (gitignored)
```

---

## Build Commands

```bash
python build.py                  # Desktop dev build (with HAI)
python build.py --release        # Desktop release build (no HAI)
python build_mobile.py           # Mobile PWA build
python release.py                # Package release ZIP

BUILD_ALL.bat                    # Build all 3 targets
DEPLOY.bat                       # Build + commit + push + deploy gh-pages
LAUNCH.bat                       # Interactive menu (build, run, HAI, council)
```

---

## Architecture Notes

- **Build system:** Python scripts that concatenate CSS/JS source files and inject data via string replacement into HTML templates
- **CSS:** 39 component files in `src/css/`, concatenated in order defined by `build-order.txt`
- **JS:** Currently monolithic `app.js` (Phase 2 will split into ~25 modules)
- **State:** `state.js` module created (AppState + Storage wrapper), to be wired in Phase 2
- **Data:** Python files in `data/` folders export dicts/lists; build.py imports them dynamically
- **Mobile:** PWA with service worker; 0.6 MB shell loads data JSON files on demand
- **Desktop:** Single self-contained HTML file with all data embedded
- **HAI:** Ollama-powered local AI chat (dev builds only, stripped from release/mobile)
- **Council:** 5 AI agents for content generation, QA, and theological review (run independently)
