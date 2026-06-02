# LLM04 — Data and Model Poisoning Healthcare Demo

A full Streamlit UI demo for OWASP LLM04: Data and Model Poisoning, using synthetic healthcare examples.

## Modules

1. Vulnerable Healthcare AI
2. Secure Healthcare AI
3. Side-by-Side Comparison
4. Interactive Levels
5. Dataset Poisoning Lab

## Healthcare Scenarios

- Healthcare PHI/PII poisoning
- Philips MRI machine safety-control manipulation
- Philips image-guided therapy calibration and dose-alert poisoning
- Diagnostic label poisoning
- Backdoor trigger poisoning

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Trainer Notes

- Answers for the interactive levels are in `Answers.txt`.
- The UI intentionally does not show default answer prompts in the interactive mode.
- Moving to the next level clears previous inputs.
- All data is synthetic and for education only.

## Security Controls Demonstrated

- Dataset provenance validation
- Signed/approved data manifests
- PHI/PII redaction before training/RAG
- Suspicious instruction detection
- Quarantine workflow for poisoned records
- Human-in-the-loop clinical safety review
- Dataset version rollback and re-training from clean data
