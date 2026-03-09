"""
tests/test_health.py — Verify Hallelujah AI server starts and health endpoint responds.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import httpx
import asyncio


async def test_health():
    """Test that the health endpoint returns server status."""
    async with httpx.AsyncClient() as client:
        resp = await client.get("http://127.0.0.1:8741/health")
        assert resp.status_code == 200
        data = resp.json()
        assert data["server"] == "running"
        assert "ollama" in data
        print(f"[PASS] Health endpoint: server={data['server']}, ollama={data['ollama']['status']}")
        return data


async def test_models():
    """Test that the models endpoint returns available models."""
    async with httpx.AsyncClient() as client:
        resp = await client.get("http://127.0.0.1:8741/models")
        assert resp.status_code == 200
        data = resp.json()
        print(f"[PASS] Models endpoint: {len(data['models'])} models available")
        return data


if __name__ == "__main__":
    print("Testing Hallelujah AI Server...")
    print("-" * 40)
    asyncio.run(test_health())
    asyncio.run(test_models())
    print("-" * 40)
    print("All health tests passed!")
