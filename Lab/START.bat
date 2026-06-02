@echo off
setlocal EnableExtensions EnableDelayedExpansion
cd /d "%~dp0"

set "APP_URL=http://localhost:8000/"
set "VENV_DIR=%CD%\.venv"
set "PYTHON_EXE=%VENV_DIR%\Scripts\python.exe"

echo Philips Healthcare AI Demo - RAG Edition
echo ==========================================
echo.

echo [1/6] Checking Python...
set "BASE_PYTHON=python"
python --version >nul 2>nul
if errorlevel 1 (
  py -3 --version >nul 2>nul
  if not errorlevel 1 (
    set "BASE_PYTHON=py -3"
  )
)

%BASE_PYTHON% --version >nul 2>nul
if errorlevel 1 (
  echo Python was not found.
  echo Install Python 3.10 or newer from https://www.python.org/downloads/
  echo Make sure "Add python.exe to PATH" is selected, then run START.bat again.
  pause
  exit /b 1
)

echo [2/6] Preparing local virtual environment...
if not exist "%PYTHON_EXE%" (
  %BASE_PYTHON% -m venv "%VENV_DIR%"
  if errorlevel 1 (
    echo Failed to create virtual environment at "%VENV_DIR%".
    pause
    exit /b 1
  )
) else (
  echo Existing virtual environment found.
)

echo [3/6] Installing Python dependencies inside .venv...
"%PYTHON_EXE%" -m pip install --upgrade pip
if errorlevel 1 (
  echo Failed to upgrade pip in the virtual environment.
  pause
  exit /b 1
)

"%PYTHON_EXE%" -m pip install -r app\requirements.txt
if errorlevel 1 (
  echo Failed to install Python dependencies.
  pause
  exit /b 1
)

echo [4/6] Checking Ollama...
set "OLLAMA_EXE="
for /f "delims=" %%O in ('where ollama 2^>nul') do (
  if not defined OLLAMA_EXE set "OLLAMA_EXE=%%O"
)
if not defined OLLAMA_EXE (
  echo Ollama was not found.
  where winget >nul 2>nul
  if not errorlevel 1 (
    set /p INSTALL_OLLAMA="Install Ollama now using winget? (Y/N): "
    if /I "!INSTALL_OLLAMA!"=="Y" (
      winget install --id Ollama.Ollama -e --accept-package-agreements --accept-source-agreements
    )
  )
  for /f "delims=" %%O in ('where ollama 2^>nul') do (
    if not defined OLLAMA_EXE set "OLLAMA_EXE=%%O"
  )
  if not defined OLLAMA_EXE (
    if exist "%LOCALAPPDATA%\Programs\Ollama\ollama.exe" (
      set "OLLAMA_EXE=%LOCALAPPDATA%\Programs\Ollama\ollama.exe"
    )
  )
)

"%OLLAMA_EXE%" --version >nul 2>nul
if errorlevel 1 (
  echo Install Ollama from https://ollama.com and run START.bat again.
  pause
  exit /b 1
)

"%OLLAMA_EXE%" list >nul 2>nul
if errorlevel 1 (
  echo Starting Ollama service...
  start "Ollama" /min "%OLLAMA_EXE%" serve
  set /a OLLAMA_WAIT=0
  call :WAIT_FOR_OLLAMA
  if errorlevel 1 (
    echo Ollama did not become ready within 30 seconds.
    echo Start Ollama manually and run START.bat again.
    pause
    exit /b 1
  )
)

echo [5/6] Preparing Ollama models...
"%OLLAMA_EXE%" list | findstr /I /C:"dolphin-ctf" >nul
if errorlevel 1 (
  echo Creating dolphin-ctf model from Modelfile-ctf...
  "%OLLAMA_EXE%" create dolphin-ctf -f Modelfile-ctf
  if errorlevel 1 (
    echo Failed to create dolphin-ctf model.
    pause
    exit /b 1
  )
) else (
  echo dolphin-ctf model already exists.
)

"%OLLAMA_EXE%" list | findstr /I /C:"nomic-embed-text" >nul
if errorlevel 1 (
  echo Pulling nomic-embed-text embedding model...
  "%OLLAMA_EXE%" pull nomic-embed-text
  if errorlevel 1 (
    echo Failed to pull nomic-embed-text.
    pause
    exit /b 1
  )
) else (
  echo nomic-embed-text model already exists.
)

echo [6/6] Starting demo server...
echo.
echo Open this URL in your browser:
echo   %APP_URL%
echo.
echo Keep this window open. Press Ctrl+C to stop the server.
echo.

set "PYTHONDONTWRITEBYTECODE=1"
"%PYTHON_EXE%" -m uvicorn app.rag_server:app --host 127.0.0.1 --port 8000
set "SERVER_EXIT=%ERRORLEVEL%"

echo.
echo Server stopped.
pause
exit /b %SERVER_EXIT%

:WAIT_FOR_OLLAMA
set /a OLLAMA_WAIT=0
:WAIT_FOR_OLLAMA_LOOP
timeout /t 2 /nobreak >nul
"%OLLAMA_EXE%" list >nul 2>nul
if not errorlevel 1 exit /b 0
set /a OLLAMA_WAIT+=1
if !OLLAMA_WAIT! GEQ 15 exit /b 1
goto WAIT_FOR_OLLAMA_LOOP
