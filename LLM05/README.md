# LLM05 — Improper Output Handling Healthcare Streamlit Demo

A complete end-to-end Streamlit UI demo for **OWASP LLM05: Improper Output Handling** using healthcare scenarios around PI/PHI, Philips-style ultrasound, patient monitoring, image-guided therapy, diagnostic & clinical informatics, magnetic resonance imaging, and computed tomography.

## Fixes included

- No `bleach` dependency. The demo uses built-in Python sanitization/escaping helpers.
- Fixes `st.session_state.level_input cannot be modified after the widget with key level_input is instantiated` by using dynamic level input keys and safe callbacks.
- Interactive levels mode hides default prompts and clears the answer field after each level.
- `Answers.txt` contains the exact answer key and the app validates against it.

## Run

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
streamlit run app.py
```

All data is synthetic and for security education only.
