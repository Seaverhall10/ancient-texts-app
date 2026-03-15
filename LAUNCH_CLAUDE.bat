@echo off
cd /d "%~dp0"
echo Starting Claude Code in: %cd%
echo.
npx -y @anthropic-ai/claude-code
