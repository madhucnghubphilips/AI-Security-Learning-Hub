#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

echo "[1/2] Installing Python requirements..."
if command -v python3 >/dev/null 2>&1; then
	python3 -m pip install -r requirements.txt
else
	python -m pip install -r requirements.txt
fi

echo "[2/2] Starting Streamlit server..."
if command -v streamlit >/dev/null 2>&1; then
	streamlit run app.py
elif command -v python3 >/dev/null 2>&1; then
	python3 -m streamlit run app.py
else
	python -m streamlit run app.py
fi
