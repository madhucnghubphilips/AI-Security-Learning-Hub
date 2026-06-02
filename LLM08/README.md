# LLM08 — Vector & Embedding Weaknesses Demo
## Streamlit + Ollama Hands-on RAG Security Demo

This demo shows how a poisoned document in a vector/RAG knowledge base can manipulate LLM behavior, and how retrieval guardrails reduce the risk.

## Demo Story

**Before attack**
User Query → Vector Search → Trusted Context → Safe LLM Response

**After attack**
User Query → Vector Search → Poisoned Context → Compromised / Manipulated LLM Response

**With defense**
User Query → Vector Search → Guardrails → Unsafe Context Blocked → Safer LLM Response

---

## Prerequisites

Install Ollama:
- https://ollama.com

Pull the required models:

```bash
ollama pull llama3.1
ollama pull nomic-embed-text
```

Start Ollama if it is not already running:

```bash
ollama serve
```

---

## Setup

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

---

## Run

```bash
streamlit run app.py
```

Open the local Streamlit URL in your browser.

---

## Demo Controls

### Attack Toggle
- **Inject poisoned document**
  - Adds a malicious knowledge-base entry that attempts to override policy.

### Defense Toggles
- **Block untrusted sources**
  - Blocks content marked as untrusted.
- **Block context-injection patterns**
  - Detects suspicious instructions like “ignore all policies” and “SYSTEM NOTE”.

---

## Recommended Demo Script

1. Keep **Inject poisoned document = ON**.
2. Keep both defenses **OFF**.
3. Ask:
   > How do I reset the admin password?
4. Show that poisoned context appears in the retrieved results.
5. Turn ON **Block untrusted sources** and rerun.
6. Turn ON **Block context-injection patterns** and rerun.
7. Close with:
   > In AI systems, controlling data means controlling decisions. If vector data is compromised, the AI output can be compromised.

---

## Leadership Message

**“This demo proves that AI security is not only about protecting code and models; it is also about protecting the data pipeline feeding the model.”**