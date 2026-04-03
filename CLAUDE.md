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
python agents/build_content_map.py     # Rebuild CONTENT_MAP.json after data changes
```
> **Note**: Use `./venv/Scripts/python.exe` instead of bare `python` — bare `python` may not resolve correctly in Git Bash.

## PROJECT STRUCTURE (see PROJECT.md for full map)
```
src/css/         49 component CSS files + build-order.txt
src/js/          app.js (main) + state.js (state management)
data/            74 text folders + flow/ + shared era files
agents/          7 AI agents (Oracle, Scribe, Arbiter, Lector, Architect, Reader, Claude Auditor)
hai/             Hallelujah AI (dev-only chat: app.py, server, pipeline, policy)
docs/            Research notes, vision docs, handoffs, comms
tools/           One-off utility scripts
electron/        Desktop Electron app
```

## BUILD SYSTEM
- **CSS**: 49 component files concatenated via `src/css/build-order.txt`
- **JS**: Currently monolithic `app.js` (~10,535 lines; Phase 2 will split into ~25 modules)
- **Desktop**: `build.py` → single 65 MB HTML with all data embedded
- **Mobile**: `build_mobile.py` → 0.7 MB shell + per-text JSON (on-demand loading)
- **Deploy**: `DEPLOY.bat` uses temp-directory approach for gh-pages (NEVER `git checkout --orphan` in working dir)

## THEOLOGICAL LAWS (NEVER VIOLATE)

### Scripture & Language
1. Bible = 100% Word of God — the authoritative foundation
2. Hebrew is Yahweh's language — always go back to Hebrew/Greek first in any dispute
3. Scripture = ESV unless noted
4. Evidence tiers: [A] Direct Scripture / [B] Valid inference / [C] Ancient parallels

### Non-Canonical Texts
5. Non-canonical texts = NEVER "the Bible says" → use "According to 1 Enoch..."
6. 1 Enoch = highly authoritative — Jude quotes it as prophecy (Jude 14-15), DSS confirms, Ethiopian Orthodox canon
7. Canon was a historical process (Jerome, Trent) — 1 Enoch failed politics, not theology

### Divine Council & Spiritual Beings
8. Deut 32:8 — use DSS/LXX "sons of God" not MT "sons of Israel" (scribal alteration)
9. Genesis 6:1-4 — sons of God = divine/angelic beings (argue against Sethite view — introduced 3rd c. AD, zero Hebrew grounding)
10. Divine council = real heavenly administration, not metaphors (Ps 82, 1 Kings 22, Job 1-2, Dan 7, Isa 6)
11. Four categories: imprisoned Watchers / territorial princes (Deut 32:8) / demons (disembodied Nephilim, 1 Enoch 15:8-10) / Satan
12. Azazel in Lev 16 = specific imprisoned Watcher — scapegoat sends sins back to originator
13. Pagan mythologies = corrupted memories of real events involving real beings

### The Three Rebellions
14. Satan fell BEFORE Eden — throne guardian cherub (Ezek 28:13-15), fell between creation and Eden
15. Three INDEPENDENT rebellions: Eden (Nachash) → Hermon (200 Watchers) → Babel (nations assigned to corrupt sons of God)
16. Three reversals through Christ: Cross (Col 2:15) → Proclamation to imprisoned spirits (1 Pet 3:19, kerysso not euangelizo) → Pentecost (Acts 2 reverses Babel/Deut 32:8)
17. Genesis 3:15 = thesis statement of entire Bible — everything from Gen 4 to Rev 20 is this verse playing out

### Christology
18. Jesus = the Word, present at creation (John 1:1-3 echoes Gen 1:1)
19. Cloud-rider = exclusively divine prerogative — Mark 14:62-63 (high priest tore robes over divine cloud-rider claim, not Messiah claim)
20. Jesus' priesthood = Melchizedekian, NOT Levitical (wrong tribe — Judah not Levi, Heb 7:13-14)

### Salvation & Ekklesia
21. Salvation = covenantal, not transactional — never imply "say this prayer" formula
22. Ekklesia = governing assembly, NOT institutional "church" — cosmic assignment (Eph 3:10, 1 Cor 6:3)
23. Afterlife = Sheol → bodily resurrection → new earth — NOT "souls go to heaven" (Platonic infiltration via Alexandria)

### Prophets & Content
24. Prophets = covenant prosecutors using riv (lawsuit) framework — royal messengers, not inspired commentators
25. Raw emotional texture of Psalms and Prophets NEVER sanitized
26. Holy Spirit gifts continue — cessationism not supported exegetically (1 Cor 13:10 teleios = Christ's return, not completed canon)

### Content Writing Standards
27. Era chapters: 3-6 sections minimum, 800-1200 characters each
28. cross_refs must include type tag (ot/nt/ane/dss/pseudepigrapha/thematic)
29. Always give Hebrew/Greek BEFORE theological interpretation
30. Tone: truth with good delivery — not apologetic, not aggressive — make people lean in

> **Master reference**: See `docs/SEAVER_THEOLOGY_LAW.md` for the full theological framework with scripture citations and detailed arguments. This is a living document — still being refined.

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
Phase 2 ⬜ JS module split (~25 files from ~10,535-line app.js)
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
**Baseline (2026-04-03)**: 0 CRITICAL, 0 warnings, 546 passed.
Session 12 ran Arbiter on all 27 texts (61 era files) — 177 CRITICALs found, 43 fixed + systemic fixes.
~110 thematic text CRITICALs remain (systemic: evidence tiers, Rule 5 gaps, ESV accuracy).
Fix all CRITICAL findings before deploying.

## RULE: Rebuild Content Map After Data Changes
After adding/modifying era files, flow files, or manifest entries, rebuild the AI navigation index:
```bash
python agents/build_content_map.py
```
This updates `CONTENT_MAP.json` which all agents read for project context.

## RULE: Update All Docs Before Closing (MANDATORY)
Every session that adds features, fixes content, or changes architecture MUST update these before the final commit:
- `STATUS.md` — current completion state, recent changes, statistics
- `CONTENT_MAP.json` — rebuild via `python agents/build_content_map.py`
- Memory files — session plan, architecture reference, any new feedback
- `CLAUDE.md` — if new rules, patterns, or commands were established
- `PROJECT.md` — if directory structure or file counts changed

Do NOT wait for the user to ask. Do NOT treat this as optional. If you modified 30 files and didn't update STATUS.md, the session is not done.

## RULE: Complete Everything — No Stubs, No Gaps (MANDATORY)
If a task involves N items, do all N. Not N-10. Not "most of them."
- 70 Bible Analysis entries = write all 70, not 60
- 7 narrative chapters = write all 7, not 4 + "we'll do the rest later"
- 13 texts to audit = audit all 13, not "the important ones"

"Skip stubs" is not a valid scope decision unless the user explicitly says to skip them. Before marking any task complete, verify: is this actually 100% done?

## RULE: Test in Browser — Not Just Code Analysis (MANDATORY)
After building features, verify them in the mobile browser (desktop 78MB is too large for preview):
```bash
python build_mobile.py
# Use preview_start with "mobile" server config
# Navigate to the feature, click buttons, verify state changes
# Take screenshots to show the user
```
Build compiling ≠ feature working. QA passing ≠ UI rendering correctly. Never claim "verified" from grep or code-reading alone.
