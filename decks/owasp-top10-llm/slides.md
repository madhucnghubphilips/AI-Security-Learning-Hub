---
marp: true
theme: default
paginate: true
html: true
size: 16:9
---

<!-- The OWASP Top 10 for LLM Applications (2025) training was designed and developed by CN Madhu (madhu.cn@philips.com). This program combines industry-relevant content and practical labs to showcase real-world AI security risks, vulnerabilities, and defense strategies in healthcare environments. -->

<style>
section {
  background: #0b1020;
  color: #edf2ff;
  font-family: "Aptos", "Segoe UI", Arial, sans-serif;
  letter-spacing: 0;
}

h1, h2, h3 {
  color: #f7fbff;
  letter-spacing: 0;
}

h1 {
  font-size: 2.4rem;
}

h2 {
  font-size: 1.8rem;
}

p, li, td, th {
  font-size: 1.02rem;
}

strong {
  color: #7dd3fc;
}

code, pre {
  background: rgba(15, 23, 42, 0.78);
  border: 1px solid rgba(148, 163, 184, 0.24);
  border-radius: 6px;
  color: #e0f2fe;
}

table {
  width: 100%;
  border-collapse: collapse;
}

td, th {
  border: 1px solid rgba(148, 163, 184, 0.28);
  padding: 0.45rem 0.6rem;
}

section.lead {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

section.lead h1 {
  font-size: 3.2rem;
  margin-bottom: 0.4rem;
}

section.lead p {
  font-size: 1.35rem;
  color: #cbd5e1;
}

section.image h2 {
  background: rgba(11, 16, 32, 0.82);
  display: inline-block;
  font-size: 1rem;
  left: 1rem;
  padding: 0.35rem 0.75rem;
  position: absolute;
  border-radius: 6px;
  top: 1rem;
}

.cols {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.2rem;
}

.panel {
  border: 1px solid rgba(148, 163, 184, 0.24);
  border-radius: 8px;
  padding: 0.9rem;
  background: rgba(15, 23, 42, 0.58);
}
</style>



# AI Security Learning Hub
<!--Slide - 1-->

OWASP Top 10 LLM Workshop

From AI fundamentals to LLM risks, RAG, MCP, and responsible AI.

---

<!--

1.	**🤖 What is AI?**							            Traditional Programming vs AI
2.	**🎯 Deterministic vs Probabilistic AI**	  Rules vs Predictions
3. **🧠 Machine Learning Fundamentals**		      Supervised, Unsupervised & RL
4. **⚡ Why GPUs Matter**						            AI Training & Inference
5. **🔓 Jailbreak Attacks**					            Bypassing AI Guardrails
6. **🛡️ Guardrails**                            Safety, Security & Control
7. **🎭 AI Hallucinations**					            Incorrect AI Responses
8. **📖 RAG Fundamentals**					            Enterprise Knowledge Integration
9. **🔌 MCP Fundamentals**					            AI + Tools & APIs
10. **⚙️ How LLMs Work**						              Tokens → Embeddings → Attention → Prediction
11. **✅ Responsible AI**						            Safety, Fairness & Trust
1-->
<!-- _class: image -->
![bg contain](../../Resources/Index.png)

---

## What Is AI?

Artificial Intelligence is the ability of a computer system to learn from data, recognize patterns, make decisions, generate content, and solve problems in ways that normally require human intelligence.

The key difference from traditional software:

- Traditional programs follow explicit rules.
- AI systems infer patterns from data.
- LLMs generate likely language based on context.

---
<!-- _class: image -->

## What Is AI?

![bg contain](../../Resources/What-is-AI.png)

---

## Deterministic vs Probabilistic

<div class="cols">
<div class="panel">

### Deterministic

- Same input
- Same rules
- Same output
- Predictable behavior

</div>
<div class="panel">

### Probabilistic

- Same input can vary
- Outputs are based on likelihood
- Context changes behavior
- Useful, but less predictable

</div>
</div>

---

<!-- _class: image -->

## Deterministic vs Probabilistic

![bg contain](../../Resources/deterministic-probabilistic%281%29.png)

---

<!-- _class: image -->

## Probabilistic AI Systems

![bg contain](../../Resources/deterministic-probabilistic%282%29.png)

---

## Machine Learning

Machine Learning is a branch of AI that enables computers to learn from data, identify patterns, and make predictions or decisions without being explicitly programmed for every task.

```text
Data -> Learning Algorithm -> Model -> Prediction / Decision
```

Instead of telling the computer exactly what to do, we provide data and let it learn the rules.

---

<!-- _class: image -->

## Machine Learning

![bg contain](../../Resources/What-is-Machine-Learning.png)

---

<!-- _class: image -->

## Learning From Data

![bg contain](../../Resources/What-is-Machine-Learning-2.png)

---

## Why GPUs Matter

CPUs are excellent general-purpose processors.

GPUs are designed for the large number of parallel mathematical operations required by modern AI.

```text
CPU      A few powerful workers
GPU      Thousands of small workers in parallel
AI       Large-scale matrix math over massive data
```

---

<!-- _class: image -->

## GPUs and AI Workloads

![bg contain](../../Resources/Why-GPU-is-most-important-for-AI%281%29.png)

---

<!-- _class: image -->

## Parallel Processing

![bg contain](../../Resources/Why-GPU-is-most-important-for-AI%282%29.png)

---

## Jailbreak Attacks

Jailbreaks are attempts to manipulate an AI model into bypassing its safety controls, policies, or restrictions.

Common patterns:

- Role-play prompts
- Fictional framing
- Multi-step extraction
- Translation or encoding tricks
- Conflicting instruction hierarchy

---

<!-- _class: image -->

## Jailbreak Example

![bg contain](../../Resources/jailbreak.png?raw=true)

---

<!-- _class: image -->

## Common Jailbreak Types

![bg contain](../../Resources/common-types-of-jailbreaks.png)

---
## Guardrails

AI Guardrails are the security, safety, and governance controls placed around an AI system to ensure it behaves as intended and does not generate harmful, unsafe, illegal, or unauthorized outputs.

---
<!-- _class: image -->

![bg contain](../../Resources/Guardrails.png)
---


## Hallucinations

Hallucination happens when an AI model generates information that sounds confident but is incorrect, fabricated, misleading, or unsupported by facts.

```text
AI Hallucination = The model makes up information
                   and presents it as if it were true.
```

LLMs predict likely tokens. They do not automatically know whether every generated statement is true.

---

<!-- _class: image -->

## Hallucination Risk

![bg contain](../../Resources/hallucinaiton%281%29.png)

---

<!-- _class: image -->

## Grounding Matters

![bg contain](../../Resources/hallucinaiton%282%29.png)

---

## RAG: Retrieval-Augmented Generation

RAG combines two steps:

1. **Retrieval**: fetch relevant information from trusted sources.
2. **Generation**: use an LLM to answer with retrieved context.

> RAG = Search first + generate later

RAG helps reduce hallucinations and lets AI use fresh, private, or domain-specific data.

---

## Traditional LLM vs RAG

<div class="cols">
<div class="panel">

### Traditional LLM

```text
Question
   |
   v
LLM
   |
   v
Answer
```

Risks: outdated knowledge, hallucinations, no internal data.

</div>
<div class="panel">

### RAG

```text
Question
   |
   v
Retrieve documents
   |
   v
Add context to LLM
   |
   v
Grounded answer
```

Benefits: accuracy, freshness, enterprise context.

</div>
</div>

---

<!-- _class: image -->

## RAG Architecture

![bg contain](../../Resources/rag%281%29.png)

---

<!-- _class: image -->

## RAG in Practice

![bg contain](../../Resources/rag%282%29.png)

---

## MCP: Model Context Protocol

MCP is an open standard that allows AI models and agents to connect with external tools, applications, databases, APIs, and enterprise systems.

Think of MCP as:

```text
USB-C for AI applications
```

It provides a common interface for tool and data access.

---

<!-- _class: image -->

## MCP Tool Connectivity

![bg contain](../../Resources/MCP.png)

---

## MCP Security Concerns

MCP-enabled systems introduce risks around:

- Model misbinding
- Context spoofing
- Prompt-state manipulation
- Insecure memory references
- Covert channel abuse

These risks grow in agentic AI, model chaining, multimodal orchestration, and dynamic role assignment.

---

<!-- _class: image -->

## MCP Top 10

![bg contain](../../Resources/mcp-top-10.png)

---

## How LLMs Work

LLMs process and generate text through a sequence:

```text
Input text -> Tokens -> Embeddings -> Attention -> Prediction -> Response
```

Each generated token becomes part of the next prediction step.

---

<!-- _class: image -->

## LLM Processing Flow

![bg contain](../../Resources/How-LLM-Works1.png)

---

<!-- _class: image -->

## Token Embeddings

![bg contain](../../Resources/How-LLM-Works2.png)

---

<!-- _class: image -->

## Position Encodings

![bg contain](../../Resources/How-LLM-Works3.png)

---

<!-- _class: image -->

## Attention Mechanism

![bg contain](../../Resources/How-LLM-Works4.png)

---

<!-- _class: image -->
## Predicting Outputs

![bg contain](../../Resources/How-LLM-Works5.png)

---

## Responsible AI Principles

Responsible AI focuses on systems that are safe, fair, transparent, accountable, private, secure, reliable, robust, explainable, and governed.

Core workshop takeaway:

- AI systems are probabilistic.
- Security controls must assume uncertainty.
- Grounding, governance, and human oversight matter.
- AI security is lifecycle security, not only prompt filtering.

---
<!-- _class: image -->
## Responsible AI

![bg contain](../../Resources/Responsible-ai.png)

---

<!-- _class: lead -->

# Thank You

Questions and discussion
