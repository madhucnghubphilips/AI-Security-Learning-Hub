# LLM03 Supply Chain Vulnerabilities — Vulnerable OSS Download Lab

A safe, defensive Streamlit training application for OWASP LLM03 — Supply Chain Vulnerabilities.

## Safety Note

This lab does not download real malicious packages and does not execute harmful code.

The "vulnerable OSS download" is a local simulated OSS registry included inside this project. It demonstrates how supply-chain compromise can happen using harmless files and visible indicators.

## Quick Start

```bash
cd llm03_supply_chain_vuln_oss_lab
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

Open: http://localhost:8501

## What the lab covers

- Safe OSS package download simulation
- Vulnerable OSS package download simulation
- Manifest comparison
- AI-assisted supply-chain attack flow
- Detection checks
- Security gates
- CTF questions
