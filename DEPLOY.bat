@echo off
title Ancient Texts — Build + Deploy
cd /d "%~dp0"
color 0E

echo.
echo   ============================================================
echo        ANCIENT TEXTS STUDY APP — BUILD ^& DEPLOY
echo   ============================================================
echo.
echo   This will:
echo     1. Build desktop, release, and mobile versions
echo     2. Commit changes to main branch
echo     3. Push to GitHub (main)
echo     4. Deploy mobile PWA to GitHub Pages (gh-pages)
echo.
echo   Press any key to start, or Ctrl+C to cancel...
pause >nul

:: ── Activate venv ──
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
) else (
    echo [ERROR] No venv found. Run LAUNCH.bat first to set up.
    pause
    exit /b 1
)

:: ── Step 1: Desktop build ──
echo.
echo   [1/6] Building desktop version...
python build.py
if errorlevel 1 (
    echo   [FAILED] Desktop build failed!
    pause
    exit /b 1
)
echo         Done.

:: ── Step 2: Release build ──
echo   [2/6] Building release version...
python build.py --release
if errorlevel 1 (
    echo   [FAILED] Release build failed!
    pause
    exit /b 1
)
echo         Done.

:: ── Step 3: Mobile PWA build ──
echo   [3/6] Building mobile PWA...
python build_mobile.py
if errorlevel 1 (
    echo   [FAILED] Mobile build failed!
    pause
    exit /b 1
)
echo         Done.

:: ── Step 4: Commit to main ──
echo   [4/6] Committing changes to main...
git add -A
git diff --cached --quiet
if errorlevel 1 (
    set /p COMMIT_MSG="   Commit message: "
    git commit -m "%COMMIT_MSG%"
    if errorlevel 1 (
        echo   [FAILED] Git commit failed!
        pause
        exit /b 1
    )
    echo         Committed.
) else (
    echo         No changes to commit.
)

:: ── Step 5: Push main ──
echo   [5/6] Pushing to GitHub (main)...
git push origin main
if errorlevel 1 (
    echo   [FAILED] Push to main failed!
    pause
    exit /b 1
)
echo         Done.

:: ── Step 6: Deploy mobile to gh-pages ──
echo   [6/6] Deploying mobile PWA to GitHub Pages...

:: Use a temp directory to avoid polluting the working tree
set DEPLOY_TMP=%TEMP%\ancient-texts-deploy-%RANDOM%
mkdir "%DEPLOY_TMP%"
cd /d "%DEPLOY_TMP%"

git init >nul 2>&1
git checkout --orphan gh-pages >nul 2>&1
xcopy /E /I /Q /Y "%~dp0output\mobile\*" . >nul 2>&1
git add -A >nul 2>&1
git commit -m "Deploy mobile PWA" >nul 2>&1
git remote add origin https://github.com/Seaverhall10/ancient-texts-app.git >nul 2>&1
git push origin gh-pages --force >nul 2>&1

if errorlevel 1 (
    cd /d "%~dp0"
    rmdir /S /Q "%DEPLOY_TMP%" 2>nul
    echo   [FAILED] gh-pages deploy failed!
    pause
    exit /b 1
)

cd /d "%~dp0"
rmdir /S /Q "%DEPLOY_TMP%" 2>nul
echo         Done.

echo.
echo   ============================================================
echo        ALL BUILDS + DEPLOY COMPLETE
echo   ============================================================
echo.
echo     Desktop:  output\AncientTextsStudy.html
echo     Release:  output\AncientTextsStudy-Release.html
echo     Mobile:   output\mobile\index.html
echo.
echo     GitHub:   https://github.com/Seaverhall10/ancient-texts-app
echo     Live:     https://seaverhall10.github.io/ancient-texts-app/
echo.
pause
