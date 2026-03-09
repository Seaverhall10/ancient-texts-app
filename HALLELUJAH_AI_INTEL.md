# HALLELUJAH AI — Intelligence Document

**Last Updated**: 2026-03-02
**Status**: OPERATIONAL
**Classification**: Internal — Creator Eyes Only

---

## System State

| Component | Status | Details |
|-----------|--------|---------|
| Python | 3.12.10 | `C:\Users\User\AppData\Local\Programs\Python\Python312\` |
| Ollama | 0.17.4 | `C:\Users\User\AppData\Local\Programs\Ollama\` |
| Mistral 7B | Loaded | 4.4 GB, Q4_K_M quantization, 7.2B params |
| FastAPI Server | Running | `127.0.0.1:8741` (localhost ONLY) |
| Pipeline Tests | ALL PASS | 7/7 tests green |
| Health Check | GREEN | Server + Ollama both connected |
| UI Integration | Complete | Chat drawer in app.js + styles.css |
| Disk | 285 GB free | C: drive, 61% available |
| RAM | 15.4 GB free | 31.8 GB total |

---

## Architecture

```
User ──► PyWebView App ──► FastAPI (8741) ──► Ollama (11434) ──► Mistral 7B
                │                │
                │                ├── pipeline/bible_bound.py (system prompt from YAML)
                │                ├── pipeline/verifier.py (A/B/C/U audit)
                │                └── policy/*.yaml (transparent, editable)
                │
                └── src/js/app.js (chat drawer, streaming, context sync)
```

**Data Flow**:
1. User types message in chat drawer
2. JavaScript sends POST to `127.0.0.1:8741/chat/stream`
3. FastAPI loads policy YAMLs → builds system prompt
4. Injects current study context (chapter, era, Hebrew/Greek terms, cross-refs)
5. Sends to Ollama's local `/api/chat` endpoint
6. Streams tokens back via Server-Sent Events
7. Verifier runs post-response audit (labels, citations, sections)
8. Audit trail displayed in UI

---

## File Inventory (20 new files)

### Server (57K total)
| File | Lines | Purpose |
|------|-------|---------|
| `server/__init__.py` | 1 | Package marker |
| `server/main.py` | ~170 | FastAPI routes: /health, /models, /chat, /chat/stream, /policy |
| `server/config.py` | ~25 | Config: host, port, Ollama URL, security flags |
| `server/providers/__init__.py` | 1 | Package marker |
| `server/providers/ollama.py` | ~95 | Ollama REST adapter (health, list, chat, stream) |
| `server/providers/llamacpp.py` | ~10 | Stub for future llama.cpp support |

### Pipeline (46K total)
| File | Lines | Purpose |
|------|-------|---------|
| `pipeline/__init__.py` | 1 | Package marker |
| `pipeline/bible_bound.py` | ~145 | System prompt builder from YAML policies |
| `pipeline/verifier.py` | ~100 | Response quality checker (A/B/C/U, citations, sections) |
| `pipeline/context_builder.py` | ~60 | Study context formatter |

### Policy (28K total)
| File | Purpose | Key Content |
|------|---------|-------------|
| `policy/bible_bound.yaml` | Hermeneutic principles | 7 principles, divine council theology, canon rules |
| `policy/claim_labels.yaml` | Evidence classification | A/B/C/U definitions + 5 enforcement rules |
| `policy/response_format.yaml` | Response structure | Study (7 sections), Prophecy (4 sections), General |
| `policy/boundaries.yaml` | Behavioral bounds | 7 Scripture-based boundaries + refusal protocol |
| `policy/security.yaml` | Privacy/security | Creator protection, data sovereignty, network hardening |
| `policy/README.md` | Documentation | How to edit, what each file does |

### Tests (20K total)
| File | Tests | Requires Server |
|------|-------|-----------------|
| `tests/test_health.py` | 2 | Yes |
| `tests/test_chat.py` | 2 | Yes + Ollama |
| `tests/test_pipeline.py` | 5 | No (offline) |

### Modified Existing Files
| File | Change | Lines Added |
|------|--------|-------------|
| `app.py` | Backend server startup in background thread | ~60 lines |
| `src/js/app.js` | Chat drawer module (before closing IIFE) | ~450 lines |
| `src/css/styles.css` | Chat panel styles (appended at end) | ~400 lines |
| `requirements.txt` | fastapi, uvicorn, httpx, pyyaml | 5 lines |

---

## Security Posture

| Control | Status | Detail |
|---------|--------|--------|
| Server binding | LOCKED | `127.0.0.1` only — never `0.0.0.0` |
| External connections | ZERO | No outbound requests, no telemetry |
| Creator identity | PROTECTED | Pseudonym: "A servant of the Most High" |
| Conversation storage | RAM ONLY | Nothing written to disk by default |
| PII logging | DISABLED | `LOG_PII = False` in config |
| CORS | Localhost only | Safe for local file:// access |
| Error scrubbing | Active | No paths/usernames in error messages |
| Family protection | Active | policy/security.yaml extends to all associates |

---

## Known Limitations

1. **Model compliance**: Mistral 7B doesn't always use A/B/C/U labels (audit score ~20/100 on first test). Needs prompt tuning or a more instruction-following model.
2. **First load latency**: ~30-90 seconds on first query as model loads into RAM.
3. **No GPU detection**: Haven't verified if Ollama is using GPU acceleration.
4. **No conversation persistence**: Chat history lost on app restart (by design for security, but optionally enable later).
5. **No RAG yet**: The existing study data (331K interlinear words, 553 glossary terms) isn't indexed for retrieval. Currently sends raw context only.
6. **Build not re-run**: The chat code is in source files but `build.py` hasn't been re-run to compile a new HTML output. Need to rebuild.
7. **Python not in system PATH**: Works via full path but `LAUNCH_AI.bat` may fail. Needs PATH fix or explicit path in batch file.

---

## Performance Baseline

| Metric | Value | Notes |
|--------|-------|-------|
| Server startup | ~3 seconds | FastAPI + uvicorn |
| Health check | <50ms | Instant |
| First model query | 30-90 seconds | Model loading into RAM |
| Subsequent queries | 5-30 seconds | Depends on prompt length |
| System prompt size | ~5,749 chars | All policies loaded |
| Context-aware prompt | ~6,034 chars | With study context injected |
| Streaming latency | ~200ms first token | After model warm |
