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

VENV_DIR=".venv"
if [ ! -d "$VENV_DIR" ]; then
    echo "[*] Creating virtual environment..."
    $PYTHON -m venv "$VENV_DIR"
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to create virtual environment."
        echo "On Ubuntu/Debian, install venv support with:"
        echo "  sudo apt install python3-venv"
        exit 1
    fi
fi

VENV_PYTHON="$VENV_DIR/bin/python"
echo "[*] Using virtual environment: $VENV_DIR"

echo "[*] Installing requirements..."
$VENV_PYTHON -m pip install --upgrade pip
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to upgrade pip in the virtual environment."
    exit 1
fi

$VENV_PYTHON -m pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install requirements."
    exit 1
fi

echo ""
echo "[*] Starting Streamlit app..."
$VENV_PYTHON -m streamlit run app.py
