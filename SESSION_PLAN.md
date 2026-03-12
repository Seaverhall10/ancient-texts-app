# Overnight Session Plan — 2026-03-12
## Top 10 Game-Changing Upgrades

### COMPLETED (Previous Session)
1. **Reading Mode Toggle** — Scripture / Study / Interlinear per chapter ✅
2. **Firebase Auth + Cloud Sync** — Email/password login, Firestore sync ✅
3. **NT Era Depth Wave 1** — 14 new era files, 42 study chapters across 11 NT books ✅

### IN PROGRESS (This Session)

#### 4. NT Era Depth Wave 2 — 6 More NT Eras
Adding second eras to the remaining thin NT books that benefit from depth:
- `data/1john/era_1john_spirits.py` — Testing the Spirits & Overcoming (1 John 4-5)
- `data/1timothy/era_1tim_warfare.py` — Cosmic Order & Spiritual Warfare
- `data/2peter/era_2pet_judgment.py` — Watchers' Judgment & Cosmic Dissolution (2 Pet 2-3)
- `data/2thessalonians/era_2thess_mystery.py` — Mystery of Lawlessness (2 Thess 2)
- `data/2timothy/era_2tim_endurance.py` — Last Words, Scripture, Crown
- `data/titus/era_titus_grace.py` — The Grace That Trains

Each era = 3 study chapters with full divine council theology, Greek terms, ANE backdrop, Second Temple sources, cross-refs, commentary sections.

After these: **ALL 27 NT books will have 2+ eras** (except the 4 single-chapter books: 2 John, 3 John, Philemon, Jude — which are appropriate at 1 era).

#### 5. Hidden Treasures Discovery Feature
New Library section showcasing 8 lesser-known texts most US Christians have never read:
- 1 Enoch (Book of the Watchers) — Jude quotes it
- War Scroll (1QM) — Sons of Light vs. Darkness
- Book of Giants — Nephilim narrative fragments
- Jubilees — Genesis retold with angel of presence
- Genesis Apocryphon — Noah/Lamech first-person accounts
- Book of Jasher — Referenced in Joshua 10:13
- Josephus — Eyewitness of Temple destruction
- Community Rule (1QS) — Two Spirits doctrine

**Implementation**: Data array `HIDDEN_TREASURES` added to app.js, rendering section in `renderLibraryMain()`, new CSS in `src/css/hidden-treasures.css`.

#### 6. Cross-Reference Preview Tooltips
Hover/tap a cross-ref pill → shows preview tooltip with the target verse text (from flow translations). No navigation needed for a quick look.

**Implementation**: New tooltip div, event delegation for hover/tap on `.cross-ref-pill`, lookup flow verse data by reference, position tooltip near the pill.

#### 7. Study Notes Export (Markdown)
Export button on each chapter card → generates clean Markdown of the study content (title, synopsis, key verse, terms, commentary, cross-refs).

**Implementation**: New `exportChapterMarkdown(chapterId)` function, clipboard + download options.

#### 8. Quick Verse Lookup
Type any scripture reference in the search bar → instantly shows the flow translation + link to the interlinear. Separate from full-text search.

**Implementation**: Parse reference in search handler, show instant result card.

### PLANNED (After Above)

#### 9. Update STATUS.md
Reflect current stats: 200+ eras, 937+ chapters, new features (reading modes, auth, hidden treasures).

#### 10. Full Build + Deploy
- `python build.py` (dev)
- `python build.py --release` (release)
- `python build_mobile.py` (PWA)
- Commit + push + deploy gh-pages

---

## Files Modified This Session
| File | Changes |
|------|---------|
| `src/js/app.js` | HIDDEN_TREASURES data, renderLibraryMain() treasures section, export function, verse lookup |
| `src/css/hidden-treasures.css` | New — treasure card styles |
| `src/css/build-order.txt` | Add hidden-treasures.css |
| `data/1john/era_1john_spirits.py` | New era file (agent) |
| `data/1timothy/era_1tim_warfare.py` | New era file (agent) |
| `data/2peter/era_2pet_judgment.py` | New era file (agent) |
| `data/2thessalonians/era_2thess_mystery.py` | New era file (agent) |
| `data/2timothy/era_2tim_endurance.py` | New era file (agent) |
| `data/titus/era_titus_grace.py` | New era file (agent) |
| `manifest.json` | 6 new era entries |
| `STATUS.md` | Updated stats |

## Manifest Entries Needed
```json
{"id": "1john_spirits", "text": "1john", "name": "Testing the Spirits", "data_file": "era_1john_spirits"}
{"id": "1tim_warfare", "text": "1timothy", "name": "Cosmic Order & Spiritual Warfare", "data_file": "era_1tim_warfare"}
{"id": "2pet_judgment", "text": "2peter", "name": "The Watchers' Judgment", "data_file": "era_2pet_judgment"}
{"id": "2thess_mystery", "text": "2thessalonians", "name": "The Mystery of Lawlessness", "data_file": "era_2thess_mystery"}
{"id": "2tim_endurance", "text": "2timothy", "name": "The Last Words", "data_file": "era_2tim_endurance"}
{"id": "titus_grace", "text": "titus", "name": "The Grace That Trains", "data_file": "era_titus_grace"}
```

## Key Decisions
- 4 single-chapter NT books (2 John, 3 John, Philemon, Jude) stay at 1 era — appropriate for their length
- Hidden Treasures uses existing text IDs, linking to specific eras (e.g., War Scroll links to dss_sectarian → war_scroll era)
- Export is Markdown-first (not PDF) — simpler, more useful, no library dependency
- All era files follow the standard CHAPTERS list pattern with full divine council theology
