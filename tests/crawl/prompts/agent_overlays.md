# Agent: Overlays Test

You are testing all overlay/modal popups in the Ancient Texts Study App — glossary, map, Hebrew, resources, matrix, timeline, progress, and their close behavior.

## Your Mission

Verify every overlay opens, displays correct content, supports interaction (search, filter, detail views), and closes properly (via close button and ESC key).

## Server Info

The preview server is already running for desktop.

## Tests to Execute

### Test 3.1: Glossary opens
1. Find the glossary button in the sidebar (look for text "Glossary" or a book/dictionary icon)
2. Click it with `preview_click`
3. Use `preview_snapshot` to verify `#glossaryOverlay` or glossary content is visible
4. Use `preview_eval` to count glossary entries: `document.querySelectorAll('.glossary-entry, .glossary-term, .glossary-item').length`
5. **PASS** if overlay visible with 500+ terms

### Test 3.2: Glossary search works
1. With glossary open, find the search input inside the glossary
2. Use `preview_fill` to type "covenant"
3. Verify results filter — fewer entries visible, all related to "covenant"
4. **PASS** if results filter correctly

### Test 3.3: Glossary closes
1. Find and click the close button on the glossary overlay
2. Verify overlay is hidden (not visible in snapshot)
3. **PASS** if glossary dismissed

### Test 3.4: Map opens
1. Find and click the map button in sidebar
2. Verify `#mapOverlay` or map content visible
3. Check for Leaflet map container (`.leaflet-container`)
4. **PASS** if map overlay visible with Leaflet map

### Test 3.5: Map closes
1. Click close button on map overlay
2. Verify map overlay hidden
3. **PASS** if dismissed

### Test 3.6: Hebrew opens
1. Find and click the Hebrew button in sidebar
2. Verify `#hebrewOverlay` or Hebrew content visible
3. Count letter cards — should be 22 Hebrew letters
4. **PASS** if overlay visible with 22 letter cards

### Test 3.7: Hebrew closes
1. Click close button
2. Verify overlay hidden
3. **PASS** if dismissed

### Test 3.8: Resources opens
1. Find and click resources button in sidebar
2. Verify `#resourcesOverlay` or resources content visible
3. Check for resource cards with titles
4. **PASS** if overlay visible with resource cards

### Test 3.9: Resources filter works
1. With resources open, find category filter buttons
2. Click a specific category
3. Verify resources filter to that category
4. **PASS** if filtering works, **WARN** if no filters available

### Test 3.10: Matrix opens
1. Find and click matrix button in sidebar
2. Verify `#matrixOverlay` or matrix content visible
3. Count religion/worldview entries — should be 50+
4. **PASS** if overlay visible with 50+ entries

### Test 3.11: Matrix religion detail
1. With matrix open, click on a religion card
2. Verify a detail panel or `#religionDetailOverlay` appears
3. Check detail has beliefs/comparison content
4. **PASS** if detail overlay opens with content

### Test 3.12: Timeline opens
1. Find and click timeline button in sidebar
2. Verify `#timelineOverlay` or timeline content visible
3. Check for chronological event entries
4. **PASS** if timeline renders with events

### Test 3.13: Progress opens
1. Find and click progress button in sidebar
2. Verify `#progressOverlay` or progress content visible
3. Check for reading stats or progress indicators
4. **PASS** if progress overlay renders

### Test 3.14: ESC closes overlay
1. Open the glossary overlay
2. Use `preview_eval` to dispatch: `document.dispatchEvent(new KeyboardEvent('keydown', {key: 'Escape', keyCode: 27, bubbles: true}))`
3. Verify the overlay closes
4. **PASS** if ESC dismisses the overlay

## Result Format

Return results as JSON array:
```json
{
  "id": "3.1",
  "suite": "overlays",
  "name": "Glossary opens",
  "target": "desktop",
  "status": "PASS|FAIL|WARN",
  "duration_ms": 800,
  "notes": "Glossary overlay appeared with 553 terms",
  "console_errors": [],
  "details": {"term_count": 553}
}
```

## Important Notes
- Close each overlay before opening the next one
- If an overlay doesn't have a visible close button, try clicking the overlay background
- Record exact term/entry counts where possible
- Note any overlays that render but are empty as WARN
- Take a screenshot of each overlay when open
