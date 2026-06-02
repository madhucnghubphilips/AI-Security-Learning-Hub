@echo off
setlocal

echo ============================================
echo  LLM07 - LLM10 Demo Apps
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
python -m pip install -r "%ROOT%LLM07\llm07_system_prompt_leakage_realtime_demo\requirements.txt"
python -m pip install -r "%ROOT%LLM8 Vector and Embedding Weaknesses\llm08_streamlit_ollama_demo\requirements.txt"
python -m pip install -r "%ROOT%LLM09 Misinformation\llm09\requirements.txt"
python -m pip install -r "%ROOT%LLM10 - Unbounded Consumption\llm10_unbounded_consumption_streamlit_demo\requirements.txt"

echo.
echo [*] Launching apps in the background...

start /B "" python -m streamlit run "%ROOT%LLM07\llm07_system_prompt_leakage_realtime_demo\app.py" --server.port 8517 >NUL 2>&1
start /B "" python -m streamlit run "%ROOT%LLM8 Vector and Embedding Weaknesses\llm08_streamlit_ollama_demo\app.py" --server.port 8518 >NUL 2>&1
start /B "" python -m streamlit run "%ROOT%LLM09 Misinformation\llm09\app.py" --server.port 8519 >NUL 2>&1
start /B "" python -m streamlit run "%ROOT%LLM10 - Unbounded Consumption\llm10_unbounded_consumption_streamlit_demo\app.py" --server.port 8520 >NUL 2>&1

echo.
echo [*] Apps launched:
echo     LLM07  http://localhost:8517
echo     LLM08  http://localhost:8518
echo     LLM09  http://localhost:8519
echo     LLM10  http://localhost:8520
echo.
