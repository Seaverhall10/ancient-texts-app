"""
pipeline/verifier.py — Response quality checker for Hallelujah AI.
Scans AI responses to verify they follow the Bible-bound guidelines:
- Checks for A/B/C/U claim labels
- Checks that required response sections are present
- Flags potential issues

This is a post-processing pass — it doesn't modify the response,
it produces an audit trail the user can inspect.
"""
import re
from typing import Optional


def verify_response(content: str) -> dict:
    """
    Verify a response against Bible-bound guidelines.
    Returns an audit object with label counts, sections found, and flags.
    """
    audit = {
        "labels": {"A": 0, "B": 0, "C": 0, "U": 0},
        "sections_found": [],
        "flags": [],
        "verse_citations": 0,
        "score": 0
    }

    if not content:
        audit["flags"].append("Empty response")
        return audit

    # Count claim labels
    # Match patterns like [A], [B], [C], [U] at start of lines or inline
    for label in ["A", "B", "C", "U"]:
        pattern = rf'\[{label}\]'
        matches = re.findall(pattern, content)
        audit["labels"][label] = len(matches)

    total_labels = sum(audit["labels"].values())

    # Count verse citations (patterns like "Genesis 1:1", "John 3:16", "Ps 82:1")
    verse_pattern = r'(?:Genesis|Exodus|Leviticus|Numbers|Deuteronomy|Joshua|Judges|Ruth|' \
                    r'1\s*Samuel|2\s*Samuel|1\s*Kings|2\s*Kings|1\s*Chronicles|2\s*Chronicles|' \
                    r'Ezra|Nehemiah|Esther|Job|Psalms?|Proverbs?|Ecclesiastes|' \
                    r'Song\s*of\s*Solomon|Isaiah|Jeremiah|Lamentations|Ezekiel|Daniel|' \
                    r'Hosea|Joel|Amos|Obadiah|Jonah|Micah|Nahum|Habakkuk|Zephaniah|' \
                    r'Haggai|Zechariah|Malachi|' \
                    r'Matthew|Mark|Luke|John|Acts|Romans|' \
                    r'1\s*Corinthians|2\s*Corinthians|Galatians|Ephesians|Philippians|' \
                    r'Colossians|1\s*Thessalonians|2\s*Thessalonians|' \
                    r'1\s*Timothy|2\s*Timothy|Titus|Philemon|Hebrews|James|' \
                    r'1\s*Peter|2\s*Peter|1\s*John|2\s*John|3\s*John|Jude|Revelation)' \
                    r'\s+\d+[:\d\-,\s]*'
    verse_matches = re.findall(verse_pattern, content, re.IGNORECASE)
    audit["verse_citations"] = len(verse_matches)

    # Check for required sections (study response format)
    section_markers = {
        "Fresh Summary": r'(?:fresh\s+summary|summary|overview)',
        "Key Verses": r'(?:key\s+verse|key\s+scripture|key\s+passage)',
        "Language Notes": r'(?:language\s+note|hebrew|greek|aramaic|original\s+language)',
        "Canonical Connections": r'(?:canonical\s+connection|cross[- ]?reference|related\s+passage|connection)',
        "Implications": r'(?:implication|application|takeaway|practical)',
        "Discussion Prompts": r'(?:discussion|question|prompt|further\s+study)',
    }

    for section_name, pattern in section_markers.items():
        if re.search(pattern, content, re.IGNORECASE):
            audit["sections_found"].append(section_name)

    # Generate flags
    if total_labels == 0:
        audit["flags"].append("No claim labels [A/B/C/U] found — claims are unlabeled")

    if audit["labels"]["U"] > audit["labels"]["A"]:
        audit["flags"].append("More speculative [U] claims than explicit Scripture [A] claims")

    if audit["verse_citations"] == 0:
        audit["flags"].append("No verse citations found")

    if len(audit["sections_found"]) < 3:
        audit["flags"].append(f"Only {len(audit['sections_found'])} of 6 standard sections detected")

    # Calculate quality score (0-100)
    score = 0
    score += min(30, total_labels * 5)  # Up to 30 for labels
    score += min(30, audit["verse_citations"] * 5)  # Up to 30 for citations
    score += min(30, len(audit["sections_found"]) * 5)  # Up to 30 for sections
    score += 10 if audit["labels"]["U"] == 0 else 0  # Bonus for no speculation
    audit["score"] = min(100, score)

    return audit
