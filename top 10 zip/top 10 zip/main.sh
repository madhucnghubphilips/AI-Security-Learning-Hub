#!/bin/bash

echo "============================================"
echo " Starting all LLM Demo Apps"
echo "============================================"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

source "$SCRIPT_DIR/start_1.sh"
source "$SCRIPT_DIR/start_2.sh"
source "$SCRIPT_DIR/start_3.sh"
source "$SCRIPT_DIR/start_4.sh"

echo ""
echo "All groups launched. Press Ctrl+C to stop all apps."
wait