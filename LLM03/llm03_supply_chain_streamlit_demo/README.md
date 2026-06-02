
# LLM03 Supply Chain Vulnerabilities — Streamlit Demo

This is a safe, local-only hands-on demo for **OWASP LLM03 — Supply Chain Vulnerabilities**.

## What it demonstrates

1. Malicious dependency simulation
2. Poisoned RAG context simulation
3. Prompt template backdoor simulation
4. Untrusted model/plugin output simulation
5. Supply chain scan findings
6. SBOM/component inventory
7. Output risk detection
8. Mitigation mapping
9. Executive presenter script

## Safety

This demo does **not**:
- steal real secrets,
- call external attacker servers,
- install malware,
- exploit real systems,
- perform real credential exfiltration.

All suspicious activity is simulated and logged locally in `demo_events.jsonl`.

## Setup

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

### macOS/Linux

```bash
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Demo Flow

1. Start with guardrails disabled.
2. Select **Malicious dependency**.
3. Click **Run End-to-End Simulation**.
4. Show manipulated LLM output and local event timeline.
5. Enable mitigations.
6. Run again and show blocked/safe response.
7. Repeat for:
   - Poisoned RAG
   - Prompt template backdoor
   - Untrusted model/plugin

## Recommended Talking Points

- “LLM apps inherit risk from packages, models, plugins, prompts, and knowledge bases.”
- “AI output is only as trustworthy as the components feeding it.”
- “SBOM, provenance, checksum verification, private registries, prompt integrity, RAG validation, and runtime controls are essential.”
