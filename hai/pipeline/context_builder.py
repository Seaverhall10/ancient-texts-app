"""
pipeline/context_builder.py — Study context builder for Hallelujah AI.
This module is used by the frontend to package the current study state
(chapter, era, interlinear data, cross-refs) into a context object
that gets injected into the LLM prompt.

Note: Most context building happens in the JavaScript frontend (app.js)
since all the data is already loaded there. This module provides
server-side utilities if needed for heavier processing.
"""


def build_context_from_chapter(chapter_data: dict, text_name: str = "", era_name: str = "") -> dict:
    """
    Build a study context dict from a chapter data object.
    This is the format expected by pipeline/bible_bound.py's build_system_prompt().
    """
    context = {
        "text_name": text_name,
        "era_name": era_name,
        "chapter_title": chapter_data.get("title", ""),
        "chapter_ref": chapter_data.get("ref", ""),
        "key_verse": "",
        "chapter_content": "",
        "hebrew_terms": chapter_data.get("hebrew_terms", []),
        "cross_refs": chapter_data.get("cross_refs", [])
    }

    # Extract key verse
    kv = chapter_data.get("key_verse", {})
    if isinstance(kv, dict):
        context["key_verse"] = f"{kv.get('ref', '')} — {kv.get('text', '')}"
    elif isinstance(kv, str):
        context["key_verse"] = kv

    # Build chapter content from sections
    sections = chapter_data.get("sections", [])
    content_parts = []
    for section in sections:
        if isinstance(section, dict):
            heading = section.get("heading", "")
            body = section.get("body", "")
            if heading:
                content_parts.append(f"### {heading}")
            if body:
                # Strip HTML tags for plain text context
                import re
                plain = re.sub(r'<[^>]+>', '', body)
                content_parts.append(plain)

    context["chapter_content"] = "\n\n".join(content_parts)

    return context


def truncate_context(context: dict, max_chars: int = 8000) -> dict:
    """Truncate chapter content to fit within context window limits."""
    content = context.get("chapter_content", "")
    if len(content) > max_chars:
        context["chapter_content"] = content[:max_chars] + "\n[... truncated ...]"
    return context
