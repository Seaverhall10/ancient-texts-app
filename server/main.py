"""
server/main.py — Hallelujah AI Backend Server.
FastAPI app serving the Bible-bound chat pipeline,
launcher hub, full-screen chat UI, and RAG search.

All processing happens locally. No data leaves your machine.
"""
import os
import json
import asyncio
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional

from server.config import SERVER_HOST, SERVER_PORT, POLICY_DIR, VERIFY_RESPONSES, BASE_DIR
from server.providers import ollama
from pipeline.bible_bound import build_system_prompt, build_full_system_prompt, get_modes
from pipeline.verifier import verify_response

app = FastAPI(title="Hallelujah AI", version="3.0.0")

# UI directory for static files
UI_DIR = os.path.join(BASE_DIR, "ui")

# Allow local HTML file to make requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files for CSS/JS
app.mount("/ui", StaticFiles(directory=UI_DIR), name="ui")


# ── Request/Response Models ──────────────────────────────

class ChatRequest(BaseModel):
    message: str
    history: list[dict] = []
    model: Optional[str] = None
    temperature: float = 0.7
    bible_bound: bool = True
    analysis_mode: bool = True  # Berean Protocol — critical analysis always on by default
    study_context: Optional[dict] = None  # Current chapter/era/text context from UI
    mode: str = "general"  # general, bible_study, berean, dev


class ChatResponse(BaseModel):
    content: str
    audit: Optional[dict] = None
    model: str = ""
    sources: Optional[dict] = None


class PolicyUpdateRequest(BaseModel):
    filename: str
    content: str


# ── Build RAG index on startup ────────────────────────────

@app.on_event("startup")
async def startup_build_index():
    """Build the RAG knowledge index if it doesn't exist."""
    try:
        from server.rag.indexer import build_index, DB_PATH
        if not os.path.exists(DB_PATH):
            print("[hallelujah-ai] Building knowledge index (first run)...")
            build_index(force=True)
        else:
            print(f"[hallelujah-ai] Knowledge index ready: {DB_PATH}")
    except Exception as e:
        print(f"[hallelujah-ai] RAG index warning: {e}")
        print("[hallelujah-ai] Chat will work but without study content integration.")


@app.on_event("startup")
async def startup_prewarm():
    """Pre-warm the LLM so the first user query is fast.

    Without this, the first query takes 30-90 seconds while
    Ollama loads the model into RAM. Pre-warming does this
    at server startup so the user never waits.
    """
    try:
        from server.providers.ollama import prewarm_model
        await prewarm_model()
    except Exception as e:
        print(f"[hallelujah-ai] Pre-warm skipped: {e}")


# ── Page Routes ───────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def launcher_page():
    """Serve the launcher hub page."""
    launcher_path = os.path.join(UI_DIR, "launcher.html")
    if os.path.exists(launcher_path):
        return FileResponse(launcher_path, media_type="text/html")
    return HTMLResponse("<h1>Hallelujah AI</h1><p>launcher.html not found</p>", status_code=404)


@app.get("/chat", response_class=HTMLResponse)
async def chat_page():
    """Serve the full-screen chat page."""
    chat_path = os.path.join(UI_DIR, "chat.html")
    if os.path.exists(chat_path):
        return FileResponse(chat_path, media_type="text/html")
    return HTMLResponse("<h1>Chat page not found</h1>", status_code=404)


# ── Modes ────────────────────────────────────────────────

@app.get("/modes")
async def modes_list():
    """Return available chat modes and their descriptions."""
    return {"modes": get_modes()}


# ── Health ────────────────────────────────────────────────

@app.get("/health")
async def health():
    """Health check — returns server + Ollama status."""
    ollama_status = await ollama.check_health()
    return {
        "server": "running",
        "ollama": ollama_status,
        "pipeline": "bible_bound",
        "policy_dir": POLICY_DIR,
        "verify_enabled": VERIFY_RESPONSES
    }


# ── Models ────────────────────────────────────────────────

@app.get("/models")
async def models():
    """List available Ollama models."""
    model_list = await ollama.list_models()
    return {"models": model_list}


# ── RAG Search ────────────────────────────────────────────

@app.get("/search")
async def rag_search(
    q: str = Query(..., description="Search query"),
    limit: int = Query(5, description="Max results per category")
):
    """Search the knowledge index. Returns relevant study content."""
    try:
        from server.rag.search import search, get_index_stats
        results = search(q, top_k=limit)
        stats = get_index_stats()
        return {
            "query": q,
            "results": results.get("results", []),
            "context_text": results.get("context_text", ""),
            "source_count": results.get("source_count", 0),
            "sources": results.get("sources", {}),
            "stats": stats
        }
    except Exception as e:
        return {"query": q, "results": [], "error": str(e)}


# ── Chat (non-streaming) ─────────────────────────────────

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    """Send a message and get a complete response."""
    # Search RAG for relevant study content
    rag_context = ""
    sources = None
    try:
        from server.rag.search import search
        rag_results = search(req.message, top_k=5)
        rag_context = rag_results.get("context_text", "")
        if rag_results.get("source_count", 0) > 0:
            sources = rag_results.get("sources", {})
    except Exception:
        pass  # RAG is optional — chat works without it

    # Build FULL system prompt (expanded for 16K context model)
    system = build_full_system_prompt(
        bible_bound=req.bible_bound,
        study_context=req.study_context,
        analysis_mode=req.analysis_mode,
        rag_context=rag_context,
        mode=req.mode
    )

    # Build message list
    messages = list(req.history) + [{"role": "user", "content": req.message}]

    try:
        content = await ollama.chat(
            messages=messages,
            model=req.model,
            system=system,
            temperature=req.temperature
        )
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Ollama error: {str(e)}")

    # Verify response if enabled
    audit = None
    if VERIFY_RESPONSES and req.bible_bound:
        audit = verify_response(content)

    return ChatResponse(
        content=content,
        audit=audit,
        model=req.model or "default",
        sources=sources
    )


# ── Chat (streaming via SSE) ─────────────────────────────

@app.post("/chat/stream")
async def chat_stream(req: ChatRequest):
    """Stream response tokens via Server-Sent Events."""
    # Search RAG for relevant study content
    rag_context = ""
    sources = None
    try:
        from server.rag.search import search
        rag_results = search(req.message, top_k=5)
        rag_context = rag_results.get("context_text", "")
        if rag_results.get("source_count", 0) > 0:
            sources = rag_results.get("sources", {})
    except Exception:
        pass  # RAG is optional

    system = build_full_system_prompt(
        bible_bound=req.bible_bound,
        study_context=req.study_context,
        analysis_mode=req.analysis_mode,
        rag_context=rag_context,
        mode=req.mode
    )
    messages = list(req.history) + [{"role": "user", "content": req.message}]

    # Send sources info first so the UI can display them
    async def generate():
        # Emit sources metadata first
        if sources:
            yield f"data: {json.dumps({'sources': sources})}\n\n"

        full_response = ""
        try:
            async for token in ollama.chat_stream(
                messages=messages,
                model=req.model,
                system=system,
                temperature=req.temperature
            ):
                full_response += token
                yield f"data: {json.dumps({'token': token})}\n\n"

            # After streaming completes, send audit if enabled
            audit = None
            if VERIFY_RESPONSES and req.bible_bound:
                audit = verify_response(full_response)
            yield f"data: {json.dumps({'done': True, 'audit': audit})}\n\n"

        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"

    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"
        }
    )


# ── Policy Management ─────────────────────────────────────

@app.get("/policy")
async def get_policies():
    """Return all policy files for display in the UI."""
    policies = {}
    if os.path.isdir(POLICY_DIR):
        for fname in os.listdir(POLICY_DIR):
            if fname.endswith((".yaml", ".yml")):
                fpath = os.path.join(POLICY_DIR, fname)
                with open(fpath, "r", encoding="utf-8") as f:
                    policies[fname] = f.read()
    return {"policies": policies}


@app.post("/policy")
async def update_policy(req: PolicyUpdateRequest):
    """Update a policy file from the UI editor."""
    # Sanitize filename
    safe_name = os.path.basename(req.filename)
    if not safe_name.endswith((".yaml", ".yml")):
        raise HTTPException(status_code=400, detail="Only YAML policy files can be edited")

    fpath = os.path.join(POLICY_DIR, safe_name)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(req.content)

    return {"status": "saved", "file": safe_name}


# ── Run directly ──────────────────────────────────────────

def start_server():
    """Start the server (called from app.py or directly)."""
    import uvicorn
    uvicorn.run(app, host=SERVER_HOST, port=SERVER_PORT, log_level="info")


if __name__ == "__main__":
    start_server()
