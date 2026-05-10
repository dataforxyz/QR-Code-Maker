@echo off
echo Building QR Code Maker...
echo.

REM Check if uv is available
uv --version >nul 2>&1
if errorlevel 1 (
    echo Error: uv is not installed or not in PATH
    echo Please install uv first: https://github.com/astral-sh/uv
    pause
    exit /b 1
)

REM Install dependencies if needed
echo Installing dependencies...
uv sync --group dev

REM Run the build script
echo.
echo Running build script...
uv run python build.py

echo.
echo Build process completed!
pause
