"""
release.py — Package a versioned release of the Ancient Texts Study App.

Usage:
  python release.py                    # Build + package with auto-incremented version
  python release.py --version 3.1.0    # Build + package with specific version
  python release.py --skip-build       # Package from existing release build

Creates:
  releases/AncientTextsStudy-vX.Y.Z/
    PC/
      AncientTextsStudy.html           # Desktop app (~65 MB single file)
      LAUNCH.bat                       # Windows launcher
      LAUNCH.command                   # macOS launcher
    Mobile/
      index.html + data/ + sw.js       # Mobile PWA (chunked for phones/tablets)
      LAUNCH-MOBILE.bat                # Windows: serve + open in browser
      LAUNCH-MOBILE.command            # macOS: serve + open in browser
    README.txt                         # User guide (covers both versions)
    CHANGELOG.txt                      # Version history
    FEEDBACK.txt                       # How to give feedback
    VERSION.txt
  releases/AncientTextsStudy-vX.Y.Z.zip   # Distributable archive
"""

import os
import sys
import json
import shutil
import zipfile
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE, "output")
RELEASE_DIR = os.path.join(BASE, "releases")
MANIFEST_PATH = os.path.join(BASE, "manifest.json")
RELEASE_HTML = os.path.join(OUTPUT_DIR, "AncientTextsStudy-Release.html")

# ── Version Management ───────────────────────────────────────

VERSION_FILE = os.path.join(BASE, "VERSION")

def get_current_version():
    """Read current version from VERSION file."""
    if os.path.exists(VERSION_FILE):
        return open(VERSION_FILE, "r").read().strip()
    return "3.0.0"

def increment_version(v):
    """Increment patch version: 3.0.0 -> 3.0.1"""
    parts = v.split(".")
    parts[-1] = str(int(parts[-1]) + 1)
    return ".".join(parts)

def save_version(v):
    """Save version to VERSION file."""
    with open(VERSION_FILE, "w") as f:
        f.write(v)


# ── Changelog ─────────────────────────────────────────────────

def generate_changelog(version):
    return f"""ANCIENT TEXTS STUDY APP — CHANGELOG
====================================

Version {version} ({datetime.now().strftime('%Y-%m-%d')})
--------------------------------------
NEW: Two release versions — PC and Mobile
- PC Release: Single-file desktop app (~65 MB HTML)
- Mobile Release: Progressive Web App with on-demand data loading
- Both contain identical content (74 texts, all interlinear, all study tools)

Content:
- 74 texts: 39 Old Testament + 27 New Testament + 8 Second Temple
- 895 study chapters with cross-references and divine council notes
- 31,101 verse-by-verse flow translations (formal equivalence)
- 444,339 interlinear words (Hebrew OT + Greek NT) with click-to-view popups
- 5,932 cross-references across OT, NT, ANE, and DSS sources
- 553 glossary terms (Hebrew, Greek, Aramaic)
- Ancient World Map with 60+ archaeological overlays and journey routes
- Bible Truth Matrix: 30+ worldviews compared across 13 doctrines
- Biblical + World History Timeline: 80+ events from Creation to modern era
- Study Trails: 4 curated thematic paths through Scripture
- Full-text search across all study content and flow translations
- Reading progress tracker with per-chapter checkboxes
- Resizable 3-column layout with keyboard shortcuts (PC)
- Learn Hebrew module (Aleph-Bet, vowels, roots, practice)
- Dark theme optimized for extended study sessions

Previous versions:
- v3.2.0: Full OT/NT coverage with all 39 OT Hebrew interlinear
- v3.0.0: Initial multi-text release
"""


# ── README ────────────────────────────────────────────────────

def generate_readme(version):
    return f"""ANCIENT TEXTS STUDY APP v{version}
{'=' * (28 + len(version))}

A comprehensive Bible study application for deep Scripture research
with original languages, cross-references, and ancient context.

This release includes TWO versions — same content, optimized for different devices.

=====================================================================
  PC VERSION  (in the PC/ folder)
=====================================================================

  Best for: Desktop and laptop computers
  How to run: Double-click PC/LAUNCH.bat (Windows) or PC/LAUNCH.command (macOS)

  - Single self-contained HTML file (~65 MB)
  - Opens instantly in any browser — no internet needed
  - 3-column resizable layout with keyboard shortcuts
  - Full interlinear popups, study tools, maps, timeline

=====================================================================
  MOBILE VERSION  (in the Mobile/ folder)
=====================================================================

  Best for: Phones, tablets, and sharing over slow connections
  How to run: Double-click Mobile/LAUNCH-MOBILE.bat (Windows)
              or Mobile/LAUNCH-MOBILE.command (macOS)

  - Progressive Web App — install to home screen for offline use
  - Same 74 texts and all study content as the PC version
  - Data loads on demand (fast startup, smaller initial download)
  - Touch-optimized navigation
  - Can also be hosted on any web server for remote access

  To use on your phone:
  1. Run LAUNCH-MOBILE on your computer (starts a local server)
  2. On your phone, open the URL shown in the terminal
     (your phone must be on the same WiFi network)
  3. Tap "Add to Home Screen" when prompted

=====================================================================
  WHAT'S INSIDE (BOTH VERSIONS)
=====================================================================

- 74 texts: 39 OT + 27 NT + 8 Second Temple / Apocryphal
- Every word of the Hebrew OT and Greek NT with interlinear popups
- Verse-by-verse flow translations with scholarly notes
- Cross-references linking passages across all texts
- Ancient World Map with archaeological sites and journey routes
- Bible Truth Matrix comparing 30+ worldviews to biblical teaching
- Biblical Timeline from Creation through modern history
- Curated Study Trails for thematic deep dives
- Full-text search across all content
- Reading progress tracker

KEYBOARD SHORTCUTS (PC version)
--------------------------------
  Ctrl+K     Search texts and verses
  Alt+H      Toggle sidebar
  Alt+F      Fullscreen reading mode
  Alt+L      Toggle reading pane
  Alt+Left   Previous chapter
  Alt+Right  Next chapter
  ?          Show all shortcuts
  Esc        Close any overlay

SYSTEM REQUIREMENTS
-------------------
- Any modern web browser (Chrome, Firefox, Edge, Safari)
- No internet connection needed after first load

CREDITS
-------
Built by Seaver Hall
Powered by divine council theology, Second Temple scholarship,
and a deep love for the Word of God.

"The heavens declare the glory of God,
 and the sky above proclaims his handiwork." — Psalm 19:1 (ESV)
"""


# ── Feedback Guide ────────────────────────────────────────────

def generate_feedback():
    return """HOW TO GIVE FEEDBACK
====================

Thank you for testing the Ancient Texts Study App! Your feedback
is incredibly valuable in making this the best Bible study tool possible.

WAYS TO GIVE FEEDBACK
---------------------

1. USAGE DATA (Most Helpful!)
   - Open the app
   - Use it naturally — study, search, explore
   - Click "App Info & Analytics" in the sidebar
   - Scroll to "Your Usage Summary"
   - Click "Export Usage Data (JSON)"
   - Send the downloaded JSON file back to us

2. BUG REPORTS
   Please include:
   - What you were doing when the bug occurred
   - What you expected to happen
   - What actually happened
   - Your browser name and version
   - Screenshot if possible

3. FEATURE REQUESTS
   Tell us:
   - What you wish the app could do
   - How you'd use the feature in your study
   - How important it is to you (nice-to-have vs essential)

4. GENERAL IMPRESSIONS
   - What do you love?
   - What confuses you?
   - What feels missing?
   - Would you recommend this to others?

WHAT WE'RE LOOKING FOR
----------------------
- Which texts do you spend the most time in?
- Is the interlinear (original language) feature useful?
- Do you use the cross-references?
- Is the Bible Truth Matrix helpful?
- Is the timeline useful?
- How do you feel about the dark theme?
- Is navigation intuitive?
- Does search find what you're looking for?

Thank you for being part of building something meaningful!
"""


# ── Build & Package ──────────────────────────────────────────

def main():
    skip_build = "--skip-build" in sys.argv
    version = None

    # Parse args
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--version" and i + 1 < len(args):
            version = args[i + 1]
            i += 2
        else:
            i += 1

    # Determine version
    current = get_current_version()
    if version is None:
        version = increment_version(current)

    print("=" * 60)
    print("  ANCIENT TEXTS STUDY APP — Release Packager")
    print(f"  Version: {version}")
    print(f"  Date:    {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    # Step 1: Build in release mode (desktop + mobile)
    if not skip_build:
        print("\n[1/7] Building release version...")
        import subprocess
        ret = subprocess.call([sys.executable, os.path.join(BASE, "build.py"), "--release"])
        if ret != 0:
            print("ERROR: Desktop build failed!")
            sys.exit(1)
        print("\n  Building mobile PWA...")
        ret = subprocess.call([sys.executable, os.path.join(BASE, "build_mobile.py")])
        if ret != 0:
            print("ERROR: Mobile build failed!")
            sys.exit(1)
    else:
        print("\n[1/7] Skipping build (--skip-build)")

    # Verify release HTML exists
    if not os.path.exists(RELEASE_HTML):
        print(f"ERROR: Release HTML not found at {RELEASE_HTML}")
        print("Run without --skip-build first.")
        sys.exit(1)

    # Step 2: Create release folder
    release_name = f"AncientTextsStudy-v{version}"
    release_path = os.path.join(RELEASE_DIR, release_name)
    print(f"\n[2/7] Creating release folder: {release_name}/")
    if os.path.exists(release_path):
        shutil.rmtree(release_path)
    os.makedirs(release_path, exist_ok=True)

    # ── Step 3: PC Release ──────────────────────────────────────
    pc_path = os.path.join(release_path, "PC")
    os.makedirs(pc_path, exist_ok=True)
    print("[3/7] Assembling PC Release...")

    # Copy the app
    dest_html = os.path.join(pc_path, "AncientTextsStudy.html")
    shutil.copy2(RELEASE_HTML, dest_html)
    html_size = os.path.getsize(dest_html)
    print(f"  - PC/AncientTextsStudy.html ({html_size / 1024 / 1024:.1f} MB)")

    # Windows launcher
    with open(os.path.join(pc_path, "LAUNCH.bat"), "w") as f:
        f.write('@echo off\r\n')
        f.write('echo Opening Ancient Texts Study App (PC)...\r\n')
        f.write('start "" "%~dp0AncientTextsStudy.html"\r\n')
    print("  - PC/LAUNCH.bat (Windows)")

    # macOS launcher
    mac_launcher = os.path.join(pc_path, "LAUNCH.command")
    with open(mac_launcher, "w") as f:
        f.write('#!/bin/bash\n')
        f.write('cd "$(dirname "$0")"\n')
        f.write('open AncientTextsStudy.html\n')
    os.chmod(mac_launcher, 0o755)
    print("  - PC/LAUNCH.command (macOS)")

    # ── Step 4: Mobile Release ──────────────────────────────────
    mobile_src = os.path.join(OUTPUT_DIR, "mobile")
    mobile_path = os.path.join(release_path, "Mobile")
    mobile_size = 0
    file_count = 0
    if os.path.isdir(mobile_src):
        print(f"\n[4/7] Assembling Mobile Release...")
        shutil.copytree(mobile_src, mobile_path, dirs_exist_ok=True)

        # Mobile Windows launcher (starts a local server, auto-detects IP)
        with open(os.path.join(mobile_path, "LAUNCH-MOBILE.bat"), "w") as f:
            f.write('@echo off\r\n')
            f.write('title Ancient Texts Study App - Mobile Server\r\n')
            f.write('cd /d "%~dp0"\r\n')
            f.write('echo.\r\n')
            f.write('echo   ============================================\r\n')
            f.write('echo     ANCIENT TEXTS STUDY APP - Mobile Server\r\n')
            f.write('echo   ============================================\r\n')
            f.write('echo.\r\n')
            f.write('\r\n')
            f.write(':: Find local WiFi IP address\r\n')
            f.write('set "LOCAL_IP="\r\n')
            f.write('for /f "tokens=2 delims=:" %%a in (\'ipconfig ^| findstr /C:"IPv4" ^| findstr /V "127.0.0"\') do (\r\n')
            f.write('    if not defined LOCAL_IP (\r\n')
            f.write('        for /f "tokens=*" %%b in ("%%a") do set "LOCAL_IP=%%b"\r\n')
            f.write('    )\r\n')
            f.write(')\r\n')
            f.write('\r\n')
            f.write('where python >nul 2>&1\r\n')
            f.write('if %errorlevel%==0 (\r\n')
            f.write('    echo   On this PC:    http://localhost:8080\r\n')
            f.write('    if defined LOCAL_IP (\r\n')
            f.write('        echo   On your phone: http://%LOCAL_IP%:8080\r\n')
            f.write('    ) else (\r\n')
            f.write('        echo   On your phone: http://YOUR_PC_IP:8080\r\n')
            f.write('    )\r\n')
            f.write('    echo.\r\n')
            f.write('    echo   Your phone must be on the same WiFi network.\r\n')
            f.write('    echo   Press Ctrl+C to stop the server.\r\n')
            f.write('    echo.\r\n')
            f.write('    start "" "http://localhost:8080"\r\n')
            f.write('    python -m http.server 8080\r\n')
            f.write(') else (\r\n')
            f.write('    echo   [ERROR] Python not found!\r\n')
            f.write('    echo   Install Python 3 from https://python.org\r\n')
            f.write('    echo   Or open index.html directly in a browser.\r\n')
            f.write('    pause\r\n')
            f.write(')\r\n')
        print("  - Mobile/LAUNCH-MOBILE.bat (Windows)")

        # Mobile macOS launcher
        mac_mobile = os.path.join(mobile_path, "LAUNCH-MOBILE.command")
        with open(mac_mobile, "w") as f:
            f.write('#!/bin/bash\n')
            f.write('cd "$(dirname "$0")"\n')
            f.write('echo ""\n')
            f.write('echo "  ============================================"\n')
            f.write('echo "    ANCIENT TEXTS STUDY APP — Mobile Server"\n')
            f.write('echo "  ============================================"\n')
            f.write('echo ""\n')
            f.write('echo "  Open in your browser:  http://localhost:8080"\n')
            f.write('echo "  On your phone:         http://$(ipconfig getifaddr en0):8080"\n')
            f.write('echo ""\n')
            f.write('echo "  Press Ctrl+C to stop the server."\n')
            f.write('echo ""\n')
            f.write('open "http://localhost:8080"\n')
            f.write('python3 -m http.server 8080\n')
        os.chmod(mac_mobile, 0o755)
        print("  - Mobile/LAUNCH-MOBILE.command (macOS)")

        mobile_size = sum(
            os.path.getsize(os.path.join(r, f))
            for r, _, files in os.walk(mobile_path) for f in files
        )
        file_count = sum(len(f) for _, _, f in os.walk(mobile_path))
        print(f"  - Mobile/ total: {mobile_size / 1024 / 1024:.1f} MB, {file_count} files")
    else:
        print(f"\n[4/7] No mobile build found — skipping (run build_mobile.py first)")

    # ── Step 5: Shared docs at root ─────────────────────────────
    print(f"\n[5/7] Writing release docs...")

    # README
    with open(os.path.join(release_path, "README.txt"), "w") as f:
        f.write(generate_readme(version))
    print("  - README.txt")

    # Changelog
    with open(os.path.join(release_path, "CHANGELOG.txt"), "w") as f:
        f.write(generate_changelog(version))
    print("  - CHANGELOG.txt")

    # Feedback guide
    with open(os.path.join(release_path, "FEEDBACK.txt"), "w") as f:
        f.write(generate_feedback())
    print("  - FEEDBACK.txt")

    # Version file
    with open(os.path.join(release_path, "VERSION.txt"), "w") as f:
        f.write(f"Ancient Texts Study App\nVersion: {version}\nBuild Date: {datetime.now().strftime('%Y-%m-%d')}\n")
    print("  - VERSION.txt")

    # Step 6: Create ZIP
    zip_path = os.path.join(RELEASE_DIR, f"{release_name}.zip")
    print(f"\n[6/7] Creating ZIP archive: {release_name}.zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(release_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.join(release_name, os.path.relpath(file_path, release_path))
                zf.write(file_path, arcname)
    zip_size = os.path.getsize(zip_path)
    print(f"  ZIP size: {zip_size / 1024 / 1024:.1f} MB")

    # Step 7: Save version
    save_version(version)
    print(f"\n[7/7] Version saved: {version}")

    # Summary
    pc_size_str = f"{html_size / 1024 / 1024:.1f} MB"
    has_mobile = os.path.isdir(mobile_path)

    print(f"\n{'=' * 60}")
    print(f"  RELEASE PACKAGED SUCCESSFULLY")
    print(f"  Version:    {version}")
    print(f"  PC Release: {pc_size_str}")
    if has_mobile:
        print(f"  Mobile:     {mobile_size / 1024 / 1024:.1f} MB ({file_count} files)")
    else:
        print(f"  Mobile:     NOT INCLUDED (build mobile first)")
    print(f"  ZIP:        {zip_size / 1024 / 1024:.1f} MB")
    print(f"  Location:   {release_path}")
    print(f"{'=' * 60}")
    print(f"\nReady to distribute! Share the ZIP file with testers.")


if __name__ == "__main__":
    main()
