"""
server/rag/indexer.py — Build the Hallelujah AI knowledge index.

Reads ALL study content from the Ancient Texts Study app and indexes it
into a SQLite FTS5 database for fast full-text retrieval.

Content indexed:
  - 839+ study chapters (synopsis, sections, cross-refs, Hebrew terms)
  - 553 glossary terms (Hebrew/Greek/Aramaic with definitions)
  - 22,723 flow verse translations
  - 59+ prophecy matrix entries
  - 500+ book prophecy entries
  - 5,932 cross-references
  - 7 policy YAML files (Berean Protocol, hermeneutics, boundaries, etc.)

Usage:
  python -m server.rag.indexer          # Build/rebuild the index
  python -m server.rag.indexer --force  # Force full rebuild
"""
import os
import sys
import json
import sqlite3
import importlib.util
import time
import yaml

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data")
POLICY_DIR = os.path.join(BASE_DIR, "policy")
RAG_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(RAG_DIR, "hallelujah.db")
CONTENT_MAP = os.path.join(BASE_DIR, "CONTENT_MAP.json")
MANIFEST_PATH = os.path.join(BASE_DIR, "manifest.json")


def load_module(name, path):
    """Dynamically load a Python data module."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def create_tables(conn):
    """Create all FTS5 and regular tables."""
    c = conn.cursor()

    # Drop existing tables for clean rebuild
    c.execute("DROP TABLE IF EXISTS chapters_fts")
    c.execute("DROP TABLE IF EXISTS glossary_fts")
    c.execute("DROP TABLE IF EXISTS flow_fts")
    c.execute("DROP TABLE IF EXISTS prophecy_fts")
    c.execute("DROP TABLE IF EXISTS policy_fts")
    c.execute("DROP TABLE IF EXISTS cross_refs")
    c.execute("DROP TABLE IF EXISTS meta")

    # Chapters — full study content
    c.execute("""
        CREATE VIRTUAL TABLE chapters_fts USING fts5(
            chapter_id,
            text_id,
            ref,
            title,
            synopsis,
            section_content,
            hebrew_terms,
            cross_ref_notes,
            ane_backdrop,
            divine_council_note,
            key_verse_text,
            tokenize='porter unicode61'
        )
    """)

    # Glossary — Hebrew/Greek/Aramaic terms
    c.execute("""
        CREATE VIRTUAL TABLE glossary_fts USING fts5(
            term_slug,
            hebrew,
            transliteration,
            strongs,
            gloss,
            definition,
            chapters_used,
            tokenize='porter unicode61'
        )
    """)

    # Flow verse translations
    c.execute("""
        CREATE VIRTUAL TABLE flow_fts USING fts5(
            text_id,
            chapter_num,
            verse_num,
            ref,
            flow_text,
            tokenize='porter unicode61'
        )
    """)

    # Prophecies (matrix + tracker combined)
    c.execute("""
        CREATE VIRTUAL TABLE prophecy_fts USING fts5(
            prophecy_id,
            category,
            title,
            ot_ref,
            nt_ref,
            ot_text,
            nt_text,
            fulfillment,
            status,
            ot_hebrew,
            significance,
            tokenize='porter unicode61'
        )
    """)

    # Policy knowledge — Berean Protocol, hermeneutics, analytical frameworks
    c.execute("""
        CREATE VIRTUAL TABLE policy_fts USING fts5(
            policy_file,
            policy_name,
            section_id,
            section_name,
            content,
            scriptural_basis,
            tokenize='porter unicode61'
        )
    """)

    # Cross-references (regular table for graph queries)
    c.execute("""
        CREATE TABLE cross_refs (
            source_chapter TEXT,
            ref TEXT,
            note TEXT,
            type TEXT
        )
    """)
    c.execute("CREATE INDEX idx_xref_source ON cross_refs(source_chapter)")
    c.execute("CREATE INDEX idx_xref_ref ON cross_refs(ref)")

    # Metadata
    c.execute("""
        CREATE TABLE meta (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    """)

    conn.commit()


def index_chapters(conn):
    """Index all study chapters from era data files."""
    print("\n[chapters] Indexing study chapters...")

    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    all_texts = manifest.get("texts", [])
    text_map = {t["id"]: t for t in all_texts}

    chapter_count = 0
    xref_count = 0
    c = conn.cursor()

    for era in manifest.get("eras", []):
        text_id = era.get("text")
        text_def = text_map.get(text_id)
        if not text_def:
            continue

        # Skip html_fragment eras
        if era.get("content_type") == "html_fragment":
            continue

        data_dir = text_def.get("data_dir", text_id)
        data_file = os.path.join(DATA_DIR, data_dir, era["data_file"] + ".py")
        if not os.path.exists(data_file):
            data_file = os.path.join(DATA_DIR, era["data_file"] + ".py")
        if not os.path.exists(data_file):
            continue

        try:
            mod = load_module(era["data_file"], data_file)
        except Exception as e:
            print(f"  WARNING: Could not load {era['data_file']}: {e}")
            continue

        chapters = getattr(mod, "CHAPTERS", [])

        for ch in chapters:
            ch_id = ch.get("id", "")
            ref = ch.get("ref", "")
            title = ch.get("title", "")
            synopsis = ch.get("synopsis", "")

            # Concatenate all section bodies
            sections = ch.get("sections", [])
            section_text = "\n\n".join(
                f"{s.get('heading', '')}\n{s.get('body', '')}"
                for s in sections
            )

            # Hebrew terms as comma-separated (can be strings or dicts)
            raw_terms = ch.get("hebrew_terms", [])
            term_strs = []
            for t in raw_terms:
                if isinstance(t, str):
                    term_strs.append(t)
                elif isinstance(t, dict):
                    # Some texts use {term, transliteration, meaning} dicts
                    term_strs.append(
                        f"{t.get('term', '')} ({t.get('transliteration', '')}): {t.get('meaning', '')}"
                    )
            hebrew_terms = ", ".join(term_strs)

            # Cross-reference notes
            xrefs = ch.get("cross_refs", [])
            xref_notes = "\n".join(
                f"{x.get('ref', '')}: {x.get('note', '')}"
                for x in xrefs
            )

            # Index cross-refs into separate table too
            for x in xrefs:
                c.execute(
                    "INSERT INTO cross_refs (source_chapter, ref, note, type) VALUES (?, ?, ?, ?)",
                    (ch_id, x.get("ref", ""), x.get("note", ""), x.get("type", ""))
                )
                xref_count += 1

            ane = ch.get("ane_backdrop", "") or ""
            council = ch.get("divine_council_note", "") or ""

            key_verse = ch.get("key_verse", {})
            kv_text = ""
            if key_verse:
                kv_text = f"{key_verse.get('ref', '')}: {key_verse.get('text', '')}"

            c.execute(
                "INSERT INTO chapters_fts VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (ch_id, text_id, ref, title, synopsis, section_text,
                 hebrew_terms, xref_notes, ane, council, kv_text)
            )
            chapter_count += 1

    conn.commit()
    print(f"  Indexed {chapter_count} chapters, {xref_count} cross-references")
    return chapter_count


def index_glossary(conn):
    """Index the glossary of Hebrew/Greek/Aramaic terms."""
    print("\n[glossary] Indexing glossary terms...")

    glossary_path = os.path.join(DATA_DIR, "glossary.py")
    if not os.path.exists(glossary_path):
        print("  WARNING: glossary.py not found")
        return 0

    mod = load_module("glossary", glossary_path)
    glossary = getattr(mod, "GLOSSARY", {})

    c = conn.cursor()
    count = 0

    for slug, entry in glossary.items():
        hebrew = entry.get("hebrew", "")
        translit = entry.get("transliteration", "")
        strongs = entry.get("strongs", "")
        gloss = entry.get("gloss", "")
        definition = entry.get("definition", "")
        chapters = ", ".join(entry.get("chapters_used", []))

        c.execute(
            "INSERT INTO glossary_fts VALUES (?, ?, ?, ?, ?, ?, ?)",
            (slug, hebrew, translit, strongs, gloss, definition, chapters)
        )
        count += 1

    conn.commit()
    print(f"  Indexed {count} glossary terms")
    return count


def index_flow_verses(conn):
    """Index all flow verse translations."""
    print("\n[flow] Indexing flow verse translations...")

    flow_dir = os.path.join(DATA_DIR, "flow")
    if not os.path.isdir(flow_dir):
        print("  WARNING: flow/ directory not found")
        return 0

    c = conn.cursor()
    count = 0

    # Map of flow file prefixes to text IDs
    for flow_file in sorted(os.listdir(flow_dir)):
        if not (flow_file.startswith("flow_") and flow_file.endswith(".py")):
            continue
        # Handle multi-part files like flow_genesis_1_10.py
        if flow_file.count("_") > 1:
            # Extract book name from flow_genesis_1_10.py → genesis
            parts = flow_file.replace("flow_", "").replace(".py", "").split("_")
            # The book name is everything before the first numeric part
            book_parts = []
            for p in parts:
                if p.isdigit():
                    break
                book_parts.append(p)
            text_id = "_".join(book_parts) if book_parts else parts[0]
        else:
            text_id = flow_file.replace("flow_", "").replace(".py", "")

        flow_path = os.path.join(flow_dir, flow_file)
        try:
            mod = load_module(flow_file.replace(".py", ""), flow_path)
        except Exception as e:
            print(f"  WARNING: Could not load {flow_file}: {e}")
            continue

        # Find the FLOW_* data attribute
        flow_data = None
        for attr in dir(mod):
            if attr.startswith("FLOW"):
                flow_data = getattr(mod, attr)
                break

        if not flow_data or not isinstance(flow_data, dict):
            continue

        for ch_num, verses in flow_data.items():
            if not isinstance(verses, dict):
                continue
            for v_num, text in verses.items():
                if not isinstance(text, str):
                    continue
                ref = f"{text_id} {ch_num}:{v_num}"
                c.execute(
                    "INSERT INTO flow_fts VALUES (?, ?, ?, ?, ?)",
                    (text_id, str(ch_num), str(v_num), ref, text)
                )
                count += 1

    conn.commit()
    print(f"  Indexed {count} flow verse translations")
    return count


def index_prophecies(conn):
    """Index prophecy matrix and book prophecies."""
    print("\n[prophecy] Indexing prophecies...")

    c = conn.cursor()
    count = 0

    # Prophecy Matrix
    pm_path = os.path.join(DATA_DIR, "prophecy_matrix.py")
    if os.path.exists(pm_path):
        mod = load_module("prophecy_matrix", pm_path)
        matrix = getattr(mod, "PROPHECY_MATRIX", [])

        for p in matrix:
            c.execute(
                "INSERT INTO prophecy_fts VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    p.get("id", ""),
                    p.get("category", ""),
                    p.get("title", ""),
                    p.get("ot_ref", ""),
                    p.get("nt_ref", ""),
                    p.get("ot_text", ""),
                    p.get("nt_text", ""),
                    p.get("fulfillment", ""),
                    p.get("status", ""),
                    p.get("ot_hebrew", ""),
                    p.get("significance", "")
                )
            )
            count += 1

    # Book Prophecies (prophecy tracker)
    pt_path = os.path.join(DATA_DIR, "prophecy_tracker.py")
    if os.path.exists(pt_path):
        mod = load_module("prophecy_tracker", pt_path)
        books = getattr(mod, "BOOK_PROPHECIES", {})

        for book_id, book_data in books.items():
            for p in book_data.get("prophecies", []):
                # Combine Christian and Jewish views into fulfillment text
                christian = p.get("christian_view", {})
                jewish = p.get("jewish_view", {})
                fulfillment = (
                    f"Christian: {christian.get('explanation', '')} "
                    f"Jewish: {jewish.get('explanation', '')}"
                )
                status = christian.get("status", "")
                nt_ref = christian.get("fulfillment_ref", "")

                c.execute(
                    "INSERT INTO prophecy_fts VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (
                        p.get("id", ""),
                        p.get("category", ""),
                        p.get("title", ""),
                        p.get("ref", ""),
                        nt_ref,
                        p.get("text_snippet", ""),
                        "",
                        fulfillment,
                        status,
                        "",
                        ""
                    )
                )
                count += 1

    conn.commit()
    print(f"  Indexed {count} prophecy entries")
    return count


def index_policies(conn):
    """Index all YAML policy files into searchable knowledge.

    This makes the full Berean Protocol, hermeneutic principles, analytical
    lenses, cognitive bias detection, and all other policy content available
    to the AI through RAG retrieval. The system prompt only has room for
    compressed versions — this gives the AI access to the FULL frameworks.
    """
    print("\n[policy] Indexing policy YAML files...")

    if not os.path.isdir(POLICY_DIR):
        print("  WARNING: policy/ directory not found")
        return 0

    c = conn.cursor()
    count = 0

    for fname in sorted(os.listdir(POLICY_DIR)):
        if not fname.endswith(".yaml"):
            continue

        fpath = os.path.join(POLICY_DIR, fname)
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f) or {}
        except Exception as e:
            print(f"  WARNING: Could not load {fname}: {e}")
            continue

        policy_name = data.get("name", fname.replace(".yaml", ""))

        # Index core_principles (critical_analysis.yaml, bible_bound.yaml)
        for principle in data.get("core_principles", []):
            pid = principle.get("id", "")
            rule = principle.get("rule", "")
            basis = principle.get("basis", "")
            c.execute(
                "INSERT INTO policy_fts VALUES (?, ?, ?, ?, ?, ?)",
                (fname, policy_name, pid, "Core Principle", rule, basis)
            )
            count += 1

        # Index hermeneutic principles (bible_bound.yaml)
        for principle in data.get("principles", []):
            pid = principle.get("id", "")
            rule = principle.get("rule", "")
            basis = principle.get("basis", "")
            c.execute(
                "INSERT INTO policy_fts VALUES (?, ?, ?, ?, ?, ?)",
                (fname, policy_name, pid, "Hermeneutic Principle", rule, basis)
            )
            count += 1

        # Index boundaries (boundaries.yaml)
        for boundary in data.get("boundaries", []):
            bid = boundary.get("id", "")
            rule = boundary.get("rule", "")
            basis = boundary.get("basis", "")
            c.execute(
                "INSERT INTO policy_fts VALUES (?, ?, ?, ?, ?, ?)",
                (fname, policy_name, bid, "Boundary", rule, basis)
            )
            count += 1

        # Index analytical method steps (critical_analysis.yaml)
        method = data.get("analytical_method", {})
        if method:
            for step in method.get("steps", []):
                step_name = step.get("name", "")
                desc = step.get("description", "")
                step_id = f"STEP:{step.get('step', '')}"
                c.execute(
                    "INSERT INTO policy_fts VALUES (?, ?, ?, ?, ?, ?)",
                    (fname, policy_name, step_id, f"Berean Decomposition: {step_name}", desc, "")
                )
                count += 1

        # Index evidence confidence scale (critical_analysis.yaml)
        for level in data.get("evidence_confidence_scale", []):
            level_name = level.get("level", "")
            defn = level.get("definition", "")
            example = level.get("example", "")
            content = f"{defn} Example: {example}" if example else defn
            c.execute(
                "INSERT INTO policy_fts VALUES (?, ?, ?, ?, ?, ?)",
                (fname, policy_name, level_name, "Evidence Confidence Scale", content, "")
            )
            count += 1

        # Index cognitive biases (critical_analysis.yaml)
        for bias in data.get("cognitive_biases_to_flag", []):
            bias_name = bias.get("name", "")
            desc = bias.get("description", "")
            counter = bias.get("counter", "")
            content = f"{desc} Counter: {counter}" if counter else desc
            c.execute(
                "INSERT INTO policy_fts VALUES (?, ?, ?, ?, ?, ?)",
                (fname, policy_name, f"BIAS:{bias_name}", f"Cognitive Bias: {bias_name}", content, "")
            )
            count += 1

        # Index analytical lenses (pattern_recognition.yaml)
        for lens_key, lens in data.get("analytical_lenses", {}).items():
            lens_name = lens.get("name", lens_key)
            desc = lens.get("description", "")
            checklist = lens.get("checklist", [])
            principle = lens.get("key_principle", "")
            content = f"{desc}\nChecklist:\n" + "\n".join(f"- {item}" for item in checklist)
            if principle:
                content += f"\nKey principle: {principle}"
            c.execute(
                "INSERT INTO policy_fts VALUES (?, ?, ?, ?, ?, ?)",
                (fname, policy_name, f"LENS:{lens_key}", f"Analytical Lens: {lens_name}", content, "")
            )
            count += 1

        # Index recurring patterns (pattern_recognition.yaml)
        patterns_section = data.get("recurring_patterns", {})
        for pattern in patterns_section.get("patterns", []):
            p_name = pattern.get("name", "")
            desc = pattern.get("description", "")
            indicator = pattern.get("indicator", "")
            content = f"{desc} Indicator: {indicator}" if indicator else desc
            c.execute(
                "INSERT INTO policy_fts VALUES (?, ?, ?, ?, ?, ?)",
                (fname, policy_name, f"PATTERN:{p_name}", f"Deception Pattern: {p_name}", content, "")
            )
            count += 1

        # Index the Kingdom Test (critical_analysis.yaml)
        kingdom = data.get("the_ultimate_test", {})
        if kingdom:
            k_name = kingdom.get("name", "")
            k_desc = kingdom.get("description", "")
            k_basis = "\n".join(kingdom.get("basis", []))
            how_to = "\n".join(kingdom.get("how_to_call_out_evil", []))
            content = f"{k_desc}\nHow to call out evil:\n{how_to}" if how_to else k_desc
            c.execute(
                "INSERT INTO policy_fts VALUES (?, ?, ?, ?, ?, ?)",
                (fname, policy_name, "KINGDOM_TEST", f"The Kingdom Test: {k_name}", content, k_basis)
            )
            count += 1

        # Index divine council theology (bible_bound.yaml)
        council = data.get("divine_council_theology", {})
        if council:
            position = council.get("position", "")
            d32 = council.get("deuteronomy_32_8", "")
            gen6 = council.get("genesis_6", "")
            christo = council.get("christological", "")
            content = f"{position}\nDeut 32:8: {d32}\nGenesis 6: {gen6}\nChristological: {christo}"
            c.execute(
                "INSERT INTO policy_fts VALUES (?, ?, ?, ?, ?, ?)",
                (fname, policy_name, "DIVINE_COUNCIL", "Divine Council Theology", content, "Psalm 82:1, 1 Kings 22:19-23, Deuteronomy 32:8-9, Job 1-2")
            )
            count += 1

        # Index claim labels (claim_labels.yaml)
        labels = data.get("labels", {})
        for label_key, label_data in labels.items():
            if isinstance(label_data, dict):
                l_name = label_data.get("name", "")
                l_def = label_data.get("definition", "")
                l_req = label_data.get("requirement", "")
                l_ex = label_data.get("example", "")
                content = f"[{label_key}] {l_name}: {l_def}. Requirement: {l_req}. Example: {l_ex}"
                c.execute(
                    "INSERT INTO policy_fts VALUES (?, ?, ?, ?, ?, ?)",
                    (fname, policy_name, f"LABEL:{label_key}", f"Claim Label [{label_key}]", content, "1 Thessalonians 5:21")
                )
                count += 1

        # Index forbidden phrases and tone (critical_analysis.yaml)
        tone = data.get("tone", {})
        if isinstance(tone, dict):
            tone_rule = tone.get("rule", "")
            forbidden = tone.get("forbidden_phrases", [])
            if tone_rule or forbidden:
                content = tone_rule
                if forbidden:
                    content += "\nForbidden phrases:\n" + "\n".join(f"- {fp}" for fp in forbidden)
                c.execute(
                    "INSERT INTO policy_fts VALUES (?, ?, ?, ?, ?, ?)",
                    (fname, policy_name, "TONE", "Tone and Conduct", content, "")
                )
                count += 1

        # Index integrity requirements (pattern_recognition.yaml)
        integrity = data.get("integrity_requirements", [])
        if integrity:
            content = "Intellectual integrity requirements:\n" + "\n".join(f"- {r}" for r in integrity)
            c.execute(
                "INSERT INTO policy_fts VALUES (?, ?, ?, ?, ?, ?)",
                (fname, policy_name, "INTEGRITY", "Integrity Requirements", content, "")
            )
            count += 1

        # Index forbidden analytical behaviors (pattern_recognition.yaml)
        forbidden_list = data.get("forbidden", [])
        if forbidden_list:
            content = "Forbidden analytical behaviors:\n" + "\n".join(f"- {r}" for r in forbidden_list)
            c.execute(
                "INSERT INTO policy_fts VALUES (?, ?, ?, ?, ?, ?)",
                (fname, policy_name, "FORBIDDEN", "Forbidden Behaviors", content, "")
            )
            count += 1

        # Index identity info (critical_analysis.yaml)
        identity = data.get("identity", "")
        if identity and isinstance(identity, str) and len(identity) > 20:
            c.execute(
                "INSERT INTO policy_fts VALUES (?, ?, ?, ?, ?, ?)",
                (fname, policy_name, "IDENTITY", "AI Identity", identity, "")
            )
            count += 1

    conn.commit()
    print(f"  Indexed {count} policy entries from {len([f for f in os.listdir(POLICY_DIR) if f.endswith('.yaml')])} YAML files")
    return count


def build_index(force=False):
    """Build the complete RAG index."""
    if os.path.exists(DB_PATH) and not force:
        # Check if index is recent (within last hour)
        age = time.time() - os.path.getmtime(DB_PATH)
        if age < 3600:
            print(f"[rag] Index exists and is recent ({age:.0f}s old). Use --force to rebuild.")
            return DB_PATH

    print("=" * 60)
    print("  HALLELUJAH AI — Building Knowledge Index")
    print("  \"Buy truth, and do not sell it\" — Proverbs 23:23")
    print("=" * 60)

    start = time.time()

    conn = sqlite3.connect(DB_PATH)
    create_tables(conn)

    chapters = index_chapters(conn)
    glossary = index_glossary(conn)
    flow = index_flow_verses(conn)
    prophecies = index_prophecies(conn)
    policies = index_policies(conn)

    # Write metadata
    c = conn.cursor()
    c.execute("INSERT INTO meta VALUES ('built_at', ?)", (time.strftime("%Y-%m-%d %H:%M:%S"),))
    c.execute("INSERT INTO meta VALUES ('chapters', ?)", (str(chapters),))
    c.execute("INSERT INTO meta VALUES ('glossary', ?)", (str(glossary),))
    c.execute("INSERT INTO meta VALUES ('flow_verses', ?)", (str(flow),))
    c.execute("INSERT INTO meta VALUES ('prophecies', ?)", (str(prophecies),))
    c.execute("INSERT INTO meta VALUES ('policies', ?)", (str(policies),))
    conn.commit()

    # Get DB size
    conn.close()
    db_size = os.path.getsize(DB_PATH)
    elapsed = time.time() - start

    print(f"\n{'=' * 60}")
    print(f"  INDEX BUILT SUCCESSFULLY")
    print(f"  Location: {DB_PATH}")
    print(f"  Size: {db_size / 1024 / 1024:.1f} MB")
    print(f"  Chapters: {chapters}")
    print(f"  Glossary terms: {glossary}")
    print(f"  Flow verses: {flow}")
    print(f"  Prophecies: {prophecies}")
    print(f"  Policy entries: {policies}")
    print(f"  Time: {elapsed:.1f}s")
    print(f"{'=' * 60}")

    return DB_PATH


if __name__ == "__main__":
    force = "--force" in sys.argv
    build_index(force=force)
