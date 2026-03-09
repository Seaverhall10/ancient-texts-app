# Agent: Content Integrity Test

You are testing the data integrity of the Ancient Texts Study App — verifying that eras, flow translations, cross-references, glossary terms, matrix entries, timeline events, and other content loads correctly.

## Your Mission

Verify all major content categories have the expected data volume and render properly. This is the most comprehensive suite — you're checking that 74 texts worth of data actually made it into the build.

## Server Info

The preview server is already running for desktop.

## Tests to Execute

### Test 6.1: Genesis has 16 eras
1. Navigate to Genesis
2. Count era entries in the sidebar
3. Use `preview_eval`: count sidebar era items for Genesis
4. **PASS** if exactly 16 eras, **WARN** if close, **FAIL** if very different

### Test 6.2: Genesis chapters render
1. In Genesis, click on the first era
2. Verify chapter cards render with visible content
3. Check at least one card has body text (not just a title)
4. **PASS** if chapter cards with content visible

### Test 6.3: Flow translations visible
1. Open a Genesis chapter card
2. Look for verse-by-verse flow translation text
3. Check for verse numbers and formatted paragraphs
4. **PASS** if flow text visible with verse numbers

### Test 6.4: Cross-references work
1. In a chapter, find a cross-reference indicator (usually an icon or link)
2. Click it to open the xref drawer/panel
3. Verify drawer shows referenced passages (book + chapter + verse)
4. **PASS** if xref drawer opens with references, **WARN** if no xrefs found in this chapter

### Test 6.5: Xref navigation
1. With xref drawer open, click a cross-reference link
2. Verify navigation to the target passage/text
3. **PASS** if target passage loads

### Test 6.6: NT text loads (Matthew)
1. Navigate to Matthew
2. Verify eras render in sidebar
3. Check chapter content renders
4. **PASS** if Matthew loads with eras and content

### Test 6.7: Apocryphal text loads (1 Enoch)
1. Navigate to 1 Enoch
2. Verify eras render (no flow translations expected)
3. Check console for errors
4. **PASS** if eras visible and no JS errors

### Test 6.8: Glossary has 500+ terms
1. Open glossary overlay
2. Count entries using `preview_eval`: `document.querySelectorAll('.glossary-entry, .glossary-term, .glossary-item').length`
3. **PASS** if 500+ terms, **WARN** if 400-500, **FAIL** if <400

### Test 6.9: Matrix has 50+ religions
1. Open matrix overlay
2. Count religion entries using `preview_eval`
3. **PASS** if 50+ entries

### Test 6.10: Timeline has events
1. Open timeline overlay
2. Check for timeline event entries
3. Count events — should be 20+
4. **PASS** if chronological events render

### Test 6.11: Hebrew has 22 letters
1. Open Hebrew overlay
2. Count letter cards
3. **PASS** if exactly 22 Hebrew letters

### Test 6.12: Bookmarks persist
1. Navigate to Genesis, find a bookmarkable element
2. Click to add a bookmark (star or bookmark icon)
3. Use `preview_eval` to reload: `location.reload()`
4. Wait for reload, then check if bookmark is still present
5. **PASS** if bookmark survives reload

### Test 6.13: Reading progress
1. Mark a chapter as read (click the read/checkmark indicator)
2. Open progress overlay
3. Check if progress counter reflects the marked chapter
4. **PASS** if progress updates, **WARN** if can't find the read toggle

### Test 6.14: Study trails
1. Find and navigate to a study trail
2. Verify trail cards render with scripture references
3. **PASS** if trail content visible, **WARN** if no trails found

### Test 6.15: Prophecy matrix
1. Navigate to prophecy matrix view (may be a separate view from Bible Truth Matrix)
2. Check for OT prophecy / NT fulfillment entries
3. **PASS** if prophecy grid renders

### Test 6.16: Core beliefs
1. Navigate to core beliefs section
2. Find a topic (e.g., "divine council")
3. Verify content renders with scripture references
4. **PASS** if content visible, **WARN** if section not found

### Test 6.17: Resources populate
1. Open resources overlay
2. Check for resource cards with titles and external links
3. Count resources — should be 5+
4. **PASS** if 5+ resource cards visible

### Test 6.18: Analytics tracking
1. Navigate through 2-3 texts
2. Use `preview_eval` to check localStorage for analytics: `localStorage.getItem('atl-analytics-events') || localStorage.getItem('genesis-analytics')`
3. Check if events were logged
4. **PASS** if analytics events found, **WARN** if no analytics key found

## Result Format

Return results as JSON array:
```json
{
  "id": "6.1",
  "suite": "content",
  "name": "Genesis has 16 eras",
  "target": "desktop",
  "status": "PASS|FAIL|WARN",
  "duration_ms": 600,
  "notes": "Genesis shows 16 eras in sidebar",
  "console_errors": [],
  "details": {"era_count": 16}
}
```

## Important Notes
- This suite tests data volume — record counts and measurements
- Close overlays between tests
- Some features (study trails, core beliefs) may be views rather than overlays
- If a feature can't be found, report as WARN with notes about what you tried
- Take screenshots of: Genesis eras, glossary full, matrix full, timeline
