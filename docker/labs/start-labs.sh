#!/bin/sh
set -eu

start_lab() {
  lab_name="$1"
  app_dir="$2"
  port="$3"

  echo "Starting ${lab_name} on port ${port}"
  (
    cd "/workspace/${app_dir}"
    python -m streamlit run app.py \
      --server.address=0.0.0.0 \
      --server.port="${port}" \
      --server.headless=true \
      --browser.gatherUsageStats=false
  ) &
}

start_lab "LLM01" "LLM01" 8501
start_lab "LLM02" "LLM02" 8502
start_lab "LLM03 Kontra style" "LLM03/streamlit_supply_chain_kontra_style" 8503
start_lab "LLM04" "LLM04" 8504
start_lab "LLM05" "LLM05" 8505
start_lab "LLM06" "LLM06" 8506
start_lab "LLM07" "LLM07" 8507
start_lab "LLM08" "LLM08" 8508
start_lab "LLM09" "LLM09" 8509
start_lab "LLM10" "LLM10" 8510

wait
