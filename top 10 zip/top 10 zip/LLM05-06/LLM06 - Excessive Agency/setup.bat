@echo off
setlocal

cd /d "%~dp0"

echo [1/2] Installing Python requirements...
where py >nul 2>nul
if %errorlevel%==0 (
	py -m pip install -r requirements.txt
) else (
	python -m pip install -r requirements.txt
)

if errorlevel 1 (
	echo Failed to install dependencies.
	exit /b 1
)

echo [2/2] Starting Streamlit server...
streamlit run app.py

if errorlevel 1 (
	echo Streamlit command failed. Trying python module fallback...
	where py >nul 2>nul
	if %errorlevel%==0 (
		py -m streamlit run app.py
	) else (
		python -m streamlit run app.py
	)
)
