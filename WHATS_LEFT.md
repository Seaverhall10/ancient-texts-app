# ANCIENT TEXTS STUDY APP — MASTER COMPLETION PLAN
*Last updated: Feb 22, 2026 — post NT Greek interlinear expansion*

---

## CURRENT STATE (as of Feb 22, 2026)

### What's COMPLETE
- **15 OT books** (Gen–Dan): Hebrew interlinear (194,031 words) + Flow translations (14,394 verses) + Era study files
- **27 NT books**: Greek interlinear (7,927 verses / 137,554 words) + Era files (37 eras) + info.py
- **9 Non-canon texts**: 1 Enoch, Book of Giants, Jubilees, Jasher, Genesis Apocryphon, DSS Sectarian, Josephus, Heavenly Court
- **Core Beliefs** (39 topics), **Prophecy Tracker** (52 prophecies), **Study Controls**
- **Build**: 694 chapters, 49.6 MB HTML, 0 warnings

### What's MISSING

---

## TIER 1 — CRITICAL CONTENT GAPS

### 1A. NT Flow Translations [HIGHEST PRIORITY]
**Gap**: All 27 NT books have zero flow translation files. The entire New Testament has no
verse-by-verse English prose renditions. This is the biggest gap in the app.

**What's needed**: `data/flow/flow_{book}.py` for all 27 NT books, matching OT format.
**Total scope**: 7,927 NT verses + study notes
**Tool**: `data/generate_nt_flow.py` — Claude API generator (SCRIBE key, Opus model)
**Priority order** (shortest to longest):

| Book | Verses | Priority |
|------|--------|----------|
| 2 John | 13 | 1 |
| 3 John | 15 | 2 |
| Philemon | 25 | 3 |
| Jude | 25 | 4 |
| Titus | 46 | 5 |
| 2 Thessalonians | 47 | 6 |
| 2 Peter | 61 | 7 |
| 2 Timothy | 83 | 8 |
| 1 Thessalonians | 89 | 9 |
| Philippians | 104 | 10 |
| 1 John | 105 | 11 |
| 1 Peter | 105 | 12 |
| James | 108 | 13 |
| 1 Timothy | 113 | 14 |
| Colossians | 95 | 15 |
| Galatians | 149 | 16 |
| Ephesians | 155 | 17 |
| Hebrews | 303 | 18 |
| 2 Corinthians | 256 | 19 |
| Romans | 430 | 20 |
| 1 Corinthians | 437 | 21 |
| Revelation | 405 | 22 |
| Mark | 673 | 23 |
| Matthew | 1,068 | 24 |
| Acts | 1,002 | 25 |
| Luke | 1,149 | 26 |
| John | 866 | 27 |

**Generator**: `python data/generate_nt_flow.py --book philemon`
**Run all**: `python data/generate_nt_flow.py --all`

---

### 1B. Missing OT Canon Books [24 BOOKS]
**Gap**: 24 OT books completely absent from the app. Only 15/39 OT books present.

**Missing books by category**:

| Category | Books |
|----------|-------|
| Major Prophets | Jeremiah (52ch, 1,364v), Ezekiel (48ch, 1,273v) |
| Wisdom / Poetry | Job (42ch, 1,070v), Proverbs (31ch, 915v), Ecclesiastes (12ch, 222v), Song of Solomon (8ch, 117v), Lamentations (5ch, 154v) |
| Post-exilic History | 1 Chronicles (29ch), 2 Chronicles (36ch), Ezra (10ch), Nehemiah (13ch), Esther (10ch) |
| Minor Prophets (12) | Hosea, Joel, Amos, Obadiah, Jonah, Micah, Nahum, Habakkuk, Zephaniah, Haggai, Zechariah, Malachi |

**For each missing book, need**:
1. Hebrew interlinear data (OSHB source via `build_interlinear.py`)
2. `data/{book}/info.py` — overview, author, date, theology
3. Era files (2-6 per book, study chapters with ANE context)
4. `data/flow/flow_{book}.py` — verse-by-verse English translations
5. `manifest.json` entries (text + eras)

**Start with**: Jeremiah (most cross-referenced), then Ezekiel, then Job

---

## TIER 2 — CONTENT ENRICHMENT

### 2A. NT Era Enrichment
**Gap**: Most NT books have only 1 era file vs OT books which have 4-8 each.
Single-era NT books that need expansion:
- Mark (1 era → needs 2-3: Galilean ministry, Jerusalem/Passion)
- Hebrews (1 era → needs 3-4: Christology, Priesthood, Faith chapter, Eschatology)
- James (1 era → needs 2: Practical Wisdom, Trials & Faith)
- 1 Peter (1 era → needs 2: Exile/Suffering, Hope of Glory)
- 1 Corinthians (1 era → needs 3: Divisions, Body of Christ, Resurrection)
- 1 Timothy (1 era → needs 2: Church order, Doctrine)
- Ephesians (1 era → needs 2: Cosmic Christ, Armor of God)

### 2B. NT Study Notes Enrichment
**Gap**: NT era files have fewer deep-dive notes than OT equivalents.
OT avg: 190 notes/book. NT avg: much lower.
- Add Greek term boxes (like OT HEBREW: note blocks)
- Add Second Temple context blocks
- Add divine council connections (especially in Revelation, Ephesians, Colossians)

### 2C. Interlinear Book Selector UX
**Gap**: NT books not visible in the interlinear dropdown UI.
- Need to group: OT (Hebrew) vs NT (Greek) in the selector
- Show language badge: "HEBREW" or "GREEK"
- Update the interlinear panel header to show language

---

## TIER 3 — UX IMPROVEMENTS

### 3A. Book Grouping in Main Selector
Group texts by testament (OT | NT | DSS | Pseudepigrapha | Historical | Thematic)
with visual headers in the text list panel.

### 3B. NT Flow in Reader
Once NT flow files exist, the flow reader tab needs to work for NT books.
Verify the flow reader renders NT books correctly (LTR, Greek terms styled correctly).

### 3C. Prophecy Tracker Expansion
Currently 52 prophecies. Expand to cover:
- Servant Songs (Isaiah 42, 49, 50, 53) with NT fulfillments
- Psalm 22 verse-by-verse fulfillment map
- Daniel 9:24-27 timeline visualization

---

## TIER 4 — NEW TEXTS TO ADD

### 4A. High Value Additions
| Text | Category | Size | Priority |
|------|----------|------|----------|
| 1 Maccabees | Deuterocanonical | 16 ch | HIGH — bridges OT/NT |
| 2 Maccabees | Deuterocanonical | 15 ch | HIGH — Hanukkah, resurrection |
| Wisdom of Solomon | Deuterocanonical | 19 ch | HIGH — cited by NT authors |
| Sirach / Ecclesiasticus | Deuterocanonical | 51 ch | MED |
| 2 Enoch | Pseudepigrapha | 73 ch | MED — Slavonic Enoch |
| Testament of 12 Patriarchs | Pseudepigrapha | 12 parts | MED |

### 4B. THC Expansion
- Church Fathers section (Clement, Ignatius, Justin Martyr, Irenaeus)
- Sethite debunking deep-dives (full GROK_DEEP_DIVE treatment)
- Intertestamental timeline visualization

---

## EXECUTION STRATEGY

### Phase 1 — NT Flow Translations (USE CLAUDE API)
```bash
# Generate NT flow files using the Scribe agent / Claude API
python data/generate_nt_flow.py --book 2john     # 13 verses, ~5min
python data/generate_nt_flow.py --book 3john     # 15 verses
python data/generate_nt_flow.py --book philemon  # 25 verses
python data/generate_nt_flow.py --book jude      # 25 verses
# ... then medium books, then large books
python data/generate_nt_flow.py --all            # run all 27
```

### Phase 2 — Hebrew Interlinear for Missing OT Books
```bash
# Build Hebrew interlinear for all 24 missing OT books
# (OSHB XML source — requires download)
python data/build_interlinear.py --book jeremiah
python data/build_interlinear.py --book ezekiel
# etc.
```

### Phase 3 — Missing OT Book Content (USE SCRIBE AGENT / COUNCIL)
```bash
# Use Scribe agent to generate info.py + era files
python agents/scribe.py --task "Write era files for Jeremiah"
# Or run full Council pipeline
python agents/run_council.py
```

### Phase 4 — OT Flow Translations for Missing Books (USE CLAUDE API)
```bash
python data/generate_ot_flow.py --book jeremiah
# etc.
```

### Phase 5 — NT Era Enrichment
Use Scribe agent to expand single-era NT books.

### Phase 6 — New Texts, UX Polish, Future Expansion

---

## PROGRESS TRACKING

| Task | Status | Notes |
|------|--------|-------|
| NT Greek interlinear (27 books) | ✅ DONE | 137,554 words |
| NT era files (27 books) | ✅ DONE | 37 eras |
| OT Hebrew interlinear (15 books) | ✅ DONE | 194,031 words |
| OT Flow translations (15 books) | ✅ DONE | 14,394 verses |
| NT Flow translations | ⬜ TODO | 7,927 verses |
| Missing OT interlinear (24 books) | ⬜ TODO | ~25,000+ words est |
| Missing OT book content | ⬜ TODO | 24 books |
| Missing OT flow translations | ⬜ TODO | ~8,000+ verses est |
| NT era enrichment | ⬜ TODO | 20+ books need expansion |
| Interlinear book selector UX | ⬜ TODO | NT books not in dropdown |
| Deuterocanonical texts (6) | ⬜ TODO | Future phase |
| THC expansion | ⬜ TODO | Future phase |

---

## QUICK WINS (can do right now)
1. **NT flow 2 John** — 13 verses, ~10 min API call → immediate visible result
2. **NT flow 3 John** — 15 verses → done in same session
3. **NT flow Philemon** — 25 verses → one complete NT book with full features
4. **Fix interlinear selector** — UX fix to show NT books in dropdown (code change, ~30min)
