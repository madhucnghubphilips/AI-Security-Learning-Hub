@echo off
setlocal

echo ============================================
echo  LLM09 - Misinformation Demo
echo ============================================

:: Detect Python executable (python3 > python > py launcher)
set PYTHON=
where python3 >nul 2>&1
if not errorlevel 1 set PYTHON=python3

if not defined PYTHON (
    where python >nul 2>&1
    if not errorlevel 1 set PYTHON=python
)

if not defined PYTHON (
    where py >nul 2>&1
    if not errorlevel 1 set PYTHON=py
)

if not defined PYTHON (
    echo ERROR: No Python installation found.
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

echo [*] Using: %PYTHON%
%PYTHON% --version
echo.

echo [*] Installing requirements...
%PYTHON% -m pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install requirements.
    pause
    exit /b 1
)

echo.
echo [*] Starting Streamlit app...
%PYTHON% -m streamlit run app.py

pause
