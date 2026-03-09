# Agent: Mobile-Specific Test

You are testing the mobile PWA build of the Ancient Texts Study App — loading behavior, bottom navigation, tools popup, responsive overlays, data fetching, and service worker.

## Your Mission

Verify the mobile PWA loads, navigates correctly, fetches data on demand, and all features work in mobile layout. This catches the exact class of bugs (like stale service worker cache) that have broken the app before.

## Server Info

The preview server should be configured for the mobile build. The mobile app URL serves from the `output/mobile/` directory.

## Important: Mobile Viewport

Before testing, resize the viewport to mobile dimensions (375x812) using `preview_resize` with preset "mobile".

## Tests to Execute

### Test 7.1: Loading overlay behavior
1. Set viewport to mobile (375x812)
2. Navigate to the mobile URL
3. Check for loading overlay element
4. Wait up to 15 seconds, checking every 2 seconds if overlay has dismissed
5. **PASS** if overlay appears then dismisses, **FAIL** if stuck after 15s

### Test 7.2: Bottom nav renders
1. After load, use `preview_snapshot` to find bottom navigation bar
2. Count nav buttons — should be 5
3. Verify buttons have icons and/or labels
4. **PASS** if 5 nav buttons visible at bottom

### Test 7.3: Tools popup
1. Find the tools button in bottom nav
2. Click it
3. Verify a tools popup/menu appears with options (Glossary, Map, Hebrew, etc.)
4. **PASS** if tools popup opens with options

### Test 7.4: Glossary on mobile
1. Open glossary from tools popup
2. Verify overlay renders in mobile-friendly layout (full screen or nearly)
3. Check terms are visible and the list scrolls
4. Close the overlay
5. **PASS** if glossary works on mobile

### Test 7.5: Map on mobile
1. Open map from tools popup
2. Verify Leaflet map renders in mobile viewport
3. Check map is visible (`.leaflet-container` exists)
4. Close the overlay
5. **PASS** if map renders on mobile

### Test 7.6: Matrix on mobile
1. Open matrix from tools popup
2. Verify grid renders (may be single-column on mobile)
3. Close the overlay
4. **PASS** if matrix renders responsively

### Test 7.7: Timeline on mobile
1. Open timeline from tools
2. Verify events render and are scrollable
3. Close the overlay
4. **PASS** if timeline works on mobile

### Test 7.8: Hebrew on mobile
1. Open Hebrew from tools
2. Verify letter grid renders
3. Close the overlay
4. **PASS** if Hebrew works on mobile

### Test 7.9: Text data loading (Genesis)
1. From library, click Genesis
2. Check network requests for JSON data file (e.g., `eras/genesis.json`)
3. Wait for content to render
4. Verify chapter/era content is visible
5. Check no 404 errors in network tab
6. **PASS** if data loads and renders, **FAIL** if 404 or no content

### Test 7.10: Interlinear on mobile
1. With Genesis loaded, open reading pane
2. Check interlinear words render
3. Click a word to verify popup works
4. **PASS** if interlinear and popup work on mobile

### Test 7.11: Search on mobile
1. Find and use search input
2. Type "covenant"
3. Verify results appear
4. Click a result
5. **PASS** if search works on mobile

### Test 7.12: Sidebar toggle
1. Find hamburger/menu toggle button
2. Click it — sidebar should slide in
3. Click again or click outside — sidebar should close
4. **PASS** if sidebar toggles correctly

### Test 7.13: Service worker registration
1. Use `preview_eval`: `navigator.serviceWorker.controller ? 'active' : (navigator.serviceWorker.ready ? 'ready' : 'none')`
2. Also try: `navigator.serviceWorker.getRegistrations().then(r => r.length)`
3. **PASS** if service worker is registered

### Test 7.14: Offline handling
1. Check if app has any offline indicators or error handling
2. Use `preview_eval` to check for offline event listeners: `typeof window.offlineHandler !== 'undefined'`
3. **PASS** if offline handling exists, **WARN** if no explicit handling found

### Test 7.15: Viewport and meta tags
1. Use `preview_eval`: `document.querySelector('meta[name="viewport"]')?.content`
2. Check for: `width=device-width, initial-scale=1`
3. Check: `document.querySelector('meta[name="theme-color"]')?.content`
4. Check: `document.querySelector('link[rel="manifest"]')?.href`
5. **PASS** if proper mobile meta tags present

## Result Format

Return results as JSON array:
```json
{
  "id": "7.1",
  "suite": "mobile",
  "name": "Loading overlay behavior",
  "target": "mobile",
  "status": "PASS|FAIL|WARN",
  "duration_ms": 3500,
  "notes": "Loading overlay dismissed after 2.1 seconds",
  "console_errors": [],
  "details": {"load_time_ms": 2100}
}
```

## Important Notes
- ALWAYS resize to mobile viewport before testing
- Mobile loads data on demand (JSON files), not embedded like desktop
- The tools popup is unique to mobile — desktop uses sidebar buttons instead
- Network requests are critical — any 404s on data files is a FAIL
- Take screenshots of: loading state, bottom nav, tools popup, a rendered text
