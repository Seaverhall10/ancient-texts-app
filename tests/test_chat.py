"""
tests/test_chat.py — Verify chat endpoint returns responses.
Requires: Hallelujah AI server running + Ollama with a model loaded.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import httpx
import asyncio


async def test_chat_basic():
    """Test basic chat request returns a response."""
    async with httpx.AsyncClient(timeout=120.0) as client:
        resp = await client.post("http://127.0.0.1:8741/chat", json={
            "message": "What is Genesis 1:1 about? Keep it brief.",
            "bible_bound": True
        })
        assert resp.status_code == 200
        data = resp.json()
        assert "content" in data
        assert len(data["content"]) > 0
        print(f"[PASS] Chat response received ({len(data['content'])} chars)")
        print(f"  First 200 chars: {data['content'][:200]}...")
        if data.get("audit"):
            audit = data["audit"]
            print(f"  Audit: A={audit['labels']['A']} B={audit['labels']['B']} C={audit['labels']['C']} U={audit['labels']['U']}")
            print(f"  Score: {audit['score']}/100")
        return data


async def test_chat_with_context():
    """Test chat with study context injected."""
    async with httpx.AsyncClient(timeout=120.0) as client:
        resp = await client.post("http://127.0.0.1:8741/chat", json={
            "message": "Tell me about this chapter.",
            "bible_bound": True,
            "study_context": {
                "text_name": "Genesis",
                "era_name": "Creation Narrative",
                "chapter_title": "Creation Account",
                "chapter_ref": "Genesis 1",
                "key_verse": "Genesis 1:1 — In the beginning, God created the heavens and the earth.",
                "hebrew_terms": ["elohim", "bara", "ruach"],
                "cross_refs": [
                    {"ref": "John 1:1-3", "note": "Logos doctrine parallels creation"},
                    {"ref": "Hebrews 11:3", "note": "By faith we understand the worlds were framed"}
                ]
            }
        })
        assert resp.status_code == 200
        data = resp.json()
        assert len(data["content"]) > 0
        print(f"[PASS] Context-aware chat response ({len(data['content'])} chars)")
        return data


if __name__ == "__main__":
    print("Testing Hallelujah AI Chat...")
    print("-" * 40)
    asyncio.run(test_chat_basic())
    print()
    asyncio.run(test_chat_with_context())
    print("-" * 40)
    print("All chat tests passed!")
