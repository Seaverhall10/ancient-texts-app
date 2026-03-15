# Ancient Texts Study App — Online Session Pack
## Upload ALL files in this folder to give Claude complete project context

### What This Is
This pack contains everything needed for an online Claude session to understand and generate content for the Ancient Texts Study App — a deep scripture study application built by Seaver Hall.

**Read these files in this order:**
1. **CLAUDE.md** — Project rules, 30 theological laws, build commands, protocols
2. **SEAVER_THEOLOGY_LAW.md** — Seaver's full theological framework (MASTER REFERENCE)
3. **PROJECT.md** — Directory structure & architecture
4. **STATUS.md** — Current completion state, what's done, what's missing, priorities
5. **manifest.json** — All 80 texts, 246 eras, data file mappings
6. **CONTENT_MAP.json** — Master AI navigation index (cross-refs, gaps, hot passages)

**Template files (for generating new content):**
7. **era_01_creation.py** — Gold-standard era file template (Genesis creation)
8. **era_08_joseph.py** — Recently written clean era file (Genesis Joseph)
9. **flow_genesis.py** — Flow translation file format
10. **glossary.py** — Glossary entry format

---

### Quick Stats (v3.3.0)
- 80 texts (39 OT + 27 NT + 5 DSS + 1 Pseudepigrapha + 1 Historical + 4 Thematic + 3 Study)
- 246 study eras, 1,059 chapters
- 444,339 interlinear words (Hebrew + Greek)
- 31,101 flow verse translations, 9,497 scholarly notes
- 6,990 cross-references, 607 glossary terms
- 24 map journey routes, 206 waypoints

---

### How to Generate Content

#### Era Files (study chapters)
Use `era_01_creation.py` and `era_08_joseph.py` as templates. Every chapter MUST have:

```python
CHAPTERS = [
    {
        "id": "unique-id",           # kebab-case, e.g. "gen-creation-1"
        "ref": "Genesis 1-2",        # Scripture reference
        "chapter_num": 1,            # Sequential number within era
        "title": "Chapter Title",    # Display title (NOT "heading")
        "era": "era_identifier",     # Which era this belongs to
        "type": "deep_dive",         # Usually "deep_dive" or "overview"
        "synopsis": "2-3 sentence summary with [A][B][C] evidence tiers...",
        "key_verse": {
            "ref": "Genesis 1:1",
            "text": "In the beginning, God created...",
            "translation": "ESV"
        },
        "hebrew_terms": [
            {"term": "elohim", "transliteration": "elohim", "meaning": "God/gods/divine beings"}
        ],
        "ane_backdrop": "Ancient Near Eastern context paragraph...",
        "second_temple": [
            {"source": "1 Enoch 2:1-5:3", "summary": "...", "relevance": "..."}
        ],
        "cross_refs": [
            {"ref": "John 1:1-3", "note": "Connection note...", "type": "nt"},
            {"ref": "1 Enoch 2:1", "note": "...", "type": "pseudepigrapha"}
        ],
        "divine_council_note": "Divine council connection or None...",
        "sections": [
            {"heading": "Section Title", "body": "800-1200 chars of scholarly content..."},
            {"heading": "Another Section", "body": "More content..."}
        ]
    }
]
```

**Required cross_ref types:** ot, nt, ane, dss, pseudepigrapha, thematic
**Required second_temple format:** Array of objects with source, summary, relevance
**Section depth:** 3-6 sections per chapter, 800-1200 characters each
**Evidence tiers in synopses:** [A] Direct Scripture / [B] Valid inference / [C] Ancient parallels

#### Flow Files (verse-by-verse translations)
```python
FLOW_GENESIS = {
    1: {  # chapter number
        1: "In the beginning, God created the heavens and the earth.",
        2: "The earth was without form and void...",
    },
    2: { ... }
}

NOTES_GENESIS = {
    "1:1": "Hebrew: bereshit bara elohim — 'In the beginning, God created'...",
    "1:26": "The plural 'let us make' reflects the divine council..."
}
```

#### Glossary Entries
```python
GLOSSARY = {
    "elohim": {
        "hebrew": "אֱלֹהִים",
        "transliteration": "elohim",
        "strongs": "H430",
        "gloss": "God, gods, divine beings",
        "definition": "Full scholarly definition...",
        "language": "hebrew",
        "chapters_used": ["gen-creation-1", "gen-council-2"]
    }
}
```

---

### Theological Non-Negotiables (Summary)
1. Bible = 100% Word of God; Hebrew/Greek = primary authority
2. Divine council = REAL heavenly administration (Ps 82, Deut 32:8-9 DSS)
3. Gen 6 sons of God = divine/angelic beings (NEVER Sethite view)
4. Deut 32:8 = DSS/LXX "sons of God" (NOT MT "sons of Israel")
5. Non-canonical: "According to 1 Enoch..." NEVER "the Bible says..."
6. Three INDEPENDENT rebellions: Eden → Hermon → Babel
7. Satan fell BEFORE Eden — Eden was his first act of war
8. Salvation = covenantal, NOT transactional ("say this prayer")
9. Afterlife = Sheol → bodily resurrection → new earth (NOT Platonic "souls in heaven")
10. Ekklesia = governing assembly, NOT institutional "church"
11. Prophets = covenant prosecutors (riv framework)
12. Jesus' priesthood = Melchizedekian, NOT Levitical
13. Holy Spirit gifts continue (anti-cessationism)
14. ESV baseline unless noted
15. Evidence tiers: [A] Direct Scripture / [B] Valid inference / [C] Ancient parallels

See **SEAVER_THEOLOGY_LAW.md** for the full framework with scripture citations.

---

### What the Online Session Can Help With
- **Generate new era files** for books needing depth (Minor Prophets, Luke, John)
- **Write new study trail content** (5 trails proposed in STATUS.md)
- **Expand glossary entries** (Hebrew/Greek/Aramaic terms)
- **Write flow translation notes** (scholarly annotations)
- **Create cross-references** connecting texts
- **Draft thematic deep dives** (articles, era chapters)
- **Review theological accuracy** against the framework

**Always output valid Python** that can be dropped directly into the `data/` folder structure.

---

*Pack generated: March 14, 2026*
*Project version: 3.3.0*
*Author: Seaver Hall*
