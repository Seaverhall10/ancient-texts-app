"""
server/providers/ollama.py — Ollama REST API adapter.
Connects to the local Ollama instance for fully local inference.
No data leaves your machine.

Key config:
  - num_ctx=16384: 16K context for Qwen 2.5 7B (supports up to 128K)
  - Tuned sampling: top_k=40, top_p=0.9, repeat_penalty=1.15
  - num_thread=10: i7-9850H has 12 threads, leave 2 for OS
  - timeout=300s: CPU inference can take minutes for long responses
  - Streaming preferred: tokens appear as generated
  - Pre-warming: model loaded into RAM at server startup
"""
import httpx
import json
from typing import AsyncIterator, Optional
from server.config import OLLAMA_BASE_URL, OLLAMA_DEFAULT_MODEL

# ── Model Parameters ─────────────────────────────────────
# Context window: Qwen 2.5 supports 128K. We use 16K for CPU speed.
NUM_CTX = 16384

# Sampling: tuned for Bible-bound responses (consistent but not robotic)
TOP_K = 40          # Consider top 40 tokens (reduces hallucination)
TOP_P = 0.9         # Nucleus sampling at 90% probability mass
REPEAT_PENALTY = 1.15  # Discourage repetitive text

# Threading: i7-9850H = 6 cores / 12 threads. Use 10, leave 2 for OS.
NUM_THREAD = 10


def _build_options(temperature: float = 0.7) -> dict:
    """Build the standard Ollama options dict with all tuning parameters."""
    return {
        "temperature": temperature,
        "num_ctx": NUM_CTX,
        "top_k": TOP_K,
        "top_p": TOP_P,
        "repeat_penalty": REPEAT_PENALTY,
        "num_thread": NUM_THREAD,
    }


async def check_health() -> dict:
    """Check if Ollama is running and return status."""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.get(f"{OLLAMA_BASE_URL}/api/tags")
            if resp.status_code == 200:
                data = resp.json()
                models = [m["name"] for m in data.get("models", [])]
                return {
                    "status": "connected",
                    "url": OLLAMA_BASE_URL,
                    "models": models,
                    "default_model": OLLAMA_DEFAULT_MODEL
                }
            return {"status": "error", "detail": f"HTTP {resp.status_code}"}
    except Exception as e:
        return {"status": "offline", "detail": str(e)}


async def list_models() -> list[str]:
    """List all available Ollama models."""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.get(f"{OLLAMA_BASE_URL}/api/tags")
            if resp.status_code == 200:
                return [m["name"] for m in resp.json().get("models", [])]
    except Exception:
        pass
    return []


async def prewarm_model(model: str = None):
    """Load model into RAM by sending a minimal prompt.

    This eliminates the 30-90 second cold start on the first real query.
    Called at server startup so the model is ready when the user opens chat.
    """
    model = model or OLLAMA_DEFAULT_MODEL
    try:
        async with httpx.AsyncClient(timeout=180.0) as client:
            print(f"[hallelujah-ai] Pre-warming model '{model}' (loading into RAM)...")
            resp = await client.post(
                f"{OLLAMA_BASE_URL}/api/generate",
                json={
                    "model": model,
                    "prompt": "Hello",
                    "options": {"num_ctx": NUM_CTX, "num_predict": 1},
                }
            )
            if resp.status_code == 200:
                print(f"[hallelujah-ai] Model '{model}' is warm and ready.")
            else:
                print(f"[hallelujah-ai] Pre-warm returned HTTP {resp.status_code}")
    except Exception as e:
        print(f"[hallelujah-ai] Pre-warm failed (non-fatal): {e}")
        print("[hallelujah-ai] First query will be slower while model loads.")


async def chat(
    messages: list[dict],
    model: Optional[str] = None,
    system: Optional[str] = None,
    temperature: float = 0.7
) -> str:
    """Send a chat request to Ollama and return the full response."""
    model = model or OLLAMA_DEFAULT_MODEL
    payload = {
        "model": model,
        "messages": messages,
        "stream": False,
        "options": _build_options(temperature)
    }
    if system:
        payload["messages"] = [{"role": "system", "content": system}] + payload["messages"]

    # 600s timeout: 16K context on CPU with full Berean decomposition can take 5+ minutes
    async with httpx.AsyncClient(timeout=600.0) as client:
        resp = await client.post(f"{OLLAMA_BASE_URL}/api/chat", json=payload)
        resp.raise_for_status()
        data = resp.json()
        return data.get("message", {}).get("content", "")


async def chat_stream(
    messages: list[dict],
    model: Optional[str] = None,
    system: Optional[str] = None,
    temperature: float = 0.7
) -> AsyncIterator[str]:
    """Stream chat response tokens from Ollama."""
    model = model or OLLAMA_DEFAULT_MODEL
    payload = {
        "model": model,
        "messages": messages,
        "stream": True,
        "options": _build_options(temperature)
    }
    if system:
        payload["messages"] = [{"role": "system", "content": system}] + payload["messages"]

    async with httpx.AsyncClient(timeout=600.0) as client:
        async with client.stream("POST", f"{OLLAMA_BASE_URL}/api/chat", json=payload) as resp:
            resp.raise_for_status()
            async for line in resp.aiter_lines():
                if line.strip():
                    try:
                        chunk = json.loads(line)
                        token = chunk.get("message", {}).get("content", "")
                        if token:
                            yield token
                        if chunk.get("done", False):
                            return
                    except json.JSONDecodeError:
                        continue
