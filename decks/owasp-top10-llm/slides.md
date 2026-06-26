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
  background: #ffffff;
  color: #111827;
  font-family: "Aptos", "Segoe UI", Arial, sans-serif;
  letter-spacing: 0;
}

h1, h2, h3 {
  color: #111827;
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
  color: #0f4c81;
}

code, pre {
  background: #f8fafc;
  border: 1px solid #d0d7de;
  border-radius: 6px;
  color: #111827;
}

pre {
  line-height: 1.22;
  padding: 0.55rem 0.7rem;
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
  color: #374151;
  font-size: 1.35rem;
}

section.image h2 {
  background: rgba(255, 255, 255, 0.9);
  border-radius: 6px;
  display: inline-block;
  font-size: 1rem;
  left: 1rem;
  padding: 0.35rem 0.75rem;
  position: absolute;
  top: 1rem;
}

.cols {
  align-items: stretch;
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.panel {
  background: #f8fafc;
  border: 1px solid #d0d7de;
  border-radius: 8px;
  min-width: 0;
  padding: 0.75rem;
}

.panel h3 {
  margin-top: 0;
}

.panel p {
  font-size: 0.92rem;
}

.panel pre {
  font-size: 0.82rem;
}
</style>

<!-- _class: lead -->

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


![bg contain](../../Resources/deterministic-probabilistic%281%29.png)

---

<!-- _class: image -->


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


![bg contain](../../Resources/What-is-Machine-Learning.png)

---

<!-- _class: image -->


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

![bg contain](../../Resources/GPUvsCPU_001.png)


---

<!-- _class: image -->


![bg contain](../../Resources/Why-GPU-is-most-important-for-AI%281%29.png)

---

<!-- _class: image -->

![bg contain](../../Resources/Why-GPU-is-most-important-for-AI%282%29.png)

---

<!-- _class: image -->

![bg contain](../../Resources/CPU_GPU_TPU_NPU.png)

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


![bg contain](../../Resources/jailbreak.png?raw=true)

---

<!-- _class: image -->


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


![bg contain](../../Resources/hallucinaiton%281%29.png)

---

<!-- _class: image -->


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


![bg contain](../../Resources/rag%281%29.png)

---

<!-- _class: image -->


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


![bg contain](../../Resources/How-LLM-Works1.png)

---

<!-- _class: image -->


![bg contain](../../Resources/How-LLM-Works2.png)

---

<!-- _class: image -->


![bg contain](../../Resources/How-LLM-Works3.png)

---

<!-- _class: image -->


![bg contain](../../Resources/How-LLM-Works4.png)

---

<!-- _class: image -->


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


![bg contain](../../Resources/Responsible-ai.png)

---

<!-- _class: lead -->

# Thank You

Questions and discussion
