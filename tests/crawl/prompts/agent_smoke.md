# Agent: Smoke Test

You are testing the Ancient Texts Study App for basic load and render functionality.

## Your Mission

Verify that both desktop and mobile builds load successfully, render the library, and have no critical errors.

## Server Info

- **Desktop**: The preview server is already running. Use `preview_snapshot` and `preview_screenshot` to inspect it.
- **Mobile**: Will need to navigate to the mobile URL separately.

## Tests to Execute

### Test 1.1: Desktop loads
1. Use `preview_snapshot` to get the page accessibility tree
2. Verify the page title contains "Ancient Texts"
3. Use `preview_console_logs` with `level: "error"` to check for console errors
4. **PASS** if title present and zero console errors, **FAIL** otherwise

### Test 1.2: Library grid renders
1. Use `preview_snapshot` to check for library content
2. Look for text cards (library items with book names like Genesis, Exodus, Romans, etc.)
3. Use `preview_eval` with `document.querySelectorAll('.text-card, .library-card, [data-text-id]').length` to count cards
4. **PASS** if 70+ text cards found, **FAIL** otherwise

### Test 1.3: Sidebar renders
1. Use `preview_snapshot` to find sidebar navigation
2. Look for sidebar tool buttons (Glossary, Map, Hebrew, Resources, Matrix, Timeline, Progress)
3. **PASS** if sidebar exists with tool buttons, **FAIL** if missing

### Test 1.4: Mobile loads
1. Use `preview_eval` to navigate: `window.location.href = 'MOBILE_URL'` (replace with actual URL)
2. Wait 3 seconds, then check for loading overlay
3. Wait up to 15 seconds total for loading to complete
4. Use `preview_console_logs` with `level: "error"` to check for errors
5. **PASS** if page loads and overlay dismisses, **FAIL** if stuck on loading

### Test 1.5: Mobile library renders
1. After mobile loads, use `preview_snapshot` to check for library content
2. Look for text cards or list items
3. Check for bottom navigation bar
4. **PASS** if library content and bottom nav visible, **FAIL** otherwise

## Result Format

Return your results as a JSON array. For each test:

```json
{
  "id": "1.1",
  "suite": "smoke",
  "name": "Desktop loads",
  "target": "desktop",
  "status": "PASS",
  "duration_ms": 1200,
  "notes": "Title: Ancient Texts Library, 0 console errors",
  "console_errors": [],
  "details": {}
}
```

For failures, include:
```json
{
  "status": "FAIL",
  "error": "Description of what went wrong",
  "expected": "What should have happened",
  "actual": "What actually happened",
  "console_errors": ["any error messages"]
}
```

## Important Notes
- Take a screenshot after each test for the record
- If a test fails, continue with remaining tests (don't abort)
- Note any warnings as WARN status (non-critical issues)
- Record exact counts and measurements where possible
