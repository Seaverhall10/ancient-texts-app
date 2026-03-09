"""
app.py — PyWebView launcher for Ancient Texts Study + Hallelujah AI.
Starts the local AI backend server, then opens the launcher hub
in a native desktop window.

Navigation flow:
  Launcher Hub → Chat (full-screen) OR Study (built HTML)

Robust startup:
 - Kills any stale server on the port before starting
 - Builds RAG index on first run
 - Verifies server is healthy before opening UI
 - Graceful fallback if dependencies are missing
 - Clean shutdown when window closes
"""
import os
import sys
import subprocess
import threading
import time
import signal
import socket

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Ensure output exists
html_path = os.path.join(BASE_DIR, 'output', 'AncientTextsStudy.html')

if not os.path.exists(html_path):
    print("[build] Output not found — running build.py first...")
    subprocess.run([sys.executable, os.path.join(BASE_DIR, 'build.py')], check=True)


# ── Port Management ─────────────────────────────────────────
def is_port_in_use(port, host="127.0.0.1"):
    """Check if a port is currently in use."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        try:
            s.connect((host, port))
            return True
        except (ConnectionRefusedError, socket.timeout, OSError):
            return False


def kill_process_on_port(port):
    """Kill any process listening on the given port (Windows)."""
    try:
        # Use netstat to find the PID
        result = subprocess.run(
            ['netstat', '-ano'],
            capture_output=True, text=True, timeout=5
        )
        for line in result.stdout.splitlines():
            # Look for LISTENING on our port
            if f":{port}" in line and "LISTENING" in line:
                parts = line.split()
                pid = int(parts[-1])
                if pid > 0:
                    print(f"[hallelujah-ai] Killing stale process on port {port} (PID {pid})...")
                    try:
                        subprocess.run(
                            ['taskkill', '/PID', str(pid), '/F'],
                            capture_output=True, timeout=5
                        )
                        # Wait for port to free up
                        for _ in range(10):
                            time.sleep(0.5)
                            if not is_port_in_use(port):
                                print(f"[hallelujah-ai] Port {port} is now free.")
                                return True
                    except Exception as e:
                        print(f"[hallelujah-ai] Could not kill PID {pid}: {e}")
        return False
    except Exception as e:
        print(f"[hallelujah-ai] Port cleanup error: {e}")
        return False


def ensure_port_free(port, host="127.0.0.1"):
    """Make sure the port is free, killing stale processes if needed."""
    if not is_port_in_use(port, host):
        return True

    print(f"[hallelujah-ai] Port {port} is in use. Attempting cleanup...")

    # First try: check if it's our own server already running healthy
    try:
        import urllib.request
        resp = urllib.request.urlopen(f"http://{host}:{port}/health", timeout=2)
        data = resp.read().decode()
        if "bible_bound" in data:
            print(f"[hallelujah-ai] Existing Hallelujah AI server detected. Killing to restart fresh...")
            kill_process_on_port(port)
            time.sleep(1)
            if not is_port_in_use(port, host):
                return True
    except Exception:
        pass

    # Second try: force kill whatever's on the port
    kill_process_on_port(port)
    time.sleep(1)

    # Final check
    if is_port_in_use(port, host):
        print(f"[hallelujah-ai] WARNING: Port {port} still in use after cleanup.")
        print(f"[hallelujah-ai] Chat features may be unavailable.")
        return False

    return True


# ── Ollama Management ───────────────────────────────────────
def ensure_ollama_running():
    """Make sure Ollama is running. Start it if not."""
    try:
        import urllib.request
        resp = urllib.request.urlopen("http://localhost:11434/api/tags", timeout=3)
        data = resp.read().decode()
        print("[hallelujah-ai] Ollama is running.")
        return True
    except Exception:
        print("[hallelujah-ai] Ollama not responding. Attempting to start...")
        try:
            # Try to start Ollama
            subprocess.Popen(
                ['ollama', 'serve'],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                creationflags=subprocess.CREATE_NO_WINDOW if hasattr(subprocess, 'CREATE_NO_WINDOW') else 0
            )
            # Wait for it to come up
            for i in range(15):
                time.sleep(1)
                try:
                    urllib.request.urlopen("http://localhost:11434/api/tags", timeout=2)
                    print("[hallelujah-ai] Ollama started successfully.")
                    return True
                except Exception:
                    pass
            print("[hallelujah-ai] Ollama did not start in time.")
            return False
        except FileNotFoundError:
            print("[hallelujah-ai] Ollama not installed. Chat features will be unavailable.")
            print("[hallelujah-ai] Download from: https://ollama.com/download")
            return False
        except Exception as e:
            print(f"[hallelujah-ai] Could not start Ollama: {e}")
            return False


# ── Start Hallelujah AI Backend Server ────────────────────
server_thread = None
server_started = False
server_ready = threading.Event()


def start_backend():
    """Start the FastAPI backend in a background thread."""
    global server_started
    try:
        # Add project root to path so imports work
        if BASE_DIR not in sys.path:
            sys.path.insert(0, BASE_DIR)

        from server.config import SERVER_HOST, SERVER_PORT
        import uvicorn

        print(f"[hallelujah-ai] Starting backend on {SERVER_HOST}:{SERVER_PORT}...")
        server_started = True
        server_ready.set()
        uvicorn.run(
            "server.main:app",
            host=SERVER_HOST,
            port=SERVER_PORT,
            log_level="warning",
            access_log=False
        )
    except ImportError as e:
        print(f"[hallelujah-ai] Backend dependencies not installed: {e}")
        print("[hallelujah-ai] Install with: pip install fastapi uvicorn httpx pyyaml")
        print("[hallelujah-ai] Chat features will be unavailable.")
        server_ready.set()  # Unblock the main thread even on failure
    except Exception as e:
        print(f"[hallelujah-ai] Backend error: {e}")
        server_ready.set()


def wait_for_server(timeout=15):
    """Wait for the backend server to be ready."""
    import urllib.request
    from server.config import SERVER_HOST, SERVER_PORT
    url = f"http://{SERVER_HOST}:{SERVER_PORT}/health"
    start = time.time()
    while time.time() - start < timeout:
        try:
            resp = urllib.request.urlopen(url, timeout=2)
            data = resp.read().decode()
            if "running" in data:
                print("[hallelujah-ai] Backend server ready!")
                return True
        except Exception:
            time.sleep(0.5)
    print("[hallelujah-ai] Backend server did not respond in time. Chat may be slow to connect.")
    return False


# ── PyWebView JS-API Bridge ──────────────────────────────
# This lets the launcher/chat pages call Python functions for navigation
# (needed to switch between http:// served pages and file:// study HTML)

class Api:
    """JavaScript-accessible API for PyWebView navigation."""

    def navigate(self, target):
        """Navigate the window to a different page.

        Called from launcher.html: window.pywebview.api.navigate('study')
        Called from chat.html:     window.pywebview.api.navigate('launcher')
        """
        global window
        if target == 'study':
            # Load the built study HTML (file:// URL)
            study_url = 'file:///' + html_path.replace('\\', '/')
            print(f"[hallelujah-ai] Navigating to Study App...")
            window.load_url(study_url)
        elif target == 'launcher':
            # Back to the launcher hub
            launcher_url = f'http://{SERVER_HOST}:{SERVER_PORT}/'
            print(f"[hallelujah-ai] Navigating to Launcher Hub...")
            window.load_url(launcher_url)
        elif target == 'chat':
            # Full-screen chat
            chat_url = f'http://{SERVER_HOST}:{SERVER_PORT}/chat'
            print(f"[hallelujah-ai] Navigating to Full Chat...")
            window.load_url(chat_url)
        else:
            print(f"[hallelujah-ai] Unknown navigation target: {target}")

    def get_study_url(self):
        """Return the study app URL (for fallback navigation)."""
        return 'file:///' + html_path.replace('\\', '/')


# ── Main Startup Sequence ──────────────────────────────────
print()
print("=" * 60)
print("  HALLELUJAH AI — Bible-Bound Study Assistant")
print("  \"The fear of YHWH is the beginning of wisdom\"")
print("=" * 60)
print()

# Step 1: Ensure Ollama is running
ollama_ok = ensure_ollama_running()

# Step 2: Free the port if needed
try:
    if BASE_DIR not in sys.path:
        sys.path.insert(0, BASE_DIR)
    from server.config import SERVER_HOST, SERVER_PORT
    port_ok = ensure_port_free(SERVER_PORT, SERVER_HOST)
except ImportError:
    SERVER_PORT = 8741
    SERVER_HOST = "127.0.0.1"
    port_ok = ensure_port_free(SERVER_PORT, SERVER_HOST)

# Step 3: Start backend in background thread
if port_ok:
    try:
        server_thread = threading.Thread(target=start_backend, daemon=True)
        server_thread.start()
        # Wait for the server thread to signal it's starting
        server_ready.wait(timeout=5)
        if server_started:
            wait_for_server(timeout=15)
    except Exception as e:
        print(f"[hallelujah-ai] Could not start backend: {e}")
else:
    print("[hallelujah-ai] Skipping backend startup (port unavailable).")
    print("[hallelujah-ai] Chat features will be unavailable this session.")

# Step 4: Launch PyWebView Window
try:
    import webview
except ImportError:
    print()
    print("pywebview not installed. Install with: pip install pywebview")
    print("Falling back to browser...")
    import webbrowser
    if server_started:
        # Open the launcher in browser
        webbrowser.open(f'http://{SERVER_HOST}:{SERVER_PORT}/')
        print()
        print("[hallelujah-ai] Server running. Press Ctrl+C to stop.")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass
    else:
        webbrowser.open('file:///' + html_path.replace('\\', '/'))
    sys.exit(0)

# Create the JS-API bridge
api = Api()

# Determine the startup URL
if server_started:
    # Open the launcher hub (served by FastAPI)
    startup_url = f'http://{SERVER_HOST}:{SERVER_PORT}/'
    print()
    print("[launch] Opening Hallelujah AI Launcher Hub...")
    print("[launch] Choose 'Chat About Something' or 'Explore, Study, Research'")
else:
    # Fallback: open the study app directly
    startup_url = 'file:///' + html_path.replace('\\', '/')
    print()
    print("[launch] Opening Study App (backend unavailable)...")

print()

window = webview.create_window(
    'Hallelujah AI',
    url=startup_url,
    js_api=api,
    width=1400,
    height=900,
    min_size=(800, 600),
    text_select=True
)
webview.start()

# Clean shutdown
print()
print("[hallelujah-ai] Window closed. Shutting down...")
print("[hallelujah-ai] Hallelujah. All glory to the Most High.")
