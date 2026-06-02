@echo off
setlocal

echo ============================================
echo  LLM01 - LLM02 Demo Apps
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

set ROOT=%~dp0

:: Create virtual environment if it doesn't exist
if not exist "%ROOT%venv\Scripts\activate.bat" (
    echo [*] Creating virtual environment...
    %PYTHON% -m venv "%ROOT%venv"
)

echo [*] Activating virtual environment...
call "%ROOT%venv\Scripts\activate.bat"

echo [*] Installing requirements...
python -m pip install -r "%ROOT%LLM01 Prompt Injection\llm01_healthcare_prompt_injection_gandalf_levels_demo\llm01_healthcare_gandalf_demo\requirements.txt"
python -m pip install -r "%ROOT%LLM02 Sensitive Information Disclosure\llm02_healthcare_prompt_injection_demo\requirements.txt"

echo.
echo [*] Launching apps in the background...

start /B "" python -m streamlit run "%ROOT%LLM01 Prompt Injection\llm01_healthcare_prompt_injection_gandalf_levels_demo\llm01_healthcare_gandalf_demo\app.py" --server.port 8511 >NUL 2>&1
start /B "" python -m streamlit run "%ROOT%LLM02 Sensitive Information Disclosure\llm02_healthcare_prompt_injection_demo\app.py" --server.port 8512 >NUL 2>&1

echo.
echo [*] Apps launched:
echo     LLM01  http://localhost:8511
echo     LLM02  http://localhost:8512
echo.
