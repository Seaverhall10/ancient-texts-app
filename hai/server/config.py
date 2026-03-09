"""
server/config.py — Configuration for Hallelujah AI backend.
All settings are transparent and editable.

SECURITY: This server binds to 127.0.0.1 ONLY.
It is never accessible from outside this machine.
"""
import os

# Server — LOCKED to localhost. Never change to 0.0.0.0
SERVER_HOST = "127.0.0.1"
SERVER_PORT = int(os.environ.get("HAI_PORT", "8741"))

# Ollama — local only
OLLAMA_BASE_URL = "http://localhost:11434"
OLLAMA_DEFAULT_MODEL = os.environ.get("HAI_MODEL", "hallelujah")

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POLICY_DIR = os.path.join(BASE_DIR, "policy")

# Pipeline
MAX_CONTEXT_CHARS = 8000  # Max chars of study context injected into prompt
STREAM_ENABLED = True
VERIFY_RESPONSES = True  # Run the A/B/C/U verifier on every response

# Security
LOG_PII = False  # NEVER log personal information
SAVE_CONVERSATIONS = False  # Conversations stay in RAM only by default
ALLOW_EXTERNAL_CONNECTIONS = False  # No outbound requests ever
