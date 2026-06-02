# Kontra-Style Supply Chain Security Lab

Original Streamlit training app inspired by the public Kontra interactive learning style. It does **not** copy Kontra proprietary screens or text. It uses a similar educational flow: understand the scenario, inspect the vulnerable setup, identify the weakness, and apply the secure fix.

## Topic
OWASP LLM03 / Software Supply Chain Vulnerabilities for AI and LLM applications.

## Features
- 14-step guided interactive learning path
- Vulnerable setup vs secure fix view
- Quiz and scoring
- Mini scanner for supply-chain red flags
- Secure release checklist
- Downloadable JSON lab report

## Run Locally
```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
streamlit run app.py
```

## Suggested Usage
Use this for internal security awareness, OWASP LLM Top 10 workshops, developer enablement, AppSec onboarding, or DevSecOps CI/CD security training.

## Training Steps
1. Mission Brief: What is the Supply Chain?
2. Untrusted Package Install
3. Dependency Confusion
4. Version Pinning and Hashes
5. Vulnerable Transitive Dependency
6. Malicious Pretrained Model
7. Poisoned Dataset
8. Insecure Plugin
9. CI/CD Secret Exposure
10. Unsigned Container Image
11. Build Script Tampering
12. SBOM and Provenance Gate
13. Runtime Drift
14. Final Fix Challenge
