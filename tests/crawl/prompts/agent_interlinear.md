# Agent: Interlinear / Reading Pane Test

You are testing the interlinear reading pane — the core study engine of the Ancient Texts Study App. This includes Hebrew/Greek word display, word popups, chapter navigation, font scaling, row toggles, and user modes.

## Your Mission

Verify the reading pane opens, displays original-language words, responds to all controls (nav, font, toggles, modes), and closes properly.

## Server Info

The preview server is already running for desktop.

## Pre-requisite

First navigate to Genesis so you have a text loaded before testing the reading pane.

## Tests to Execute

### Test 4.1: Reading pane opens
1. Make sure Genesis is loaded (navigate if needed)
2. Find the reading pane toggle button
3. Click it with `preview_click`
4. Verify reading pane becomes visible in snapshot
5. **PASS** if pane visible with content area

### Test 4.2: Hebrew interlinear renders
1. With reading pane open on Genesis
2. Look for Hebrew word cards in the pane content
3. Use `preview_eval` to check: `document.querySelectorAll('.il-word, .word-card, [data-strongs]').length`
4. Verify words have Hebrew text, transliteration, and English glosses
5. **PASS** if Hebrew word cards visible (10+ words expected per verse)

### Test 4.3: Word click popup
1. Find a word card in the interlinear
2. Click it
3. Verify a popup/detail panel appears with word information
4. Check popup shows: Strong's number, morphology, definition
5. **PASS** if popup appears with lexical data

### Test 4.4: Word popup closes
1. Click elsewhere on the page (not on the popup)
2. Verify popup dismisses
3. **PASS** if popup hidden

### Test 4.5: Chapter nav — next
1. Note the current chapter number displayed
2. Find and click the "next chapter" button (arrow or >)
3. Verify chapter number increments
4. Check new chapter's words render
5. **PASS** if next chapter loads

### Test 4.6: Chapter nav — previous
1. Find and click the "previous chapter" button
2. Verify chapter number decrements
3. **PASS** if previous chapter loads

### Test 4.7: Book selector dropdown
1. Find the book selector dropdown in reading pane
2. Change it to "Exodus" (or another OT book)
3. Verify new book's interlinear loads (Hebrew words change)
4. **PASS** if book changes and new words render

### Test 4.8: NT Greek interlinear
1. Change book selector to "Romans" or another NT book
2. Verify Greek words render (different script from Hebrew)
3. Check language badge/indicator shows Greek
4. **PASS** if Greek word cards visible

### Test 4.9: Font scale increase
1. Find the font increase button (+ or zoom in)
2. Click it
3. Check that font scale display updates (e.g., "1.0" → "1.1")
4. **PASS** if scale increases

### Test 4.10: Font scale decrease
1. Find the font decrease button (- or zoom out)
2. Click it
3. Check font scale display updates downward
4. **PASS** if scale decreases

### Test 4.11: Toggle morphology row
1. Find morphology toggle in study controls
2. Toggle it off
3. Verify morphology row disappears from word cards
4. Use `preview_eval` to check visibility of morph elements
5. **PASS** if morphology row hidden

### Test 4.12: Toggle transliteration row
1. Find transliteration toggle
2. Toggle it off
3. Verify transliteration row hidden
4. **PASS** if transliteration hidden

### Test 4.13: User mode switch
1. Find user mode selector (Reader / Student / Scholar)
2. Switch to "Reader" mode
3. Verify fewer interlinear rows visible (simplified view)
4. Switch back to "Scholar"
5. Verify all rows return
6. **PASS** if mode switching changes visible rows

### Test 4.14: Reading pane fullscreen
1. Find the expand/fullscreen button for reading pane
2. Click it
3. Verify pane expands (wider than before)
4. **PASS** if pane expands, content still visible

### Test 4.15: Reading pane close
1. Find and click the close button for reading pane
2. Verify reading pane is hidden
3. **PASS** if pane closes

## Result Format

Return results as JSON array:
```json
{
  "id": "4.1",
  "suite": "interlinear",
  "name": "Reading pane opens",
  "target": "desktop",
  "status": "PASS|FAIL|WARN",
  "duration_ms": 900,
  "notes": "Pane opened, Genesis Chapter 1 Hebrew words visible",
  "console_errors": [],
  "details": {"word_count": 45, "language": "hebrew"}
}
```

## Important Notes
- The interlinear is the most complex feature — take extra care with selectors
- Word cards may use various class names: `.il-word`, `.word-card`, `.interlinear-word`
- If word popup doesn't appear on first click, try clicking a different word
- Record word counts and language badges where possible
- Take screenshots of: pane open, word popup, Greek text, mode changes
