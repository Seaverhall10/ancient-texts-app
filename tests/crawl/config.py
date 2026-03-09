# ═══════════════════════════════════════════════════════════════
# Agent Crawl — Configuration
# ═══════════════════════════════════════════════════════════════

import os

# ── Paths ────────────────────────────────────────────────────
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
BUILD_SCRIPT = os.path.join(PROJECT_ROOT, 'build.py')
BUILD_MOBILE_SCRIPT = os.path.join(PROJECT_ROOT, 'build_mobile.py')
OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'output')
DESKTOP_HTML = os.path.join(OUTPUT_DIR, 'AncientTextsStudy.html')
MOBILE_DIR = os.path.join(OUTPUT_DIR, 'mobile')
MOBILE_INDEX = os.path.join(MOBILE_DIR, 'index.html')

SUITES_DIR = os.path.join(os.path.dirname(__file__), 'suites')
PROMPTS_DIR = os.path.join(os.path.dirname(__file__), 'prompts')
RESULTS_DIR = os.path.join(os.path.dirname(__file__), 'results')

# ── Servers ──────────────────────────────────────────────────
# Matches .claude/launch.json server configurations
DESKTOP_PORT = 8765
MOBILE_PORT = 8766
DESKTOP_URL = f'http://localhost:{DESKTOP_PORT}'
MOBILE_URL = f'http://localhost:{MOBILE_PORT}'

# ── Timeouts (seconds) ──────────────────────────────────────
PAGE_LOAD_TIMEOUT = 10
OVERLAY_TIMEOUT = 5
INTERACTION_DELAY = 0.5
MOBILE_BOOTSTRAP_TIMEOUT = 15

# ── Test Thresholds ─────────────────────────────────────────
MAX_CONSOLE_ERRORS = 0
MAX_LOAD_TIME_DESKTOP = 3.0    # seconds
MAX_LOAD_TIME_MOBILE = 5.0     # seconds
MAX_MEMORY_MB = 200
MIN_GLOSSARY_TERMS = 500
MIN_MATRIX_RELIGIONS = 50
MIN_LIBRARY_TEXTS = 70
GENESIS_ERA_COUNT = 16
HEBREW_LETTER_COUNT = 22

# ── Suite Order ─────────────────────────────────────────────
SUITE_ORDER = [
    '01_smoke',
    '02_navigation',
    '03_overlays',
    '04_interlinear',
    '05_search',
    '06_content',
    '07_mobile',
    '08_performance',
]
