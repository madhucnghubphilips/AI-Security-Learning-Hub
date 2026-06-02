#!/bin/bash

echo "============================================"
echo " LLM03 - LLM04 Demo Apps"
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
python -m pip install -r "$SCRIPT_DIR/LLM03/Demo3/llm03_supply_chain_streamlit_demo/requirements.txt"
python -m pip install -r "$SCRIPT_DIR/LLM04/llm04_data_model_poisoning_demo/requirements.txt"

echo ""
echo "[*] Launching apps in the background..."

python -m streamlit run "$SCRIPT_DIR/LLM03/Demo3/llm03_supply_chain_streamlit_demo/app.py" --server.port 8513 &
python -m streamlit run "$SCRIPT_DIR/LLM04/llm04_data_model_poisoning_demo/app.py" --server.port 8514 &

echo ""
echo "[*] Apps launched:"
echo "    LLM03  http://localhost:8513"
echo "    LLM04  http://localhost:8514"
echo ""
