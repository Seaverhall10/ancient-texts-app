# Agent: Search Test

You are testing the search functionality of the Ancient Texts Study App — full-text search, flow translation search, result navigation, edge cases, and keyboard shortcuts.

## Your Mission

Verify search works correctly: returns relevant results, navigates to references, handles edge cases gracefully, and responds to keyboard shortcuts.

## Server Info

The preview server is already running for desktop.

## Tests to Execute

### Test 5.1: Search input accessible
1. Use `preview_snapshot` to find the search input element
2. Look for input with id like `searchInput` or placeholder containing "Search"
3. Verify it exists and is interactive
4. **PASS** if search input found and focusable

### Test 5.2: Basic search — "covenant"
1. Use `preview_fill` to type "covenant" in the search input
2. Wait 1-2 seconds for search to process
3. Use `preview_snapshot` to check for search results
4. Count the number of results shown
5. **PASS** if multiple search results appear containing "covenant"

### Test 5.3: Search result navigation
1. With search results showing, click the first result
2. Verify navigation occurs — text view loads or chapter scrolls
3. Check that relevant content is visible
4. **PASS** if clicking a result navigates to the referenced passage

### Test 5.4: Clear search
1. Clear the search input (triple-click to select all, then delete)
2. Verify search results container empties or hides
3. **PASS** if results clear when input is emptied

### Test 5.5: No results search
1. Type "xyzzy999" (gibberish that won't match anything)
2. Wait for search to process
3. Verify a "no results" message appears or empty state shown
4. Check console for errors
5. **PASS** if no results shown and no JS errors

### Test 5.6: Flow translation search
1. Search for a known phrase (try "In the beginning" or "God created")
2. Verify flow translation matches appear
3. Check results reference verse-level passages
4. **PASS** if flow search returns verse-level matches

### Test 5.7: Special character search
1. Search with special characters: try `"the Lord"` (with quotes)
2. Check console for errors
3. Verify app doesn't crash
4. Search with `&` or `<` characters
5. **PASS** if no console errors and app remains stable

### Test 5.8: Keyboard shortcut Ctrl+K
1. First click somewhere else to defocus search
2. Use `preview_eval` to dispatch: `document.dispatchEvent(new KeyboardEvent('keydown', {key: 'k', ctrlKey: true, bubbles: true}))`
3. Check if search input received focus
4. Use `preview_eval`: `document.activeElement.id` or similar to verify
5. **PASS** if Ctrl+K focuses the search input

## Result Format

Return results as JSON array:
```json
{
  "id": "5.2",
  "suite": "search",
  "name": "Basic search - covenant",
  "target": "desktop",
  "status": "PASS|FAIL|WARN",
  "duration_ms": 1100,
  "notes": "Search returned 23 results for 'covenant'",
  "console_errors": [],
  "details": {"result_count": 23, "query": "covenant"}
}
```

## Important Notes
- Clear the search input between tests
- If search is debounced, wait at least 500ms after typing
- Results may appear in a dropdown, list, or dedicated results area
- Take screenshots of: results for "covenant", no results state
