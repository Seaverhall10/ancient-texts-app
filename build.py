"""
build.py — Assemble AncientTexts.html from data files + CSS + JS.

Reads:
  manifest.json              (text/era definitions, category metadata)
  data/<text>/era_*.py       (chapter data per era, auto-discovered)
  data/<text>/chapters/*.html (HTML fragments for thematic texts)
  data/glossary.py           (multi-language term glossary)
  data/<text>/interlinear*.py (interlinear data per text, optional)
  src/css/styles.css         (dark theme stylesheet)
  src/js/app.js              (IIFE application controller)

Outputs:
  output/AncientTextsStudy.html   (single self-contained file)
  Also copies to Desktop

Build profiles:
  python build.py                              # full library
  python build.py --profile sons-of-god        # Gen, Exod, 1 Enoch, Giants, Jubilees, Jasher + HC
  python build.py --profile full-with-thematic # everything including thematic studies
  python build.py --texts genesis,exodus       # specific texts only
"""
import os
import sys
import json
import shutil
import importlib.util
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE, "data")
SRC_CSS = os.path.join(BASE, "src", "css", "styles.css")
SRC_JS = os.path.join(BASE, "src", "js", "app.js")
MANIFEST_PATH = os.path.join(BASE, "manifest.json")
OUTPUT_DIR = os.path.join(BASE, "output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "AncientTextsStudy.html")
DESKTOP = os.path.join(os.path.expanduser("~"), "Desktop", "AncientTextsStudy.html")

# Build profiles: named sets of texts to include
PROFILES = {
    "full": None,  # None = include everything
    "sons-of-god": ["genesis", "exodus", "1enoch", "giants", "jubilees", "jasher", "genesis_apocryphon", "heavenly_court"],
    "canon-only": ["genesis", "exodus"],
    "dss": ["genesis", "exodus", "1enoch", "giants", "genesis_apocryphon", "dss_sectarian"],
    "full-with-thematic": None,  # None = include everything (same as full, explicit name for clarity)
}


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def load_module(name, path):
    """Dynamically load a Python data module and return it."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


RELEASE_MODE = False

def parse_args():
    """Parse command-line arguments."""
    global RELEASE_MODE
    profile = "full"
    text_filter = None

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--profile" and i + 1 < len(args):
            profile = args[i + 1]
            i += 2
        elif args[i] == "--texts" and i + 1 < len(args):
            text_filter = [t.strip() for t in args[i + 1].split(",")]
            i += 2
        elif args[i] == "--release":
            RELEASE_MODE = True
            i += 1
        else:
            i += 1

    if text_filter:
        return text_filter
    if profile in PROFILES and PROFILES[profile] is not None:
        return PROFILES[profile]
    return None  # None = include all


def build():
    text_filter = parse_args()

    print("=" * 60)
    print("  ANCIENT TEXTS LIBRARY \u2014 Build System")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    if text_filter:
        print(f"  Profile: {text_filter}")
    print("=" * 60)

    # \u2500\u2500 Load manifest \u2500\u2500
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)
    manifest["build_date"] = datetime.now().strftime("%Y-%m-%d")

    # Filter texts if profile specified
    all_texts = manifest.get("texts", [])
    if text_filter:
        all_texts = [t for t in all_texts if t["id"] in text_filter]
        manifest["texts"] = all_texts

    active_text_ids = {t["id"] for t in all_texts}

    # Filter eras to only include active texts
    manifest["eras"] = [e for e in manifest["eras"] if e.get("text") in active_text_ids]

    print(f"\n[manifest] {len(all_texts)} texts, {len(manifest['eras'])} eras")

    # \u2500\u2500 Load era data files (auto-discover from text subdirs) \u2500\u2500
    era_data = {}
    total_chapters = 0
    total_inserts = 0
    total_fragments = 0

    for era in manifest["eras"]:
        text_id = era.get("text")
        text_def = next((t for t in all_texts if t["id"] == text_id), None)
        if not text_def:
            continue

        # Skip html_fragment eras — handled separately below
        if era.get("content_type") == "html_fragment":
            continue

        data_dir = text_def.get("data_dir", text_id)
        data_file = os.path.join(DATA_DIR, data_dir, era["data_file"] + ".py")

        # Fallback: try flat data/ dir (backward compat during migration)
        if not os.path.exists(data_file):
            data_file = os.path.join(DATA_DIR, era["data_file"] + ".py")

        if not os.path.exists(data_file):
            print(f"  WARNING: {era['data_file']}.py not found \u2014 skipping")
            era_data[era["id"]] = []
            continue

        mod = load_module(era["data_file"], data_file)
        chapters = getattr(mod, "CHAPTERS", [])
        era_data[era["id"]] = chapters

        ch_count = sum(1 for c in chapters if c.get("type") in ("chapter", "study"))
        ins_count = sum(1 for c in chapters if c.get("type") == "historical_insert")
        total_chapters += ch_count
        total_inserts += ins_count
        print(f"  [{era['id']:28s}] {ch_count} chapters, {ins_count} inserts")

    # \u2500\u2500 Load HTML fragment eras (thematic texts like Heavenly Court) \u2500\u2500
    for era in manifest["eras"]:
        if era.get("content_type") != "html_fragment":
            continue

        text_id = era.get("text")
        text_def = next((t for t in all_texts if t["id"] == text_id), None)
        if not text_def:
            continue

        data_dir = text_def.get("data_dir", text_id)
        fragments = era.get("fragments", [])
        era_entries = []
        frag_count = 0

        for frag in fragments:
            frag_path = os.path.join(DATA_DIR, data_dir, "chapters", frag["file"])
            if not os.path.exists(frag_path):
                print(f"  WARNING: fragment {frag['file']} not found \u2014 skipping")
                era_entries.append({
                    "id": frag["id"],
                    "type": "html_fragment",
                    "ref": frag.get("ref", ""),
                    "title": frag.get("title", ""),
                    "html": f"<article class=\"chapter\"><p>Fragment not found: {frag['file']}</p></article>"
                })
                continue

            html_content = read_file(frag_path)
            era_entries.append({
                "id": frag["id"],
                "type": "html_fragment",
                "ref": frag.get("ref", ""),
                "title": frag.get("title", ""),
                "html": html_content
            })
            frag_count += 1

        era_data[era["id"]] = era_entries
        total_fragments += frag_count
        print(f"  [{era['id']:28s}] {frag_count} fragments (html)")

    print(f"\n  Total: {total_chapters} chapters, {total_inserts} historical inserts, {total_fragments} html fragments")

    # \u2500\u2500 Load glossary \u2500\u2500
    # \u2500\u2500 Load text introductions (info.py per text) \u2500\u2500
    text_intros = {}
    for text_def in all_texts:
        data_dir = text_def.get("data_dir", text_def["id"])
        info_path = os.path.join(DATA_DIR, data_dir, "info.py")
        if os.path.exists(info_path):
            info_mod = load_module(f"info_{text_def['id']}", info_path)
            info = getattr(info_mod, "TEXT_INFO", None)
            if info:
                text_intros[text_def["id"]] = info
    print(f"[intros] {len(text_intros)} text introductions loaded: {', '.join(text_intros.keys()) if text_intros else 'none'}")

    glossary_path = os.path.join(DATA_DIR, "glossary.py")
    glossary_mod = load_module("glossary", glossary_path)
    glossary = getattr(glossary_mod, "GLOSSARY", {})
    print(f"[glossary] {len(glossary)} terms loaded")

    # \u2500\u2500 Load interlinear data per text \u2500\u2500
    interlinear_data = {}  # {constant_name: data}
    for text_def in all_texts:
        il_const = text_def.get("interlinear")
        if not il_const:
            continue

        data_dir = text_def.get("data_dir", text_def["id"])

        # Try text subdir first, then flat dir
        il_files = []
        text_data_dir = os.path.join(DATA_DIR, data_dir)
        if os.path.isdir(text_data_dir):
            for f in os.listdir(text_data_dir):
                if f.startswith("interlinear") and f.endswith(".py"):
                    il_files.append(os.path.join(text_data_dir, f))

        # Fallback: flat data/ dir — check standard names and NT variant
        if not il_files:
            candidates = []
            if text_def["id"] == "genesis":
                candidates.append(os.path.join(DATA_DIR, "interlinear.py"))
            candidates.append(os.path.join(DATA_DIR, f"interlinear_{text_def['id']}.py"))
            candidates.append(os.path.join(DATA_DIR, f"interlinear_nt_{text_def['id']}.py"))
            for candidate in candidates:
                if os.path.exists(candidate):
                    il_files.append(candidate)
                    break  # use first match

        for il_path in il_files:
            mod_name = os.path.splitext(os.path.basename(il_path))[0]
            il_mod = load_module(mod_name, il_path)

            # Try multiple constant name patterns
            il = None
            for attr_name in [il_const, "INTERLINEAR", f"INTERLINEAR_{text_def['id'].upper()}"]:
                il = getattr(il_mod, attr_name, None)
                if il:
                    break
            if not il:
                # Try any dict attribute
                for attr in dir(il_mod):
                    if attr.startswith("INTERLINEAR"):
                        il = getattr(il_mod, attr)
                        break

            if il:
                interlinear_data[il_const] = il
                total_words = sum(
                    sum(len(v["words"]) for v in ch["verses"])
                    for ch in il.values()
                )
                print(f"[interlinear-{text_def['id']}] {len(il)} chapters, {total_words:,} words")

    # \u2500\u2500 Load and merge flow translations \u2500\u2500
    flow_dir = os.path.join(DATA_DIR, "flow")
    if os.path.isdir(flow_dir):
        for flow_file in sorted(os.listdir(flow_dir)):
            if flow_file.startswith("flow_") and flow_file.endswith(".py") and flow_file.count("_") == 1:
                book_name = flow_file.replace("flow_", "").replace(".py", "")
                flow_path = os.path.join(flow_dir, flow_file)
                try:
                    flow_mod = load_module(flow_file.replace(".py", ""), flow_path)
                except Exception as e:
                    print(f"[flow-{book_name}] SKIP — {e}")
                    continue
                flow_data = getattr(flow_mod, f"FLOW_{book_name.upper()}", None)
                if not flow_data:
                    for attr in dir(flow_mod):
                        if attr.startswith("FLOW"):
                            flow_data = getattr(flow_mod, attr)
                            break
                # Also load notes if available
                notes_data = getattr(flow_mod, f"NOTES_{book_name.upper()}", None)
                if not notes_data:
                    for attr in dir(flow_mod):
                        if attr.startswith("NOTES"):
                            notes_data = getattr(flow_mod, attr)
                            break
                if flow_data:
                    il_const = f"INTERLINEAR_{book_name.upper()}"
                    il = interlinear_data.get(il_const)
                    # Also check NT prefix (INTERLINEAR_NT_2JOHN etc.)
                    if il is None:
                        il_const_nt = f"INTERLINEAR_NT_{book_name.upper()}"
                        il = interlinear_data.get(il_const_nt)
                    if il:
                        merged = 0
                        notes_merged = 0
                        for ch_key, ch_data in il.items():
                            ch_num = int(ch_key) if isinstance(ch_key, str) else ch_key
                            ch_flows = flow_data.get(ch_num, {})
                            ch_notes = notes_data.get(ch_num, {}) if notes_data else {}
                            if ch_flows or ch_notes:
                                for verse in ch_data.get("verses", []):
                                    v_flow = ch_flows.get(verse["num"])
                                    if v_flow:
                                        verse["flow"] = v_flow
                                        merged += 1
                                    v_note = ch_notes.get(verse["num"])
                                    if v_note:
                                        verse["note"] = v_note
                                        notes_merged += 1
                        notes_str = f", {notes_merged} notes" if notes_merged else ""
                        print(f"[flow-{book_name}] {merged} verse translations{notes_str} merged")

    # \u2500\u2500 Read CSS \u2500\u2500
    css = read_file(SRC_CSS)
    print(f"[css] styles.css ({len(css):,} chars)")

    # \u2500\u2500 Read JS and inject data \u2500\u2500
    js = read_file(SRC_JS)
    js = js.replace("__MANIFEST_DATA__", json.dumps(manifest, ensure_ascii=False))
    js = js.replace("__ERA_DATA__", json.dumps(era_data, ensure_ascii=False))
    js = js.replace("__GLOSSARY_DATA__", json.dumps(glossary, ensure_ascii=False))
    js = js.replace("__TEXT_INTROS_DATA__", json.dumps(text_intros, ensure_ascii=False))

    # Inject Prophecy Matrix data
    prophecy_path = os.path.join(DATA_DIR, "prophecy_matrix.py")
    prophecy_data = []
    if os.path.exists(prophecy_path):
        pm_mod = load_module("prophecy_matrix", prophecy_path)
        prophecy_data = getattr(pm_mod, "PROPHECY_MATRIX", [])
        print(f"[prophecy] {len(prophecy_data)} prophecy entries loaded")
    js = js.replace("__PROPHECY_DATA__", json.dumps(prophecy_data, ensure_ascii=False))

    # Inject Prophecy Tracker (per-book) data
    tracker_path = os.path.join(DATA_DIR, "prophecy_tracker.py")
    tracker_data = {}
    if os.path.exists(tracker_path):
        pt_mod = load_module("prophecy_tracker", tracker_path)
        tracker_data = getattr(pt_mod, "BOOK_PROPHECIES", {})
        total_props = sum(b.get("prophecy_count", 0) for b in tracker_data.values())
        print(f"[prophecy-tracker] {len(tracker_data)} books, {total_props} prophecies loaded")
    js = js.replace("__PROPHECY_TRACKER_DATA__", json.dumps(tracker_data, ensure_ascii=False))

    # Inject Resources data
    resources_path = os.path.join(DATA_DIR, "resources.py")
    resources_data = []
    if os.path.exists(resources_path):
        res_mod = load_module("resources", resources_path)
        resources_data = getattr(res_mod, "RESOURCES", [])
        print(f"[resources] {len(resources_data)} study resources loaded")
    js = js.replace("__RESOURCES_DATA__", json.dumps(resources_data, ensure_ascii=False))

    # Inject Core Beliefs data
    beliefs_path = os.path.join(DATA_DIR, "core_beliefs.py")
    beliefs_data = {}
    if os.path.exists(beliefs_path):
        cb_mod = load_module("core_beliefs", beliefs_path)
        beliefs_data = getattr(cb_mod, "CORE_BELIEFS", {})
        if isinstance(beliefs_data, list):
            # Flat list of topics — count by category
            categories = set(t.get("category", "") for t in beliefs_data)
            print(f"[core-beliefs] {len(categories)} categories, {len(beliefs_data)} topics loaded")
        else:
            cats = beliefs_data.get("categories", [])
            topics = sum(len(c.get("topics", [])) for c in cats)
            print(f"[core-beliefs] {len(cats)} categories, {topics} topics loaded")
    js = js.replace("__CORE_BELIEFS_DATA__", json.dumps(beliefs_data, ensure_ascii=False))

    # Inject Religions Detail data (for Bible Truth Matrix click-through views)
    religions_path = os.path.join(DATA_DIR, "religions_data.py")
    religions_detail = {}
    if os.path.exists(religions_path):
        rel_mod = load_module("religions_data", religions_path)
        religions_detail = getattr(rel_mod, "RELIGIONS_DETAIL", {})
        print(f"[religions] {len(religions_detail)} religion profiles loaded")
    js = js.replace("__RELIGIONS_DETAIL_DATA__", json.dumps(religions_detail, ensure_ascii=False))

    # Inject interlinear data per text (OT Hebrew + NT Greek)
    il_books = [
        ("GENESIS", "__INTERLINEAR_DATA__"),
        ("EXODUS", "__INTERLINEAR_EXODUS_DATA__"),
        ("LEVITICUS", "__INTERLINEAR_LEVITICUS_DATA__"),
        ("NUMBERS", "__INTERLINEAR_NUMBERS_DATA__"),
        ("DEUTERONOMY", "__INTERLINEAR_DEUTERONOMY_DATA__"),
        ("JOSHUA", "__INTERLINEAR_JOSHUA_DATA__"),
        ("JUDGES", "__INTERLINEAR_JUDGES_DATA__"),
        ("RUTH", "__INTERLINEAR_RUTH_DATA__"),
        ("1SAMUEL", "__INTERLINEAR_1SAMUEL_DATA__"),
        ("2SAMUEL", "__INTERLINEAR_2SAMUEL_DATA__"),
        ("1KINGS", "__INTERLINEAR_1KINGS_DATA__"),
        ("2KINGS", "__INTERLINEAR_2KINGS_DATA__"),
        ("PSALMS", "__INTERLINEAR_PSALMS_DATA__"),
        ("ISAIAH", "__INTERLINEAR_ISAIAH_DATA__"),
        ("DANIEL", "__INTERLINEAR_DANIEL_DATA__"),
        # NT Greek (27 books)
        ("NT_MATTHEW",        "__INTERLINEAR_NT_MATTHEW_DATA__"),
        ("NT_MARK",           "__INTERLINEAR_NT_MARK_DATA__"),
        ("NT_LUKE",           "__INTERLINEAR_NT_LUKE_DATA__"),
        ("NT_JOHN",           "__INTERLINEAR_NT_JOHN_DATA__"),
        ("NT_ACTS",           "__INTERLINEAR_NT_ACTS_DATA__"),
        ("NT_ROMANS",         "__INTERLINEAR_NT_ROMANS_DATA__"),
        ("NT_1CORINTHIANS",   "__INTERLINEAR_NT_1CORINTHIANS_DATA__"),
        ("NT_2CORINTHIANS",   "__INTERLINEAR_NT_2CORINTHIANS_DATA__"),
        ("NT_GALATIANS",      "__INTERLINEAR_NT_GALATIANS_DATA__"),
        ("NT_EPHESIANS",      "__INTERLINEAR_NT_EPHESIANS_DATA__"),
        ("NT_PHILIPPIANS",    "__INTERLINEAR_NT_PHILIPPIANS_DATA__"),
        ("NT_COLOSSIANS",     "__INTERLINEAR_NT_COLOSSIANS_DATA__"),
        ("NT_1THESSALONIANS", "__INTERLINEAR_NT_1THESSALONIANS_DATA__"),
        ("NT_2THESSALONIANS", "__INTERLINEAR_NT_2THESSALONIANS_DATA__"),
        ("NT_1TIMOTHY",       "__INTERLINEAR_NT_1TIMOTHY_DATA__"),
        ("NT_2TIMOTHY",       "__INTERLINEAR_NT_2TIMOTHY_DATA__"),
        ("NT_TITUS",          "__INTERLINEAR_NT_TITUS_DATA__"),
        ("NT_PHILEMON",       "__INTERLINEAR_NT_PHILEMON_DATA__"),
        ("NT_HEBREWS",        "__INTERLINEAR_NT_HEBREWS_DATA__"),
        ("NT_JAMES",          "__INTERLINEAR_NT_JAMES_DATA__"),
        ("NT_1PETER",         "__INTERLINEAR_NT_1PETER_DATA__"),
        ("NT_2PETER",         "__INTERLINEAR_NT_2PETER_DATA__"),
        ("NT_1JOHN",          "__INTERLINEAR_NT_1JOHN_DATA__"),
        ("NT_2JOHN",          "__INTERLINEAR_NT_2JOHN_DATA__"),
        ("NT_3JOHN",          "__INTERLINEAR_NT_3JOHN_DATA__"),
        ("NT_JUDE",           "__INTERLINEAR_NT_JUDE_DATA__"),
        ("NT_REVELATION",     "__INTERLINEAR_NT_REVELATION_DATA__"),
        # New OT books (24 books added March 2026)
        ("JOB",              "__INTERLINEAR_JOB_DATA__"),
        ("PROVERBS",         "__INTERLINEAR_PROVERBS_DATA__"),
        ("ECCLESIASTES",     "__INTERLINEAR_ECCLESIASTES_DATA__"),
        ("SONGOFSOLOMON",    "__INTERLINEAR_SONGOFSOLOMON_DATA__"),
        ("JEREMIAH",         "__INTERLINEAR_JEREMIAH_DATA__"),
        ("EZEKIEL",          "__INTERLINEAR_EZEKIEL_DATA__"),
        ("LAMENTATIONS",     "__INTERLINEAR_LAMENTATIONS_DATA__"),
        ("1CHRONICLES",      "__INTERLINEAR_1CHRONICLES_DATA__"),
        ("2CHRONICLES",      "__INTERLINEAR_2CHRONICLES_DATA__"),
        ("EZRA",             "__INTERLINEAR_EZRA_DATA__"),
        ("NEHEMIAH",         "__INTERLINEAR_NEHEMIAH_DATA__"),
        ("ESTHER",           "__INTERLINEAR_ESTHER_DATA__"),
        ("HOSEA",            "__INTERLINEAR_HOSEA_DATA__"),
        ("JOEL",             "__INTERLINEAR_JOEL_DATA__"),
        ("AMOS",             "__INTERLINEAR_AMOS_DATA__"),
        ("OBADIAH",          "__INTERLINEAR_OBADIAH_DATA__"),
        ("JONAH",            "__INTERLINEAR_JONAH_DATA__"),
        ("MICAH",            "__INTERLINEAR_MICAH_DATA__"),
        ("NAHUM",            "__INTERLINEAR_NAHUM_DATA__"),
        ("HABAKKUK",         "__INTERLINEAR_HABAKKUK_DATA__"),
        ("ZEPHANIAH",        "__INTERLINEAR_ZEPHANIAH_DATA__"),
        ("HAGGAI",           "__INTERLINEAR_HAGGAI_DATA__"),
        ("ZECHARIAH",        "__INTERLINEAR_ZECHARIAH_DATA__"),
        ("MALACHI",          "__INTERLINEAR_MALACHI_DATA__"),
    ]
    for book_key, placeholder in il_books:
        il_data = interlinear_data.get(f"INTERLINEAR_{book_key}", {})
        js = js.replace(placeholder, json.dumps(il_data, ensure_ascii=False))

    # Strip Hallelujah AI module in release mode
    if RELEASE_MODE:
        import re
        hai_marker = '//  HALLELUJAH AI'
        hai_start = js.find(hai_marker)
        if hai_start > 0:
            # Back up to the decorator line
            hai_start = js.rfind('// ', 0, hai_start)
            hai_start = max(0, js.rfind('\n', 0, hai_start)) + 1
            # Find the Launch section
            hai_end = js.find("// \u2500\u2500 Launch", hai_start)
            if hai_end > 0:
                removed = hai_end - hai_start
                js = js[:hai_start] + '\n    // [Hallelujah AI removed in release build]\n\n    ' + js[hai_end:]
                print(f"[release] Stripped Hallelujah AI module ({removed:,} chars removed)")
        # Remove initHallelujahChat() call
        js = js.replace('initHallelujahChat();', '// [HAI removed in release]')
        # Inject IS_RELEASE flag at top of JS
        js = '    var IS_RELEASE = true;\n' + js
        print("[release] Release build mode active")

    print(f"[js]  app.js ({len(js):,} chars after injection)")

    # \u2500\u2500 Assemble HTML \u2500\u2500
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{manifest['title']} &mdash; {manifest['subtitle']}</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <style>
{css}
    </style>
</head>
<body>
    <!-- Skip to content (accessibility) -->
    <a class="skip-to-content" href="#mainContent">Skip to content</a>

    <button class="sidebar-toggle" id="sidebarToggle" aria-label="Toggle sidebar menu">&#9776;</button>
    <div class="sidebar-backdrop" id="sidebarBackdrop" role="presentation"></div>

    <div class="app-container">
        <aside class="sidebar" id="sidebar" role="navigation" aria-label="Library navigation">
            <div class="sidebar-header">
                <h1>{manifest['title']}</h1>
                <div class="subtitle">{manifest['subtitle']}</div>
            </div>

            <div class="search-container" role="search">
                <input type="text" class="search-input" id="searchInput"
                       placeholder="Search... (Ctrl+K)" autocomplete="off"
                       aria-label="Search all texts">
                <div class="search-results" id="searchResults" role="listbox" aria-label="Search results"></div>
            </div>

            <nav class="sidebar-nav" id="sidebarNav" role="tree" aria-label="Text navigation"></nav>

            <div class="sidebar-footer">
                <button class="sidebar-btn" id="mapBtn" aria-label="Open ancient world map">
                    <span aria-hidden="true">&#x1F5FA;</span> Ancient World Map
                </button>
                <button class="sidebar-btn" id="glossaryBtn" aria-label="Open glossary">
                    <span aria-hidden="true">&#x1F4D6;</span> Glossary
                </button>
                <button class="sidebar-btn" id="hebrewBtn" aria-label="Learn to read Hebrew">
                    <span aria-hidden="true">&#x05D0;</span> Learn Hebrew
                </button>
                <button class="sidebar-btn" id="resourcesBtn" aria-label="Open study resources">
                    <span aria-hidden="true">&#x1F3AC;</span> Resources
                </button>
                <button class="sidebar-btn" id="matrixBtn" aria-label="Open Bible truth matrix">
                    <span aria-hidden="true">&#x2727;</span> Bible Truth Matrix
                </button>
                <button class="sidebar-btn" id="timelineBtn" aria-label="Open biblical timeline">
                    <span aria-hidden="true">&#x1F551;</span> Biblical Timeline
                </button>
                <button class="sidebar-btn" id="progressBtn" aria-label="Open developer progress">
                    <span aria-hidden="true">&#x1F4CA;</span> Developer Progress
                </button>
                <button class="help-shortcut-btn" id="shortcutHelpBtn" aria-label="Keyboard shortcuts">
                    Keyboard Shortcuts <kbd>?</kbd>
                </button>
                <div class="bookmarks-section">
                    <h4>Bookmarks</h4>
                    <div id="bookmarksContainer" aria-label="Saved bookmarks"></div>
                </div>
            </div>
        </aside>

        <div class="resize-handle" id="sidebarHandle" data-target="sidebar"></div>

        <main class="main-content" id="mainContent" role="main" tabindex="-1">
            <div class="era-header">
                <h2>Loading...</h2>
            </div>
        </main>

        <!-- Study View Controls (toggle callout sections) -->
        <div class="study-controls" id="studyControls">
            <button class="study-toggle active" data-toggle="hebrew-terms" title="Toggle Hebrew term boxes">Hebrew</button>
            <button class="study-toggle active" data-toggle="ane-callout" title="Toggle ANE context boxes">ANE</button>
            <button class="study-toggle active" data-toggle="second-temple" title="Toggle Second Temple boxes">2nd Temple</button>
            <button class="study-toggle active" data-toggle="council-note" title="Toggle Divine Council notes">Council</button>
            <button class="study-toggle active" data-toggle="cross-refs" title="Toggle cross references">Xrefs</button>
        </div>

        <div class="resize-handle" id="paneHandle" data-target="pane"></div>

        <!-- Interlinear Reading Pane -->
        <div class="reading-pane" id="readingPane">
        <div class="reading-pane-header">
            <div class="reading-pane-title-row">
                <button class="il-nav-btn" id="ilPrev" title="Previous chapter">&#x25C0;</button>
                <select class="il-book-select" id="ilBookSelect" title="Switch interlinear book"></select>
                <span class="il-lang-badge" id="ilLangBadge">HEBREW</span>
                <h3 id="readingPaneTitle">Genesis 1</h3>
                <button class="il-nav-btn" id="ilNext" title="Next chapter">&#x25B6;</button>
            </div>
            <div class="reading-pane-controls">
                <button class="sync-btn" id="syncToPane"
                        title="Sync reading pane to study chapter">Sync &#x25B6;</button>
                <button class="sync-btn" id="syncToStudy"
                        title="Sync study content to this chapter">&#x25C0; Sync</button>
                <div class="font-size-controls">
                    <button class="font-size-btn" id="fontDecrease" title="Decrease font size">A-</button>
                    <span class="font-size-label" id="fontSizeLabel">100%</span>
                    <button class="font-size-btn" id="fontIncrease" title="Increase font size">A+</button>
                </div>
                <div class="il-copy-menu">
                    <button class="il-copy-btn" id="ilCopyBtn">&#x1F4CB; Copy</button>
                    <div class="il-copy-dropdown" id="ilCopyDropdown">
                        <button class="il-copy-option" data-format="english">English Only</button>
                        <button class="il-copy-option" data-format="hebrew" id="ilCopyScript">Script Only</button>
                        <button class="il-copy-option" data-format="both" id="ilCopyBoth">English + Script</button>
                        <button class="il-copy-option" data-format="interlinear">Full Interlinear</button>
                    </div>
                </div>
                <select id="readingPaneMode" class="reading-pane-select">
                    <option value="full">Full Interlinear</option>
                    <option value="hebrew">Hebrew Only</option>
                    <option value="english">English Only</option>
                </select>
                <button class="reading-pane-expand" id="readingPaneExpand"
                        title="Expand reading pane (Alt+F)">&#x26F6;</button>
                <button class="reading-pane-close" id="readingPaneClose">&times;</button>
            </div>
        </div>
        <div class="reading-pane-options-row">
            <div class="user-mode-selector" role="radiogroup" aria-label="Reading mode">
                <button class="user-mode-btn" data-mode="reader" aria-pressed="false">Reader</button>
                <button class="user-mode-btn" data-mode="student" aria-pressed="false">Student</button>
                <button class="user-mode-btn active" data-mode="scholar" aria-pressed="true">Scholar</button>
            </div>
            <div class="il-row-toggles" aria-label="Visible interlinear rows">
                <button class="il-row-toggle active" data-row="translit" aria-pressed="true"><span class="toggle-dot"></span> Translit</button>
                <button class="il-row-toggle active" data-row="gloss" aria-pressed="true"><span class="toggle-dot"></span> Gloss</button>
                <button class="il-row-toggle active" data-row="morph" aria-pressed="true"><span class="toggle-dot"></span> Morph</button>
                <button class="il-row-toggle active" data-row="strongs" aria-pressed="true"><span class="toggle-dot"></span> Strong's</button>
                <button class="il-row-toggle active" data-row="flow" aria-pressed="true" title="Show flow translation (when available)"><span class="toggle-dot"></span> Flow</button>
                <button class="il-row-toggle" data-row="notes" aria-pressed="false" title="Show verse-by-verse study notes"><span class="toggle-dot"></span> Notes</button>
            </div>
            <button class="hc-toggle" id="hcToggle" aria-pressed="false" title="Toggle high contrast">HC</button>
            <div class="col-width-control" title="Adjust column widths">
                <span class="col-label">EN</span>
                <input type="range" id="colWidthSlider" min="0" max="100" value="42" class="col-slider">
                <span class="col-label">HE</span>
            </div>
        </div>
        <div class="reading-progress"><div class="reading-progress-bar" id="readingProgressBar"></div></div>
        <div class="reading-pane-content" id="readingPaneContent"></div>
        <div class="il-legend">
            <div class="il-legend-item"><span class="il-legend-dot" style="background:#6a9a78"></span>Verb</div>
            <div class="il-legend-item"><span class="il-legend-dot" style="background:#d4a574"></span>Noun</div>
            <div class="il-legend-item"><span class="il-legend-dot" style="background:#a3b18a"></span>Prep</div>
            <div class="il-legend-item"><span class="il-legend-dot" style="background:#7db4e0"></span>Conj</div>
            <div class="il-legend-item"><span class="il-legend-dot" style="background:#b794d4"></span>Adj</div>
            <div class="il-legend-item"><span class="il-legend-dot" style="background:#5eaaa8"></span>Pron</div>
            <div class="il-legend-item"><span class="il-legend-dot" style="background:#c9a84c"></span>Name</div>
        </div>
    </div>

    </div><!-- end .app-container -->

    <!-- Reading Pane Toggle -->
    <button class="reading-pane-toggle" id="readingPaneToggle"
            title="Toggle Interlinear Hebrew (Alt+H)"
            aria-label="Toggle interlinear Hebrew reading pane">&#x05E2;</button>

    <!-- Layout Presets -->
    <div class="layout-presets" id="layoutPresets">
        <button class="preset-btn" data-preset="study" title="Study Focus">&#x1F4D6;</button>
        <button class="preset-btn active" data-preset="split" title="Even Split">&#x25A3;</button>
        <button class="preset-btn" data-preset="interlinear" title="Interlinear Focus">&#x1F4DC;</button>
    </div>

    <!-- Word Popup -->
    <div class="word-popup" id="wordPopup"></div>

    <!-- Copy Toast -->
    <div class="copy-toast" id="copyToast">Copied!</div>

    <!-- Developer Progress Overlay -->
    <div class="progress-overlay" id="progressOverlay">
        <div class="progress-modal">
            <div class="progress-modal-header">
                <h2>Developer Progress</h2>
                <button class="progress-close" id="progressClose">&times;</button>
            </div>
            <div id="progressContent"></div>
        </div>
    </div>

    <!-- Bible Truth Matrix Overlay -->
    <div class="progress-overlay matrix-overlay" id="matrixOverlay">
        <div class="progress-modal matrix-modal">
            <div class="progress-modal-header">
                <h2>&#x2727; Bible Truth Matrix</h2>
                <p style="margin:0;font-size:0.82rem;color:var(--text-secondary)">How 52+ worldviews compare to biblical teaching across 13 doctrines &mdash; click any card to explore</p>
                <button class="progress-close" id="matrixClose">&times;</button>
            </div>
            <div id="matrixContent"></div>
        </div>
    </div>

    <!-- Religion Detail Overlay -->
    <div class="progress-overlay religion-detail-overlay" id="religionDetailOverlay">
        <div class="progress-modal religion-detail-modal">
            <div class="progress-modal-header religion-detail-header">
                <div id="religionDetailTitle"></div>
                <button class="progress-close" id="religionDetailClose">&times;</button>
            </div>
            <div id="religionDetailContent"></div>
        </div>
    </div>

    <!-- Biblical Timeline Overlay -->
    <div class="progress-overlay timeline-overlay" id="timelineOverlay">
        <div class="progress-modal timeline-modal">
            <div class="progress-modal-header">
                <h2>&#x1F551; Biblical &amp; World History Timeline</h2>
                <p style="margin:0;font-size:0.82rem;color:var(--text-secondary)">From Creation to the modern era &mdash; biblical events alongside world history</p>
                <button class="progress-close" id="timelineClose">&times;</button>
            </div>
            <div id="timelineContent"></div>
        </div>
    </div>

    <!-- Keyboard Shortcut Help Modal -->
    <div class="shortcut-help-overlay" id="shortcutHelp">
        <div class="shortcut-help-modal">
            <button class="shortcut-help-close" id="shortcutHelpClose">&times;</button>
            <h2>Keyboard Shortcuts</h2>
            <div class="shortcut-section">
                <h3>Navigation</h3>
                <div class="shortcut-row"><span class="shortcut-desc">Search texts &amp; verses</span><span class="shortcut-keys"><kbd>Ctrl</kbd><kbd>K</kbd></span></div>
                <div class="shortcut-row"><span class="shortcut-desc">Toggle sidebar</span><span class="shortcut-keys"><kbd>Alt</kbd><kbd>H</kbd></span></div>
                <div class="shortcut-row"><span class="shortcut-desc">Previous chapter</span><span class="shortcut-keys"><kbd>Alt</kbd><kbd>&#x2190;</kbd></span></div>
                <div class="shortcut-row"><span class="shortcut-desc">Next chapter</span><span class="shortcut-keys"><kbd>Alt</kbd><kbd>&#x2192;</kbd></span></div>
            </div>
            <div class="shortcut-section">
                <h3>Reading Pane</h3>
                <div class="shortcut-row"><span class="shortcut-desc">Fullscreen reading mode</span><span class="shortcut-keys"><kbd>Alt</kbd><kbd>F</kbd></span></div>
                <div class="shortcut-row"><span class="shortcut-desc">Toggle reading pane</span><span class="shortcut-keys"><kbd>Alt</kbd><kbd>L</kbd></span></div>
            </div>
            <div class="shortcut-section">
                <h3>Hallelujah AI</h3>
                <div class="shortcut-row"><span class="shortcut-desc">Toggle AI chat panel</span><span class="shortcut-keys"><kbd>Alt</kbd><kbd>A</kbd></span></div>
            </div>
            <div class="shortcut-section">
                <h3>General</h3>
                <div class="shortcut-row"><span class="shortcut-desc">Show this help</span><span class="shortcut-keys"><kbd>?</kbd></span></div>
                <div class="shortcut-row"><span class="shortcut-desc">Close any overlay</span><span class="shortcut-keys"><kbd>Esc</kbd></span></div>
            </div>
        </div>
    </div>

    <!-- Cross-Reference Drawer -->
    <div class="xref-drawer" id="xrefDrawer">
        <div class="xref-drawer-header">
            <h3 id="xrefTitle">Cross References</h3>
            <button class="xref-close" id="xrefClose">&times;</button>
        </div>
        <div class="xref-content" id="xrefContent"></div>
    </div>

    <!-- Ancient World Map Overlay -->
    <div class="map-overlay" id="mapOverlay">
        <div class="map-modal">
            <div class="map-modal-header">
                <h2>Ancient World Map</h2>
                <div class="map-filter-bar" id="mapFilterBar"></div>
                <button class="map-close" id="mapClose">&#x2716; Close Map</button>
            </div>
            <div class="map-container" id="mapContainer"></div>
        </div>
    </div>

    <!-- Learn Hebrew Overlay -->
    <div class="hebrew-learn-overlay" id="hebrewOverlay">
        <div class="hebrew-learn-modal">
            <div class="hebrew-learn-header">
                <h2>Learn to Read Biblical Hebrew</h2>
                <button class="hebrew-learn-close" id="hebrewClose">&times;</button>
            </div>
            <div class="hebrew-learn-tabs">
                <button class="hl-tab active" data-tab="alphabet">Aleph-Bet</button>
                <button class="hl-tab" data-tab="vowels">Vowels</button>
                <button class="hl-tab" data-tab="reading">Reading</button>
                <button class="hl-tab" data-tab="roots">Roots</button>
                <button class="hl-tab" data-tab="practice">Practice</button>
            </div>
            <div class="hebrew-learn-content" id="hebrewLearnContent"></div>
        </div>
    </div>

    <!-- Resources Overlay -->
    <div class="resources-overlay" id="resourcesOverlay">
        <div class="resources-modal">
            <div class="resources-modal-header">
                <h2>Study Resources</h2>
                <button class="resources-close" id="resourcesClose">&times;</button>
            </div>
            <input type="text" class="resources-search" id="resourcesSearch"
                   placeholder="Search resources..." autocomplete="off">
            <div class="resources-filters" id="resourcesFilters"></div>
            <div id="resourcesList"></div>
        </div>
    </div>

    <!-- Glossary Overlay -->
    <div class="glossary-overlay" id="glossaryOverlay">
        <div class="glossary-modal">
            <div class="glossary-modal-header">
                <h2>Glossary</h2>
                <button class="glossary-close" id="glossaryClose">&times;</button>
            </div>
            <input type="text" class="glossary-search" id="glossarySearch"
                   placeholder="Search terms..." autocomplete="off">
            <div id="glossaryList"></div>
        </div>
    </div>

    <script>
{js}
    </script>
</body>
</html>"""

    # Strip HAI references from HTML in release mode
    if RELEASE_MODE:
        # Remove the Hallelujah AI keyboard shortcut section
        hai_shortcut_start = html.find('<div class="shortcut-section">\n                <h3>Hallelujah AI</h3>')
        if hai_shortcut_start > 0:
            hai_shortcut_end = html.find('</div>', hai_shortcut_start) + 6
            html = html[:hai_shortcut_start] + html[hai_shortcut_end:]
        # Change title to release version
        html = html.replace('Developer Progress', 'About This App')
        html = html.replace('Open developer progress', 'About this app')
        html = html.replace('&#x1F4CA;', 'ℹ️')

    # \u2500\u2500 Write output \u2500\u2500
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_file = OUTPUT_FILE
    if RELEASE_MODE:
        out_file = os.path.join(OUTPUT_DIR, "AncientTextsStudy-Release.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)

    file_size = len(html.encode("utf-8"))
    line_count = html.count("\n")

    # \u2500\u2500 Copy to Desktop \u2500\u2500
    if not RELEASE_MODE:
        try:
            shutil.copy2(out_file, DESKTOP)
            print(f"\n[copy] Also copied to {DESKTOP}")
        except Exception as e:
            print(f"\n[copy] Could not copy to Desktop: {e}")

    print(f"\n{'=' * 60}")
    print(f"  BUILD SUCCESSFUL" + (" (RELEASE)" if RELEASE_MODE else ""))
    print(f"  Output: {out_file}")
    print(f"  Lines:  {line_count:,}")
    print(f"  Size:   {file_size:,} bytes ({file_size / 1024:.1f} KB)")
    il_info = " | IL: " + ", ".join(
        f"{k}={len(v)}ch" for k, v in interlinear_data.items()
    ) if interlinear_data else ""
    print(f"  Chapters: {total_chapters} | Inserts: {total_inserts} | Fragments: {total_fragments} | Terms: {len(glossary)}{il_info}")
    print(f"  Texts: {', '.join(t['name'] for t in all_texts)}")
    print(f"{'=' * 60}")

    return OUTPUT_FILE


if __name__ == "__main__":
    build()
    # Auto-rebuild content map after every build (keeps CONTENT_MAP.json current)
    try:
        import importlib.util as _ilu
        _spec = _ilu.spec_from_file_location('build_content_map',
            os.path.join(BASE, 'agents', 'build_content_map.py'))
        _mod = _ilu.module_from_spec(_spec)
        _spec.loader.exec_module(_mod)
        print("\n[content-map] Rebuilding CONTENT_MAP.json...")
        _mod.build_content_map()
    except Exception as _e:
        print(f"[content-map] Skipped: {_e}")
