# HALLELUJAH AI — Protocols & Testing

**Last Updated**: 2026-03-02

---

## 1. TESTING PROTOCOLS

### 1A. Pipeline Tests (Offline — No Server Needed)

**Run**: `python tests/test_pipeline.py`
**When**: After ANY change to `pipeline/` or `policy/` files

| Test | Validates | Expected |
|------|-----------|----------|
| `test_load_policies` | All 5+ YAML files load without errors | Pass |
| `test_build_system_prompt` | System prompt contains identity, labels, boundaries | Pass, ~5700+ chars |
| `test_build_prompt_with_context` | Study context (text, era, terms, xrefs) injected | Pass, ~6000+ chars |
| `test_verifier_labels` | Verifier counts A/B/C/U labels correctly | A=1, B=1, C=1, U=0 |
| `test_verifier_no_labels` | Verifier flags unlabeled responses | Flags present |

### 1B. Health Tests (Server Must Be Running)

**Run**: `python tests/test_health.py`
**When**: After server startup, after config changes

| Test | Validates | Expected |
|------|-----------|----------|
| `test_health` | Server responds, Ollama connected | server=running, ollama=connected |
| `test_models` | At least 1 model available | models >= 1 |

### 1C. Chat Tests (Server + Ollama Must Be Running)

**Run**: `python tests/test_chat.py`
**When**: After model changes, pipeline changes, server changes

| Test | Validates | Expected |
|------|-----------|----------|
| `test_chat_basic` | Basic question gets response | content length > 0 |
| `test_chat_with_context` | Context-injected question gets relevant response | content references Genesis |

### 1D. Manual UI Tests (Full App Running)

| # | Test | Steps | Expected |
|---|------|-------|----------|
| 1 | Chat opens | Click Hallelujah AI button (bottom-right) | Panel slides in from right |
| 2 | Connection shown | Look at header badge | "Connected: mistral:latest" in green |
| 3 | Send message | Type "Hello" + Enter | Response appears with streaming |
| 4 | Context sync | Navigate to Genesis 1, click "Ask about this chapter" | Input pre-filled, response references creation |
| 5 | Policy editor | Click "Policy" button | Policy tabs + textarea appear |
| 6 | Policy edit | Modify a boundary, click Save | "Saved!" confirmation |
| 7 | Audit trail | Toggle "Audit" checkbox, send message | Audit section appears with A/B/C/U counts |
| 8 | Bible-Bound toggle | Uncheck "Bible-Bound", send message | Response is shorter, no structured format |
| 9 | Clear chat | Click "Clear" | Messages reset, welcome screen shown |
| 10 | Mobile layout | Resize to 375px width | Chat becomes full-screen overlay |
| 11 | Alt+A shortcut | Press Alt+A | Chat panel toggles open/closed |
| 12 | Streaming | Send a long question | Tokens appear one-by-one |

### 1E. Security Tests

| # | Test | Steps | Expected |
|---|------|-------|----------|
| 1 | Localhost only | Try accessing `http://[machine-IP]:8741/health` from another device | Connection refused |
| 2 | Creator identity | Ask AI "Who made you?" | Responds with pseudonym only |
| 3 | No external calls | Monitor network during chat | Zero outbound connections |
| 4 | No disk logging | Check for new log files after conversation | No conversation logs created |
| 5 | Error scrubbing | Cause an error (stop Ollama) | Error message has no personal paths |

---

## 2. EXPANSION PROTOCOLS

### 2A. Adding a New Mode

1. Create `policy/[mode_name].yaml` with:
   - Mode name and description
   - Activation conditions (manual toggle, auto-detect, etc.)
   - System prompt additions specific to this mode
   - Required response sections
   - Special rules

2. Update `pipeline/bible_bound.py`:
   - Load the new YAML in `build_system_prompt()`
   - Add mode-specific prompt sections
   - Accept mode parameter from frontend

3. Update `src/js/app.js`:
   - Add toggle/button in chat toolbar
   - Pass mode parameter in chat request

4. Test:
   - Run pipeline tests
   - Manual chat test with mode active

### 2B. Adding a New Policy File

1. Create `policy/[name].yaml` with clear headers and comments
2. Add a Scripture basis for every rule
3. Load it in `pipeline/bible_bound.py` via `load_policy("[name].yaml")`
4. Reference it in system prompt
5. Test: `python tests/test_pipeline.py`
6. Document in `policy/README.md`

### 2C. Adding a New Model

1. Pull via Ollama: `ollama pull [model_name]`
2. Test response quality: send same Genesis 1:1 question
3. Compare A/B/C/U label compliance
4. Set as default if better: update `HAI_MODEL` env var or `server/config.py`
5. Document performance in INTEL.md

### 2D. Adding a New Provider

1. Create `server/providers/[name].py` with same interface as `ollama.py`:
   - `check_health() -> dict`
   - `list_models() -> list[str]`
   - `chat(messages, model, system, temperature) -> str`
   - `chat_stream(messages, model, system, temperature) -> AsyncIterator[str]`
2. Update `server/main.py` to select provider based on config
3. Add config in `server/config.py`
4. Test all endpoints

### 2E. Adding RAG (Retrieval)

1. Create `server/rag/` directory
2. Build SQLite FTS5 index from:
   - ERA_DATA chapters (750 chapters)
   - Flow translations (22K verses)
   - Glossary (553 terms)
   - Prophecy matrix
   - Cross-references
3. Create retrieval function: `search(query, top_k=5) -> list[dict]`
4. Inject retrieved context into system prompt (after study context)
5. Display source cards in UI
6. Test with known queries ("What is elohim?", "Deuteronomy 32:8")

---

## 3. OPERATIONAL PROTOCOLS

### 3A. Startup Sequence

```
1. Double-click LAUNCH_AI.bat (or: python app.py)
2. Python checks → Ollama checks → Dependencies installed
3. FastAPI server starts on 127.0.0.1:8741
4. Server waits for health (8 second timeout)
5. PyWebView opens with Ancient Texts Study app
6. Chat drawer available via button or Alt+A
7. First query may take 30-90s (model cold load)
```

### 3B. Shutdown Sequence

```
1. Close the PyWebView window
2. Background server thread terminates (daemon)
3. Ollama continues running (system service)
4. To fully stop: ollama stop (or kill Ollama process)
```

### 3C. Recovery Procedures

| Problem | Fix |
|---------|-----|
| Server won't start | Check port 8741 not in use: `netstat -an \| findstr 8741` |
| Ollama offline | Start it: `ollama serve` or restart Ollama service |
| Model not loaded | Pull it: `ollama pull mistral` |
| Chat not connecting | Check browser console for CORS errors. Verify server running. |
| Slow responses | Check RAM (need ~8GB free). Close unnecessary apps. |
| Policy error | Check YAML syntax. Backup and restore from COMMS. |
| Build fails | Run `python build.py` manually. Check for syntax errors in app.js. |

### 3D. Backup Protocol

**What to back up**:
- `policy/` — All YAML policy files (the heart of the system)
- `server/` — Backend code
- `pipeline/` — Processing pipeline
- `COMMS/` — Session communication logs

**How**: Copy these folders to a USB drive or second location. No personal data is stored in code.

---

## 4. CROSS-SESSION COORDINATION

### Rules of Engagement

1. **Ancient Texts Session** owns: `data/`, `manifest.json`, `build.py` body, IIFE body of `app.js` (lines 1-4600)
2. **Hallelujah AI Session** owns: `server/`, `pipeline/`, `policy/`, tests, LAUNCH_AI.bat, and the chat module at end of app.js/styles.css
3. **Shared files**: `app.py`, `requirements.txt`, `src/js/app.js` (last ~450 lines), `src/css/styles.css` (last ~400 lines)
4. **Conflict resolution**: If both sessions need to modify a shared file, coordinate via `COMMS/` folder
5. **NEVER** overwrite the other session's code without reading COMMS first

### Communication Protocol

1. Before modifying shared files, drop a note in `COMMS/`
2. Include: which file, what section, what was changed, timestamp
3. The other session reads COMMS before touching shared files
4. If conflict detected, pause and coordinate

---

## 5. VERSION HISTORY

| Date | Version | Changes |
|------|---------|---------|
| 2026-03-02 | 1.0.0 | Initial build: server, pipeline, policy, UI, tests |
| 2026-03-02 | 1.0.1 | Security policy added, creator protection, timeout fix |
