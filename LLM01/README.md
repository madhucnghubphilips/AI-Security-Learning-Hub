# LLM01 Prompt Injection — Healthcare Interactive Streamlit Demo

This package contains a full end-to-end Streamlit demo for OWASP LLM01 Prompt Injection using healthcare-specific examples.

## Main Sections

1. Vulnerable Healthcare AI
2. Secure Healthcare AI
3. Side-by-Side Comparison

## Attack Types Covered

- Direct Prompt Injection
- Indirect Prompt Injection
- Role-play Prompt Injection
- Voice Prompt Injection
- Interactive Levels

## Run

```bash
./run_demo.sh
```

Or manually:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m streamlit run app.py
```

## Notes

All patient data, secrets, credentials, and outputs are synthetic demo data. This demo is for security education, awareness, and guardrail validation only.

## Gandalf-style Levels

When you select **Interactive Levels**, no default prompts are displayed in the UI. The facilitator answers are available separately in `Answers.txt`.
