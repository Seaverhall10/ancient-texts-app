# Agent: Performance & Error Audit Test

You are auditing the Ancient Texts Study App for console errors, load times, memory usage, and stability under rapid navigation.

## Your Mission

Find any hidden errors, measure performance baselines, and stress-test rapid navigation. This suite catches silent failures that look fine visually but indicate problems under the hood.

## Server Info

The preview server is already running for both desktop and mobile.

## Tests to Execute

### Test 8.1: No console errors on load
1. Check console for error-level messages: `preview_console_logs` with `onlyErrors: true`
2. Count any `console.error` entries
3. List the errors if any exist
4. **PASS** if zero console errors, **FAIL** if any errors present

### Test 8.2: No unexpected warnings
1. Check console for warning-level messages
2. Filter out known/expected warnings (e.g., Leaflet deprecation, third-party lib notices)
3. Count unexpected warnings
4. **PASS** if zero unexpected warnings, **WARN** if only third-party warnings

### Test 8.3: Page load time
1. Use `preview_eval`:
```javascript
(function() {
  var timing = performance.getEntriesByType('navigation')[0];
  if (timing) return {
    domContentLoaded: Math.round(timing.domContentLoadedEventEnd - timing.startTime),
    loadComplete: Math.round(timing.loadEventEnd - timing.startTime),
    domInteractive: Math.round(timing.domInteractive - timing.startTime)
  };
  return 'PerformanceNavigationTiming not available';
})()
```
2. Record DOMContentLoaded time
3. **PASS** if DOMContentLoaded < 3000ms, **WARN** if 3000-5000ms, **FAIL** if >5000ms

### Test 8.4: Memory baseline
1. Use `preview_eval`:
```javascript
(function() {
  if (performance.memory) return {
    usedHeapMB: Math.round(performance.memory.usedJSHeapSize / 1024 / 1024),
    totalHeapMB: Math.round(performance.memory.totalJSHeapSize / 1024 / 1024),
    limitMB: Math.round(performance.memory.jsHeapSizeLimit / 1024 / 1024)
  };
  return 'performance.memory not available (non-Chromium browser)';
})()
```
2. Record used heap in MB
3. **PASS** if <200MB, **WARN** if 200-300MB, **FAIL** if >300MB

### Test 8.5: Search index build time
1. Use `preview_eval`:
```javascript
(function() {
  var start = performance.now();
  if (typeof buildSearchIndex === 'function') buildSearchIndex();
  var elapsed = Math.round(performance.now() - start);
  return {build_time_ms: elapsed};
})()
```
2. Record build time
3. **PASS** if <2000ms, **WARN** if 2000-5000ms, **FAIL** if >5000ms

### Test 8.6: Large text render (Genesis)
1. Start a timer
2. Navigate to Genesis (largest text with 16 eras)
3. Wait for content to fully render
4. Record time from navigation start to content visible
5. **PASS** if renders in <2s, **WARN** if 2-4s, **FAIL** if >4s

### Test 8.7: Rapid navigation stress
1. Navigate quickly through 5 texts, clicking each within 1 second:
   - Genesis → Exodus → Romans → 1 Enoch → Matthew
2. Use `preview_click` on each text card rapidly
3. After final click, wait 2 seconds
4. Verify Matthew (final text) renders correctly
5. Check console for errors
6. **PASS** if final text renders with no crashes/errors

### Test 8.8: No failed network requests (mobile)
1. Navigate to mobile URL
2. Wait for full load including data fetching
3. Check network requests for any 404 or 500 status
4. Use `preview_eval` or `preview_network` with `filter: "failed"`
5. **PASS** if zero failed requests, **FAIL** if any failures

## Result Format

Return results as JSON array:
```json
{
  "id": "8.3",
  "suite": "performance",
  "name": "Page load time",
  "target": "desktop",
  "status": "PASS|FAIL|WARN",
  "duration_ms": 0,
  "notes": "DOMContentLoaded: 1847ms, Load: 2341ms",
  "console_errors": [],
  "details": {
    "dom_content_loaded_ms": 1847,
    "load_complete_ms": 2341,
    "dom_interactive_ms": 1200
  }
}
```

## Important Notes
- Performance numbers vary by machine — record the actual values regardless of pass/fail
- `performance.memory` is Chrome-only; if not available, mark test as WARN
- For the stress test (8.7), rapid means clicking every ~1 second, not simultaneously
- Check console after EVERY test — performance issues often surface as errors
- Take screenshots of: initial load state, Genesis loaded, after stress test
