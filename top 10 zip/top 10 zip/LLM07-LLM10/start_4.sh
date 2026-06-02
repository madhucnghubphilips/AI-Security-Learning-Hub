#!/bin/bash

echo "============================================"
echo " LLM07 - LLM10 Demo Apps"
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
python -m pip install -r "$SCRIPT_DIR/LLM07/llm07_system_prompt_leakage_realtime_demo/requirements.txt"
python -m pip install -r "$SCRIPT_DIR/LLM8 Vector and Embedding Weaknesses/llm08_streamlit_ollama_demo/requirements.txt"
python -m pip install -r "$SCRIPT_DIR/LLM09 Misinformation/llm09/requirements.txt"
python -m pip install -r "$SCRIPT_DIR/LLM10 - Unbounded Consumption/llm10_unbounded_consumption_streamlit_demo/requirements.txt"

echo ""
echo "[*] Launching apps in the background..."

python -m streamlit run "$SCRIPT_DIR/LLM07/llm07_system_prompt_leakage_realtime_demo/app.py" --server.port 8517 &
python -m streamlit run "$SCRIPT_DIR/LLM8 Vector and Embedding Weaknesses/llm08_streamlit_ollama_demo/app.py" --server.port 8518 &
python -m streamlit run "$SCRIPT_DIR/LLM09 Misinformation/llm09/app.py" --server.port 8519 &
python -m streamlit run "$SCRIPT_DIR/LLM10 - Unbounded Consumption/llm10_unbounded_consumption_streamlit_demo/app.py" --server.port 8520 &

echo ""
echo "[*] Apps launched:"
echo "    LLM07  http://localhost:8517"
echo "    LLM08  http://localhost:8518"
echo "    LLM09  http://localhost:8519"
echo "    LLM10  http://localhost:8520"
echo ""
