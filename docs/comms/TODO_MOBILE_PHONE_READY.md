# TO-DO: True Mobile Phone Version
*Created: March 7, 2026 — For next session*

## Goal
Get the Ancient Texts Study App installable on Seaver's phone as a real
offline app he can use anywhere — no PC running, no WiFi dependency.

---

## RECOMMENDED APPROACH: GitHub Pages PWA
Deploy the mobile PWA to GitHub Pages (free). Visit the URL once on your
phone, tap "Add to Home Screen", and it caches everything for offline use.
Works on both iPhone and Android. Zero cost, no app store.

---

## TASK LIST

### Phase 1: Deploy to GitHub Pages
- [ ] Create a GitHub repo (public or private with Pages enabled)
- [ ] Push `output/mobile/` contents to the repo's `gh-pages` branch (or `docs/` folder)
- [ ] Enable GitHub Pages in repo settings
- [ ] Verify the site loads at `https://username.github.io/repo-name/`
- [ ] Update `manifest.webmanifest` start_url and scope for the deployed URL
- [ ] Update service worker scope/paths if needed for the new base URL

### Phase 2: Real Phone Testing
- [ ] Open the deployed URL on actual iPhone (Safari)
- [ ] Open the deployed URL on actual Android phone (Chrome)
- [ ] Check: Does the page render correctly? (dark theme, gold accents, text readable)
- [ ] Check: Are fonts big enough to read? (minimum 16px for body text on mobile)
- [ ] Check: Can you tap sidebar items easily? (minimum 44px touch targets)
- [ ] Check: Does the sidebar open/close smoothly?
- [ ] Check: Can you select a text (e.g., Genesis) and see chapters load?
- [ ] Check: Does interlinear popup work on tap? (not hover — phones don't hover)
- [ ] Check: Does search work?
- [ ] Check: Does the reading pane scroll smoothly?

### Phase 3: PWA Install & Offline
- [ ] iPhone Safari: tap Share → "Add to Home Screen" — verify it installs
- [ ] Android Chrome: verify "Install app" banner appears (or use menu → Install)
- [ ] After install: open the app from home screen (should show splash, no browser chrome)
- [ ] Load a few texts while online (Genesis, Romans, Isaiah) to cache them
- [ ] Turn on Airplane Mode
- [ ] Reopen the app — verify it loads from cache
- [ ] Navigate to a previously loaded text — verify it works offline
- [ ] Navigate to a NOT-yet-loaded text — verify graceful error (not white screen)
- [ ] Check: app icon shows correctly on home screen
- [ ] Check: splash screen shows correctly on launch

### Phase 4: Mobile UI Fixes (based on phone testing)
- [ ] Fix any text that's too small (bump to 16px+ minimum)
- [ ] Fix any buttons/links that are hard to tap (44px minimum touch target)
- [ ] Fix any layout overflow (horizontal scroll = broken)
- [ ] Fix any popup/modal that doesn't fit phone screen
- [ ] Fix interlinear popups for touch (tap instead of hover)
- [ ] Add pull-to-refresh? (optional, nice UX)
- [ ] Test landscape orientation — does it still work?
- [ ] Ensure status bar color matches app theme (meta theme-color)
- [ ] Test notch/safe-area on iPhone (viewport-fit=cover already set)

### Phase 5: Service Worker & Caching Polish
- [ ] Verify SW caches the app shell (index.html, CSS, JS) on first load
- [ ] Verify SW caches data files when each text is first opened
- [ ] Add a "downloading..." indicator when loading a new text's data
- [ ] Handle SW updates gracefully (new version available → prompt to refresh)
- [ ] Test cache size — will 102 MB of data fit in phone storage?
- [ ] Add offline fallback page for texts not yet cached

### Phase 6: Build Pipeline Integration
- [ ] Add deploy script: `python deploy_mobile.py` (or `DEPLOY.bat`)
  - Builds mobile PWA
  - Pushes to GitHub Pages
  - One command from build to live on phone
- [ ] Update `release.py` to note the live URL in README
- [ ] Update LAUNCH.bat menu if needed

### Phase 7: Final Verification
- [ ] Full walkthrough on iPhone: install → browse 3+ texts → go offline → reopen
- [ ] Full walkthrough on Android: same
- [ ] Share URL with a test user if possible
- [ ] Update STATUS.md, MEMORY.md, COMMS with results

---

## ALTERNATIVE APPROACHES (if GitHub Pages doesn't work)

### Option B: Netlify (also free)
- Drag-and-drop deploy at netlify.com
- Same PWA approach, just different host
- Free tier: 100 GB bandwidth/month (more than enough)

### Option C: Cloudflare Pages (also free)
- Connect to GitHub repo, auto-deploys on push
- Unlimited bandwidth on free tier

### Option D: Native App Wrapper (Capacitor)
- Wraps the PWA into a real .apk (Android) or .ipa (iOS)
- More complex: needs Android Studio / Xcode
- Only needed if PWA approach doesn't meet requirements
- Save this for later — PWA should be sufficient

---

## NOTES
- The PWA already has: manifest.webmanifest, service worker, iOS meta tags, icons
- Current mobile build is ~102 MB total data — service worker caches on demand
- iPhone requires Safari for "Add to Home Screen" (Chrome on iOS can't install PWAs)
- The 67 MB desktop HTML is NOT suitable for phones — use the mobile PWA only
