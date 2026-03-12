# Ancient Texts Study App — Future Session Plans
*Created: March 12, 2026*
*Current State: 77 texts, 230 eras, 978 chapters, v3.3.0*

---

## SESSION PLAN A: Minor Prophets Depth Expansion
**Priority: HIGH | Estimated: 2-3 sessions | Impact: 51 chapters enriched**

The 12 Minor Prophets are currently at 25-40% of Genesis-level depth. Each book needs:
- Richer `hebrew_terms` (3-4 per chapter vs current 0-1)
- Expanded `ane_backdrop` with actual ANE parallels
- `second_temple` sources where applicable (Qumran, LXX variants)
- More `cross_refs` (each chapter should have 5-8)
- Fuller `sections` with commentary (3-4 sections per chapter, 800-1200 chars each)

### Books to expand (by session):
**Session A1** — Hosea (14 ch), Joel (3 ch), Amos (9 ch)
**Session A2** — Obadiah (1 ch), Jonah (4 ch), Micah (7 ch), Nahum (3 ch)
**Session A3** — Habakkuk (3 ch), Zephaniah (3 ch), Haggai (2 ch), Zechariah (14 ch), Malachi (4 ch)

### Template: Use Genesis era files as the gold standard
- Read `data/genesis/era_creation.py` for format reference
- Each chapter should match the richness of Genesis chapters

---

## SESSION PLAN B: NT Era Expansion (Major Books)
**Priority: HIGH | Estimated: 3-4 sessions | Impact: ~40-60 new eras + 120-200 new chapters**

Currently thin books (only 2 eras each for 20+ chapter books):

### Session B1 — Matthew (28 chapters, currently 2 eras)
Add 4-6 more eras:
- Sermon on the Mount (Matt 5-7)
- Parables of the Kingdom (Matt 13)
- Confrontations with Religious Leaders (Matt 15-16, 21-23)
- Olivet Discourse & End Times (Matt 24-25)
- Passion & Resurrection (Matt 26-28)

### Session B2 — Luke (24 chapters, currently 2 eras)
Add 4-6 more eras:
- Birth Narrative & Temple (Luke 1-2)
- Galilean Ministry (Luke 4-9)
- Journey to Jerusalem (Luke 9:51-19:27 — unique "travel narrative")
- Jerusalem Ministry & Passion (Luke 19-23)
- Resurrection & Ascension (Luke 24)

### Session B3 — John (21 chapters, currently 2 eras)
Add 4-6 more eras:
- Prologue & Early Signs (John 1-4)
- Festival Discourses (John 5-10)
- Hour of Glory (John 11-12)
- Upper Room Discourse (John 13-17)
- Passion & Resurrection (John 18-21)

### Session B4 — Acts (28 chapters, currently 2 eras)
Add 4-6 more eras:
- Pentecost & Early Church (Acts 1-5)
- Stephen & Persecution (Acts 6-8)
- Conversion of Saul & Cornelius (Acts 9-12)
- First Missionary Journey (Acts 13-14)
- Jerusalem Council & Paul's Later Journeys (Acts 15-20)
- Paul's Trials & Rome (Acts 21-28)

---

## SESSION PLAN C: Hebrew Terms Gap Fill (DSS, 1 Enoch, Jasher)
**Priority: MEDIUM | Estimated: 2 sessions | Impact: ~124 chapters enriched**

### Session C1 — DSS Sectarian (26 chapters at 0% hebrew_terms)
- Add 2-3 hebrew_terms per chapter
- Focus on Qumran-specific vocabulary (yahad, moreh tsedek, kittim, etc.)
- Terms should connect to biblical parallels

### Session C2 — 1 Enoch (55/73 chapters empty) + Jasher (43/49 chapters empty)
- 1 Enoch: Ge'ez terms with Hebrew/Aramaic roots, Watchers vocabulary
- Jasher: Hebrew terms connecting to Torah parallels
- Note: These are non-canonical — use "According to..." framing

---

## SESSION PLAN D: Study Trail Conversions
**Priority: MEDIUM | Estimated: 1-2 sessions | Impact: 4 trails modernized**

Four trails still use old step-by-step format. Convert to rich article format (like Divine Council and Messianic trails):

1. **Covenant Arc** — covenant progression from Adam through New Covenant
2. **Adam to Jesus** — genealogical and theological line from creation to incarnation
3. **Cosmic Geography** — biblical geography as theological map (Eden, Babel, Zion, Sinai, etc.)
4. **Dead Sea Scrolls Connection** — how DSS illuminate NT and Second Temple context

### For each trail:
- Convert step-by-step format to full `CHAPTERS` list with proper era file structure
- Add hebrew_terms, ane_backdrop, second_temple, cross_refs, sections
- Each trail should become a thematic text entry in manifest (like `parables_invitation`)

---

## SESSION PLAN E: Large OT Book Era Expansion
**Priority: MEDIUM-LOW | Estimated: 2-3 sessions | Impact: ~30-50 new eras**

Large books with disproportionately few eras relative to chapter count:

### Session E1 — Psalms (150 chapters)
Group by type: Royal Psalms, Lament Psalms, Praise Psalms, Wisdom Psalms, Zion Psalms
Add 5-8 thematic eras covering major psalm groupings

### Session E2 — Isaiah (66 chapters)
Currently grouped broadly. Add eras for:
- Judgment Oracles (1-12)
- Oracles Against Nations (13-23)
- Isaiah's Apocalypse (24-27)
- Woe Oracles (28-35)
- Suffering Servant Songs (40-55)
- New Creation (56-66)

### Session E3 — Jeremiah (52 ch), Ezekiel (48 ch)
- Jeremiah: Add 4-5 eras (call narrative, temple sermon, judgment oracles, book of consolation, fall of Jerusalem)
- Ezekiel: Add 4-5 eras (throne vision, siege prophecies, oracles against nations, new temple vision, valley of dry bones)

---

## SESSION PLAN F: YouTube & Resource Integration
**Priority: USER-REQUESTED | Estimated: 1 session**

- Add YouTube video links to key study chapters
- Sources to include:
  - **Michael Heiser** — Naked Bible Podcast, Divine Council lectures
  - **The Bible Project** — book overviews, theme videos
  - **Dr. John Walton** — ANE context, Genesis interpretation
  - **InspiringPhilosophy** — apologetics, theology
  - **Dr. Michael Brown** — Jewish roots, Hebrew language
- Integration: Add `resources` or `videos` array to chapter data
- UI: Video thumbnail cards within chapter sections

---

## SESSION PLAN G: PDF Export Feature
**Priority: MEDIUM | Estimated: 1 session**

- Markdown export already exists
- Add PDF generation using:
  - Option 1: Client-side with jsPDF or html2pdf.js (no server needed)
  - Option 2: Python-side with WeasyPrint or reportlab (build-time)
- Export should include: chapter title, synopsis, key verse, hebrew terms, sections, cross-refs
- Match the dark gold design aesthetic

---

## SESSION PLAN H: JS Module Split (Phase 2)
**Priority: LOW (architecture) | Estimated: 2-3 sessions | Impact: Code maintainability**

Split 7,907-line `app.js` into ~25 modules:
- `core.js` — initialization, routing, state
- `library.js` — library grid, text cards, categories
- `sidebar.js` — navigation tree, search, bookmarks
- `chapter.js` — chapter rendering, reading modes
- `interlinear.js` — word cards, popups, grammar colors
- `search.js` — full-text search engine
- `timeline.js` — timeline rendering
- `map.js` — ancient world map (Leaflet)
- `matrix.js` — Bible Truth Matrix
- `prophecy.js` — prophecy matrix + tracker
- `trails.js` — study trails
- `hebrew.js` — Learn Hebrew module
- `glossary.js` — glossary rendering
- `auth.js` — Firebase auth + sync
- `notes.js` — study notes
- `analytics.js` — usage tracking
- `utils.js` — shared utilities

### Approach:
- Use ES modules with import/export (or concatenation with clear section markers)
- `build.py` concatenates in dependency order
- `state.js` already exists as the state management module

---

## SESSION PLAN I: Apocryphal Flow Translations
**Priority: LOW | Estimated: 3-4 sessions | Impact: 8 texts get verse-level translations**

Currently NO non-canonical text has flow translations. Add for:
1. 1 Enoch (108 chapters — largest)
2. Jubilees (50 chapters)
3. Jasher (91 chapters)
4. Book of Giants (fragments)
5. Genesis Apocryphon (fragments)
6. DSS Sectarian (community rule, war scroll, etc.)
7. Josephus excerpts
8. Heavenly Court compilation

### Approach:
- Use existing `generate_ot_flow.py` pattern adapted for each text
- Source translations: Public domain (Charles, R.H. for 1 Enoch/Jubilees)
- Always label: "According to [text name]..." not "the Bible says..."

---

## SESSION PLAN J: Google Drive Sync & Folder Organization
**Priority: USER-REQUESTED | Estimated: 1 session**

**STATUS: COMPLETED (March 12, 2026)**
- Wiped old disorganized folder, copied 903 clean source files (167 MB)
- Drive path: `G:\My Drive\ANCIENT_TEXTS Study App\`
- Excluded: output/, venv/, dist/, .git/, releases/, archive/
- To set up on new machine: copy folder → `python -m venv venv` → `pip install -r requirements.txt` → `BUILD_ALL.bat`
- Or: `git clone https://github.com/Seaverhall10/ancient-texts-app.git`

---

## SESSION PLAN K: Heavenly Court Polish
**Priority: MEDIUM | Estimated: 1 session | Impact: Quality improvement**

User noted "goofy graphics" and flow issues in the Heavenly Court deep dive. Needs:
1. Review all Heavenly Court era files for content quality
2. Fix any rendering/display issues (graphics, layout)
3. Ensure content flow is smooth and scholarly
4. Verify all divine council references are properly sourced
5. Add missing cross-refs and hebrew_terms where thin

---

## PRIORITY ORDER FOR NEXT SESSIONS

| # | Plan | Sessions | Impact |
|---|------|----------|--------|
| ~~1~~ | ~~**J** — Google Drive sync/org~~ | ~~1~~ | ✅ DONE (March 12) |
| 1 | **B** — NT era expansion | 3-4 | 120-200 new chapters for major NT books |
| 2 | **A** — Minor Prophets depth | 2-3 | 51 chapters enriched to Genesis quality |
| 3 | **D** — Study Trail conversions | 1-2 | 4 trails modernized |
| 4 | **C** — Hebrew terms gap fill | 2 | 124 chapters enriched |
| 5 | **K** — Heavenly Court polish | 1 | Quality fix (user-noted issues) |
| 6 | **F** — YouTube integration | 1 | User-requested feature |
| 7 | **E** — Large OT book expansion | 2-3 | Psalms/Isaiah/Jeremiah/Ezekiel depth |
| 8 | **G** — PDF export | 1 | Feature completion |
| 9 | **H** — JS module split | 2-3 | Architecture improvement |
| 10 | **I** — Apocryphal flows | 3-4 | Nice-to-have content |

---

## RUNNING TOTALS IF ALL PLANS COMPLETED

| Metric | Current | After All Plans |
|--------|---------|-----------------|
| Texts | 77 | ~81 (4 trail conversions) |
| Eras | 230 | ~290-310 |
| Study chapters | 978 | ~1,300-1,500 |
| Cross-references | 6,863 | ~9,000+ |
| Glossary terms | 567 | ~600+ |
