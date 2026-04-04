# Ancient Texts Study App — Current Status
*Last updated: 2026-04-03 (Session 17)*

---

## WHAT IS COMPLETE

### Core App — Two Versions
- [x] **PC Version**: Single-file HTML app (`build.py → output/AncientTextsStudy.html`, ~68 MB dev / ~65.5 MB release)
- [x] **Mobile Version**: Progressive Web App (`build_mobile.py → output/mobile/`, 0.7 MB shell + on-demand data)
- [x] Both versions contain identical content (109 texts, all interlinear, all features)
- [x] **Electron desktop app** (Windows installer, `electron/` folder)
- [x] Release system packages both into `PC/` + `Mobile/` folders with launchers

### Build & Release System
- [x] `BUILD_ALL.bat` — one-click build of desktop + release + mobile
- [x] `LAUNCH.bat` — 8-option menu (browser, Electron, AI, build, build all, sync, council, exit)
- [x] `release.py` — versioned ZIP packaging with `PC/` and `Mobile/` folders
- [x] `LAUNCH-MOBILE.bat` — auto-detects local IP, starts server for phone access
- [x] `DEPLOY.bat` — one-click build all + commit + push + deploy gh-pages
- [x] Current version: **3.3.0**
- [x] Release ZIP: ~40 MB (includes both PC + Mobile)

### Content (105 texts total)
- [x] **109 texts** in manifest (39 OT + 27 NT + 5 DSS/Second Temple + 1 Pseudepigrapha + 2 Historical + 12 Thematic + 4 Study Trails + 3 Research Lenses + 16 extra-biblical)
- [x] **320 era files** (study chapter groupings)
- [x] **1,246 study chapters** across all texts
- [x] CONTENT_MAP.json — master AI navigation index (auto-rebuilt on every build)

### Flow Translations (verse-by-verse English prose)
**ALL 66 biblical books have flow translations — 42,373 total verses (includes extra-biblical texts).**

**OT — all 39 books complete** | **NT — all 27 books complete**

### Interlinear Data (click any word → original language popup)
- [x] **ALL 39 OT books** — 306,506 Hebrew words (from OSHB, CC BY 4.0)
- [x] **ALL 27 NT books** — 137,833 Greek words
- [x] **GRAND TOTAL: 444,339 interlinear words across 66 biblical books**

### Hallelujah AI (Local Ollama Chat)
- [x] Qwen 2.5 7B base model, custom `Modelfile`
- [x] Full prompt builder (`pipeline/bible_bound.py`) — compact + expanded modes
- [x] **Ancient linguistics baked into ALL modes by default** (not a separate mode)
  - Pictographic/Proto-Sinaitic Hebrew letter meanings
  - Gematria (Hebrew/Greek numerical values)
  - Theophoric name elements (El, Yah, YHWH, Baal)
  - Root family analysis (ישע, שלם, קדש, ברך, אמן)
  - Name change theology, number symbolism
  - Adam→Noah genealogy gospel
- [x] Policy files: `policy/linguistics.yaml`, `policy/bible_bound.yaml`, `policy/security.yaml`
- [x] 4 modes: General, Bible Study, Berean, Dev
- [x] Included in dev build only (stripped from release/mobile)
- [x] RAG context from app study data

### App Features
- [x] Full-text search across era content + 31,101 flow verses
- [x] Cross-reference navigation — "→ Go" links for biblical refs
- [x] **Cross-reference preview tooltips** — hover/tap to see connection note without navigating
- [x] Reading progress tracker — per-chapter checkboxes, localStorage
- [x] **Reading Mode Toggle** — Scripture / Study / Interlinear per chapter (CSS-driven)
- [x] **Firebase Auth + Cloud Sync** — email/password login, Firestore cloud sync
- [x] **Bible Truth Matrix** — 52 worldviews × 13 doctrines, heatmap, **sorted by alignment** with % scores
- [x] Biblical + World History Timeline — 91 events, 8 eras
- [x] Study Trails — 6 curated paths (Divine Council, Messianic, Nephilim, Covenant, Adam-to-Jesus, Cosmic Geography)
- [x] **Hidden Treasures Discovery** — 8 lesser-known texts surfaced in Library
- [x] Ancient World Map — 60+ overlays, CartoDB labels, ESRI borders/roads
- [x] Learn Hebrew module (Aleph-Bet, vowels, roots, practice)
- [x] **Study Notes Export** — Markdown download per chapter
- [x] **Prophecy Matrix** — 59 prophecies with fulfillment tracking
- [x] Usage Analytics — localStorage logging, JSON export, 5K cap
- [x] Reverse cross-references, bookmarks, breadcrumbs, prev/next nav
- [x] CSS design system (tokens, 45 component files, 6-tier responsive breakpoints, clamp())
- [x] Resizable 3-column layout with keyboard shortcuts
- [x] **All 6 mobile Study Tool buttons verified working** (Timeline, Map, Matrix, Prophecy, Hebrew, Glossary)

### Thematic Deep Dives
- [x] **The Nephilim Story** — 7-chapter continuous narrative with 3-position evidence tier toggle ([A] Canon Only / [A+B] Canon + Inference / [A+B+C] Full Picture)
- [x] **Bible Analysis** — 70/70 books, structured tabbed UI (Key Claim, Contested Words, Connections, Silences, Characters, Patterns, Hidden in Translation)
- [x] **Nephilim & Giants** — multi-era study
- [x] **Messianic Thread** — prophecy-to-fulfillment trail
- [x] **Heavenly Court** — divine council deep dive
- [x] **Jesus & the Gentiles** — 9 chapters: parables, wedding invitation theme, faith vs. theology (NEW)

### Apocryphal / Second Temple Texts (eras only, no flow/interlinear)
1 Enoch, Book of Giants, Jubilees, Jasher, Genesis Apocryphon,
DSS Sectarian, Josephus, Heavenly Court

---

## WHAT IS MISSING

### TIER 0 — Audit Fixes (Blocking Deploy)
~~All TIER 0 issues resolved as of 2026-04-03.~~
- ~~110 thematic CRITICALs~~ — fixed (Session 14)
- ~~`hebrew_terms` → `original_terms` schema rename~~ — done (336 files renamed)
- ~~18+ truncated era files~~ — verified not actually truncated (Arbiter token-limit artifact)
- ~~59 chapters missing `key_verse`~~ — all 63 filled (100% coverage)
- ~~1 unlisted CSS file~~ — verified doesn't exist (false flag)

### TIER 1 — Content Depth (Completed)
- ~~Research Lenses~~ — All 3 complete: Islam (7ch), Rabbinic Judaism (7ch), Catholicism (8ch)
- ~~Minor Prophets section depth~~ — 11 short sections expanded to 800+ chars
- ~~NT era expansion~~ — Luke now has 6 eras, John now has 6 eras
- ~~DSS Sectarian original_terms~~ — done (26/26)
- ~~1 Enoch original_terms~~ — done (73/73)
- ~~Jasher original_terms~~ — done (36/43 filled, 147 new terms)
- ~~Psalms of Solomon flow~~ — rebuilt from scratch (320 verses)

### TIER 2 — Study Trails (All Converted)
~~All 4 trails converted from step-by-step to full article format:~~
- ~~Covenant Arc~~ — 8 chapters (Eden → New Creation)
- ~~Adam to Jesus~~ — 8 chapters (Adam → Revelation 22:16)
- ~~Cosmic Geography~~ — 8 chapters (Three-Tier Cosmos → Heaven & Earth Reunited)
- ~~Dead Sea Scrolls Connection~~ — 8 chapters (Discovery → Why DSS Matter)

**NEW trails proposed (from Seaver's Theological Law document):**
10. **The Continuous Tradition** — 7 chapters: throne room across Ezek/1 Enoch/Daniel/Rev, Son of Man thread, Watchers, archangels, cosmic geography, Azazel proof case, canon history
11. **The Riv: Prophets as Covenant Prosecutors** — 9 chapters: riv framework, royal messenger protocol, Isaiah prosecution/restoration, Servant Songs, Jeremiah, Ezekiel merkavah, glory departing, Minor Prophets, lost prophets
12. **Melchizedek and the Royal Priesthood** — 9 chapters: Gen 14, Hebrew name analysis, El Elyon/divine council, Levitical requirements contrast, Psalm 110, 11QMelchizedek DSS, Hebrews 5-7, Messianic name chain, bread and wine
13. **Three Rebellions, One War** — 7 chapters: Nachash/throne guardian, Gen 3:15 thesis, Hermon/Watchers, Babel/nations, three reversals through Christ, ongoing cosmic war, Ekklesia as occupying force
14. **Resurrection and New Creation** — 8 chapters: Hebrew death/Sheol/nephesh, Platonic infiltration history, 1 Cor 15, last enemy destroyed, intermediate state, Millennium, Rev 21-22 God comes down, resurrection implications for living now

### TIER 3 — Features
15. **YouTube / Resource Links** — video sources embedded throughout study content
16. **PDF Export** — export study content as formatted PDF (Markdown export already done)

### TIER 4 — Architecture (Restructuring Plan)
17. **Phase 2**: JS module split (~25 files from 7,907-line app.js)
18. **Phase 3**: Build consolidation + data registry
19. **Phase 4**: Testing + CI/CD

### TIER 5 — Content (Nice to Have)
20. **Apocryphal flow translations** — none of the 8 non-canonical texts have verse-level translations
21. **Psalms, Isaiah, Jeremiah, Ezekiel** — large books with relatively few eras compared to chapter count

---

## APP STATISTICS (v3.3.0)

| Metric | Value |
|--------|-------|
| Total texts | **109** |
| Total era files | **332** |
| Study chapters | **1,278** |
| Flow translations | **66/102 texts** (all 39 OT + all 27 NT + extra-biblical) |
| Flow files | **111** |
| Flow verses | **42,373** |
| Flow scholarly notes | **9,497** |
| Interlinear words (OT) | **306,506** |
| Interlinear words (NT) | **137,833** |
| **Total interlinear** | **444,339** |
| Cross-references | **8,529** |
| Bible Analysis entries | **70/70** (structured tabbed UI) |
| Glossary terms | **607** |
| Map journey routes | **24** (206 waypoints) |
| Religions in Truth Matrix | **52** |
| CSS component files | **48** |
| CSS custom properties | **89** |
| JS named functions | **189** |
| Build output (dev) | ~69 MB HTML |
| Build output (release) | ~69 MB HTML |
| Mobile shell | ~0.9 MB |
| Release ZIP | ~40 MB (PC + Mobile) |
| Current version | **3.3.0** |
| Audit modules | **12** |
| Audit baseline (2026-04-03) | **0 critical**, 578 passed |

---

## RECENT CHANGES

### Continuous Improvements (2026-04-03, continued)
- **All 4 study trails converted** from step-by-step to full article format:
  - Covenant Arc (8 chapters: Eden → Noahic → Abrahamic → Mosaic → Davidic → Exile → New Covenant → New Creation)
  - Adam to Jesus: The Bloodline (8 chapters: Adam/Seth → Noah/Shem → Abraham/Jacob → Judah/Tamar → David → Exile → Two Genealogies → Seed Fulfilled)
  - Cosmic Geography (8 chapters: Three-Tier Cosmos → Sacred Mountains → Eden as Temple → Deut 32 Worldview → Holy vs Unholy Ground → Temple as Cosmos → Christ Reclaims → Heaven & Earth Reunited)
  - Dead Sea Scrolls Connection (8 chapters: Discovery → Deut 32:8 → Biblical Scrolls → Two Spirits → 1 Enoch/Jubilees → 11QMelchizedek → World Jesus Inherited → Why DSS Matter)

### Continuous Improvements (2026-04-03)
- **63 missing key_verse fields filled** across 32 era files — zero missing key_verses remaining
- **Luke expanded**: 2 new eras (8 chapters) — Parables of Mercy (Good Samaritan, Prodigal Son, Rich Man & Lazarus, Pharisee & Tax Collector) + Passion & Resurrection (Gethsemane, Trials, Cross, Emmaus Road). Luke now has 6 eras total.
- **John expanded**: 2 new eras (7 chapters) — The Seven Signs + Prologue & Cosmic Christology (logos theology, monogenes, first week of new creation). John now has 6 eras total.

### Session 16-17 (2026-04-03) — Research Lenses: Rabbinic Judaism + Catholicism
- **NEW: "Rabbinic Judaism & the Talmud"** — 7-chapter comparative study
  - Ch 1: The Oral Torah Claim (Torah she-be'al peh vs Deut 4:2)
  - Ch 2: Jesus vs. the Pharisees — What He Actually Rejected (agreements + breaks)
  - Ch 3: The Three Sects (Pharisees, Sadducees, Essenes + DSS)
  - Ch 4: How the Talmud Handles Messianic Prophecy (Isaiah 53, Daniel 9, Psalm 22)
  - Ch 5: The Parting of the Ways (Birkat haMinim, Yavneh, Bar Kokhba)
  - Ch 6: Modern Streams (Orthodox, Conservative, Reform)
  - Ch 7: What Rabbinic Judaism Preserved (Hebrew, Masoretic tradition, liturgy)
- **NEW: "Catholicism"** — 8-chapter comparative study
  - Ch 1: Peter and the Rock (petros/petra, Kepha, church fathers)
  - Ch 2: Mary — From Theotokos to Mediatrix (Immaculate Conception, Assumption)
  - Ch 3: Purgatory & Prayers for the Dead (2 Maccabees, Platonic infiltration)
  - Ch 4: The Eucharist — Transubstantiation (touto estin, Aristotelian categories)
  - Ch 5: Saints, Relics, and Intercession (Heb 4:16, 1 Tim 2:5, hero cult)
  - Ch 6: Papal Infallibility (Vatican I, ex cathedra, political context)
  - Ch 7: The Canon — Who Decided? (Trent, Jerome vs Augustine)
  - Ch 8: What Catholicism Got Right (liturgy, manuscripts, fathers, continuity)
- All 3 Research Lenses complete (Islam, Rabbinic Judaism, Catholicism)
- Arbiter reviewed: 24 CRITICALs found and fixed across both texts

### Session 15 (2026-04-03) — Research Lens: Islam & the Quran
- NEW: **"Islam & the Quran"** — 7-chapter comparative study (first Research Lens)
  - Ch 1: Muhammad & the Prophetic Pattern
  - Ch 2: Isa in the Quran vs. Jesus in the NT
  - Ch 3: Shared Prophets, Altered Stories (midrash → Quran pipeline)
  - Ch 4: The Quran's Borrowed Sources (Infancy Gospel, Seven Sleepers, Pirke de-Rabbi Eliezer)
  - Ch 5: Jinn vs. Biblical Demonology (four categories framework)
  - Ch 6: Crucifixion Denied — The Central Divide (1 Cor 15 creed, 600-year gap)
  - Ch 7: Satanic Verses, Abrogation & Textual Integrity
- Content standards: Islamic position presented first in strongest form, then biblical response with Hebrew/Greek/Arabic evidence
- 30 sections, 62 cross-references, 32 Hebrew/Greek/Arabic terms
- Arbiter review: 9 CRITICALs found and fixed

### Session 14 (2026-04-03) — Thematic Text CRITICAL Fixes
- Fixed 81 Arbiter CRITICALs across all 12 remaining thematic texts (40 files)
- ~30 "church" → "ekklesia (governing assembly)" fixes (Law #22)
- 6 Deut 32:8 + "(DSS/LXX)" qualifiers added (Law #8)
- Fictitious "metanya" Aramaic term replaced with correct Greek metanoeō
- 1 Enoch 90:31 wrong verse corrected, "7 Qumran caves" factual error fixed
- Galatians 3:19 ESV correction, Isaiah 66:8/Ezekiel 37 zionism nuances
- All thematic texts now Arbiter-reviewed and fixed

### Session 12-13 (2026-04-03) — The Reckoning + Nephilim Narrative + Bible Analysis Rebuild

**Session 12: Full Content Audit**
- Arbiter AI review of 61 era files across 27 texts: 177 CRITICAL, 601 WARNING found
- Fixed 43 CRITICALs directly: Rule 5 violations (non-canonical framing), three-rebellions conflation, Sethite dating errors, gigantes etymology, Azazel evidence tier, unnamed nephew factual error, LXX manuscript specificity
- 18 cross-ref type misclassifications fixed app-wide (1 Enoch "ot" to "pseudepigrapha", deuterocanonical corrections)
- Psalms of Solomon flow rebuilt from scratch (was 18 duplicates of Psalm 1 — now 320 real verses)
- 2 Enoch OCR cleaned (300 mid-word space artifacts from PDF extraction)
- Bible Analysis ekklesia wording fixed (Law #22)
- Parables afterlife framing fixed (Paradise = intermediate state, Law #23)
- `arbiter.py --text` handler implemented (was broken)

**Session 13: Nephilim Narrative with Evidence Tier Filter**
- NEW: **"The Nephilim Story"** — 7-chapter continuous narrative with 3-position evidence toggle
  - [A] Canon Only / [A+B] Canon + Inference / [A+B+C] Full Picture
  - CSS-driven show/hide, localStorage persistence, "Want to see more?" upsell prompts
  - 8 Arbiter CRITICALs found and fixed before commit
  - Added to Nephilim & Giants study trail
- NEW: **Bible Analysis** rebuilt from static HTML to structured tabbed UI
  - 70/70 books complete (zero stubs remaining)
  - 7 tabs per book: Key Claim, Contested Words, Connections, Silences, Characters, Patterns, Hidden in Translation
  - Hebrew/Greek Unicode throughout, severity badges, cross-reference navigation
  - Tab switching verified in mobile browser

### Session 9 (2026-03-25) — Major Content Expansion + Audit Cleanup
- **QA audit: 0 critical, 502 passed** — clean across the board
- **2 new thematic study texts** (18 chapters):
  - **Melchizedek & the Royal Priesthood** — 9 chapters across 3 eras: Genesis 14 origins, Psalm 110 + 11QMelchizedek + Hebrews 5-7, bread-and-wine fulfillment, ekklesia as royal priesthood
  - **The Riv: Prophets as Covenant Prosecutors** — 9 chapters across 3 eras: riv framework + royal messenger protocol, Isaiah/Jeremiah/Ezekiel prosecutions, the Twelve + Jesus as final prosecutor
- **5 new NT/OT era files** (16 new study chapters):
  - **Luke Travel Narrative** (`era_luke_journey.py`) — 4 chapters: Good Samaritan, Prodigal Son, parables of grace, Zacchaeus
  - **John I AM + Farewell** (`era_john_discourse.py`) — 4 chapters: seven I AM statements, Upper Room Discourse, High Priestly Prayer, Hour of Glory
  - **Amos Covenant Prosecutor** (`era_amos_riv.py`) — 3 chapters: sod/divine council authority, five failed disciplines, famine of the word
  - **Obadiah Deep Dive** (`era_obadiah_edom.py`) — 3 chapters: pride, betrayal, kingdom restoration
  - **Haggai Latter Glory** (`era_haggai_glory.py`) — 2 chapters: greater glory, Zerubbabel signet ring
- **4 Minor Prophet expansions** (8 new chapters):
  - Joel cosmic (Day of YHWH + Valley of Decision), Zephaniah nations (de-creation + remnant call)
  - Jonah mercy (reluctant prophet + divine mercy), Nahum warrior (divine warrior + Nineveh's fall)
- **DSS Sectarian hebrew_terms**: 0/26 → **26/26** populated (100%)
- **1 Enoch hebrew_terms**: 18/73 → **73/73** populated (100%)
- **21 cross-ref type tags fixed** (Galatians + Matthew)
- Content map: **88 texts, 300 eras, 1,189 chapters, 8,310 cross-references**
- QA audit: **0 critical, 0 warnings, 514 passed**

### Session 8 (2026-03-14) — Nephilim Worldwide + Short Dives
- **Nephilim Worldwide**: 6 new chapters tracking giant traditions across every continent + map integration
- **Short Dives**: 30 full mini-articles with dedicated reader
- **Unified reader** redesign with theme index, Bible Analysis tab, My Study tab
- **Landing page** redesign with study-first layout and Short Dives carousel
- Connected timeline, map, and reader — everything linked

### Session 7 — Agent Audit System, Map Enhancements, NT Era Expansion
- **Full Sentient Audit System** (`agents/audit_claude_work.py`, 1,426 lines):
  - 12 audit modules: map journeys, colors, coords, links, waypoints, eras, flow, interlinear, glossary, xrefs, code structure, AI theological review
  - Theological guardrails: Sethite contamination, canonical language, divine council, Deut 32:8, evidence tiers
  - `--full-app` scans ALL 1,059 chapters, 31,101 verses, 444,339 words, 6,990 xrefs, 607 glossary entries
- **Arbiter enhanced** with `--map` theological check on waypoint descriptions
- **Reader enhanced** with `--mode map-audit` for data integrity validation
- **Review pipeline** (`review_content.py`) now includes map + Claude Code audit in Phase 1
- **Map journey enhancements** (from Session 6 continuation):
  - 6 new journey routes (Isaac, Jesus Galilean, Jesus Final Week, Paul 1st/2nd/3rd)
  - Nimrod expanded to 10 waypoints (Gilgamesh, Eridu, Calneh, Resen, Rehoboth-Ir)
  - All 24 journeys reordered chronologically by epoch
  - 24 distinct non-yellow colors, epoch separator headers
  - White waypoint markers with drop shadow for visibility
- **NT Era Expansion**: 6 new era files (Galatians, Philippians, Colossians, 1 Thess, 1 Peter, Jude)
- **Agent Delegation Protocol** mandated in CLAUDE.md and MEMORY.md
- Stats: 80 texts → 246 eras → 1,059 chapters → 6,990 xrefs → 607 glossary
- Audit baseline: 37 critical (NT eras missing id/era), 87 warnings, 577 info

### Session 5 — Visual Polish, Map Enhancements, Name Theology
- **Patriarch Ages Lifespan Chart** — interactive bar chart (Adam through Abraham)
- **Ancient World Map**: 70+ biblical cities with scripture cross-links, "Read in App" buttons
- Map layer control groups with collapsible headers
- **Name Theology System**: 22 glossary entries (theophoric, prophet, apostle, women, places)
- 6 era sections with embedded name theology
- CSS z-index system migrated to custom properties
- 3 new thematic texts: Biblical Canon, Church History, Zionism & Israel

### Session 6 — NT Era Expansion (Matthew + Acts) + Mobile Map Fix
- **Matthew**: 3 new deep-dive eras (19 chapters):
  - Sermon on the Mount (Beatitudes, Antitheses, Lord's Prayer, Two Builders, Kingdom Charter)
  - Kingdom Parables (Sower, Wheat/Tares, Mustard Seed, Talents, Sheep and Goats)
  - Olivet Discourse through Great Commission (Passion, Crucifixion, Resurrection)
- **Acts**: 3 new deep-dive eras (11 chapters):
  - Pentecost to Persecution (Community, Stephen, Philip, Cornelius breakthrough)
  - Missionary Journeys + Jerusalem Council (Europe, Athens, Ephesus farewell)
  - Paul's Trials and Rome (Arrest, Felix/Agrippa, Shipwreck, Gospel unhindered)
- **Mobile map fix**: Layer control collapsed on mobile (<768px), CSS constraints added
- Stats: 80 texts → 246 eras → 1,049 chapters → 7,096 cross-refs
- Commits: f33238b, bf4fb10, 316d0d9

---

## EARLIER CHANGES (2026-03-12)

### Session 1 — Firebase + NT Depth + Reading Modes
- Firebase Auth with email/password login and Firestore cloud sync
- Reading Mode Toggle: Scripture / Study / Interlinear per chapter
- 14 new NT era files (42 study chapters across 11 books)

### Session 2 — Features + More NT Depth
- 6 more NT era files (18 study chapters): 1 John, 1 Timothy, 2 Peter, 2 Thessalonians, 2 Timothy, Titus
- Hidden Treasures Discovery feature (8 lesser-known texts in Library)
- Cross-reference preview tooltips (hover to see connection notes)
- Study notes Markdown export (download per chapter)
- 45 CSS component files

### Session 3 — DSS Text Grouping, Study Notes, Study Trails inline scripture
- DSS texts grouped into thematic category in sidebar
- Study Notes system with cloud sync
- Study Trails updated with inline scripture rendering

### Session 4 — Mobile Fixes, Truth Matrix Sort, Jesus & the Gentiles
- Fixed all 6 mobile Study Tool buttons (Prophecy async loading, correct function names)
- Truth Matrix sorted by alignment — most aligned first + overall % scores (color-coded)
- **"Jesus & the Gentiles" deep dive** — 9 chapters across 3 eras:
  - Part I: Why Did Jesus Speak in Parables? (Matt 13, Gentile faith, Pharisee blindness)
  - Part II: The Wedding Invitation (Wisdom's feast, wedding banquet parables, ten virgins)
  - Part III: Simple Faith vs. Theological Steps (Sermon on Mount, thief on cross, apostolic theology)
- Full biblical accuracy verification of all 9 chapters
- Fixed Chapter 4 title key bug (`heading` → `title`)
- Commits: cd97133, 946bc85, 35423ec, bdfb1ed

---

## KEY FILES

| File | Purpose |
|------|---------|
| `build.py` | Build desktop app — run after any change |
| `build.py --release` | Build release version (no HAI) |
| `build_mobile.py` | Build mobile PWA (requires release build) |
| `BUILD_ALL.bat` | One-click: desktop → release → mobile |
| `DEPLOY.bat` | One-click: build all → commit → push → deploy gh-pages |
| `LAUNCH.bat` | Main menu launcher (8 options) |
| `release.py` | Package versioned release ZIP (PC + Mobile) |
| `manifest.json` | Master text/era registry (109 texts, 332 eras) |
| `CONTENT_MAP.json` | AI navigation index (auto-built) |
| `pipeline/bible_bound.py` | HAI system prompt builder |
| `policy/linguistics.yaml` | Ancient linguistics reference data |
| `Modelfile` | Ollama model configuration |
| `app.py` | HAI server (FastAPI + pywebview) |
| `data/generate_ot_flow.py` | OT flow generator (Claude Sonnet API) |
| `data/generate_nt_flow.py` | NT flow generator (Claude API) |
| `VERSION` | Current version (3.3.0) |
| `STATUS.md` | THIS FILE |
