#!/bin/bash

echo "============================================"
echo " LLM05 - LLM06 Demo Apps"
echo "============================================"

# Detect Python executable
if command -v python3 &>/dev/null; then
    PYTHON=python3
elif command -v python &>/dev/null; then
    PYTHON=python
else
    echo "ERROR: No Python installation found."
    echo "Please install Python from https://www.python.org/"
    exit 1
fi

echo "[*] Using: $PYTHON"
$PYTHON --version
echo ""

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/venv"

if [ ! -f "$VENV_DIR/bin/activate" ]; then
    echo "[*] Creating virtual environment..."
    $PYTHON -m venv "$VENV_DIR"
fi

echo "[*] Activating virtual environment..."
source "$VENV_DIR/bin/activate"

echo "[*] Installing requirements..."
python -m pip install -r "$SCRIPT_DIR/LLM05/llm05_fixed/requirements.txt"
python -m pip install -r "$SCRIPT_DIR/LLM06 - Excessive Agency/llm06_excessive_agency_demo/requirements.txt"

echo ""
echo "[*] Launching apps in the background..."

python -m streamlit run "$SCRIPT_DIR/LLM05/llm05_fixed/app.py" --server.port 8515 &
python -m streamlit run "$SCRIPT_DIR/LLM06 - Excessive Agency/llm06_excessive_agency_demo/app.py" --server.port 8516 &

echo ""
echo "[*] Apps launched:"
echo "    LLM05  http://localhost:8515"
echo "    LLM06  http://localhost:8516"
echo ""
