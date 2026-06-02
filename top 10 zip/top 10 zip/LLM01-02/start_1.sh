#!/bin/bash

echo "============================================"
echo " LLM01 - LLM02 Demo Apps"
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
python -m pip install -r "$SCRIPT_DIR/LLM01 Prompt Injection/llm01_healthcare_prompt_injection_gandalf_levels_demo/llm01_healthcare_gandalf_demo/requirements.txt"
python -m pip install -r "$SCRIPT_DIR/LLM02 Sensitive Information Disclosure/llm02_healthcare_prompt_injection_demo/requirements.txt"

echo ""
echo "[*] Launching apps in the background..."

python -m streamlit run "$SCRIPT_DIR/LLM01 Prompt Injection/llm01_healthcare_prompt_injection_gandalf_levels_demo/llm01_healthcare_gandalf_demo/app.py" --server.port 8511 &
python -m streamlit run "$SCRIPT_DIR/LLM02 Sensitive Information Disclosure/llm02_healthcare_prompt_injection_demo/app.py" --server.port 8512 &

echo ""
echo "[*] Apps launched:"
echo "    LLM01  http://localhost:8511"
echo "    LLM02  http://localhost:8512"
echo ""
