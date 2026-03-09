# GROK HANDOFF — Ancient Texts Study App

## What This Project Is

A single-HTML scholarly Bible study application (~17MB) that combines:
- **14 texts** (Genesis through Josephus + The Heavenly Court)
- **Hebrew interlinear reading** — word-by-word Hebrew with morphology, Strong's numbers, and glosses
- **Flow translations** — curated, accurate, literal English renderings for every verse
- **Study notes** — scholarly annotations on theology, Hebrew grammar, Christ typology, and ANE context
- **553-term glossary**, maps, cross-references, bookmarks

Build system: `python build.py` → outputs `output/AncientTextsStudy.html`

---

## WHAT I NEED YOU TO DO

### Task 1: Write Flow Translations for 9 New OT Books

Interlinear Hebrew data already exists for these books (generated from OSHB). They need **flow translations** — curated English renderings with scholarly study notes.

| Book | Chapters | Interlinear File | Flow File Needed |
|------|----------|-----------------|-----------------|
| Judges | 21 | `data/interlinear_judges.py` (1.2MB) | `data/flow/flow_judges.py` |
| Ruth | 4 | `data/interlinear_ruth.py` (158KB) | `data/flow/flow_ruth.py` |
| 1 Samuel | 31 | `data/interlinear_1samuel.py` (1.6MB) | `data/flow/flow_1samuel.py` |
| 2 Samuel | 24 | `data/interlinear_2samuel.py` (1.3MB) | `data/flow/flow_2samuel.py` |
| 1 Kings | 22 | `data/interlinear_1kings.py` (1.6MB) | `data/flow/flow_1kings.py` |
| 2 Kings | 25 | `data/interlinear_2kings.py` (1.5MB) | `data/flow/flow_2kings.py` |
| Psalms | 150 | `data/interlinear_psalms.py` (2.5MB) | `data/flow/flow_psalms.py` |
| Isaiah | 66 | `data/interlinear_isaiah.py` (2.1MB) | `data/flow/flow_isaiah.py` |
| Daniel | 12 | `data/interlinear_daniel.py` (725KB) | `data/flow/flow_daniel.py` |

### Task 2: Add These 9 Books to manifest.json and build.py

Each new book needs:
1. A text entry in `manifest.json` with era definitions
2. An `info.py` scholarly introduction in `data/<book>/info.py`
3. Interlinear injection in `build.py` (load the interlinear_*.py and inject into JS)
4. Flow loader entry in `build.py` (already auto-discovers flow_*.py files)

### Task 3: Write Era Data Files for Each New Book

Each book needs era data files (the study chapter content). See existing examples in `data/genesis/`, `data/exodus/`, etc.

---

## EXACT FILE FORMAT FOR FLOW TRANSLATIONS

Every flow file MUST follow this exact Python format. See `data/flow/flow_joshua.py` (189KB, 24 chapters, 658 verses, 219 notes) as the GOLD STANDARD reference.

### Structure

```python
"""
Flow translations for <BookName> — accurate, literal English renderings.
Every verse of all <N> chapters. Formal equivalence style.
YHWH = the LORD. Original translation from the Hebrew Masoretic Text.
Study notes included for key theological moments and Christ typology.
"""

FLOW_<BOOKNAME> = {
    1: {  # Chapter 1
        1: 'In the beginning God created the heavens and the earth.',
        2: 'And the earth was formless and void, and darkness was over the surface of the deep...',
        # ... EVERY verse of the chapter
    },
    2: {  # Chapter 2
        1: '...',
        # ... EVERY verse
    },
    # ... ALL chapters
}

NOTES_<BOOKNAME> = {
    1: {
        1: 'HEBREW: bereshit — \'in the beginning.\' The word reshit implies...',
        26: 'CHRIST TYPOLOGY: The image of God (tselem elohim) in humanity...',
    },
    # ... notes for theologically significant verses (not every verse needs a note)
}
```

### Variable Naming Convention

| Book | FLOW var | NOTES var |
|------|----------|-----------|
| Judges | `FLOW_JUDGES` | `NOTES_JUDGES` |
| Ruth | `FLOW_RUTH` | `NOTES_RUTH` |
| 1 Samuel | `FLOW_1SAMUEL` | `NOTES_1SAMUEL` |
| 2 Samuel | `FLOW_2SAMUEL` | `NOTES_2SAMUEL` |
| 1 Kings | `FLOW_1KINGS` | `NOTES_1KINGS` |
| 2 Kings | `FLOW_2KINGS` | `NOTES_2KINGS` |
| Psalms | `FLOW_PSALMS` | `NOTES_PSALMS` |
| Isaiah | `FLOW_ISAIAH` | `NOTES_ISAIAH` |
| Daniel | `FLOW_DANIEL` | `NOTES_DANIEL` |

### Translation Style Rules

1. **FORMAL EQUIVALENCE** — literal, word-for-word where possible. Not paraphrase. Not dynamic equivalence.
2. **YHWH = "the LORD"** — always render the divine name as "the LORD" (all caps LORD)
3. **Accuracy over readability** — preserve Hebrew syntax and word order when English allows
4. **Every verse, no exceptions** — do NOT skip verses. Every single verse must be translated.
5. **Single-line strings** — NO newlines inside string values. All text on one line per verse.
6. **Escape single quotes** — use `\'` inside single-quoted strings
7. **No double quotes** as string delimiters — always use single quotes `'...'`

### Study Notes Style Rules

1. **Not every verse needs a note** — focus on theologically significant verses
2. **Categories to note**: Hebrew/Greek word analysis, Christ typology, covenant theology, divine council connections, ANE parallels, cross-references, prophetic fulfillment
3. **Format**: Start with category tag like `HEBREW:`, `CHRIST TYPOLOGY:`, `THEOLOGICAL:`, `ANE PARALLEL:`, etc.
4. **Include transliterated Hebrew** with meaning: `ruach elohim — 'Spirit of God'`
5. **Cross-reference** other scripture: `(cf. Gen 1:26; Ps 82:6; John 10:34)`
6. **Single-line strings** — NO newlines. Keep notes on one line even if long.
7. **THE THEOLOGICAL STANCE**: Christ IS the promised Messiah and King. This is not debatable. Notes should identify Christ typology where present, not argue for it apologetically.

### Example Notes (from Joshua — the gold standard)

```python
NOTES_JOSHUA = {
    1: {
        5: 'CHRIST TYPOLOGY: "I will not fail you or forsake you" — quoted in Hebrews 13:5 as a promise to the church. The assurance given to Joshua before conquest is the same assurance given to every believer.',
        8: 'HEBREW: hagah — "meditate." Not silent contemplation but audible recitation, murmuring the words. Torah meditation was vocal and physical, engaging the whole person.',
    },
    2: {
        11: 'THEOLOGICAL: Rahab\'s confession — "the LORD your God, He is God in heaven above and on earth beneath" — is a full monotheistic creed from a pagan prostitute. She confesses YHWH\'s universal sovereignty. This is cited in Hebrews 11:31 and James 2:25 as an example of saving faith.',
    },
}
```

---

## HOW THE BUILD SYSTEM WORKS

### Flow Translation Loading (build.py lines ~265-307)

```python
# build.py auto-discovers flow files:
# 1. Scans data/flow/ for files matching flow_*.py
# 2. Only loads files where filename.count("_") == 1 (i.e., flow_genesis.py, NOT flow_genesis_1_10.py)
# 3. Looks for FLOW_<BOOK> and NOTES_<BOOK> constants
# 4. Merges flow text and notes into interlinear verse data
```

So if you create `data/flow/flow_judges.py` with `FLOW_JUDGES` and `NOTES_JUDGES`, the build system will auto-discover and load it.

### Interlinear Data Loading (build.py lines ~308-332)

Each interlinear book needs an explicit loader in build.py. Currently these 6 are loaded:
- genesis (from data/genesis/interlinear.py → INTERLINEAR)
- exodus (from data/interlinear_exodus.py → INTERLINEAR_EXODUS)
- leviticus, numbers, deuteronomy, joshua (similar pattern)

You need to add loaders for the 9 new books. Pattern:

```python
# In build.py, add after the existing interlinear loaders:
from data.interlinear_judges import INTERLINEAR_JUDGES
# ... then inject: js = js.replace("__INTERLINEAR_JUDGES__", json.dumps(INTERLINEAR_JUDGES))
```

And in `src/js/app.js`, add the placeholder `__INTERLINEAR_JUDGES__` where interlinear data is injected.

### Manifest Structure (manifest.json)

Each text needs a manifest entry. Example for Judges:

```json
{
    "id": "judges",
    "name": "Judges",
    "category": "canon",
    "color": "#c9a84c",
    "has_interlinear": true,
    "eras": [
        {
            "id": "othniel_ehud",
            "name": "Early Judges (Othniel, Ehud, Shamgar)",
            "chapters": ["era_01_early_judges"]
        },
        {
            "id": "deborah_gideon",
            "name": "Deborah & Gideon",
            "chapters": ["era_02_deborah_gideon"]
        }
        // ... etc
    ]
}
```

---

## COMBINE SCRIPT (data/flow/combine_all.py)

If you write flow translations in partial files (e.g., `flow_judges_1_10.py`, `flow_judges_11_21.py`), run `combine_all.py` to merge them into a single `flow_judges.py`.

**IMPORTANT**: Add new books to the combine list at the bottom of `combine_all.py`:

```python
for key, display in [
    ("genesis", "Genesis"),
    ("exodus", "Exodus"),
    # ... existing ...
    ("judges", "Judges"),  # ADD
    ("ruth", "Ruth"),      # ADD
    # etc.
]:
    discover_and_combine(key, display)
```

The combine script auto-discovers all `flow_<book>*.py` partials via glob.

---

## CURRENT STATUS

### COMPLETE (flow translations done, building successfully):
| Book | Chapters | Verses | Notes | File Size |
|------|----------|--------|-------|-----------|
| Genesis | 50/50 | 1,533 | 287 | 326KB |
| Exodus | 40/40 | 1,213 | 280 | 292KB |
| Leviticus | 27/27 | 859 | 128 | 191KB |
| Numbers | 36/36 | 1,288 | 164 | 252KB |
| Deuteronomy | 34/34 | 959 | 182 | 217KB |
| Joshua | 24/24 | 658 | 219 | 190KB |

### NEEDED (interlinear data exists, flow translations needed):
| Book | Chapters | Est. Verses | Priority |
|------|----------|-------------|----------|
| Ruth | 4 | 85 | HIGH (small, quick win) |
| Daniel | 12 | 357 | HIGH (prophetic, divine council) |
| Judges | 21 | 618 | HIGH (connects Joshua → Samuel) |
| 1 Samuel | 31 | 810 | MEDIUM |
| 2 Samuel | 24 | 695 | MEDIUM |
| 1 Kings | 22 | 816 | MEDIUM |
| 2 Kings | 25 | 719 | MEDIUM |
| Isaiah | 66 | 1,292 | HIGH (messianic prophecy) |
| Psalms | 150 | 2,461 | HIGH (largest book, worship/prayer) |

---

## FILE LOCATIONS

```
ANCIENT_TEXTS_APP/
├── build.py                        # Main build system
├── manifest.json                   # Text/era definitions
├── src/
│   ├── js/app.js                   # Frontend controller
│   └── css/styles.css              # Styles
├── data/
│   ├── flow/
│   │   ├── combine_all.py          # Merge partials → combined
│   │   ├── flow_genesis.py         # COMPLETE
│   │   ├── flow_exodus.py          # COMPLETE
│   │   ├── flow_leviticus.py       # COMPLETE
│   │   ├── flow_numbers.py         # COMPLETE
│   │   ├── flow_deuteronomy.py     # COMPLETE
│   │   ├── flow_joshua.py          # COMPLETE (GOLD STANDARD)
│   │   └── [partial files]         # Various _1_10.py chunks
│   ├── genesis/                    # Genesis era data + interlinear
│   ├── exodus/                     # Exodus era data
│   ├── interlinear_exodus.py       # Exodus interlinear (auto-generated)
│   ├── interlinear_judges.py       # Judges interlinear (READY)
│   ├── interlinear_ruth.py         # Ruth interlinear (READY)
│   ├── interlinear_1samuel.py      # 1 Samuel interlinear (READY)
│   ├── interlinear_2samuel.py      # 2 Samuel interlinear (READY)
│   ├── interlinear_1kings.py       # 1 Kings interlinear (READY)
│   ├── interlinear_2kings.py       # 2 Kings interlinear (READY)
│   ├── interlinear_psalms.py       # Psalms interlinear (READY)
│   ├── interlinear_isaiah.py       # Isaiah interlinear (READY)
│   ├── interlinear_daniel.py       # Daniel interlinear (READY)
│   └── build_interlinear.py        # Generates interlinear from OSHB
└── output/
    └── AncientTextsStudy.html      # Built output (17MB)
```

---

## THEOLOGICAL GUIDELINES

1. **Christ is the promised Messiah and the King of everything.** This is the theological foundation.
2. **YHWH = the LORD.** Always. No exceptions.
3. **Formal equivalence translation.** Literal over dynamic. Preserve Hebrew syntax when English allows.
4. **Divine council theology is real.** The elohim of Psalm 82 are real spiritual beings, not human judges. 1 Enoch, the Watchers tradition, the Nephilim — all taken seriously as part of the biblical worldview.
5. **Canonical distinctions matter.** Genesis is canon. 1 Enoch is not. Don't say "the Bible says" for non-canonical texts. But non-canonical texts illuminate the canonical ones.
6. **Transliteration consistency**: Use consistent Hebrew transliterations (Shemihazah not Semjaza, elohim not Elohim when referring to the common noun).
7. **Study notes should be scholarly**, not devotional. Include Hebrew word analysis, ANE parallels, cross-references, and Christ typology where warranted.

---

## VERIFICATION

After completing flow translations for any book:

1. Run `python build.py` — should succeed with no errors
2. Check the build output shows the new flow translations merged: `[flow-judges] X verse translations, Y notes merged`
3. Open `output/AncientTextsStudy.html` in a browser
4. Navigate to the book's interlinear reading pane
5. Toggle "Flow Translation" — curated English should appear under each verse
6. Toggle "Study Notes" — gold callout boxes should appear for annotated verses

---

## PRIORITY ORDER

1. **Ruth** (4 chapters — quick win, test the pipeline)
2. **Daniel** (12 chapters — divine council, prophetic, high-value)
3. **Judges** (21 chapters — bridges Joshua → Samuel)
4. **Isaiah** (66 chapters — messianic prophecy, essential)
5. **Psalms** (150 chapters — largest, most worship/prayer content)
6. **1 Samuel** (31 chapters)
7. **2 Samuel** (24 chapters)
8. **1 Kings** (22 chapters)
9. **2 Kings** (25 chapters)

For each book: write the flow file → add to combine_all.py → add to manifest → add to build.py → build and verify.
