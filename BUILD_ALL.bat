@echo off
title Ancient Texts — Build All
cd /d "%~dp0"
color 0E

echo.
echo   ============================================================
echo          ANCIENT TEXTS STUDY APP — FULL BUILD
echo   ============================================================
echo.

:: ── Activate venv ──
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
) else (
    echo [ERROR] No venv found. Run LAUNCH.bat first to set up.
    pause
    exit /b 1
)

:: ── Step 1: Desktop build ──
echo   [1/3] Building desktop version...
python build.py
if errorlevel 1 (
    echo.
    echo   [FAILED] Desktop build failed!
    pause
    exit /b 1
)
echo         Done.
echo.

:: ── Step 2: Release build ──
echo   [2/3] Building release version...
python build.py --release
if errorlevel 1 (
    echo.
    echo   [FAILED] Release build failed!
    pause
    exit /b 1
)
echo         Done.
echo.

:: ── Step 3: Mobile PWA build ──
echo   [3/3] Building mobile PWA...
python build_mobile.py
if errorlevel 1 (
    echo.
    echo   [FAILED] Mobile build failed!
    pause
    exit /b 1
)
echo         Done.
echo.

echo   ============================================================
echo          ALL BUILDS COMPLETE
echo   ============================================================
echo.
echo     Desktop:  output\AncientTextsStudy.html
echo     Release:  output\AncientTextsStudy-Release.html
echo     Mobile:   output\mobile\index.html
echo.
pause
