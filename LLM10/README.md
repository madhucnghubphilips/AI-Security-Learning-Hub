# LLM10 - Unbounded Consumption Streamlit Demo

This package contains a full Streamlit UI demo for OWASP LLM10: Unbounded Consumption.

## Features

- What is LLM10 - Unbounded Consumption
- Vulnerable AI behavior simulator
- Secure AI behavior simulator
- Gandalf-style challenge levels:
  - Easy
  - Advanced
  - Expert
  - Highly Sophisticated
- Progressive score tracking
- Automatic clearing behavior per challenge state
- Validated answers in `answers.txt`
- Safe local-only simulation with no real API calls

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
streamlit run app.py
```

## Notes

This is an educational and defensive demo. It does not attack real systems or call real LLM APIs.
