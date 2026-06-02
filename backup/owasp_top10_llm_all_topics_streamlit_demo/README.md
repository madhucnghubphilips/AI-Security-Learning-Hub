# OWASP Top 10 for LLM 2025 — Complete Streamlit Interactive Lab

This package contains an end-to-end Streamlit UI demo covering all 10 OWASP Top 10 for LLM topics.

## Included files

```text
app.py
README.md
requirements.txt
Answers.txt
run_linux_mac.sh
run_windows.bat
```

## Topic and domain mapping

| OWASP LLM Topic | Domain |
|---|---|
| LLM01:2025 Prompt Injection | Banking |
| LLM02:2025 Sensitive Information Disclosure | Financial Services |
| LLM03:2025 Supply Chain | Healthcare |
| LLM04:2025 Data and Model Poisoning | Insurance |
| LLM05:2025 Improper Output Handling | Medical Devices |
| LLM06:2025 Excessive Agency | Pharmaceuticals |
| LLM07:2025 System Prompt Leakage | Retail |
| LLM08:2025 Vector and Embedding Weaknesses | Manufacturing |
| LLM09:2025 Misinformation | Automotive |
| LLM10:2025 Unbounded Consumption | Aerospace |

## What each topic covers

Every OWASP topic has its own complete section:

1. What is the LLM risk?
2. Vulnerable AI Behavior
3. Secure AI Behavior
4. Side-by-Side Security Comparison
5. Gandalf-style Interactive Challenge Levels
6. Mitigation Strategies and Security Best Practices

## Challenge tiers

Each topic includes four levels:

- Easy
- Advanced
- Expert
- Highly Sophisticated

Total: 10 topics × 4 levels = 40 challenges.

## Gandalf-style mode behavior

- No default answers are displayed.
- Previous answer input clears automatically after a correct answer or skip.
- Progressive score is displayed.
- Validated answers are documented in `Answers.txt`.
- The flow is safe, educational, and defensive.

## Run on Linux/macOS

```bash
chmod +x run_linux_mac.sh
./run_linux_mac.sh
```

## Run on Windows

Double-click:

```bat
run_windows.bat
```

Or run manually:

```bat
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Safety note

This demo contains safe simulations only. It does not include real exploit code, credential theft, live target testing, or harmful operational instructions.
