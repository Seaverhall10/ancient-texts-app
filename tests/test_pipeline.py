"""
tests/test_pipeline.py — Verify the Bible-bound pipeline builds correct prompts.
Does NOT require Ollama — tests the pipeline logic only.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipeline.bible_bound import build_system_prompt, load_policy, get_modes, MODES
from pipeline.verifier import verify_response


def test_load_policies():
    """Test that policy files load correctly."""
    hermeneutic = load_policy("bible_bound.yaml")
    assert hermeneutic.get("name") == "Bible-Bound Hermeneutic"
    assert len(hermeneutic.get("principles", [])) > 0
    print(f"[PASS] bible_bound.yaml loaded: {len(hermeneutic['principles'])} principles")

    labels = load_policy("claim_labels.yaml")
    assert "A" in labels.get("labels", {})
    assert "B" in labels.get("labels", {})
    assert "C" in labels.get("labels", {})
    assert "U" in labels.get("labels", {})
    print(f"[PASS] claim_labels.yaml loaded: {len(labels['labels'])} labels")

    boundaries = load_policy("boundaries.yaml")
    assert len(boundaries.get("boundaries", [])) > 0
    print(f"[PASS] boundaries.yaml loaded: {len(boundaries['boundaries'])} boundaries")


def test_build_system_prompt():
    """Test that the system prompt builds correctly for all modes."""
    # General mode
    prompt = build_system_prompt(bible_bound=True, mode="general")
    assert "Hallelujah AI" in prompt
    assert "Scripture" in prompt
    assert "[A]" in prompt
    assert "[B]" in prompt
    assert "LOGIC GUARDS" in prompt
    assert "assertive" in prompt or "conviction" in prompt
    print(f"[PASS] General prompt: {len(prompt)} chars")

    # Bible Study mode
    bs = build_system_prompt(bible_bound=True, mode="bible_study")
    assert "BIBLE STUDY MODE" in bs
    assert "Hebrew" in bs
    assert "Strong" in bs
    print(f"[PASS] Bible Study prompt: {len(bs)} chars")

    # Berean Protocol mode
    berean = build_system_prompt(bible_bound=True, mode="berean")
    assert "BEREAN PROTOCOL" in berean
    assert "E1" in berean and "E6" in berean
    print(f"[PASS] Berean prompt: {len(berean)} chars")

    # Dev mode
    dev = build_system_prompt(bible_bound=True, mode="dev")
    assert "DEV MODE" in dev
    assert "1-10" in dev
    print(f"[PASS] Dev prompt: {len(dev)} chars")

    # All modes fit in context budget
    for mode in MODES:
        p = build_system_prompt(mode=mode)
        assert len(p) < 3000, f"{mode} exceeds 3000 chars: {len(p)}"
    print(f"[PASS] All {len(MODES)} modes within budget")


def test_build_prompt_with_context():
    """Test system prompt with study context."""
    ctx = {
        "chapter_title": "In the Beginning",
        "chapter_ref": "Genesis 1",
        "key_verse": "Genesis 1:1",
    }
    prompt = build_system_prompt(bible_bound=True, study_context=ctx)
    assert "Genesis" in prompt
    assert "In the Beginning" in prompt
    assert "Genesis 1:1" in prompt
    print(f"[PASS] Context-aware prompt: {len(prompt)} chars")

    # Test with RAG context (simulating what would carry elohim/cross-refs)
    rag_text = "Glossary: elohim (H430) = God, gods\\nCross-ref: John 1:1 — Logos"
    prompt_rag = build_system_prompt(bible_bound=True, study_context=ctx, rag_context=rag_text)
    assert "elohim" in prompt_rag
    assert "John 1:1" in prompt_rag
    print(f"[PASS] RAG-enhanced prompt: {len(prompt_rag)} chars")


def test_verifier_labels():
    """Test the response verifier detects labels."""
    response = """
## Fresh Summary
[A] In the beginning, God created the heavens and the earth (Genesis 1:1).
[B] The creation account establishes God's sovereignty over all things (Genesis 1:1; Psalm 33:6).
[C] According to the Enuma Elish, ancient Near Eastern creation myths involved conflict among gods.

## Key Verses
- Genesis 1:1
- Psalm 33:6
- John 1:1-3

## Language Notes
The Hebrew word 'bara' (Strong's H1254) means to create from nothing.

## Canonical Connections
- John 1:1-3 parallels Genesis 1
- Hebrews 11:3 connects faith to creation

## Implications
God is the sovereign creator of all things.
"""
    audit = verify_response(response)
    assert audit["labels"]["A"] == 1
    assert audit["labels"]["B"] == 1
    assert audit["labels"]["C"] == 1
    assert audit["labels"]["U"] == 0
    assert audit["verse_citations"] > 0
    assert len(audit["sections_found"]) >= 3
    assert audit["score"] > 0
    print(f"[PASS] Verifier: A={audit['labels']['A']} B={audit['labels']['B']} C={audit['labels']['C']} U={audit['labels']['U']}")
    print(f"  Verses: {audit['verse_citations']}, Sections: {audit['sections_found']}")
    print(f"  Score: {audit['score']}/100, Flags: {audit['flags']}")


def test_verifier_no_labels():
    """Test the verifier flags responses without labels."""
    response = "God created the world. This is important."
    audit = verify_response(response)
    assert sum(audit["labels"].values()) == 0
    assert len(audit["flags"]) > 0
    print(f"[PASS] Verifier correctly flags unlabeled response: {audit['flags']}")


if __name__ == "__main__":
    print("Testing Hallelujah AI Pipeline...")
    print("-" * 40)
    test_load_policies()
    test_build_system_prompt()
    test_build_prompt_with_context()
    test_verifier_labels()
    test_verifier_no_labels()
    print("-" * 40)
    print("All pipeline tests passed!")
