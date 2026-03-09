# Ancient Texts Study App — Setup Guide
*How to get running from scratch (from OneDrive or any machine)*

---

## Prerequisites

1. **Python 3.10+** — https://python.org/downloads
   - During install, check "Add Python to PATH"
2. **Google Drive for Desktop** (if using OneDrive/Drive sync) — already installed

---

## First-Time Setup

### Option A: Work directly from Google Drive (Recommended)
The project folder lives at:
```
E:\My Drive\ANCIENT_TEXTS Study App\
```
This folder IS the project. Google Drive keeps it synced automatically.
Double-click `LAUNCH.bat` to run.

### Option B: Clone to Desktop
```batch
robocopy "E:\My Drive\ANCIENT_TEXTS Study App" "C:\Users\%USERNAME%\Desktop\ANCIENT_TEXTS_APP" /MIR /XD __pycache__ /XF *.pyc
```
Then run from Desktop.

---

## Running the App

### Option 1 — Double-click `LAUNCH.bat`
Handles everything: creates venv, installs packages, builds, launches.

### Option 2 — Manual
```batch
cd "E:\My Drive\ANCIENT_TEXTS Study App"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python build.py
python app.py
```

The app opens as a desktop window (via pywebview).
The built HTML file is also at: `output\AncientTextsStudy.html` — open in any browser.

---

## Rebuilding Content

Whenever you add/change era files, run:
```batch
python build.py
```
This also auto-rebuilds `CONTENT_MAP.json`.

---

## Generating Flow Translations (NT/OT)

```batch
# Single book
python data\generate_nt_flow.py --book john

# All NT books
python data\generate_nt_flow.py --all
```
Requires Anthropic API key (already in `agents\config.py`).

---

## Running the Council Agents

```batch
# Full Council run
python agents\run_council.py

# QA check
python agents\reader.py --mode qa

# Student reading simulation
python agents\reader.py --mode student --text romans
```

---

## API Keys

All 5 API keys are stored in `agents\config.py` (committed to project).
No environment variables needed unless you want to override.

| Agent | Key Variable |
|-------|-------------|
| Oracle | ORACLE_API_KEY |
| Scribe | SCRIBE_API_KEY |
| Arbiter | ARBITER_API_KEY |
| Lector | LECTOR_API_KEY |
| Architect | ARCHITECT_API_KEY |

---

## Syncing

```batch
# Sync Desktop → Google Drive
SYNC.bat

# Or PowerShell version
powershell -File sync_to_drive.ps1
```

---

## Key Files Quick Reference

| File | Purpose |
|------|---------|
| `build.py` | Builds the app HTML |
| `manifest.json` | All 50 texts + 147 eras registered here |
| `CONTENT_MAP.json` | Master AI navigation index (auto-rebuilt) |
| `STATUS.md` | What's done, what's missing |
| `WHATS_LEFT.md` | Detailed backlog with priorities |
| `agents/config.py` | API keys + agent settings |
| `agents/reader.py` | QA + content quality agent |
| `data/generate_nt_flow.py` | Flow translation generator |
| `LAUNCH.bat` | One-click launch |
| `SYNC.bat` | Sync to Google Drive |

---

## Starting a New Claude Session on This Project

1. Open Claude Code in `E:\My Drive\ANCIENT_TEXTS Study App\`
2. Claude will find `CLAUDE_CONTEXT\` folder with full memory
3. Read `CLAUDE_CONTEXT\ancient_texts_app_memory.md` first
4. Read `STATUS.md` for current state
5. Read `CONTENT_MAP.json` for complete content index

**Tell Claude:** *"This is the Ancient Texts Study App. Read STATUS.md and CLAUDE_CONTEXT/ancient_texts_app_memory.md to get up to speed."*

---

## Folder Structure

```
ANCIENT_TEXTS Study App/
  build.py               -- Main build script
  manifest.json          -- Text + era registry
  app.py                 -- Desktop window launcher
  requirements.txt       -- Python dependencies
  LAUNCH.bat             -- One-click start
  SYNC.bat               -- Google Drive sync
  STATUS.md              -- Current status
  WHATS_LEFT.md          -- Backlog
  SETUP.md               -- This file
  CONTENT_MAP.json       -- AI navigation index
  CLAUDE_CONTEXT/        -- Claude session memory
    ancient_texts_app_memory.md
    personal_INDEX.md
  data/
    manifest entries match data/{text_id}/ folders
    genesis/, exodus/, ... matthew/, mark/, ...
    1enoch/, enoch1/  (special case: data_dir='enoch1')
    flow/              -- All verse-by-verse translations
    interlinear*.py    -- Hebrew/Greek word data
    glossary.py        -- Theological term definitions
  agents/
    config.py          -- API keys + settings
    oracle.py          -- Planning agent
    scribe.py          -- Content generation agent
    arbiter.py         -- Theological accuracy agent
    lector.py          -- Language/glossary agent
    architect.py       -- Build/status agent
    reader.py          -- QA + testing agent
    build_content_map.py -- Content analytics
    run_council.py     -- Run all 5 agents
  src/
    js/app.js          -- App JavaScript
    css/styles.css     -- Styling
  output/
    AncientTextsStudy.html  -- The built app
```
