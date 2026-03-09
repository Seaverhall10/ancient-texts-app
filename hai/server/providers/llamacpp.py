"""
server/providers/llamacpp.py — llama.cpp server adapter (stub).
For future use with llama.cpp's OpenAI-compatible API.
When configured, connects to a local llama.cpp server
running with --api-server flag.
"""

# TODO: Implement when needed
# llama.cpp server exposes OpenAI-compatible endpoints at:
#   POST /v1/chat/completions
# This adapter would use the same interface as OpenAI's API.

LLAMACPP_BASE_URL = "http://localhost:8080"
