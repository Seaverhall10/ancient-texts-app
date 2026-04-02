#!/usr/bin/env python3
"""
build_mobile.py — Generates a multi-file Progressive Web App for mobile (iOS Safari).

Instead of one 67 MB HTML file, this produces:
  output/mobile/
    index.html          (~2 MB app shell)
    manifest.webmanifest
    sw.js               (service worker for offline)
    data/
      manifest.json     (~300 KB - text list, eras, categories)
      glossary.json     (~600 KB)
      text_intros.json
      prophecy.json
      prophecy_tracker.json
      core_beliefs.json
      resources.json
      eras/
        genesis.json    (era chapters for genesis)
        exodus.json     ...
      interlinear/
        genesis.json    (~2.4 MB, includes flow translations)
        exodus.json     ...

Data is loaded on demand when the user taps a text.
Initial load: ~2 MB (instant on mobile).
"""

import os
import sys
import json
import shutil
import importlib.util

# ── Paths ──
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ── Load Firebase config from local file (not tracked in git) ──
_firebase_path = os.path.join(BASE_DIR, "config", "firebase.json")
if os.path.exists(_firebase_path):
    with open(_firebase_path, "r") as _f:
        firebase_config = json.load(_f)
else:
    print("WARNING: config/firebase.json not found — Firebase auth will not work")
    firebase_config = {"apiKey":"","authDomain":"","projectId":"","storageBucket":"","messagingSenderId":"","appId":""}

DATA_DIR = os.path.join(BASE_DIR, "data")
SRC_DIR = os.path.join(BASE_DIR, "src")
SRC_JS = os.path.join(SRC_DIR, "js", "app.js")
SRC_CSS_DIR = os.path.join(SRC_DIR, "css")
SRC_CSS_ORDER = os.path.join(SRC_CSS_DIR, "build-order.txt")
SRC_CSS_MOBILE = os.path.join(SRC_CSS_DIR, "mobile.css")
OUTPUT_DIR = os.path.join(BASE_DIR, "output", "mobile")
DATA_OUT = os.path.join(OUTPUT_DIR, "data")

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
    size = os.path.getsize(path)
    print(f"  {os.path.relpath(path, OUTPUT_DIR)} ({size:,} bytes)")

def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    print("=" * 60)
    print("  MOBILE PWA BUILD")
    print("=" * 60)

    # ── Clean output ──
    if os.path.exists(OUTPUT_DIR):
        try:
            shutil.rmtree(OUTPUT_DIR)
        except PermissionError:
            # Windows file lock — just overwrite files instead
            print("  [warn] Could not delete output dir (in use), will overwrite files")
    os.makedirs(DATA_OUT, exist_ok=True)
    os.makedirs(os.path.join(DATA_OUT, "eras"), exist_ok=True)
    os.makedirs(os.path.join(DATA_OUT, "interlinear"), exist_ok=True)

    # ══════════════════════════════════════════════════════════
    # 1. LOAD ALL DATA (same as build.py)
    # ══════════════════════════════════════════════════════════
    print("\n[1/6] Loading data...")

    manifest = json.loads(read_file(os.path.join(BASE_DIR, "manifest.json")))
    manifest["version"] = read_file(os.path.join(BASE_DIR, "VERSION")).strip() if os.path.exists(os.path.join(BASE_DIR, "VERSION")) else "3.2"
    manifest["build_date"] = __import__("datetime").datetime.now().strftime("%Y-%m-%d %H:%M")

    # Glossary
    glossary = {}
    gpath = os.path.join(DATA_DIR, "glossary.py")
    if os.path.exists(gpath):
        gmod = load_module("glossary", gpath)
        glossary = getattr(gmod, "GLOSSARY", {})
    print(f"  Glossary: {len(glossary)} terms")

    # Text intros
    text_intros = {}
    for t in manifest.get("texts", []):
        tid = t["id"]
        data_dir = t.get("data_dir", tid)
        info_path = os.path.join(DATA_DIR, data_dir, "info.py")
        if os.path.exists(info_path):
            try:
                mod = load_module(f"info_{tid}", info_path)
                intro = getattr(mod, "TEXT_INFO", None) or getattr(mod, "INFO", None)
                if intro:
                    text_intros[tid] = intro
            except Exception:
                pass

    # Prophecy, core beliefs, resources
    prophecy = {}
    ppath = os.path.join(DATA_DIR, "prophecy_matrix.py")
    if os.path.exists(ppath):
        try:
            pmod = load_module("prophecy_matrix", ppath)
            prophecy = getattr(pmod, "PROPHECY_MATRIX", {})
        except Exception:
            pass

    prophecy_tracker = {}
    ptpath = os.path.join(DATA_DIR, "prophecy_tracker.py")
    if os.path.exists(ptpath):
        try:
            ptmod = load_module("prophecy_tracker", ptpath)
            prophecy_tracker = getattr(ptmod, "BOOK_PROPHECIES", {})
        except Exception:
            pass

    core_beliefs = {}
    cbpath = os.path.join(DATA_DIR, "core_beliefs.py")
    if os.path.exists(cbpath):
        try:
            cbmod = load_module("core_beliefs", cbpath)
            core_beliefs = getattr(cbmod, "CORE_BELIEFS", {})
        except Exception:
            pass

    resources = {}
    rpath = os.path.join(DATA_DIR, "resources.py")
    if os.path.exists(rpath):
        try:
            rmod = load_module("resources", rpath)
            resources = getattr(rmod, "RESOURCES", {})
        except Exception:
            pass

    # Era data — load all, then split per text
    era_data = {}
    # Track which Python era files we've already loaded per text to avoid duplicates
    _loaded_py_eras = {}

    for era_def in manifest.get("eras", []):
        era_id = era_def["id"]
        text_id = era_def["text"]
        data_dir = None
        for t in manifest["texts"]:
            if t["id"] == text_id:
                data_dir = t.get("data_dir", text_id)
                break
        if not data_dir:
            data_dir = text_id

        text_data_dir = os.path.join(DATA_DIR, data_dir)
        chapters = []

        # ── HTML Fragment eras (e.g., Heavenly Court) ──────────────
        # These have specific fragment lists in the manifest
        if era_def.get("content_type") == "html_fragment":
            fragments = era_def.get("fragments", [])
            ch_dir = os.path.join(text_data_dir, "chapters")
            for frag in fragments:
                frag_file = frag.get("file", "")
                frag_path = os.path.join(ch_dir, frag_file)
                if os.path.exists(frag_path):
                    try:
                        html_content = read_file(frag_path)
                        chapters.append({
                            "id": frag["id"],
                            "type": "html_fragment",
                            "ref": frag.get("ref", ""),
                            "title": frag.get("title", ""),
                            "html": html_content,
                            "sections": [{"body": html_content}]
                        })
                    except Exception:
                        pass
                else:
                    chapters.append({
                        "id": frag["id"],
                        "type": "html_fragment",
                        "ref": frag.get("ref", ""),
                        "title": frag.get("title", ""),
                        "sections": [{"body": f"<p>Fragment not found: {frag_file}</p>"}]
                    })

        # ── Python era files (standard eras) ──────────────────────
        else:
            # Check if this era has a specific data_file in the manifest
            data_file = era_def.get("data_file")
            if data_file and os.path.isdir(text_data_dir):
                py_path = os.path.join(text_data_dir, f"{data_file}.py")
                if os.path.exists(py_path):
                    try:
                        mod = load_module(f"era_{era_id}_{data_file}", py_path)
                        chs = getattr(mod, "CHAPTERS", [])
                        chapters.extend(chs)
                    except Exception:
                        pass
            else:
                # Load all era_*.py files (but only once per text)
                if text_id not in _loaded_py_eras:
                    _loaded_py_eras[text_id] = []
                    if os.path.isdir(text_data_dir):
                        for f in sorted(os.listdir(text_data_dir)):
                            if f.startswith("era_") and f.endswith(".py"):
                                try:
                                    mod = load_module(f"era_{text_id}_{f}", os.path.join(text_data_dir, f))
                                    chs = getattr(mod, "CHAPTERS", [])
                                    _loaded_py_eras[text_id].extend(chs)
                                except Exception:
                                    pass
                chapters.extend(_loaded_py_eras[text_id])

        if chapters:
            era_data[era_id] = chapters

    print(f"  Eras: {len(era_data)} loaded")

    # Inject chapter counts into manifest texts for mobile library display
    for t in manifest.get("texts", []):
        tid = t["id"]
        ch_count = 0
        for era_def in manifest.get("eras", []):
            if era_def.get("text") == tid:
                chapters = era_data.get(era_def["id"], [])
                for ch in chapters:
                    if isinstance(ch, dict) and ch.get("type") == "chapter":
                        ch_count += 1
        t["chapter_count"] = ch_count

    # Interlinear data — load all, merge flow translations
    interlinear_data = {}  # key: text_id, value: {chapter: {verses: [...]}}

    # Load interlinear Python files
    for t in manifest.get("texts", []):
        tid = t["id"]
        data_dir = t.get("data_dir", tid)

        il = None
        # Try various file patterns
        paths_to_try = [
            os.path.join(DATA_DIR, data_dir, "interlinear.py"),
            os.path.join(DATA_DIR, f"interlinear_{tid}.py"),
            os.path.join(DATA_DIR, data_dir, f"interlinear_{tid}.py"),
            os.path.join(DATA_DIR, f"interlinear_nt_{tid}.py"),
        ]
        for p in paths_to_try:
            if os.path.exists(p) and il is None:
                try:
                    mod = load_module(f"il_{tid}", p)
                    # Try various constant names
                    for attr_name in [f"INTERLINEAR_{tid.upper()}", f"INTERLINEAR_NT_{tid.upper()}", "INTERLINEAR"]:
                        il = getattr(mod, attr_name, None)
                        if il:
                            break
                except Exception as e:
                    print(f"  [warn] {tid}: {e}")

        if il:
            interlinear_data[tid] = il

    print(f"  Interlinear: {len(interlinear_data)} books loaded")

    # Merge flow translations into interlinear
    flow_dir = os.path.join(DATA_DIR, "flow")
    flow_count = 0
    if os.path.isdir(flow_dir):
        for flow_file in sorted(os.listdir(flow_dir)):
            if flow_file.startswith("flow_") and flow_file.endswith(".py") and flow_file.count("_") == 1:
                book_name = flow_file.replace("flow_", "").replace(".py", "")
                try:
                    flow_mod = load_module(flow_file.replace(".py", ""), os.path.join(flow_dir, flow_file))
                except Exception:
                    continue

                flow_data = getattr(flow_mod, f"FLOW_{book_name.upper()}", None)
                if not flow_data:
                    for attr in dir(flow_mod):
                        if attr.startswith("FLOW"):
                            flow_data = getattr(flow_mod, attr)
                            break

                notes_data = getattr(flow_mod, f"NOTES_{book_name.upper()}", None)
                if not notes_data:
                    for attr in dir(flow_mod):
                        if attr.startswith("NOTES"):
                            notes_data = getattr(flow_mod, attr)
                            break

                if flow_data and book_name in interlinear_data:
                    il = interlinear_data[book_name]
                    merged = 0
                    for ch_key, ch_data in il.items():
                        ch_num = int(ch_key) if isinstance(ch_key, str) else ch_key
                        ch_flows = flow_data.get(ch_num, {})
                        ch_notes = notes_data.get(ch_num, {}) if notes_data else {}
                        for verse in ch_data.get("verses", []):
                            v_flow = ch_flows.get(verse["num"])
                            if v_flow:
                                verse["flow"] = v_flow
                                merged += 1
                            v_note = ch_notes.get(verse["num"]) if ch_notes else None
                            if v_note:
                                verse["note"] = v_note
                    flow_count += 1

    print(f"  Flow translations: merged into {flow_count} books")

    # Write standalone flow JSON for non-interlinear texts (1 Enoch, DSS, Jubilees, etc.)
    standalone_flow_count = 0
    standalone_flow_map = {}  # textId -> {ch: {v: text}}
    standalone_notes_map = {}
    if os.path.isdir(flow_dir):
        for flow_file in sorted(os.listdir(flow_dir)):
            if flow_file.startswith("flow_") and flow_file.endswith(".py") and flow_file.count("_") == 1:
                book_name = flow_file.replace("flow_", "").replace(".py", "")
                if book_name in interlinear_data:
                    continue  # already merged into interlinear
                try:
                    flow_mod = load_module(f"sf_{book_name}", os.path.join(flow_dir, flow_file))
                except Exception:
                    continue
                flow_data = getattr(flow_mod, f"FLOW_{book_name.upper()}", None)
                if not flow_data:
                    for attr in dir(flow_mod):
                        if attr.startswith("FLOW"):
                            flow_data = getattr(flow_mod, attr)
                            break
                if not flow_data:
                    continue
                notes_data = getattr(flow_mod, f"NOTES_{book_name.upper()}", None)
                if not notes_data:
                    for attr in dir(flow_mod):
                        if attr.startswith("NOTES"):
                            notes_data = getattr(flow_mod, attr)
                            break
                # Convert int keys to string for JSON
                sf = {}
                for ch, verses in flow_data.items():
                    sf[str(ch)] = {str(v): t for v, t in verses.items()}
                standalone_flow_map[book_name] = sf
                if notes_data:
                    sn = {}
                    for ch, notes in notes_data.items():
                        sn[str(ch)] = {str(v): n for v, n in notes.items()}
                    standalone_notes_map[book_name] = sn
                standalone_flow_count += 1

    if standalone_flow_count > 0:
        flow_out_dir = os.path.join(DATA_OUT, "flow")
        os.makedirs(flow_out_dir, exist_ok=True)
        for tid, sf_data in standalone_flow_map.items():
            write_json(os.path.join(flow_out_dir, f"{tid}.json"), sf_data)
            if tid in standalone_notes_map:
                write_json(os.path.join(flow_out_dir, f"{tid}_notes.json"), standalone_notes_map[tid])
        total_sv = sum(sum(len(ch) for ch in t.values()) for t in standalone_flow_map.values())
        print(f"  Standalone flow: {standalone_flow_count} texts, {total_sv} verses -> data/flow/*.json")

    # ══════════════════════════════════════════════════════════
    # 2. WRITE JSON DATA FILES
    # ══════════════════════════════════════════════════════════
    print("\n[2/6] Writing data files...")

    write_json(os.path.join(DATA_OUT, "manifest.json"), manifest)
    write_json(os.path.join(DATA_OUT, "glossary.json"), glossary)
    write_json(os.path.join(DATA_OUT, "text_intros.json"), text_intros)
    if prophecy:
        write_json(os.path.join(DATA_OUT, "prophecy.json"), prophecy)
    if prophecy_tracker:
        write_json(os.path.join(DATA_OUT, "prophecy_tracker.json"), prophecy_tracker)
    if core_beliefs:
        write_json(os.path.join(DATA_OUT, "core_beliefs.json"), core_beliefs)
    if resources:
        write_json(os.path.join(DATA_OUT, "resources.json"), resources)
    # Religions detail (for Matrix explore cards)
    religions_detail = {}
    rdpath = os.path.join(DATA_DIR, "religions_data.py")
    if os.path.exists(rdpath):
        try:
            rdmod = load_module("religions_data", rdpath)
            religions_detail = getattr(rdmod, "RELIGIONS_DETAIL", {})
        except Exception:
            pass
    if religions_detail:
        write_json(os.path.join(DATA_OUT, "religions_detail.json"), religions_detail)
        print(f"  Religions detail: {len(religions_detail)} entries")

    # Search Q&A data
    import re as _re
    search_qa_path = os.path.join(DATA_DIR, "search_qa.py")
    search_qa_data = []
    if os.path.exists(search_qa_path):
        qa_mod = load_module("search_qa", search_qa_path)
        search_qa_data = getattr(qa_mod, "SEARCH_QA", [])
    if search_qa_data:
        write_json(os.path.join(DATA_OUT, "search_qa.json"), search_qa_data)
        print(f"  Search Q&A: {len(search_qa_data)} entries")

    # Pre-build search index for mobile
    def _strip_html(s):
        return _re.sub(r'<[^>]+>', ' ', s).replace('&amp;', '&')

    def _build_mobile_search_index():
        docs = []
        all_words = set()
        for era_def in manifest.get("eras", []):
            chapters = era_data.get(era_def["id"], [])
            text_id = era_def.get("text", "")
            for ch in chapters:
                title = ch.get("title", "") or ""
                ref = ch.get("ref", title) or title
                synopsis = ch.get("synopsis", "") or ""
                body_parts = [title, synopsis]
                for s in ch.get("sections", []):
                    body_parts.append(s.get("heading", ""))
                    body_parts.append(_strip_html(s.get("body", "")))
                if ch.get("ane_backdrop"): body_parts.append(_strip_html(ch["ane_backdrop"]))
                if ch.get("divine_council_note"): body_parts.append(_strip_html(ch["divine_council_note"]))
                st = ch.get("second_temple", [])
                if isinstance(st, list):
                    for s in st:
                        if isinstance(s, dict):
                            body_parts.append(s.get("source", ""))
                            body_parts.append(s.get("summary", ""))
                tokens = _re.sub(r'<[^>]+>', ' ', ' '.join(body_parts).lower())
                tokens = _re.sub(r'[^\w\s\'-]', ' ', tokens)
                tokens = ' '.join(tokens.split())[:800]
                docs.append({'t': 'ch', 'id': ch.get('id',''), 'x': text_id,
                    'e': era_def['id'], 'ti': title, 'r': ref, 'tk': tokens,
                    'sn': (synopsis or title)[:150]})
                for w in _re.findall(r'[a-z]{3,}', (title + ' ' + ref + ' ' + synopsis).lower()):
                    all_words.add(w)
        # Glossary
        for slug, term in glossary.items():
            trans = term.get("transliteration", slug)
            defn = term.get("definition", "")
            gloss_str = term.get("gloss", "")
            tokens = _re.sub(r'[^\w\s\'-]', ' ', f"{slug} {trans} {gloss_str} {defn}".lower())
            docs.append({'t': 'gl', 'id': slug, 'ti': f"{trans} ({gloss_str})" if gloss_str else trans,
                'r': term.get("strongs", ""), 'tk': tokens, 'sn': defn[:150]})
            for w in _re.findall(r'[a-z]{3,}', f"{slug} {trans} {gloss_str}".lower()):
                all_words.add(w)
        word_list = sorted(all_words)
        bigrams = {}
        for i, word in enumerate(word_list):
            for j in range(len(word) - 1):
                bg = word[j:j+2]
                if bg not in bigrams: bigrams[bg] = []
                bigrams[bg].append(i)
        return {'docs': docs, 'words': word_list, 'bigrams': bigrams}

    mobile_si = _build_mobile_search_index()
    write_json(os.path.join(DATA_OUT, "search_index.json"), mobile_si)
    print(f"  Search index: {len(mobile_si['docs'])} docs, {len(mobile_si['words'])} fuzzy words")

    # Split era data per text
    eras_by_text = {}
    for era_def in manifest.get("eras", []):
        tid = era_def["text"]
        eid = era_def["id"]
        if eid in era_data:
            if tid not in eras_by_text:
                eras_by_text[tid] = {}
            eras_by_text[tid][eid] = era_data[eid]

    for tid, data in eras_by_text.items():
        write_json(os.path.join(DATA_OUT, "eras", f"{tid}.json"), data)
    print(f"  Era files: {len(eras_by_text)} texts")

    # Write interlinear per text
    for tid, data in interlinear_data.items():
        write_json(os.path.join(DATA_OUT, "interlinear", f"{tid}.json"), data)
    print(f"  Interlinear files: {len(interlinear_data)} texts")

    # ══════════════════════════════════════════════════════════
    # 3. GENERATE MOBILE APP.JS (with data loader)
    # ══════════════════════════════════════════════════════════
    print("\n[3/6] Generating mobile app.js...")

    js = read_file(SRC_JS)

    # Replace all data constants with empty objects
    # Manifest loads at boot; everything else loads on demand
    js = js.replace("__MANIFEST_DATA__", "__MANIFEST_PLACEHOLDER__")  # will be loaded via fetch
    js = js.replace("__ERA_DATA__", "{}")
    js = js.replace("__GLOSSARY_DATA__", "{}")
    js = js.replace("__TEXT_INTROS_DATA__", "{}")
    js = js.replace("__PROPHECY_DATA__", "{}")
    js = js.replace("__PROPHECY_TRACKER_DATA__", "{}")
    js = js.replace("__CORE_BELIEFS_DATA__", "{}")
    js = js.replace("__RESOURCES_DATA__", "{}")

    # Load Short Dive articles
    sd_articles = {}
    sd_path1 = os.path.join(DATA_DIR, "short_dives.py")
    sd_path2 = os.path.join(DATA_DIR, "short_dives_2.py")
    if os.path.exists(sd_path1):
        sd_mod1 = load_module("short_dives", sd_path1)
        sd_articles.update(getattr(sd_mod1, "SHORT_DIVE_ARTICLES", {}))
    if os.path.exists(sd_path2):
        sd_mod2 = load_module("short_dives_2", sd_path2)
        sd_articles.update(getattr(sd_mod2, "SHORT_DIVE_ARTICLES_2", {}))
    js = js.replace("__SHORT_DIVES_DATA__", json.dumps(sd_articles, ensure_ascii=False))
    js = js.replace("__RELIGIONS_DETAIL_DATA__", "{}")
    js = js.replace("__SEARCH_QA_DATA__", "[]")
    js = js.replace("__SEARCH_INDEX_DATA__", '{"docs":[],"words":[],"bigrams":{}}')

    # Replace all interlinear placeholders with empty objects
    import re
    js = re.sub(r'__INTERLINEAR_[A-Z0-9_]*_DATA__', '{}', js)
    js = re.sub(r'__INTERLINEAR_DATA__', '{}', js)

    # Change const to var for data that will be reassigned
    js = js.replace("    const MANIFEST = __MANIFEST_PLACEHOLDER__;", "    var MANIFEST = {};")
    js = js.replace("    const ERA_DATA = {};", "    var ERA_DATA = {};")
    js = js.replace("    const GLOSSARY = {};", "    var GLOSSARY = {};")
    js = js.replace("    const TEXT_INTROS = {};", "    var TEXT_INTROS = {};")
    js = js.replace("    const PROPHECY_MATRIX = {};", "    var PROPHECY_MATRIX = {};")
    js = js.replace("    const BOOK_PROPHECIES = {};", "    var BOOK_PROPHECIES = {};")
    js = js.replace("    const CORE_BELIEFS = {};", "    var CORE_BELIEFS = {};")
    js = js.replace("    const RESOURCES = {};", "    var RESOURCES = {};")

    # Change all INTERLINEAR consts to var
    js = re.sub(r'    const (INTERLINEAR\w*) = \{\};', r'    var \1 = {};', js)

    # Replace standalone flow/notes placeholders with empty objects
    # (Mobile loads flow data on-demand, but standalone flow for non-interlinear
    #  texts like 1 Enoch needs to be embedded since there's no interlinear JSON)
    js = js.replace("__STANDALONE_FLOW_DATA__", '{}')
    js = js.replace("__STANDALONE_NOTES_DATA__", '{}')

    # ── SAFETY CHECK: fail build if any __*_DATA__ placeholders remain ──
    remaining = re.findall(r'__[A-Z_]+_DATA__', js)
    if remaining:
        unique = list(set(remaining))
        print(f"\n  *** BUILD ERROR: {len(unique)} unreplaced placeholder(s) found! ***")
        for p in sorted(unique):
            print(f"      {p}")
        print("  Add replacements to build_mobile.py before the safety check.")
        print("  This WILL crash the mobile app with a silent ReferenceError.\n")
        sys.exit(1)

    # Add IS_RELEASE and IS_MOBILE flags INSIDE the existing IIFE (after 'use strict')
    js = js.replace(
        "    'use strict';",
        "    'use strict';\n    var IS_RELEASE = true;\n    var IS_MOBILE = true;"
    )

    # Strip HAI module
    hai_marker = '//  HALLELUJAH AI'
    hai_start = js.find(hai_marker)
    if hai_start > 0:
        hai_start = js.rfind('// ', 0, hai_start)
        hai_start = max(0, js.rfind('\n', 0, hai_start)) + 1
        # Stop HAI strip at Firebase Auth section (comes between HAI and Launch)
        hai_end = js.find("// \u2500\u2500 Firebase Auth", hai_start)
        if hai_end < 0:
            hai_end = js.find("// \u2500\u2500 Launch", hai_start)
        if hai_end > 0:
            js = js[:hai_start] + '\n    // [HAI removed in mobile build]\n\n    ' + js[hai_end:]
    js = js.replace('initHallelujahChat();', '// [HAI removed]')

    # ── Inject data loader module ──
    # This goes right after the IS_MOBILE declaration, before everything else
    data_loader = """
    // ── MOBILE DATA LOADER ──────────────────────────────────
    var _loadedTexts = {};
    var _loadingTexts = {};
    var _dataBase = 'data/';

    function _showLoading(msg) {
        var el = document.getElementById('mobileLoadingOverlay');
        if (el) {
            el.querySelector('.mobile-loading-text').textContent = msg || 'Loading...';
            el.style.display = 'flex';
        }
    }

    function _hideLoading() {
        var el = document.getElementById('mobileLoadingOverlay');
        if (el) el.style.display = 'none';
    }

    async function _fetchJSON(path) {
        var resp = await fetch(_dataBase + path);
        if (!resp.ok) throw new Error('Failed to load ' + path + ': ' + resp.status);
        return resp.json();
    }

    async function mobileBootstrap() {
        _showLoading('Loading library...');
        try {
            MANIFEST = await _fetchJSON('manifest.json');
            TEXT_INTROS = await _fetchJSON('text_intros.json');
            // Re-populate top-level vars that were initialized from empty MANIFEST
            texts = MANIFEST.texts || [];
            categories = MANIFEST.categories || [];
        } catch(e) {
            console.error('[mobile] Bootstrap failed:', e);
            document.body.innerHTML = '<div style="padding:2rem;color:#e05540;font-size:1.2rem"><h2>Failed to load app data</h2><p>' + e.message + '</p><p>Try refreshing the page. If that doesn\\'t work, clear your browser cache and reload.</p></div>';
            return false;
        }
        _hideLoading();
        return true;
    }

    // Safety: if loading overlay is still visible after 15 seconds, hide it and show error
    setTimeout(function() {
        var el = document.getElementById('mobileLoadingOverlay');
        if (el && el.style.display === 'flex') {
            el.style.display = 'none';
            console.error('[mobile] Loading timeout — overlay dismissed after 15s');
        }
    }, 15000);

    async function loadTextData(textId) {
        if (_loadedTexts[textId]) return true;
        if (_loadingTexts[textId]) return _loadingTexts[textId];

        var p = (async function() {
            _showLoading('Loading ' + textId + '...');
            try {
                // Load era data
                var eraData = await _fetchJSON('eras/' + textId + '.json').catch(function() { return {}; });
                Object.keys(eraData).forEach(function(k) { ERA_DATA[k] = eraData[k]; });

                // Load interlinear + flow data
                var ilData = await _fetchJSON('interlinear/' + textId + '.json').catch(function() { return {}; });
                // Assign to the correct global variable
                var ilKey = 'INTERLINEAR_' + textId.toUpperCase();
                var ntBooks = ['matthew','mark','luke','john','acts','romans','1corinthians',
                    '2corinthians','galatians','ephesians','philippians','colossians',
                    '1thessalonians','2thessalonians','1timothy','2timothy','titus','philemon',
                    'hebrews','james','1peter','2peter','1john','2john','3john','jude','revelation'];
                if (ntBooks.indexOf(textId) !== -1) {
                    ilKey = 'INTERLINEAR_NT_' + textId.toUpperCase();
                }
                // Special case: genesis uses INTERLINEAR (no suffix)
                if (textId === 'genesis') ilKey = 'INTERLINEAR';

                // Assign via eval to dynamic variable name (safe — we control the key)
                try { eval(ilKey + ' = ilData;'); } catch(e) {}

                // Load standalone flow for non-interlinear texts (1 Enoch, Jubilees, DSS, etc.)
                if (!ilData || Object.keys(ilData).length === 0) {
                    var sfData = await _fetchJSON('flow/' + textId + '.json').catch(function() { return null; });
                    if (sfData) {
                        STANDALONE_FLOW[textId] = sfData;
                        var snData = await _fetchJSON('flow/' + textId + '_notes.json').catch(function() { return null; });
                        if (snData) STANDALONE_NOTES[textId] = snData;
                    }
                }

                _loadedTexts[textId] = true;
                _hideLoading();
                // Rebuild search index to include newly loaded text data
                if (typeof buildSearchIndex === 'function') buildSearchIndex(true);
                return true;
            } catch(e) {
                _hideLoading();
                console.error('Failed to load data for', textId, e);
                return false;
            }
        })();

        _loadingTexts[textId] = p;
        return p;
    }

    async function loadGlossary() {
        if (Object.keys(GLOSSARY).length > 0) return;
        try {
            GLOSSARY = await _fetchJSON('glossary.json');
        } catch(e) { console.error('Failed to load glossary', e); }
    }

    async function loadSearchData() {
        if (SEARCH_QA.length > 0 && SEARCH_INDEX.docs && SEARCH_INDEX.docs.length > 0) return;
        try {
            SEARCH_QA = await _fetchJSON('search_qa.json');
        } catch(e) { console.error('Failed to load search Q&A', e); }
        try {
            SEARCH_INDEX = await _fetchJSON('search_index.json');
        } catch(e) { console.error('Failed to load search index', e); }
    }

    async function loadProphecy() {
        if (Object.keys(PROPHECY_MATRIX).length > 0) return;
        try {
            PROPHECY_MATRIX = await _fetchJSON('prophecy.json');
        } catch(e) {}
        try {
            BOOK_PROPHECIES = await _fetchJSON('prophecy_tracker.json');
        } catch(e) {}
    }

    async function loadCoreBeliefs() {
        if (Object.keys(CORE_BELIEFS).length > 0) return;
        try {
            CORE_BELIEFS = await _fetchJSON('core_beliefs.json');
        } catch(e) {}
    }

    async function loadReligionsDetail() {
        if (Object.keys(RELIGIONS_DETAIL).length > 0) return;
        try {
            RELIGIONS_DETAIL = await _fetchJSON('religions_detail.json');
        } catch(e) {}
    }

    async function loadResources() {
        if (Object.keys(RESOURCES).length > 0) return;
        try {
            RESOURCES = await _fetchJSON('resources.json');
        } catch(e) {}
    }

    // ── END MOBILE DATA LOADER ──────────────────────────────
"""
    # Insert data loader after IS_MOBILE line (inside the existing IIFE)
    js = js.replace(
        "    var IS_MOBILE = true;",
        "    var IS_MOBILE = true;\n" + data_loader,
        1
    )

    # ── Patch selectText to be async ──
    # Wrap the existing selectText to load data first
    old_select = "    function selectText(textId, skipPushState) {"
    new_select = """    async function selectText(textId, skipPushState) {
        // Mobile: load text data on demand
        if (typeof IS_MOBILE !== 'undefined' && IS_MOBILE) {
            await loadTextData(textId);
        }"""
    js = js.replace(old_select, new_select, 1)

    # ── Patch showBibleMode to load data first ──
    old_bible = "    function showBibleMode(textId, chapterIndex) {"
    new_bible = """    async function showBibleMode(textId, chapterIndex) {
        // Mobile: load text data on demand
        if (typeof IS_MOBILE !== 'undefined' && IS_MOBILE) {
            await loadTextData(textId);
        }"""
    js = js.replace(old_bible, new_bible, 1)

    # ── Patch showBookLanding to load data first ──
    old_landing = "    function showBookLanding(textId) {"
    new_landing = """    async function showBookLanding(textId) {
        // Mobile: load text data on demand
        if (typeof IS_MOBILE !== 'undefined' && IS_MOBILE) {
            await loadTextData(textId);
        }"""
    js = js.replace(old_landing, new_landing, 1)

    # ── Patch handleHash to be async (so it can await showBookLanding/showBibleMode) ──
    old_hash = "    function handleHash() {"
    new_hash = "    async function handleHash() {"
    js = js.replace(old_hash, new_hash, 1)

    # Make the showBookLanding call in handleHash use await
    old_hash_book = """            hashHandling = true;
            showBookLanding(bookId);
            hashHandling = false;"""
    new_hash_book = """            hashHandling = true;
            await showBookLanding(bookId);
            hashHandling = false;"""
    js = js.replace(old_hash_book, new_hash_book, 1)

    # Make the showBibleMode call in handleHash use await
    old_hash_read = """            hashHandling = true;
            showBibleMode(parts[1], chapterNum - 1);
            hashHandling = false;"""
    new_hash_read = """            hashHandling = true;
            await showBibleMode(parts[1], chapterNum - 1);
            hashHandling = false;"""
    js = js.replace(old_hash_read, new_hash_read, 1)

    # ── Patch init to bootstrap ──
    # Find the init/DOMContentLoaded section and wrap it
    old_init = "    document.addEventListener('DOMContentLoaded', function() {"
    if old_init in js:
        new_init = """    document.addEventListener('DOMContentLoaded', async function() {
        if (typeof IS_MOBILE !== 'undefined' && IS_MOBILE) {
            var ok = await mobileBootstrap();
            if (!ok) return;
        }"""
        js = js.replace(old_init, new_init, 1)
    else:
        # Try alternate init pattern
        old_init2 = "    function init() {"
        if old_init2 in js:
            new_init2 = """    async function init() {
        try {
        if (typeof IS_MOBILE !== 'undefined' && IS_MOBILE) {
            var ok = await mobileBootstrap();
            if (!ok) return;
        }"""
            js = js.replace(old_init2, new_init2, 1)
            # Also add closing try/catch at the end of init
            # Find the closing of init (the showLibrary call is near the end)
            old_show_lib = "        showLibrary();\n    }"
            if old_show_lib in js:
                new_show_lib = """        showLibrary();
        } catch(e) {
            console.error('[init] Error during startup:', e);
            _hideLoading();
            var mc = document.getElementById('mainContent');
            if (mc) mc.innerHTML = '<div style="padding:2rem;color:#e05540"><h2>Startup Error</h2><p>' + e.message + '</p><p>Try refreshing the page.</p></div>';
        }
    }"""
                js = js.replace(old_show_lib, new_show_lib, 1)

    # ── Patch glossary overlay to lazy-load ──
    old_glossary = "    function openGlossary() {"
    if old_glossary in js:
        new_glossary = """    async function openGlossary() {
        if (typeof IS_MOBILE !== 'undefined' && IS_MOBILE) await loadGlossary();"""
        js = js.replace(old_glossary, new_glossary, 1)

    print(f"  Mobile app.js: {len(js):,} chars")

    # ══════════════════════════════════════════════════════════
    # 4. GENERATE HTML SHELL
    # ══════════════════════════════════════════════════════════
    print("\n[4/6] Generating HTML shell...")

    # ── Read CSS (concatenation from build-order.txt, same as build.py) ──
    if os.path.exists(SRC_CSS_ORDER):
        css_parts = []
        css_files = []
        for line in read_file(SRC_CSS_ORDER).strip().splitlines():
            line = line.strip()
            if line and not line.startswith('#'):
                fpath = os.path.join(SRC_CSS_DIR, line)
                if os.path.exists(fpath):
                    css_parts.append(open(fpath, 'r', encoding='utf-8').read())
                    css_files.append(line)
                else:
                    print(f"  WARNING: CSS file not found: {line}")
        css = ''.join(css_parts)
        print(f"  [css] {len(css_files)} component files ({len(css):,} chars)")

    # Mobile-specific CSS additions (read from source file)
    if os.path.exists(SRC_CSS_MOBILE):
        mobile_css = read_file(SRC_CSS_MOBILE)
        print(f"  [css] mobile.css ({len(mobile_css):,} chars)")
    else:
        print("  WARNING: mobile.css not found, using empty mobile CSS")
        mobile_css = ""

    # Legacy inline mobile CSS removed — now reads from src/css/mobile.css
    _mobile_css_removed = """
/* ── Mobile PWA Overrides ── */
@supports (-webkit-touch-callout: none) {
    body { padding-top: env(safe-area-inset-top); padding-bottom: env(safe-area-inset-bottom); }
    .sidebar-toggle { top: calc(0.5rem + env(safe-area-inset-top)); }
}

/* Loading overlay */
#mobileLoadingOverlay {
    display: none;
    position: fixed; top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(12,14,20,0.92);
    z-index: 100000;
    align-items: center; justify-content: center;
    flex-direction: column;
}
.mobile-loading-spinner {
    width: 40px; height: 40px;
    border: 3px solid #c9a84c30;
    border-top-color: #c9a84c;
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }
.mobile-loading-text { margin-top: 1rem; color: #c9a84c; font-size: 0.9rem; }

/* ── MOBILE OVERHAUL ─────────────────────────── */
/* Global touch optimization */
a, button, [role="button"], .library-card, .cross-ref-pill,
.il-word, .chapter-link, .era-toggle, .library-text-link,
.sidebar-btn, .bottom-nav-btn {
    -webkit-tap-highlight-color: transparent;
    touch-action: manipulation;
}
body { overflow-wrap: break-word; word-break: break-word; }
body.sidebar-open .main-content { overflow: hidden !important; }

.library-subtitle { max-width: min(500px, 100%); }
.library-thesis { max-width: min(700px, 100%); }
.library-featured { max-width: min(700px, 100%); }
.word-popup { width: min(300px, calc(100vw - 24px)); }

/* Sidebar close button */
.sidebar-close-btn {
    display: none; position: absolute; top: 10px; right: 10px;
    background: none; border: 1px solid rgba(201,168,76,0.3);
    color: #c9a84c; font-size: 1.6rem; width: 44px; height: 44px;
    border-radius: 4px; cursor: pointer; z-index: 10; line-height: 1;
}
.sidebar-close-btn:hover { background: #1e2233; }

/* Mobile Bottom Navigation */
.mobile-bottom-nav {
    display: none; position: fixed; bottom: 0; left: 0; right: 0;
    background: #181c28; border-top: 1px solid rgba(201,168,76,0.25);
    z-index: 9999; padding: 4px 0 calc(4px + env(safe-area-inset-bottom, 0px));
    justify-content: space-around; align-items: center;
    backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
}
.bottom-nav-btn {
    display: flex; flex-direction: column; align-items: center; gap: 2px;
    background: none; border: none; color: #9a968e;
    padding: 8px 4px 6px; min-width: 56px; min-height: 48px;
    cursor: pointer; border-radius: 4px; transition: color 0.15s, background 0.15s;
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
}
.bottom-nav-btn.active, .bottom-nav-btn:active {
    color: #c9a84c; background: rgba(201,168,76,0.15);
}
.bottom-nav-icon { font-size: 1.25rem; line-height: 1; }
.bottom-nav-label {
    font-size: 0.625rem; font-weight: 500; letter-spacing: 0.02em; text-transform: uppercase;
}

/* Mobile Tools Popup Sheet */
.mobile-tools-popup {
    display: none; position: fixed; inset: 0; z-index: 10000;
}
.mobile-tools-popup.open { display: block; }
.mobile-tools-backdrop {
    position: absolute; inset: 0; background: rgba(0,0,0,0.6);
}
.mobile-tools-sheet {
    position: absolute; bottom: 60px; left: 0; right: 0;
    background: #1a1e2e; border-top: 2px solid #c9a84c;
    border-radius: 16px 16px 0 0; padding: 16px 12px 20px;
    max-height: 70vh; overflow-y: auto;
    box-shadow: 0 -8px 32px rgba(0,0,0,0.5);
    animation: toolsSlideUp 0.25s ease-out;
}
@keyframes toolsSlideUp {
    from { transform: translateY(100%); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}
.mobile-tools-header {
    display: flex; justify-content: space-between; align-items: center;
    padding: 0 4px 12px; border-bottom: 1px solid rgba(201,168,76,0.2);
    margin-bottom: 12px; color: #c9a84c; font-size: 1rem; font-weight: 600;
}
.mobile-tools-close {
    background: none; border: 1px solid rgba(201,168,76,0.3); color: #c9a84c;
    font-size: 1.4rem; width: 36px; height: 36px; border-radius: 6px; cursor: pointer;
    display: flex; align-items: center; justify-content: center; line-height: 1;
}
.mobile-tools-grid {
    display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px;
}
.mobile-tool-item {
    display: flex; align-items: center; gap: 10px;
    background: rgba(201,168,76,0.06); border: 1px solid rgba(201,168,76,0.15);
    border-radius: 10px; padding: 14px 12px; color: #e0dcd4;
    font-size: 0.88rem; font-family: inherit; cursor: pointer; min-height: 52px;
    transition: background 0.15s, border-color 0.15s;
}
.mobile-tool-item:active {
    background: rgba(201,168,76,0.18); border-color: #c9a84c;
}
.mobile-tool-icon { font-size: 1.3rem; flex-shrink: 0; }

@media (max-width: 768px) {
    .mobile-bottom-nav { display: flex; }
    .sidebar-close-btn { display: flex; align-items: center; justify-content: center; }
    /* Fix z-index: overlays must appear above sidebar (z-index 100) */
    .progress-overlay { z-index: 110 !important; }
    .glossary-overlay { z-index: 110 !important; }
    .map-overlay { z-index: 110 !important; }
    .hebrew-overlay { z-index: 110 !important; }
    .resources-overlay { z-index: 110 !important; }
    .religion-detail-overlay { z-index: 110 !important; }
    .main-content { padding-bottom: 80px !important; }

    .sidebar {
        width: min(280px, 85vw); z-index: 100;
        height: 100vh; height: 100dvh;
        overflow-y: auto;
    }
    .sidebar-nav {
        flex: unset !important;
        overflow-y: visible !important;
    }
    .sidebar-footer {
        flex-shrink: 1 !important;
        padding-top: 0;
    }
    .sidebar-footer .sidebar-btn { display: none; }
    .sidebar-tools-toggle {
        display: flex; align-items: center; justify-content: center; gap: 6px;
        width: 100%; padding: 10px; margin-top: 4px;
        background: rgba(201,168,76,0.08); border: 1px solid rgba(201,168,76,0.2);
        border-radius: 6px; color: #c9a84c; font-size: 0.85rem;
        cursor: pointer; min-height: 44px; font-family: inherit;
    }
    .sidebar-tools-toggle:active { background: rgba(201,168,76,0.15); }
    .sidebar-tools-toggle .arrow { transition: transform 0.2s; }
    .sidebar-footer.tools-expanded .sidebar-btn { display: flex; }
    .sidebar-footer.tools-expanded .sidebar-tools-toggle .arrow { transform: rotate(180deg); }
    .sidebar-backdrop { z-index: 99; }
    .sidebar-toggle {
        z-index: 101; min-width: 44px; min-height: 44px; padding: 10px 14px;
        top: calc(12px + env(safe-area-inset-top, 0px));
        left: calc(12px + env(safe-area-inset-left, 0px));
    }
    .sidebar-header { padding-right: 50px; }

    .app-container { height: 100vh; height: 100dvh; }
    .main-content { height: 100vh; height: 100dvh; overflow-y: auto; }
    .reading-pane { height: 100vh; height: 100dvh; }

    .library-text-link { padding: 12px 14px; min-height: 44px; }
    .sidebar-btn { min-height: 44px; font-size: 0.95rem; }
    .chapter-link { padding: 10px 12px; min-height: 44px; }
    button, .btn { min-height: 44px; }
    .era-toggle { min-height: 44px; }
    .cross-ref-pill { min-height: 36px; padding: 8px 12px; }
    .book-tab { min-height: 44px; }
    .bookmark-item { min-height: 44px; padding: 10px 8px; }
    .xref-close, .glossary-close, .resources-close, .progress-close,
    .reading-pane-close, .bookmark-remove, .hebrew-learn-close, .map-close {
        min-width: 44px; min-height: 44px;
        display: inline-flex; align-items: center; justify-content: center;
    }
    .study-toggle { min-height: 36px; padding: 6px 10px; font-size: 0.75rem; }
    .il-nav-btn { min-width: 36px; min-height: 36px; font-size: 0.75rem; }
    .il-word { padding: 6px 8px 4px; }
    .study-controls {
        flex-wrap: nowrap; overflow-x: auto; -webkit-overflow-scrolling: touch;
        max-width: calc(100vw - 16px); bottom: calc(64px + env(safe-area-inset-bottom, 0px));
        gap: 4px; padding: 6px 8px; scrollbar-width: none;
        z-index: 9998 !important;
    }
    .study-controls::-webkit-scrollbar { display: none; }
    .reading-pane-header { padding: 4px 8px !important; }
    .reading-pane-title-row { gap: 4px; }
    .reading-pane-title-row h2 { font-size: 1rem !important; }
    .reading-pane-controls {
        flex-wrap: nowrap !important; overflow-x: auto; -webkit-overflow-scrolling: touch;
        gap: 4px !important; padding: 4px 0 !important; scrollbar-width: none;
    }
    .reading-pane-controls::-webkit-scrollbar { display: none; }
    .reading-pane-controls button, .reading-pane-controls select,
    .reading-pane-controls .il-mode-select { min-height: 36px; font-size: 0.78rem; padding: 4px 8px; }
    .reading-pane-controls .font-controls { gap: 2px; }
    .reading-pane-controls .font-controls button { min-width: 32px; min-height: 32px; padding: 2px; }
    .reading-pane-options-row {
        flex-wrap: wrap !important; gap: 4px;
    }
    .il-row-toggles {
        flex-direction: row !important; flex-wrap: wrap; gap: 3px;
        order: -1; width: 100% !important;
        padding: 4px 8px; justify-content: center;
        background: rgba(12,14,20,0.95); border-bottom: 1px solid rgba(201,168,76,0.15);
    }
    .il-row-toggle {
        writing-mode: horizontal-tb !important; min-height: 28px !important;
        padding: 4px 10px !important; font-size: 0.7rem !important; width: auto !important;
        white-space: nowrap !important;
    }
    .user-mode-selector { order: 0; }
    .col-width-control { display: none !important; }
    .hc-toggle { order: 1; }
    .il-verse-row { flex-wrap: wrap; }
    .user-mode-btn { min-height: 36px !important; padding: 6px 12px !important; font-size: 0.8rem !important; }

    .chapter-ref, .era-theme-tag, .scripture-block .verse-ref,
    .callout-label, .cross-refs-section h4, .terms-section h4 { font-size: 0.8125rem; }
    .breadcrumb-bar { font-size: 0.8125rem; }
    .term-card .term-strongs { font-size: 0.72rem; }

    .chapter-copy-btn { opacity: 0.5; }
    .il-verse-copy { opacity: 0.4; }
    .chapter-card:hover, .library-card:hover { transform: none; }
    .main-content, .reading-pane-content, .sidebar { overscroll-behavior-y: contain; }
    .help-shortcut-btn { display: none; }
    .search-input::placeholder { font-size: 0.85rem; }
    .search-results { max-height: 50vh; }
    .glossary-overlay, .resources-overlay, .hebrew-learn-overlay, .map-overlay,
    .matrix-overlay, .timeline-overlay, .progress-overlay {
        z-index: 10000 !important; padding: 8px !important;
    }
    .glossary-modal, .resources-modal, .hebrew-learn-modal, .map-modal {
        max-height: 90vh; padding: 12px !important; width: 100%;
    }
    .glossary-modal-header h2, .resources-modal-header h2 { font-size: 1.2rem; }
}

@media (max-width: 480px) {
    .library-title { font-size: 1.25rem; }
    .library-hero { padding: 24px 8px 16px; }
    .library-featured-card { padding: 14px; }
    .library-subtitle { font-size: 0.85rem; }
    .terms-grid { grid-template-columns: 1fr; }
    .chapter-card { padding: 8px; }
    .intro-facts-grid { grid-template-columns: 1fr; }
}

@media (max-width: 375px) {
    .library-title { font-size: 1.125rem; }
    .library-hero { padding: 16px 4px 8px; }
}

@media all and (display-mode: standalone) {
    body { padding-top: env(safe-area-inset-top, 20px); padding-bottom: env(safe-area-inset-bottom, 0px); }
    .mobile-bottom-nav { padding-bottom: calc(4px + env(safe-area-inset-bottom, 8px)); }
    .sidebar-toggle { top: calc(12px + env(safe-area-inset-top, 20px)); }
}
"""

    # Read the HTML template parts from build.py to get the overlays
    # We'll construct the HTML from the existing build output structure
    build_py = read_file(os.path.join(BASE_DIR, "build.py"))

    # Extract the HTML template from build.py
    html_start = build_py.find('html = f"""<!DOCTYPE html>')
    html_end = build_py.find("</html>\"\"\"", html_start) + len("</html>\"\"\"")

    # Instead of parsing build.py's template, let's build the HTML directly
    # using the same structure but with mobile additions

    # First, run the normal build to get the full HTML, then strip data
    # Actually, simpler: construct from the CSS + JS we have

    title = manifest.get("title", "Ancient Texts Library")
    subtitle = manifest.get("subtitle", "A Scholarly Study of Sacred & Ancient Writings")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="Ancient Texts">
    <meta name="theme-color" content="#0c0e14">
    <meta name="mobile-web-app-capable" content="yes">
    <link rel="manifest" href="manifest.webmanifest">
    <link rel="apple-touch-icon" href="icon-180.png">
    <title>{title} &mdash; {subtitle}</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.12.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.12.0/firebase-auth-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore-compat.js"></script>
    <script>
    window.__FIREBASE_CONFIG = {{
        apiKey: "{firebase_config['apiKey']}",
        authDomain: "{firebase_config['authDomain']}",
        projectId: "{firebase_config['projectId']}",
        storageBucket: "{firebase_config['storageBucket']}",
        messagingSenderId: "{firebase_config['messagingSenderId']}",
        appId: "{firebase_config['appId']}"
    }};
    </script>
    <style>
{css}
{mobile_css}
    </style>
</head>
<body>
    <!-- Mobile loading overlay -->
    <div id="mobileLoadingOverlay">
        <div class="mobile-loading-spinner"></div>
        <div class="mobile-loading-text">Loading library...</div>
    </div>
"""

    # Now we need the body HTML — sidebar, main content, overlays.
    # The easiest approach: run the normal build.py and extract just the body HTML,
    # then strip the inline data. But that's circular.
    # Instead, let's read the ALREADY BUILT output and extract the body.

    built_release = os.path.join(BASE_DIR, "output", "AncientTextsStudy-Release.html")
    if not os.path.exists(built_release):
        built_release = os.path.join(BASE_DIR, "output", "AncientTextsStudy.html")

    if os.path.exists(built_release):
        print("  Extracting body from existing build...")
        built_html = read_file(built_release)

        # Extract body content (between <body> and </body>)
        body_start = built_html.find("<body>")
        body_end = built_html.find("</body>")
        if body_start > 0 and body_end > 0:
            body_content = built_html[body_start + 6:body_end]

            # Remove the inline <script> tag (we'll add our own)
            script_start = body_content.rfind("<script>")
            if script_start > 0:
                body_content = body_content[:script_start]

            # ── Mobile HTML Patches ──────────────────────────
            # Add sidebar close button
            body_content = body_content.replace(
                '<div class="sidebar-header">',
                '<div class="sidebar-header"><button class="sidebar-close-btn" id="sidebarCloseBtn" aria-label="Close sidebar">&times;</button>'
            )
            # Add collapsible tools toggle to sidebar-footer
            body_content = body_content.replace(
                '<div class="sidebar-footer">',
                '<div class="sidebar-footer"><button class="sidebar-tools-toggle" id="sidebarToolsToggle" aria-label="Toggle tools"><span>&#x2699; Study Tools</span><span class="arrow">&#x25BC;</span></button>'
            )

            # Fix content-max CSS variable if present inline
            body_content = body_content.replace(
                '--content-max: clamp(640px, 85vw, 1100px)',
                '--content-max: min(1100px, 100%)'
            )
            body_content = body_content.replace(
                '--reading-pane-width: clamp(500px, 42vw, 780px)',
                '--reading-pane-width: clamp(320px, 42vw, 780px)'
            )

            html += body_content
    else:
        print("  ERROR: No existing build found. Run 'python build.py --release' first.")
        sys.exit(1)

    # Close body with our mobile JS + bottom nav + SW registration
    bottom_nav_html = """
    <!-- Mobile Tools Popup Sheet -->
    <div class="mobile-tools-popup" id="mobileToolsPopup">
        <div class="mobile-tools-backdrop" id="mobileToolsBackdrop"></div>
        <div class="mobile-tools-sheet">
            <div class="mobile-tools-header">
                <span>Study Tools</span>
                <button class="mobile-tools-close" id="mobileToolsClose">&times;</button>
            </div>
            <div class="mobile-tools-grid">
                <button class="mobile-tool-item" data-tool="matrix">
                    <span class="mobile-tool-icon">&#x1F4CA;</span><span>Truth Matrix</span>
                </button>
                <button class="mobile-tool-item" data-tool="timeline">
                    <span class="mobile-tool-icon">&#x23F3;</span><span>Timeline</span>
                </button>
                <button class="mobile-tool-item" data-tool="map">
                    <span class="mobile-tool-icon">&#x1F5FA;</span><span>Ancient Map</span>
                </button>
                <button class="mobile-tool-item" data-tool="hebrew">
                    <span class="mobile-tool-icon">&#x1F4DC;</span><span>Learn Hebrew</span>
                </button>
                <button class="mobile-tool-item" data-tool="resources">
                    <span class="mobile-tool-icon">&#x1F4DA;</span><span>Resources</span>
                </button>
                <button class="mobile-tool-item" data-tool="progress">
                    <span class="mobile-tool-icon">&#x1F4C8;</span><span>My Progress</span>
                </button>
                <button class="mobile-tool-item" data-tool="prophecy">
                    <span class="mobile-tool-icon">&#x1F52E;</span><span>Prophecy Tracker</span>
                </button>
                <button class="mobile-tool-item" data-tool="beliefs">
                    <span class="mobile-tool-icon">&#x2696;</span><span>Core Beliefs</span>
                </button>
            </div>
        </div>
    </div>

    <!-- Mobile Bottom Navigation Bar -->
    <nav class="mobile-bottom-nav" id="mobileBottomNav" aria-label="Quick navigation">
        <button class="bottom-nav-btn" data-nav="home" aria-label="Home">
            <span class="bottom-nav-icon">&#x1F3E0;</span>
            <span class="bottom-nav-label">Home</span>
        </button>
        <button class="bottom-nav-btn" data-nav="search" aria-label="Search">
            <span class="bottom-nav-icon">&#x1F50D;</span>
            <span class="bottom-nav-label">Search</span>
        </button>
        <button class="bottom-nav-btn" data-nav="tools" aria-label="Study Tools">
            <span class="bottom-nav-icon">&#x2699;</span>
            <span class="bottom-nav-label">Tools</span>
        </button>
        <button class="bottom-nav-btn" data-nav="glossary" aria-label="Glossary">
            <span class="bottom-nav-icon">&#x1F4D3;</span>
            <span class="bottom-nav-label">Glossary</span>
        </button>
        <button class="bottom-nav-btn" data-nav="bookmarks" aria-label="Bookmarks">
            <span class="bottom-nav-icon">&#x2B50;</span>
            <span class="bottom-nav-label">Saved</span>
        </button>
    </nav>
"""

    # Mobile JS patches to inject into the IIFE
    mobile_js_patches = """
    // ── Fix getTextForChapter for mobile (ERA_DATA not preloaded) ──
    // Override: try ERA_DATA first, then fall back to prefix map
    function getTextForChapter(chId) {
        if (!chId) return null;
        // Try ERA_DATA lookup (works when data is loaded)
        if (typeof MANIFEST !== 'undefined' && MANIFEST.eras) {
            for (var _i = 0; _i < MANIFEST.eras.length; _i++) {
                var _eraChapters = ERA_DATA[MANIFEST.eras[_i].id] || [];
                for (var _j = 0; _j < _eraChapters.length; _j++) {
                    if (_eraChapters[_j].id === chId) return MANIFEST.eras[_i].text;
                }
            }
        }
        // Fallback: infer text from chapter ID prefix
        var prefix = chId.split('-')[0].toLowerCase();
        var prefixMap = {
            'gen': 'genesis', 'exo': 'exodus', 'lev': 'leviticus', 'num': 'numbers',
            'deu': 'deuteronomy', 'jos': 'joshua', 'jdg': 'judges', 'rut': 'ruth',
            '1sam': '1samuel', '2sam': '2samuel', '1ki': '1kings', '2ki': '2kings',
            'psa': 'psalms', 'isa': 'isaiah', 'dan': 'daniel', 'mat': 'matthew',
            'mrk': 'mark', 'luk': 'luke', 'joh': 'john', 'act': 'acts',
            'rom': 'romans', '1cor': '1corinthians', '2cor': '2corinthians',
            'gal': 'galatians', 'eph': 'ephesians', 'phi': 'philippians',
            'col': 'colossians', 'heb': 'hebrews', 'jas': 'james',
            '1pe': '1peter', '2pe': '2peter', '1jo': '1john', '2jo': '2john',
            '3jo': '3john', 'jud': 'jude', 'rev': 'revelation',
            'job': 'job', 'pro': 'proverbs', 'ecc': 'ecclesiastes',
            'son': 'songofsolomon', 'jer': 'jeremiah', 'eze': 'ezekiel',
            'lam': 'lamentations', 'hos': 'hosea', 'joe': 'joel', 'amo': 'amos',
            'oba': 'obadiah', 'jon': 'jonah', 'mic': 'micah', 'nah': 'nahum',
            'hab': 'habakkuk', 'zep': 'zephaniah', 'hag': 'haggai',
            'zec': 'zechariah', 'mal': 'malachi', '1ch': '1chronicles',
            '2ch': '2chronicles', 'ezr': 'ezra', 'neh': 'nehemiah', 'est': 'esther',
            'en': '1enoch', '1en': '1enoch'
        };
        if (prefixMap[prefix]) return prefixMap[prefix];
        // Try matching against known text IDs
        if (typeof MANIFEST !== 'undefined' && MANIFEST.texts) {
            for (var i = 0; i < MANIFEST.texts.length; i++) {
                if (chId.toLowerCase().indexOf(MANIFEST.texts[i].id) === 0) return MANIFEST.texts[i].id;
            }
        }
        return null;
    }

    // ── Mobile Tools Popup ─────────────────────────────────
    var mobileToolsPopup = document.getElementById('mobileToolsPopup');
    var mobileToolsBackdrop = document.getElementById('mobileToolsBackdrop');
    var mobileToolsClose = document.getElementById('mobileToolsClose');

    function openMobileTools() {
        if (mobileToolsPopup) mobileToolsPopup.classList.add('open');
    }
    function closeMobileTools() {
        if (mobileToolsPopup) mobileToolsPopup.classList.remove('open');
    }
    if (mobileToolsBackdrop) mobileToolsBackdrop.addEventListener('click', closeMobileTools);
    if (mobileToolsClose) mobileToolsClose.addEventListener('click', closeMobileTools);

    // Handle tool item clicks in popup
    var toolItems = document.querySelectorAll('.mobile-tool-item');
    toolItems.forEach(function(item) {
        item.addEventListener('click', function() {
            var tool = this.dataset.tool;
            closeMobileTools();
            closeSidebarMobile();
            if (tool === 'matrix') openMatrix();
            else if (tool === 'timeline') openTimeline();
            else if (tool === 'map') openMap();
            else if (tool === 'hebrew') openHebrew();
            else if (tool === 'resources') openResources();
            else if (tool === 'progress') openProgress();
            else if (tool === 'prophecy') showProphecyTracker();
            else if (tool === 'beliefs') showCoreBeliefs();
        });
    });

    // ── Mobile Bookmarks Overlay ─────────────────────────
    function openBookmarksOverlay() {
        var old = document.getElementById('bookmarksOverlay');
        if (old) old.remove();
        var ov = document.createElement('div');
        ov.className = 'bookmarks-full-overlay';
        ov.id = 'bookmarksOverlay';
        var h = '<div class="bookmarks-full-modal">' +
            '<div class="bm-full-header"><h2>\u2B50 Saved Chapters</h2>' +
            '<button class="bm-full-close" id="bmFullClose">&times;</button></div>' +
            '<div class="bm-full-content">';
        if (bookmarks.length === 0) {
            h += '<div class="bm-empty">No saved chapters yet.<br><span style="color:#9a968e;font-size:0.85rem">Tap the \u2606 Save button on any chapter to bookmark it.</span></div>';
        } else {
            bookmarks.forEach(function(id) {
                var ref = id, chTitle = '', textId = '';
                for (var i = 0; i < MANIFEST.eras.length; i++) {
                    var chapters = ERA_DATA[MANIFEST.eras[i].id] || [];
                    for (var c = 0; c < chapters.length; c++) {
                        if (chapters[c].id === id) {
                            ref = chapters[c].ref || chapters[c].title;
                            chTitle = chapters[c].title || '';
                            textId = MANIFEST.eras[i].text;
                            break;
                        }
                    }
                    if (textId) break;
                }
                h += '<div class="bm-full-item" data-id="' + id + '" data-text="' + textId + '">' +
                    '<div class="bm-full-info"><div class="bm-full-ref">' + ref + '</div>' +
                    (chTitle && chTitle !== ref ? '<div class="bm-full-title">' + chTitle + '</div>' : '') +
                    '</div><button class="bm-full-remove" data-id="' + id + '">&times;</button></div>';
            });
        }
        h += '</div></div>';
        ov.innerHTML = h;
        document.body.appendChild(ov);
        document.getElementById('bmFullClose').addEventListener('click', function() { ov.remove(); });
        ov.addEventListener('click', function(e) {
            if (e.target === ov) { ov.remove(); return; }
            var rm = e.target.closest('.bm-full-remove');
            if (rm) { toggleBookmark(rm.dataset.id); openBookmarksOverlay(); return; }
            var item = e.target.closest('.bm-full-item');
            if (item) {
                ov.remove();
                var t = item.dataset.text || detectTextFromHash(item.dataset.id);
                if (t && t !== currentText) selectText(t, true);
                setTimeout(function() { scrollToChapter(item.dataset.id); }, 200);
            }
        });
    }

    // ── Mobile Search Overlay (delegates to unified search) ──
    // The openSearchOverlay() in app.js handles the UI.
    // Mobile just needs to pre-load the search data first.
    var _origOpenSearchOverlay = openSearchOverlay;
    openSearchOverlay = async function() {
        await loadSearchData();
        _origOpenSearchOverlay();
    };

    // ── Mobile Bottom Nav Integration ─────────────────────
    document.addEventListener('mobile-nav', function(e) {
        var action = e.detail;
        closeMobileTools();
        if (action === 'home') {
            showLibrary();
            closeSidebarMobile();
        } else if (action === 'search') {
            closeSidebarMobile();
            openSearchOverlay();
        } else if (action === 'tools') {
            closeSidebarMobile();
            openMobileTools();
        } else if (action === 'glossary') {
            openGlossary();
            closeSidebarMobile();
        } else if (action === 'bookmarks') {
            closeSidebarMobile();
            openBookmarksOverlay();
        }
    });

    // ── Back Button Support ────────────────────
    window.addEventListener('popstate', function() {
        var hash = location.hash.replace('#', '');
        if (!hash && currentText) {
            showLibrary();
        }
    });

    // ── Sidebar Tools Toggle ────────────────────
    var toolsToggle = document.getElementById('sidebarToolsToggle');
    if (toolsToggle) {
        toolsToggle.addEventListener('click', function() {
            var footer = this.closest('.sidebar-footer');
            if (footer) footer.classList.toggle('tools-expanded');
        });
    }
"""

    bottom_nav_js = """
    <script>
    // Mobile bottom nav event dispatcher
    (function() {
        var nav = document.getElementById('mobileBottomNav');
        if (!nav) return;
        nav.addEventListener('click', function(e) {
            var btn = e.target.closest('.bottom-nav-btn');
            if (!btn) return;
            var action = btn.dataset.nav;
            nav.querySelectorAll('.bottom-nav-btn').forEach(function(b) { b.classList.remove('active'); });
            btn.classList.add('active');
            document.dispatchEvent(new CustomEvent('mobile-nav', {detail: action}));
        });
    })();
    </script>

    <script>
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('./sw.js').then(function(reg) {
            reg.update();
            setInterval(function() { reg.update(); }, 60000);
            reg.addEventListener('updatefound', function() {
                var nw = reg.installing;
                if (nw) nw.addEventListener('statechange', function() {
                    if (nw.state === 'activated') window.location.reload();
                });
            });
        }).catch(function(e) { console.log('SW failed:', e); });
        navigator.serviceWorker.addEventListener('controllerchange', function() {
            window.location.reload();
        });
    }
    </script>
"""

    # Inject mobile patches into the app JS before the launch section
    js_patched = js.replace(
        "// ── Launch",
        mobile_js_patches + "\n    // ── Launch"
    )

    # Fix const interlinear declarations to var (const can't be reassigned by eval)
    js_patched = js_patched.replace("const INTERLINEAR_NT_", "var INTERLINEAR_NT_")
    js_patched = js_patched.replace("const INTERLINEAR_JOB", "var INTERLINEAR_JOB")
    js_patched = js_patched.replace("const INTERLINEAR_PROVERBS", "var INTERLINEAR_PROVERBS")
    js_patched = js_patched.replace("const INTERLINEAR_ECCLESIASTES", "var INTERLINEAR_ECCLESIASTES")
    js_patched = js_patched.replace("const INTERLINEAR_SONGOFSOLOMON", "var INTERLINEAR_SONGOFSOLOMON")
    js_patched = js_patched.replace("const INTERLINEAR_JEREMIAH", "var INTERLINEAR_JEREMIAH")
    js_patched = js_patched.replace("const INTERLINEAR_EZEKIEL", "var INTERLINEAR_EZEKIEL")
    js_patched = js_patched.replace("const INTERLINEAR_LAMENTATIONS", "var INTERLINEAR_LAMENTATIONS")
    js_patched = js_patched.replace("const INTERLINEAR_1CHRONICLES", "var INTERLINEAR_1CHRONICLES")
    js_patched = js_patched.replace("const INTERLINEAR_2CHRONICLES", "var INTERLINEAR_2CHRONICLES")
    js_patched = js_patched.replace("const INTERLINEAR_EZRA", "var INTERLINEAR_EZRA")
    js_patched = js_patched.replace("const INTERLINEAR_NEHEMIAH", "var INTERLINEAR_NEHEMIAH")
    js_patched = js_patched.replace("const INTERLINEAR_ESTHER", "var INTERLINEAR_ESTHER")
    js_patched = js_patched.replace("const INTERLINEAR_HOSEA", "var INTERLINEAR_HOSEA")
    js_patched = js_patched.replace("const INTERLINEAR_JOEL", "var INTERLINEAR_JOEL")
    js_patched = js_patched.replace("const INTERLINEAR_AMOS", "var INTERLINEAR_AMOS")
    js_patched = js_patched.replace("const INTERLINEAR_OBADIAH", "var INTERLINEAR_OBADIAH")
    js_patched = js_patched.replace("const INTERLINEAR_JONAH", "var INTERLINEAR_JONAH")
    js_patched = js_patched.replace("const INTERLINEAR_MICAH", "var INTERLINEAR_MICAH")
    js_patched = js_patched.replace("const INTERLINEAR_NAHUM", "var INTERLINEAR_NAHUM")
    js_patched = js_patched.replace("const INTERLINEAR_HABAKKUK", "var INTERLINEAR_HABAKKUK")
    js_patched = js_patched.replace("const INTERLINEAR_ZEPHANIAH", "var INTERLINEAR_ZEPHANIAH")
    js_patched = js_patched.replace("const INTERLINEAR_HAGGAI", "var INTERLINEAR_HAGGAI")
    js_patched = js_patched.replace("const INTERLINEAR_ZECHARIAH", "var INTERLINEAR_ZECHARIAH")
    js_patched = js_patched.replace("const INTERLINEAR_MALACHI", "var INTERLINEAR_MALACHI")

    # Enable single-chapter view on mobile
    js_patched = js_patched.replace(
        "var singleChapterMode = false;",
        "var singleChapterMode = true;"
    )

    # Fix Home button to navigate to library
    js_patched = js_patched.replace(
        "// Scroll to top / reset view\\n                window.scrollTo(0, 0);",
        "showLibrary();\\n                closeSidebarMobile();"
    )
    # Alternative pattern matching
    js_patched = js_patched.replace(
        "// Scroll to top / reset view\n                window.scrollTo(0, 0);",
        "showLibrary();\n                closeSidebarMobile();"
    )

    # Fix sidebar toggle to add scroll lock
    js_patched = js_patched.replace(
        "sidebar.classList.toggle('open');\n            sidebarBackdrop.classList.toggle('visible');\n        });",
        "sidebar.classList.toggle('open');\n            sidebarBackdrop.classList.toggle('visible');\n            document.body.classList.toggle('sidebar-open', sidebar.classList.contains('open'));\n        });"
    )

    # Add sidebar close button handler after backdrop click handler
    js_patched = js_patched.replace(
        "sidebarBackdrop.addEventListener('click', closeSidebarMobile);",
        "sidebarBackdrop.addEventListener('click', closeSidebarMobile);\n        document.getElementById('sidebarCloseBtn').addEventListener('click', closeSidebarMobile);"
    )

    # Fix closeSidebarMobile to remove scroll lock class
    js_patched = js_patched.replace(
        "sidebar.classList.remove('open');\n        sidebarBackdrop.classList.remove('visible');\n    }",
        "sidebar.classList.remove('open');\n        sidebarBackdrop.classList.remove('visible');\n        document.body.classList.remove('sidebar-open');\n    }"
    )

    # Fix trail step navigation: infer textId when navText is empty
    js_patched = js_patched.replace(
        "var trailStep = e.target.closest('.trail-step');\n            if (trailStep && trailStep.dataset.navText) {",
        "var trailStep = e.target.closest('.trail-step');\n            if (trailStep) {\n                var _navText = trailStep.dataset.navText || getTextForChapter(trailStep.dataset.navChapter);\n                if (_navText) { trailStep.dataset.navText = _navText; }"
    )

    # Fix: on mobile, don't open reading pane for texts without interlinear (HTML fragments)
    # The main content already shows chapter cards, reading pane just covers them
    js_patched = js_patched.replace(
        "} else {\n                // Show source reading pane for texts without interlinear\n                sourceReadingMode = true;\n                document.body.classList.add('source-reading-active');\n                setReadingPane(true);\n                renderSourceReading(textId, null);\n            }",
        "} else {\n                // On mobile, hide reading pane for texts without interlinear\n                // Main content already shows chapter cards\n                if (typeof IS_MOBILE !== 'undefined' && IS_MOBILE) {\n                    setReadingPane(false);\n                    sourceReadingMode = false;\n                    document.body.classList.remove('source-reading-active');\n                } else {\n                    sourceReadingMode = true;\n                    document.body.classList.add('source-reading-active');\n                    setReadingPane(true);\n                    renderSourceReading(textId, null);\n                }\n            }"
    )

    # Fix: on mobile, don't auto-open reading pane for texts WITH interlinear either
    # Users should see study content (deep dives, eras, chapter cards) by default
    # They can open the interlinear reader via the "Reader" bottom nav button
    js_patched = js_patched.replace(
        "sourceReadingMode = false;\n                document.body.classList.remove('source-reading-active');\n                setReadingPane(true);\n                renderInterlinear(1);",
        "sourceReadingMode = false;\n                document.body.classList.remove('source-reading-active');\n                if (typeof IS_MOBILE !== 'undefined' && IS_MOBILE) {\n                    setReadingPane(false);\n                } else {\n                    setReadingPane(true);\n                }\n                renderInterlinear(1);"
    )

    # Fix: scrollToChapter should always close reading pane on mobile
    # This ensures study content is visible after any navigation (trail stops, sidebar, etc.)
    js_patched = js_patched.replace(
        "function scrollToChapter(id) {\n        logEvent('chapter_view', id);",
        "function scrollToChapter(id) {\n        if (typeof IS_MOBILE !== 'undefined' && IS_MOBILE) { setReadingPane(false); }\n        logEvent('chapter_view', id);"
    )

    # Fix: on mobile, always regenerate content (data loads on demand, cache may be stale)
    js_patched = js_patched.replace(
        "// Cache generated HTML but always update the DOM\n        if (!textContentCache[textId]) {",
        "// Cache generated HTML but always update the DOM\n        if (typeof IS_MOBILE !== 'undefined' && IS_MOBILE) { delete textContentCache[textId]; }\n        if (!textContentCache[textId]) {"
    )

    # Fix trail step navigation: use .then() for async selectText, close reading pane on mobile
    js_patched = js_patched.replace(
        "selectText(trailStep.dataset.navText, true);\n                if (trailStep.dataset.navChapter) {\n                    requestAnimationFrame(function() {\n                        scrollToChapter(trailStep.dataset.navChapter);\n                    });\n                }",
        "var _trailChId = trailStep.dataset.navChapter;\n                selectText(trailStep.dataset.navText, true).then(function() {\n                    if (typeof IS_MOBILE !== 'undefined' && IS_MOBILE) {\n                        setReadingPane(false);\n                    }\n                    if (_trailChId) {\n                        setTimeout(function() { scrollToChapter(_trailChId); }, 150);\n                    }\n                });"
    )

    # Fix: search verse click should not re-open reading pane on mobile
    js_patched = js_patched.replace(
        "currentILBook = textId;\n                        renderInterlinear(chNum);\n                        setReadingPane(true);",
        "currentILBook = textId;\n                        renderInterlinear(chNum);\n                        if (!(typeof IS_MOBILE !== 'undefined' && IS_MOBILE)) { setReadingPane(true); }"
    )

    # Fix glossary to load data before rendering + auto-scroll to highlighted term
    js_patched = js_patched.replace(
        "function openGlossary(highlightTerm) {\n        renderGlossaryEntries(highlightTerm);",
        "async function openGlossary(highlightTerm) {\n        await loadGlossary();\n        renderGlossaryEntries(highlightTerm);"
    )

    # Fix: glossary should scroll to highlighted term after opening
    js_patched = js_patched.replace(
        "glossaryOverlay.classList.add('open');\n        if (highlightTerm) {\n            glossarySearch.value = highlightTerm;\n            filterGlossary(highlightTerm);",
        "glossaryOverlay.classList.add('open');\n        if (highlightTerm) {\n            glossarySearch.value = highlightTerm;\n            filterGlossary(highlightTerm);\n            // Auto-scroll to highlighted entry\n            setTimeout(function() {\n                var highlighted = glossaryList.querySelector('[style*=\"gold-dim\"]');\n                if (highlighted) highlighted.scrollIntoView({ behavior: 'smooth', block: 'center' });\n            }, 100);"
    )

    # Fix resources to load data before rendering
    js_patched = js_patched.replace(
        "function openResources() {\n        renderResourceFilters();",
        "async function openResources() {\n        await loadResources();\n        renderResourceFilters();"
    )

    # Fix matrix to load data before rendering
    js_patched = js_patched.replace(
        "function openMatrix() {\n        logEvent('feature', 'bible_truth_matrix');\n        renderMatrix();",
        "async function openMatrix() {\n        logEvent('feature', 'bible_truth_matrix');\n        await loadCoreBeliefs();\n        await loadReligionsDetail();\n        renderMatrix();"
    )

    # Fix religion detail to load data before showing
    js_patched = js_patched.replace(
        "function showReligionDetail(religionId) {\n        logEvent('feature', 'religion_detail_' + religionId);",
        "async function showReligionDetail(religionId) {\n        await loadReligionsDetail();\n        logEvent('feature', 'religion_detail_' + religionId);"
    )

    # Fix prophecy matrix to load data before rendering
    js_patched = js_patched.replace(
        "function showProphecyMatrix() {\n        libraryMode = true;",
        "async function showProphecyMatrix() {\n        await loadProphecy();\n        libraryMode = true;"
    )

    # Fix prophecy tracker to load data before rendering
    js_patched = js_patched.replace(
        "function showProphecyTracker(bookFilter) {\n        libraryMode = true;",
        "async function showProphecyTracker(bookFilter) {\n        await loadProphecy();\n        libraryMode = true;"
    )

    # Fix core beliefs to load data before rendering
    js_patched = js_patched.replace(
        "function showCoreBeliefs(topicId) {\n        libraryMode = true;",
        "async function showCoreBeliefs(topicId) {\n        await loadCoreBeliefs();\n        libraryMode = true;"
    )

    # Fix search results to close sidebar
    js_patched = js_patched.replace(
        "searchResults.classList.remove('visible');\n                    searchInput.value = '';\n                    var textId",
        "searchResults.classList.remove('visible');\n                    searchInput.value = '';\n                    closeSidebarMobile();\n                    var textId"
    )

    html += f"""
{bottom_nav_html}
    <script>
{js_patched}
    </script>
{bottom_nav_js}
</body>
</html>"""

    # Replace references
    html = html.replace('Developer Progress', 'About This App')
    html = html.replace('Open developer progress', 'About this app')

    # Write
    out_path = os.path.join(OUTPUT_DIR, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    html_size = len(html.encode("utf-8"))
    print(f"  index.html: {html_size:,} bytes ({html_size/1024/1024:.1f} MB)")

    # ══════════════════════════════════════════════════════════
    # 5. GENERATE PWA FILES
    # ══════════════════════════════════════════════════════════
    print("\n[5/6] Generating PWA files...")

    # manifest.webmanifest
    pwa_manifest = {
        "name": "Ancient Texts Library",
        "short_name": "Ancient Texts",
        "description": "A scholarly study of sacred & ancient writings with original language interlinear",
        "start_url": "./index.html",
        "display": "standalone",
        "background_color": "#0c0e14",
        "theme_color": "#0c0e14",
        "orientation": "portrait-primary",
        "icons": [
            {"src": "icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"}
        ]
    }
    with open(os.path.join(OUTPUT_DIR, "manifest.webmanifest"), "w") as f:
        json.dump(pwa_manifest, f, indent=2)
    print("  manifest.webmanifest")

    # Service worker (cache name includes build timestamp for cache busting)
    from datetime import datetime
    build_ts = datetime.now().strftime('%Y%m%d%H%M%S')
    sw_js = """// Ancient Texts Library — Service Worker
const CACHE_NAME = 'ancient-texts-""" + build_ts + """';
const CORE_ASSETS = [
    './',
    './index.html',
    './manifest.webmanifest',
    './data/manifest.json',
    './data/text_intros.json',
    'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css',
    'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js'
];

self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => cache.addAll(CORE_ASSETS))
    );
    self.skipWaiting();
});

self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(keys =>
            Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
        )
    );
    self.clients.claim();
});

self.addEventListener('fetch', event => {
    // Network-first for ALL requests — always try to get fresh content
    // Falls back to cache when offline
    event.respondWith(
        fetch(event.request).then(resp => {
            if (resp.ok) {
                const clone = resp.clone();
                caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
            }
            return resp;
        }).catch(() => caches.match(event.request))
    );
});
"""
    with open(os.path.join(OUTPUT_DIR, "sw.js"), "w") as f:
        f.write(sw_js)
    print("  sw.js (service worker)")

    # Generate simple SVG icons (gold ע on dark background)
    for size in [180, 192, 512]:
        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}">
  <rect width="{size}" height="{size}" fill="#0c0e14"/>
  <text x="50%" y="55%" dominant-baseline="middle" text-anchor="middle"
        font-family="serif" font-size="{int(size*0.55)}" fill="#c9a84c">ע</text>
</svg>"""
        svg_path = os.path.join(OUTPUT_DIR, f"icon-{size}.svg")
        png_path = os.path.join(OUTPUT_DIR, f"icon-{size}.png")
        with open(svg_path, "w", encoding="utf-8") as f:
            f.write(svg)
        # Try to convert SVG to PNG using Python
        try:
            import cairosvg
            cairosvg.svg2png(bytestring=svg.encode(), write_to=png_path, output_width=size, output_height=size)
            os.remove(svg_path)
        except ImportError:
            # Fallback: keep SVG, update manifest to use SVG
            os.rename(svg_path, png_path.replace('.png', '.svg'))
            print(f"  icon-{size}.svg (install cairosvg for PNG)")

    # Also add service worker registration to the HTML (fallback)
    sw_register = """
    <script>
    if ('serviceWorker' in navigator && !navigator.serviceWorker.controller) {
        navigator.serviceWorker.register('./sw.js').then(function(reg) {
            reg.update();
        }).catch(function(e) { console.log('SW failed:', e); });
    }
    </script>
"""
    # Insert before closing </body>
    final_html = read_file(out_path)
    final_html = final_html.replace("</body>", sw_register + "</body>")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    # ══════════════════════════════════════════════════════════
    # 6. SUMMARY
    # ══════════════════════════════════════════════════════════
    print("\n[6/6] Build complete!")

    # Calculate total data size
    total_data = 0
    for root, dirs, files in os.walk(DATA_OUT):
        for f in files:
            total_data += os.path.getsize(os.path.join(root, f))

    shell_size = os.path.getsize(out_path)

    print(f"\n{'=' * 60}")
    print(f"  MOBILE PWA BUILD SUCCESSFUL")
    print(f"  Output: {OUTPUT_DIR}")
    print(f"  App shell: {shell_size:,} bytes ({shell_size/1024/1024:.1f} MB)")
    print(f"  Data files: {total_data:,} bytes ({total_data/1024/1024:.1f} MB)")
    print(f"  Initial load: ~{shell_size/1024/1024:.1f} MB (shell + manifest)")
    print(f"  Per-text load: ~1-3 MB on demand")
    print(f"{'=' * 60}")
    print(f"\n  To test locally:")
    # Copy docs/ reference files to mobile output
    docs_src = os.path.join(BASE_DIR, "docs", "bible_study_reference.html")
    if os.path.exists(docs_src):
        docs_dest = os.path.join(OUTPUT_DIR, "docs")
        os.makedirs(docs_dest, exist_ok=True)
        shutil.copy2(docs_src, docs_dest)
        print(f"  Copied bible_study_reference.html to docs/")

    print(f"\n  To test locally:")
    print(f"    cd output/mobile")
    print(f"    python -m http.server 8080")
    print(f"    Open http://localhost:8080 on your phone (same WiFi)")
    print(f"\n  To deploy: upload output/mobile/ to any static host")
    print(f"  (GitHub Pages, Netlify, Vercel, Cloudflare Pages)")
    print()


if __name__ == "__main__":
    main()
