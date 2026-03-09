# Ancient Texts Study App — Claude Session Instructions

## WHO YOU'RE WORKING WITH
- **User**: Seaver Hall (NOT Sean) — spiritual researcher, builder
- **Project**: Ancient Texts Study App
- **Purpose**: Deep scripture study with original languages, cross-references,
  divine council theology, Second Temple context

## FIRST THING TO DO
1. Read `STATUS.md` — current completion state
2. Read `CLAUDE_CONTEXT/ancient_texts_app_memory.md` — full session history & lessons
3. Read `CONTENT_MAP.json` — complete content index (what exists, what's missing)

## PROJECT LOCATION
```
E:\My Drive\ANCIENT_TEXTS Study App\     ← Work from here (OneDrive, always synced)
```
Old Desktop location: `C:\Users\SeaverHall\Desktop\ANCIENT_TEXTS_APP\` (may be deleted)

## WHAT THIS IS
A single-file HTML study app built from Python data files. Contains:
- **50 texts**: 15 OT books (with Hebrew/Greek interlinear) + all 27 NT books
  (with Greek interlinear) + 8 Apocryphal/Second Temple texts
- **147 study eras** (thematic chapters with cross-refs, divine council notes, ANE context)
- **~21,500 verse-by-verse flow translations** (formal equivalence + notes)
- **~320,000 interlinear words** (click any word → original language popup)
- **4,685+ cross-references** indexed in CONTENT_MAP.json

## KEY COMMANDS
```bash
python build.py                              # Rebuild app (always run after changes)
python agents/reader.py --mode qa           # QA check
python data/generate_nt_flow.py --book X    # Generate flow for a book
LAUNCH.bat                                  # One-click run
SYNC.bat                                    # Sync to Google Drive
```

## BUILDER'S COUNCIL (5 AI Agents)
- **ORACLE** — planning, priorities
- **SCRIBE** — content generation (era files, flow translations)
- **ARBITER** — theological accuracy
- **LECTOR** — language, glossary, interlinear
- **ARCHITECT** — build, status, infrastructure

All keys in `agents/config.py`.

## THEOLOGICAL LAWS (NEVER VIOLATE)
1. Non-canonical texts (1 Enoch, Jubilees, etc.) = NEVER "the Bible says"
   Use: "According to 1 Enoch..." or "The Enochic tradition holds..."
2. Evidence tiers: [A] Direct Scripture / [B] Valid inference / [C] Ancient parallels
3. Deut 32:8 — use DSS/LXX "sons of God" not MT "sons of Israel"
4. Genesis 6:1-4 — sons of God = divine/angelic beings (argue against Sethite view)
5. Divine council = real heavenly administration, not metaphors
6. Scripture = ESV unless noted

## CRITICAL CODE PATTERNS
- **Flow files**: named `data/flow/flow_{book_id}.py`, export `FLOW_{BOOK}` + `NOTES_{BOOK}` dicts
- **Era files**: `data/{text_id}/era_*.py`, export `CHAPTERS` list
- **Interlinear (OT)**: `data/interlinear_{book}.py` or `data/{book}/interlinear.py` (Genesis)
- **Interlinear (NT)**: `data/interlinear_nt_{book}.py`
- **1 Enoch special case**: manifest has `data_dir: "enoch1"`, so files are in `data/enoch1/`
- **Build filter**: `flow_file.count("_") == 1` — only loads combined flow files, not partials
- **NT interlinear fallback**: build.py checks `INTERLINEAR_NT_{BOOK}` after `INTERLINEAR_{BOOK}`

## WHAT'S STILL NEEDED
See `STATUS.md` → "WHAT IS MISSING" section for prioritized backlog.
Quick summary: 24 OT books need to be added, NT eras could use enrichment.

## RULE: Research Before Inventing
Always mine existing era files + flow files for patterns before writing new ones.
Genesis, Exodus, Isaiah, Romans are the best template references.
