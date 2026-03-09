# COMMS — Cross-Session Communication

This folder is a shared communication channel between active Claude sessions
working on different parts of the Ancient Texts Study + Hallelujah AI project.

## Active Sessions
- **Hallelujah AI Session**: Building the local AI chat feature (server/, pipeline/, policy/)
- **Ancient Texts Session**: Expanding content, study chapters, interlinear data

## How It Works
Each session drops messages here when making changes that affect the other.
Check this folder before making edits to shared files (app.js, styles.css, build.py, app.py).

## Files Modified by Hallelujah AI Session
- `app.py` — Added backend server startup (background thread)
- `src/js/app.js` — Added chat drawer module (~450 lines at end, before closing IIFE)
- `src/css/styles.css` — Added chat panel styles (~400 lines at end)
- `requirements.txt` — Added fastapi, uvicorn, httpx, pyyaml

## New Directories (Hallelujah AI)
- `server/` — FastAPI backend (port 8741)
- `pipeline/` — Bible-bound processing pipeline
- `policy/` — Transparent YAML policy files
- `tests/` — Test files
- `LAUNCH_AI.bat` — One-click startup script
