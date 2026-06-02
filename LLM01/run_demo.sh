#!/bin/bash

echo "============================================"
echo " LLM01 - Healthcare Prompt Injection Demo"
echo "============================================"

# Detect Python executable (python3 > python)
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

echo "[*] Installing requirements..."
$PYTHON -m pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install requirements."
    exit 1
fi

echo ""
echo "[*] Starting Streamlit app..."
$PYTHON -m streamlit run app.py
