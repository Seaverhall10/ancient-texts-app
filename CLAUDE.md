# Ancient Texts Study App — Claude Session Instructions

## WHO YOU'RE WORKING WITH
- **User**: Seaver Hall (NOT Sean) — spiritual researcher, builder
- **Project**: Ancient Texts Study App (v3.3.0)
- **Purpose**: Deep scripture study with original languages, cross-references,
  divine council theology, Second Temple context

## FIRST THING TO DO
1. Read `PROJECT.md` — full directory structure & architecture
2. Read `STATUS.md` — current completion state & priorities
3. Read `CLAUDE_CONTEXT/ancient_texts_app_memory.md` — session history & lessons

## WHAT THIS IS
Two-target study app (Desktop + Mobile PWA) built from Python data files:
- **80 texts** (39 OT + 27 NT + 5 DSS + 1 Pseudepigrapha + 1 Historical + 4 Thematic + 3 Study)
- **246 study eras**, 1,059 chapters
- **444,339 interlinear words** (Hebrew + Greek, click-to-popup)
- **31,101 flow verse translations**, 9,497 scholarly notes
- **6,990 cross-references**, 607 glossary terms
- **52+ world religions** in Bible Truth Matrix
- **24 map journey routes**, 206 waypoints with descriptions

## KEY COMMANDS
```bash
python build.py                    # Desktop dev build (with HAI)
python build.py --release          # Desktop release build (no HAI)
python build_mobile.py             # Mobile PWA build
BUILD_ALL.bat                      # Build all 3 targets
DEPLOY.bat                         # Build + commit + push + deploy gh-pages
LAUNCH.bat                         # Interactive menu
python agents/reader.py --mode qa  # QA check
python agents/audit_claude_work.py --full-app  # Full sentient audit (ALL content)
python agents/audit_claude_work.py --all       # Map-only audit
python agents/arbiter.py --map                 # Theological map check
python agents/reader.py --mode map-audit       # Map data integrity
```

## PROJECT STRUCTURE (see PROJECT.md for full map)
```
src/css/         39 component CSS files + build-order.txt
src/js/          app.js (main) + state.js (state management)
data/            74 text folders + flow/ + shared era files
agents/          7 AI agents (Oracle, Scribe, Arbiter, Lector, Architect, Reader, Claude Auditor)
hai/             Hallelujah AI (dev-only chat: app.py, server, pipeline, policy)
docs/            Research notes, vision docs, handoffs, comms
tools/           One-off utility scripts
electron/        Desktop Electron app
```

## BUILD SYSTEM
- **CSS**: 39 component files concatenated via `src/css/build-order.txt`
- **JS**: Currently monolithic `app.js` (Phase 2 will split into ~25 modules)
- **Desktop**: `build.py` → single 65 MB HTML with all data embedded
- **Mobile**: `build_mobile.py` → 0.6 MB shell + per-text JSON (on-demand loading)
- **Deploy**: `DEPLOY.bat` uses temp-directory approach for gh-pages (NEVER `git checkout --orphan` in working dir)

## THEOLOGICAL LAWS (NEVER VIOLATE)
1. Non-canonical texts = NEVER "the Bible says" → use "According to 1 Enoch..."
2. Evidence tiers: [A] Direct Scripture / [B] Valid inference / [C] Ancient parallels
3. Deut 32:8 — use DSS/LXX "sons of God" not MT "sons of Israel"
4. Genesis 6:1-4 — sons of God = divine/angelic beings (argue against Sethite view)
5. Divine council = real heavenly administration, not metaphors
6. Scripture = ESV unless noted

## CRITICAL CODE PATTERNS
- **Flow files**: `data/flow/flow_{book_id}.py`, export `FLOW_{BOOK}` + `NOTES_{BOOK}`
- **Era files**: `data/{text_id}/era_*.py`, export `CHAPTERS` list
- **Interlinear (OT)**: `data/interlinear_{book}.py` or `data/{book}/interlinear.py`
- **Interlinear (NT)**: `data/interlinear_nt_{book}.py`
- **1 Enoch special case**: manifest `data_dir: "enoch1"` → files in `data/enoch1/`
- **Build filter**: `flow_file.count("_") == 1` — only loads combined flow files
- **NT interlinear fallback**: build.py checks `INTERLINEAR_NT_{BOOK}` after `INTERLINEAR_{BOOK}`

## RESTRUCTURING PLAN (In Progress)
Phase 1 ✅ CSS split + state module
Phase 2 ⬜ JS module split (~25 files from app.js)
Phase 3 ⬜ Build consolidation + data registry
Phase 4 ⬜ Testing + CI/CD

## RULE: Research Before Inventing
Always mine existing era files + flow files for patterns before writing new ones.
Genesis, Exodus, Isaiah, Romans are the best template references.

## RULE: Delegate to Agents (MANDATORY)
Minimize main conversation token usage by delegating to Task agents:
- **5+ edits** → batch into a `general-purpose` agent
- **3+ file reads** for research → `Explore` agent (model: haiku)
- **Data writing** (journeys, eras, glossary) → `general-purpose` agent
- **Builds & deploys** → `Bash` agent (run_in_background: true)
- **Parallel work** → launch multiple agents simultaneously
- **Main thread** = coordinate, small edits, communicate with user only
- Use `model: "haiku"` for straightforward tasks, `"sonnet"` for complex reasoning

## RULE: Audit Before Deploy (MANDATORY)
Every session that modifies content or code MUST run the audit before final deploy:
```bash
# Minimum (every session):
python agents/reader.py --mode qa              # 451+ structural checks
python agents/audit_claude_work.py --full-app  # Full content + code audit

# After map/journey changes:
python agents/arbiter.py --map                 # Theological guardrails

# After era file changes:
python agents/audit_claude_work.py --eras      # Era depth + field validation

# After any deploy:
# Review the report at agents/reports/claude_audit_*.md
```
**Baseline (2026-03-13)**: 0 CRITICAL target (current: 37 from new NT eras needing id/era fields).
Fix all CRITICAL findings before deploying.
