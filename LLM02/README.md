# LLM02 Healthcare Prompt Injection Demo

Full Streamlit UI demo for **OWASP LLM02 — Sensitive Information Disclosure** with healthcare examples.

## Demo Modes

1. Vulnerable Healthcare AI
2. Secure Healthcare AI
3. Side-by-Side Comparison
4. Interactive Levels

## Prompt Injection Examples

- Direct Prompt Injection
- Indirect Prompt Injection
- Role-play Prompt Injection
- Voice Prompt Injection

## Healthcare Leakage Examples

The demo uses dummy data for:

- Patient record leakage
- Clinical note leakage
- Billing/insurance leakage
- FHIR/API integration secret leakage
- System prompt leakage

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Interactive Levels

When Interactive Levels are selected, default prompts are not shown in the UI.

Sample answers are provided separately in:

```text
Answers.txt
```

## Safety Notice

This demo is for security awareness and training only.  
All patient data, credentials, tokens, URLs, and records are fake dummy data.

Do not use real patient records, real PHI/PII, real credentials, or real internal URLs.
