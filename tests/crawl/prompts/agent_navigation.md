# Agent: Navigation Test

You are testing all navigation paths in the Ancient Texts Study App — text selection, era browsing, hash routing, breadcrumbs, and category filters.

## Your Mission

Verify that users can navigate to every major section of the app and return to the library. Test both desktop and mobile navigation patterns.

## Server Info

The preview server is already running for desktop. Mobile tests use a different URL.

## Tests to Execute

### Test 2.1: Select Genesis
1. From library view, use `preview_snapshot` to find Genesis card
2. Use `preview_click` on the Genesis text card
3. Wait 1s, then use `preview_snapshot` to verify:
   - Sidebar shows Genesis eras (count them — should be 16)
   - Main content header shows "Genesis"
4. **PASS** if Genesis loads with 16 eras, **FAIL** otherwise

### Test 2.2: Select NT book (Romans)
1. Return to library (click back/library button)
2. Find and click Romans text card
3. Verify sidebar shows Romans eras
4. **PASS** if Romans loads with eras visible

### Test 2.3: Select Apocryphal (1 Enoch)
1. Return to library
2. Find and click 1 Enoch text card
3. Verify eras render (no flow translations expected for apocryphal)
4. Check no JS errors in console
5. **PASS** if 1 Enoch loads without errors

### Test 2.4: Back to library
1. From 1 Enoch view, find "Back to Library" button or breadcrumb
2. Click it
3. Verify library grid re-renders with all text cards
4. **PASS** if library grid visible with 70+ cards

### Test 2.5: Era navigation
1. Navigate to Genesis
2. Find an era name in the sidebar (e.g., "The Flood" or era 3-4)
3. Click it
4. Verify main content scrolls to show that era's chapters
5. **PASS** if content scrolls to the selected era

### Test 2.6: Chapter card interaction
1. In Genesis, find and click a chapter card
2. Verify chapter content expands or becomes visible
3. Check for flow translation text or study content
4. **PASS** if chapter content displays

### Test 2.7: Hash routing — #genesis
1. Use `preview_eval` to set `window.location.hash = '#genesis'`
2. Wait 2s for navigation
3. Verify Genesis loads (check sidebar, content header)
4. **PASS** if Genesis loads from hash

### Test 2.8: Hash routing — #romans
1. Use `preview_eval` to set `window.location.hash = '#romans'`
2. Wait 2s
3. Verify Romans loads
4. **PASS** if Romans loads from hash

### Test 2.9: Breadcrumb navigation
1. From a text view, look for breadcrumb links in the page
2. Click the "Library" breadcrumb
3. Verify returns to library view
4. **PASS** if library renders, **WARN** if no breadcrumbs found

### Test 2.10: Category filter
1. In library view, look for category filter tabs/buttons
2. Click "New Testament" or a specific category
3. Verify library filters to show only that category
4. Click "All" to reset
5. **PASS** if filtering works correctly

### Test 2.11: Mobile bottom nav
1. Navigate to mobile URL
2. Wait for load to complete
3. Find bottom navigation buttons
4. Click each one and verify it navigates to the correct view
5. **PASS** if all bottom nav buttons work

### Test 2.12: Mobile text selection
1. On mobile, find a text card in the library
2. Tap/click it
3. Verify text view loads with eras
4. **PASS** if text loads on mobile

## Result Format

Return results as a JSON array with this structure per test:
```json
{
  "id": "2.1",
  "suite": "navigation",
  "name": "Select Genesis",
  "target": "desktop",
  "status": "PASS|FAIL|WARN",
  "duration_ms": 1500,
  "notes": "Genesis loaded with 16 eras in sidebar",
  "console_errors": [],
  "details": {"era_count": 16}
}
```

## Important Notes
- Always return to library before testing the next text selection
- Take screenshots after major navigation events
- If an element isn't found by the expected selector, try alternative selectors
- Record exact era counts for Genesis (should be 16)
- Note any slow transitions (>2s) as WARN
