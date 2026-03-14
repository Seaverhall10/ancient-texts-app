# Next Session — Prioritized Fix List
*Generated from full-app audit on 2026-03-13*

---

## 🔴 TIER 0 — CRITICAL (Fix Before Deploy)

### A. 6 NT Era Files Missing `id` and `era` Fields (18 chapters)
These files have CHAPTERS entries without `id` or `era` — the app may not render them:
```
data/galatians/era_galatians_freedom.py        → 4 chapters
data/philippians/era_philippians_christ_hymn.py → 3 chapters
data/colossians/era_colossians_supremacy.py    → 3 chapters
data/1thessalonians/era_1thess_parousia.py     → 3 chapters
data/1peter/era_1peter_exiles.py               → 3 chapters
data/jude/era_jude_contend.py                  → 2 chapters
```
**Fix**: Add `id` and `era` fields to each chapter dict. Use pattern from Genesis/Romans eras.

### B. 1 Chapter Missing `ref` Field
```
ane-joseph-egypt → missing 'ref' field
```

---

## 🟡 TIER 1 — Content Gaps Found by Audit

### C. ~180 Cross-References Missing `type` Tags
These xrefs work but aren't categorized (ot/nt/ane/dss):
- **Matthew eras**: olivet-signs, gethsemane-trial, cross-burial, resurrection, sower-secrets, wheat-tares, community-parables, vineyard-wedding, talents-sheep-goats (~45 xrefs)
- **Acts eras**: all 10 chapters (~50 xrefs)
- **New NT eras**: Galatians, Philippians, Colossians, 1 Thess, 1 Peter, Jude (~85 xrefs)
**Fix**: Batch edit — add `'type': 'ot'` or `'type': 'nt'` to each cross_ref dict.

### D. Leviticus — 27 Chapters with Empty Section Bodies
All `lev-1` through `lev-27` have sections that are structural shells:
- Section headings: missing (numbered 1, 2, 3...)
- Section bodies: 0 characters
**Fix**: Write proper section headings and content for Leviticus study material. This is the biggest content gap in the OT.

### E. 2 Peter + 3 John — Empty Section Bodies
Same pattern as Leviticus — structure exists but no content:
- `2peter-1`, `2peter-2-3`, `2pet-judgment-1/2/3`: 14 empty sections
- `3john-hospitality-01`: 5 empty sections
**Fix**: Write study content for these sections.

### F. 59 Chapters Missing `key_verse`
Scattered across various texts. Low priority but affects completeness score.

### G. 1 Unlisted CSS File
`styles.css` exists on disk but isn't in `src/css/build-order.txt`.
**Fix**: Either add to build order or remove if obsolete.

---

## 🟡 TIER 2 — Map Quality Improvements

### H. 18 Waypoints with Short Descriptions (< 30 chars)
Locations that need fuller descriptions:
- Babel/Babylon, Akkad, Valley of Gerar, Beer-sheba
- Goshen, Red Sea crossing, Edom border
- Ai, Kiriath-jearim, Hazor, Gath
- Byblos, Tyre & Sidon, Upper Room, Ephesus

### I. ~28 Similar Map Colors
Purple/violet family has too many members. Consider:
- Shifting watcher_descent to a more unique hue
- Adjusting balaam, wilderness, phoenician_trade, paul_journey2

### J. 14 Waypoints Missing Scripture Refs
First/last waypoints in journeys often lack explicit refs.

### K. Shared Waypoint Coordinates (Return Trips)
~14 instances where journey start/end share coords (e.g., Abraham starts/ends at Hebron).
Most are intentional but should be reviewed.

---

## 📋 TIER 3 — Existing Priorities (from STATUS.md)

### L. Minor Prophets Depth
12 books at 25-40% of Genesis depth (51/55 chapters flagged).

### M. NT Era Expansion
Luke and John still have only 2 eras each.

### N. DSS/1 Enoch/Jasher hebrew_terms
Many chapters at 0% coverage.

### O. Study Trail Conversions
Covenant Arc, Adam-to-Jesus, Cosmic Geography, DSS Connection still in old format.

### P. JS Module Split (Phase 2)
app.js is 9,190 lines — needs splitting into ~25 modules.

---

## ⚡ Recommended Session Order

1. **First 15 min**: Fix TIER 0 criticals (A + B) — delegate to general-purpose agent
2. **Next 30 min**: Fix TIER 1 xref types (C) — delegate to agent with batch edit
3. **Next 60 min**: Write Leviticus content (D) — delegate to Scribe agent or general-purpose
4. **Ongoing**: Pick from TIER 2 or TIER 3 based on user priorities
5. **Before deploy**: Run `python agents/audit_claude_work.py --full-app` — target 0 CRITICAL

---

## 🧠 Audit Commands Reference
```bash
python agents/audit_claude_work.py --full-app  # EVERYTHING (run before deploy)
python agents/audit_claude_work.py --eras      # Era files only
python agents/audit_claude_work.py --flow      # Flow translations only
python agents/audit_claude_work.py --xrefs     # Cross-ref quality
python agents/audit_claude_work.py --glossary  # Glossary depth
python agents/audit_claude_work.py --code      # Code structure
python agents/audit_claude_work.py --map       # Map journeys
python agents/reader.py --mode qa              # 451+ structural checks
python agents/arbiter.py --map                 # Theological guardrails
```
