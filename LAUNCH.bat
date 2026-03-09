@echo off
title Ancient Texts Study App
cd /d "%~dp0"
color 0E

:MENU
cls
echo.
echo   ============================================================
echo                  ANCIENT TEXTS STUDY APP
echo           A Scholarly Study of Sacred ^& Ancient Writings
echo   ============================================================
echo.
echo     [1]  Launch App  (browser)
echo     [2]  Launch App  (Electron desktop)
echo     [3]  Launch App  (with Hallelujah AI)
echo     [4]  Build Only  (rebuild from source)
echo     [5]  Build All   (desktop + release + mobile)
echo     [6]  Sync to Google Drive
echo     [7]  Run Builder's Council  (AI agents)
echo     [8]  Exit
echo.
echo   ============================================================
set /p choice="   Choose [1-8]: "

if "%choice%"=="1" goto BROWSER
if "%choice%"=="2" goto ELECTRON
if "%choice%"=="3" goto AI
if "%choice%"=="4" goto BUILD
if "%choice%"=="5" goto BUILD_ALL
if "%choice%"=="6" goto SYNC
if "%choice%"=="7" goto COUNCIL
if "%choice%"=="8" exit /b 0
echo   Invalid choice.
timeout /t 2 >nul
goto MENU

:: ────────────────────────────────────────────────────────────
:SETUP_VENV
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
) else (
    echo [setup] Creating Python environment...
    python -m venv venv
    if errorlevel 1 (
        echo [ERROR] Python not found. Install Python 3.10+ from python.org
        pause
        goto MENU
    )
    call venv\Scripts\activate.bat
    echo [setup] Installing dependencies...
    pip install -r requirements.txt
    echo.
)
exit /b 0

:: ────────────────────────────────────────────────────────────
:ENSURE_BUILD
if not exist "output\AncientTextsStudy.html" (
    echo [build] No build found. Building now...
    call :SETUP_VENV
    python build.py
    echo.
)
exit /b 0

:: ────────────────────────────────────────────────────────────
:BROWSER
echo.
echo [launch] Opening in browser...
call :ENSURE_BUILD
start "" "output\AncientTextsStudy.html"
echo.
echo   App opened in your default browser.
echo.
pause
goto MENU

:: ────────────────────────────────────────────────────────────
:ELECTRON
echo.
where node >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Node.js not found. Install from https://nodejs.org/
    pause
    goto MENU
)
if not exist "electron\node_modules\electron" (
    echo [setup] Installing Electron dependencies...
    cd electron && npm install && cd ..
    echo.
)
call :ENSURE_BUILD
echo [launch] Starting Electron desktop app...
cd electron
npx electron .
cd ..
goto MENU

:: ────────────────────────────────────────────────────────────
:AI
echo.

:: Find Python
set "PYTHON_DIR=C:\Users\User\AppData\Local\Programs\Python\Python312"
set "PYTHON=%PYTHON_DIR%\python.exe"
set "PIP=%PYTHON_DIR%\Scripts\pip.exe"
if not exist "%PYTHON%" (
    where python >nul 2>&1
    if errorlevel 1 (
        echo [ERROR] Python not found!
        pause
        goto MENU
    )
    set "PYTHON=python"
    set "PIP=pip"
)

:: Find Ollama
set "OLLAMA_EXE=C:\Users\User\AppData\Local\Programs\Ollama\ollama.exe"
if not exist "%OLLAMA_EXE%" (
    where ollama >nul 2>&1
    if errorlevel 1 (
        echo [WARNING] Ollama not installed. Chat features unavailable.
        echo           Download from: https://ollama.com/download
    ) else (
        set "OLLAMA_EXE=ollama"
    )
)

:: Install dependencies
echo [setup] Checking dependencies...
"%PIP%" install -q --upgrade pywebview fastapi uvicorn httpx pyyaml 2>nul

:: Kill stale server on port 8741
for /f "tokens=5" %%p in ('netstat -ano ^| findstr ":8741" ^| findstr "LISTENING"') do (
    echo [startup] Killing stale server PID %%p...
    taskkill /PID %%p /F >nul 2>&1
    timeout /t 2 /nobreak >nul
)

:: Start Ollama if needed
curl -s http://localhost:11434/api/tags >nul 2>&1
if errorlevel 1 (
    echo [startup] Starting Ollama...
    start /min "" "%OLLAMA_EXE%" serve
    timeout /t 5 /nobreak >nul
)

:: Ensure Hallelujah model
curl -s http://localhost:11434/api/tags 2>nul | findstr /i "hallelujah" >nul 2>&1
if errorlevel 1 (
    echo [setup] Pulling base model + creating Hallelujah model...
    "%OLLAMA_EXE%" pull qwen2.5:7b
    "%OLLAMA_EXE%" create hallelujah -f "%~dp0hai\Modelfile"
)

echo.
echo [launch] Starting Ancient Texts + Hallelujah AI...
"%PYTHON%" hai\app.py
echo.
echo [shutdown] App closed.
pause
goto MENU

:: ────────────────────────────────────────────────────────────
:BUILD
echo.
call :SETUP_VENV
echo [build] Building study content...
python build.py
echo.
if errorlevel 1 (
    echo [!] BUILD FAILED
) else (
    echo [OK] Build complete!
)
echo.
pause
goto MENU

:: ────────────────────────────────────────────────────────────
:BUILD_ALL
echo.
call :SETUP_VENV
echo [build] Building ALL versions (desktop + release + mobile)...
echo.
echo   [1/3] Desktop build...
python build.py
if errorlevel 1 (
    echo   [FAILED] Desktop build failed!
    pause
    goto MENU
)
echo   [2/3] Release build...
python build.py --release
if errorlevel 1 (
    echo   [FAILED] Release build failed!
    pause
    goto MENU
)
echo   [3/3] Mobile PWA build...
python build_mobile.py
if errorlevel 1 (
    echo   [FAILED] Mobile build failed!
    pause
    goto MENU
)
echo.
echo   [OK] All builds complete!
echo       Desktop:  output\AncientTextsStudy.html
echo       Release:  output\AncientTextsStudy-Release.html
echo       Mobile:   output\mobile\index.html
echo.
pause
goto MENU

:: ────────────────────────────────────────────────────────────
:SYNC
echo.
echo ============================================
echo   SYNC TO GOOGLE DRIVE
echo   %date% %time%
echo ============================================
echo.

set "LOCAL=C:\Users\User\Desktop\ANCIENT_TEXTS Study App"
set "CLOUD=E:\My Drive\ANCIENT_TEXTS Study App"
set "SKIP=/XD venv __pycache__ .git node_modules archive /XF *.pyc desktop.ini /R:0 /W:0 /NP"

echo   Desktop -^> Google Drive
robocopy "%LOCAL%" "%CLOUD%" /MIR %SKIP%
if %ERRORLEVEL% LEQ 3 (echo   [OK] Google Drive synced.) else (echo   [!] Errors - code %ERRORLEVEL%)
echo.
pause
goto MENU

:: ────────────────────────────────────────────────────────────
:COUNCIL
echo.
call :SETUP_VENV
echo.
echo   Starting full council pipeline...
echo   ORACLE -^> SCRIBE -^> LECTOR -^> ARBITER -^> ARCHITECT
echo.
echo   Press Ctrl+C at any time to stop.
echo.
python agents/run_council.py
echo.
echo   COUNCIL SESSION COMPLETE
echo   Check agents/reports/ for full details
echo.
pause
goto MENU
