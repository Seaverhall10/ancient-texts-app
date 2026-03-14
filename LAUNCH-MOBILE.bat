@echo off
title Ancient Texts Study App - Mobile Server
cd /d "%~dp0"
echo.
echo   ============================================
echo     ANCIENT TEXTS STUDY APP - Mobile Server
echo   ============================================
echo.

:: Find local WiFi IP address
set "LOCAL_IP="
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /C:"IPv4" ^| findstr /V "127.0.0"') do (
    if not defined LOCAL_IP (
        for /f "tokens=*" %%b in ("%%a") do set "LOCAL_IP=%%b"
    )
)

where python >nul 2>&1
if %errorlevel%==0 (
    echo   On this PC:    http://localhost:8080
    if defined LOCAL_IP (
        echo   On your phone: http://%LOCAL_IP%:8080
    ) else (
        echo   On your phone: http://YOUR_PC_IP:8080
    )
    echo.
    echo   Your phone must be on the same WiFi network.
    echo   Press Ctrl+C to stop the server.
    echo.
    start "" "http://localhost:8080"
    python -m http.server 8080
) else (
    echo   [ERROR] Python not found!
    echo   Install Python 3 from https://python.org
    echo   Or open index.html directly in a browser.
    pause
)
