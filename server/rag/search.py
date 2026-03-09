"""
server/rag/search.py — Search the Hallelujah AI knowledge index.

Queries the SQLite FTS5 database to find study content relevant to
the user's question, then formats it for injection into the LLM prompt.

"It is the glory of God to conceal things,
 but the glory of kings is to search things out."
  — Proverbs 25:2
"""
import os
import sqlite3
import json
from typing import Optional

RAG_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(RAG_DIR, "hallelujah.db")

# Maximum characters of context to inject into prompt.
# Qwen 2.5 7B has 16K context (~64K chars).
# Full system prompt ≈ 5000 chars, conversation needs ~4000 chars.
# That leaves ~4000 chars for RAG context.
MAX_CONTEXT_CHARS = 4000


def get_db():
    """Get a database connection (read-only)."""
    if not os.path.exists(DB_PATH):
        return None
    conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def search_chapters(conn, query: str, limit: int = 3) -> list:
    """Search study chapters by content."""
    try:
        c = conn.execute(
            """SELECT chapter_id, text_id, ref, title, synopsis,
                      snippet(chapters_fts, 5, '>>>', '<<<', '...', 40) as section_snippet,
                      hebrew_terms, cross_ref_notes, key_verse_text,
                      rank
               FROM chapters_fts
               WHERE chapters_fts MATCH ?
               ORDER BY rank
               LIMIT ?""",
            (query, limit)
        )
        results = []
        for row in c.fetchall():
            results.append({
                "type": "chapter",
                "chapter_id": row["chapter_id"],
                "text_id": row["text_id"],
                "ref": row["ref"],
                "title": row["title"],
                "synopsis": row["synopsis"],
                "section_snippet": row["section_snippet"],
                "hebrew_terms": row["hebrew_terms"],
                "cross_refs": row["cross_ref_notes"][:500] if row["cross_ref_notes"] else "",
                "key_verse": row["key_verse_text"] or ""
            })
        return results
    except Exception:
        return []


def search_glossary(conn, query: str, limit: int = 5) -> list:
    """Search glossary terms."""
    try:
        c = conn.execute(
            """SELECT term_slug, hebrew, transliteration, strongs, gloss, definition,
                      chapters_used, rank
               FROM glossary_fts
               WHERE glossary_fts MATCH ?
               ORDER BY rank
               LIMIT ?""",
            (query, limit)
        )
        results = []
        for row in c.fetchall():
            results.append({
                "type": "glossary",
                "term": row["term_slug"],
                "hebrew": row["hebrew"],
                "transliteration": row["transliteration"],
                "strongs": row["strongs"],
                "gloss": row["gloss"],
                "definition": row["definition"],
                "used_in": row["chapters_used"]
            })
        return results
    except Exception:
        return []


def search_flow(conn, query: str, limit: int = 5) -> list:
    """Search flow verse translations."""
    try:
        c = conn.execute(
            """SELECT text_id, chapter_num, verse_num, ref, flow_text, rank
               FROM flow_fts
               WHERE flow_fts MATCH ?
               ORDER BY rank
               LIMIT ?""",
            (query, limit)
        )
        results = []
        for row in c.fetchall():
            results.append({
                "type": "flow_verse",
                "text_id": row["text_id"],
                "ref": row["ref"],
                "chapter": row["chapter_num"],
                "verse": row["verse_num"],
                "text": row["flow_text"]
            })
        return results
    except Exception:
        return []


def search_prophecies(conn, query: str, limit: int = 3) -> list:
    """Search prophecy entries."""
    try:
        c = conn.execute(
            """SELECT prophecy_id, category, title, ot_ref, nt_ref,
                      ot_text, fulfillment, status, ot_hebrew, significance, rank
               FROM prophecy_fts
               WHERE prophecy_fts MATCH ?
               ORDER BY rank
               LIMIT ?""",
            (query, limit)
        )
        results = []
        for row in c.fetchall():
            results.append({
                "type": "prophecy",
                "id": row["prophecy_id"],
                "category": row["category"],
                "title": row["title"],
                "ot_ref": row["ot_ref"],
                "nt_ref": row["nt_ref"],
                "ot_text": row["ot_text"][:300] if row["ot_text"] else "",
                "fulfillment": row["fulfillment"][:300] if row["fulfillment"] else "",
                "status": row["status"],
                "hebrew": row["ot_hebrew"] or ""
            })
        return results
    except Exception:
        return []


def search_policies(conn, query: str, limit: int = 3) -> list:
    """Search policy knowledge (Berean Protocol, hermeneutics, analytical frameworks).

    This gives the AI access to the FULL policy frameworks that don't fit
    in the compressed system prompt — Berean Decomposition steps, cognitive
    bias detection, analytical lenses, evidence confidence scale, etc.
    """
    try:
        c = conn.execute(
            """SELECT policy_file, policy_name, section_id, section_name,
                      content, scriptural_basis, rank
               FROM policy_fts
               WHERE policy_fts MATCH ?
               ORDER BY rank
               LIMIT ?""",
            (query, limit)
        )
        results = []
        for row in c.fetchall():
            results.append({
                "type": "policy",
                "policy": row["policy_name"],
                "section_id": row["section_id"],
                "section": row["section_name"],
                "content": row["content"],
                "basis": row["scriptural_basis"] or ""
            })
        return results
    except Exception:
        return []


def get_cross_refs(conn, chapter_id: str) -> list:
    """Get cross-references for a specific chapter."""
    try:
        c = conn.execute(
            "SELECT ref, note, type FROM cross_refs WHERE source_chapter = ?",
            (chapter_id,)
        )
        return [dict(row) for row in c.fetchall()]
    except Exception:
        return []


def search(query: str, top_k: int = 5) -> dict:
    """
    Main search function — searches all indexes and returns structured results.
    Returns a dict with categorized results and a formatted text for LLM injection.
    """
    conn = get_db()
    if conn is None:
        return {"results": [], "context_text": "", "source_count": 0}

    try:
        # Clean query for FTS5 (escape special chars)
        clean_query = sanitize_query(query)
        if not clean_query:
            return {"results": [], "context_text": "", "source_count": 0}

        # Search all indexes (expanded budget for 16K context model)
        chapters = search_chapters(conn, clean_query, limit=min(top_k, 3))
        glossary = search_glossary(conn, clean_query, limit=min(top_k, 5))
        flow = search_flow(conn, clean_query, limit=min(top_k, 5))
        prophecies = search_prophecies(conn, clean_query, limit=min(top_k, 3))
        policies = search_policies(conn, clean_query, limit=min(top_k, 3))

        all_results = chapters + glossary + flow + prophecies + policies

        # Format as text for LLM context injection
        context_text = format_context(chapters, glossary, flow, prophecies, policies)

        return {
            "results": all_results,
            "context_text": context_text,
            "source_count": len(all_results),
            "sources": {
                "chapters": len(chapters),
                "glossary": len(glossary),
                "flow_verses": len(flow),
                "prophecies": len(prophecies),
                "policies": len(policies)
            }
        }
    finally:
        conn.close()


def sanitize_query(query: str) -> str:
    """Clean a query string for FTS5 matching."""
    if not query or not query.strip():
        return ""
    # Remove FTS5 special characters that could cause syntax errors
    cleaned = query.strip()
    for char in ['"', "'", "(", ")", "*", ":", "^", "{", "}", "~", "+", "-", "!", "?"]:
        cleaned = cleaned.replace(char, " ")
    # Collapse whitespace
    cleaned = " ".join(cleaned.split())
    if not cleaned:
        return ""
    # Use OR between words for broader matching
    words = cleaned.split()
    if len(words) > 1:
        return " OR ".join(words)
    return cleaned


def format_context(chapters, glossary, flow, prophecies, policies=None) -> str:
    """Format search results as text for LLM prompt injection."""
    parts = []

    # Policy knowledge goes FIRST — it shapes how the AI thinks
    if policies:
        parts.append("=== PROTOCOL & FRAMEWORK ===")
        for pol in policies:
            entry = f"  [{pol['section_id']}] {pol['section']}"
            entry += f"\n  {pol['content'][:500]}"
            if pol['basis']:
                entry += f"\n  Scriptural basis: {pol['basis'][:200]}"
            parts.append(entry)

    if glossary:
        parts.append("=== GLOSSARY TERMS ===")
        for g in glossary:
            entry = f"  {g['term']} ({g['hebrew']}, {g['transliteration']}, {g['strongs']})"
            entry += f"\n  Gloss: {g['gloss']}"
            if g['definition']:
                # Truncate long definitions
                defn = g['definition'][:400]
                if len(g['definition']) > 400:
                    defn += "..."
                entry += f"\n  Definition: {defn}"
            if g['used_in']:
                entry += f"\n  Used in: {g['used_in']}"
            parts.append(entry)

    if chapters:
        parts.append("\n=== STUDY CHAPTERS ===")
        for ch in chapters:
            entry = f"  [{ch['ref']}] {ch['title']}"
            if ch['synopsis']:
                entry += f"\n  Synopsis: {ch['synopsis'][:300]}"
            if ch['key_verse']:
                entry += f"\n  Key verse: {ch['key_verse']}"
            if ch['section_snippet']:
                entry += f"\n  Content: {ch['section_snippet'][:400]}"
            if ch['hebrew_terms']:
                entry += f"\n  Hebrew terms: {ch['hebrew_terms']}"
            if ch['cross_refs']:
                entry += f"\n  Cross-refs: {ch['cross_refs'][:300]}"
            parts.append(entry)

    if flow:
        parts.append("\n=== VERSE TRANSLATIONS ===")
        for v in flow:
            parts.append(f"  {v['ref']}: {v['text'][:200]}")

    if prophecies:
        parts.append("\n=== PROPHECY DATA ===")
        for p in prophecies:
            entry = f"  [{p['id']}] {p['title']} ({p['category']})"
            if p['ot_ref']:
                entry += f"\n  OT: {p['ot_ref']}"
            if p['nt_ref']:
                entry += f"\n  NT: {p['nt_ref']}"
            if p['fulfillment']:
                entry += f"\n  Fulfillment: {p['fulfillment'][:200]}"
            if p['status']:
                entry += f"\n  Status: {p['status']}"
            parts.append(entry)

    full_text = "\n".join(parts)

    # Truncate to max context size
    if len(full_text) > MAX_CONTEXT_CHARS:
        full_text = full_text[:MAX_CONTEXT_CHARS] + "\n[... additional results truncated]"

    return full_text


def get_index_stats() -> dict:
    """Return stats about the current index."""
    conn = get_db()
    if conn is None:
        return {"exists": False}

    try:
        stats = {"exists": True}
        c = conn.execute("SELECT key, value FROM meta")
        for row in c.fetchall():
            stats[row["key"]] = row["value"]
        return stats
    except Exception:
        return {"exists": True, "error": "Could not read metadata"}
    finally:
        conn.close()
