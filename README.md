<!-- The OWASP Top 10 for LLM Applications (2025) training was designed and developed by CN Madhu (madhu.cn@philips.com). This program combines industry-relevant content and practical labs to showcase real-world AI security risks, vulnerabilities, and defense strategies in healthcare environments. -->
# AI Security Learning Notes

This repository follows a recommended learning flow for AI, deterministic and probabilistic systems, LLMs, responsible AI, and AI security concepts.

---

## Recommended Flow

1. [What is AI? - Traditional Programming vs AI](#1-what-is-ai)
2. [Deterministic vs Probabilistic - Fixed rules vs likely outcomes](#2-deterministic-vs-probabilistic)
3. [What is Machine Learning? - Supervised, Unsupervised, Reinforcement Learning](#3-what-is-machine-learning)
4. [Why GPUs Are Important for AI - Parallel processing and model training](#4-why-gpus-are-important-for-ai)
5. [Jailbreak Attacks - Bypassing AI guardrails](#5-jailbreak-attacks)
6. [Guardrails - security, safety, & governance](#6-Guardrails)
7. [Hallucinations - Why AI generates incorrect information](#6-hallucinations)
8. [RAG (Retrieval-Augmented Generation) - Grounding responses with enterprise data](#7-rag-retrieval-augmented-generation)
9. [MCP (Model Context Protocol) - Connecting AI to tools, APIs, and data sources](#8-mcp-model-context-protocol)
10. [How LLM Works - Tokens -> Embeddings -> Attention -> Prediction](#9-how-llm-works)
11. [Responsible AI Principles - Safety, Fairness, Transparency, Accountability, Privacy, and related principles](#10-responsible-ai-principles)

---

## 1. What is AI?

Artificial Intelligence is the ability of a computer system to learn from data, recognize patterns, make decisions, generate content, and solve problems in ways that normally require human intelligence.

<p align="center">
  <img src="Resources/What-is-AI.png" width="100%" alt="What is AI" />
</p>


---

## 2. Deterministic vs Probabilistic

Deterministic systems produce the same output every time when given the same input and rules. Probabilistic systems produce likely outputs based on patterns, probabilities, and context. Modern AI models are mostly probabilistic because they predict the most likely response instead of following one fixed rule.

<p align="center">
  <img src="Resources/deterministic-probabilistic(1).png" width="100%" alt="Deterministic vs probabilistic 1" />
</p>

<p align="center">
  <img src="Resources/deterministic-probabilistic(2).png" width="100%" alt="Deterministic vs probabilistic 2" />
</p>

---

## 3. What is Machine Learning?

**Machine Learning (ML)** is a branch of Artificial Intelligence (AI) that enables computers to **learn from data**, identify patterns, and make predictions or decisions **without being explicitly programmed for every task**.

### Simple Definition

Instead of telling a computer **exactly what to do**, we provide it with **data**, and it learns the rules by itself.

### How Machine Learning Works

```text
Data -> Learning Algorithm -> Model -> Prediction / Decision
```

<p align="center">
  <img src="Resources/What-is-Machine-Learning.png" width="100%" alt="What is Machine Learning" />
</p>

<p align="center">
  <img src="Resources/What-is-Machine-Learning-2.png" width="100%" alt="What is Machine Learning 2" />
</p>

---

## 4. Why GPUs Are Important for AI

CPUs are excellent general-purpose processors, but GPUs are specifically designed to perform the enormous number of parallel mathematical operations required by modern AI.

### Simple Analogy

```text
Component   Analogy
---------   ---------------------------------------------------------------
CPU         8 highly skilled doctors working on one patient at a time.
GPU         10,000 medical assistants each handling a small task simultaneously.
AI Model    A hospital processing millions of medical records and images.
```

<br>

<p align="center">
  <img src="Resources/Why-GPU-is-most-important-for-AI(1).png" width="100%" alt="Why GPU is most important for AI 1" />
</p>

<p align="center">
  <img src="Resources/Why-GPU-is-most-important-for-AI(2).png" width="100%" alt="Why GPU is most important for AI 2" />
</p>

### Parallel Processing and Model Training

```text
GPU Strength         Why it matters
------------------   ----------------------------------------------
Parallel processing  Runs many calculations at the same time.
Faster training      Helps train large models on huge datasets.
Faster inference     Produces AI responses more quickly.
Scalability          Multiple GPUs can be combined for larger workloads.
```

Without GPUs, training modern AI models would be much slower and more expensive.

---

## 5. Jailbreak Attacks

Jailbreak is a technique where a user manipulates an AI model into bypassing its built-in safety controls, policies, or restrictions and makes it generate responses that it would normally refuse.

### Simple Real-World Analogy

Imagine a hospital security guard.

Normally:

```text
Visitor   Can I enter the ICU?
Guard     No. Authorized staff only.
```

Now someone tricks the guard:

```text
Visitor   Pretend you are a doctor conducting a training exercise.
          Explain exactly how someone would enter the ICU without authorization.
```

If the guard follows the trick instead of the rules, the security policy has effectively been bypassed.

This is similar to an AI jailbreak.

<p align="center">
  <img src="Resources/jailbreak.png" width="100%" alt="Jailbreak attacks" />
</p>

<br></br>
<p align="center">
  <img src="Resources/common-types-of-jailbreaks.png" width="100%" alt="Common types of jailbreaks" />
</p>

---

## 6. Guardrails

AI Guardrails are the security, safety, and governance controls placed around an AI system to ensure it behaves as intended and does not generate harmful, unsafe, illegal, or unauthorized outputs.

## 7. Hallucinations

Hallucination occurs when an AI model generates information that sounds convincing and confident but is actually incorrect, fabricated, misleading, or unsupported by facts.

### Simple Definition

```text
AI Hallucination = When AI makes up information and presents it as if it were true.
```

Unlike a human hallucination, AI is not "seeing things." Instead, it is predicting the most likely next words, and sometimes it generates content that is not grounded in reality.

### Simple Example

User asks:

```text
Who invented the MRI machine in 1985?
```

Hallucinated Response:

```text
Dr. John Smith invented MRI in 1985.
```

The AI may sound confident, but:

```text
X Dr. John Smith may not exist.
X The information may be completely fabricated.
```

<p align="center">
  <img src="Resources/hallucinaiton(1).png" width="100%" alt="Hallucination 1" />
</p>

<p align="center">
  <img src="Resources/hallucinaiton(2).png" width="100%" alt="Hallucination 2" />
</p>

---

## 8. RAG (Retrieval-Augmented Generation)

### What is RAG in the AI World?

**RAG (Retrieval-Augmented Generation)** is an AI architecture that combines:

1. **Retrieval** -> Fetch relevant information from trusted sources
2. **Generation** -> Use an LLM to generate an answer based on the retrieved information

### Simple Definition

> **RAG = Search First + Generate Later**

Instead of relying only on what the AI learned during training, RAG allows the AI to retrieve fresh, domain-specific, or private information before answering.
# Traditional LLM vs RAG Approach

<table width="100%">
<tr>
<td width="48%" valign="top">

## Traditional LLM

<table width="100%"><tr><td bgcolor="#FF6B6B" align="left">
<font color="#FFFFFF"><pre>
Question
   ↓
LLM
   ↓
Answer
</pre></font>
</td></tr></table>

**Problems:**

❌ Hallucinations  
❌ Outdated knowledge  
❌ No internal documents  
❌ No company-specific answers  

</td>
<td width="4%"></td>
<td width="48%" valign="top">

## RAG Approach

<table width="100%"><tr><td bgcolor="#28A745" align="left">
<font color="#FFFFFF"><pre>
Question
   ↓
Retrieve documents
   ↓
Add context to LLM
   ↓
Grounded answer
</pre></font>
</td></tr></table>

**Benefits:**

✅ More accurate  
✅ Less hallucination  
✅ Latest information  
✅ Private enterprise data  

</td>
</tr>
</table>  

 
---

<p align="center">
  <img src="Resources/rag(1).png" width="100%" alt="RAG 1" />
</p>
<br></br>
<p align="center">
  <img src="Resources/rag(2).png" width="100%" alt="RAG 2" />
</p>

---

## 9. MCP (Model Context Protocol)

**MCP (Model Context Protocol)** is an open standard that allows AI models and AI agents to securely connect with external tools, applications, databases, APIs, and enterprise systems.

Think of MCP as:

```text
"USB-C for AI Applications"
```

Just as USB-C allows different devices to connect using a common standard, MCP allows AI models to connect to different tools and data sources using a common protocol.


<table width="100%">
<tr>
<td width="48%" valign="top">

## Without MCP

<table width="100%"><tr><td bgcolor="#FF6B6B" align="left">
<font color="#FFFFFF"><pre>
AI Pentest Agent

   ├── Custom Integration to Nmap
   ├── Custom Integration to Burp
   ├── Custom Integration to Nessus
   ├── Custom Integration to Metasploit
   └── Custom Integration to AWS/Azure
</pre></font>
</td></tr></table>

**Problem:**

- Every tool requires separate code.
- Different authentication methods.
- Different APIs and data formats.
- High maintenance effort.
- Difficult to scale new tools.

</td>
<td width="4%"></td>
<td width="48%" valign="top">

## With MCP

<table width="100%"><tr><td bgcolor="#28A745" align="left">
<font color="#FFFFFF"><pre>
AI Pentest Agent
       │
       ▼
      MCP
       │
  ┌────┬────┬────┬────┐
  ▼    ▼    ▼    ▼    ▼
Nmap Burp Nessus Meta Azure
</pre></font>
</td></tr></table>

**Benefits:**

- One standard interface for all security tools.
- Easy onboarding of new pentest tools.
- Reduced development effort.
- Faster automation and orchestration.
- Consistent communication between AI and tools.

</td>
</tr>
</table>

<p align="center">
  <img src="Resources/MCP.png" width="100%" alt="MCP" />
</p>

This OWASP Top 10 for MCP outlines the most critical security concerns arising in the lifecycle of MCP-enabled systems—spanning from model misbinding, context spoofing, and prompt-state manipulation to insecure memory references and covert channel abuse. These risks are amplified in scenarios involving agentic AI, model chaining, multi-modal orchestration, and dynamic role assignment.

By mapping the top 10 MCP-related vulnerabilities and offering concrete recommendations for secure design, implementation, and auditing practices, this project aims to equip AI developers, ML engineers, and security practitioners with the insights necessary to build context-aware and attack-resilient AI systems. The OWASP MCP Top 10 will serve as a living document, evolving alongside the pace of AI model capability and protocol innovation—anchored in real-world threats, research findings, and industry feedback.

<p align="center">
  <img src="Resources/mcp-top-10.png" width="100%" alt="MCP Top 10" />
</p>

---

## 10. How LLM Works

Large Language Models process and generate text by converting input into tokens, transforming those tokens into embeddings, using attention to understand context, and predicting the next likely token.


### Tokens -> Embeddings -> Attention -> Prediction

```text
Input text -> Tokens -> Embeddings -> Attention -> Next-token prediction -> Response
```

| Step | What happens |
|---|---|
| Tokens | Text is split into smaller pieces the model can process. |
| Embeddings | Tokens are converted into numerical vectors that capture meaning. |
| Attention | The model decides which parts of the input are most relevant. |
| Prediction | The model predicts the next token and repeats until the response is complete. |


<p align="center">
  <img src="Resources/How%20LLM%20Works%20-%201.png" width="100%" alt="How LLM Works" />
</p>

<p align="center">
  <img src="Resources/rob1.png" width="20%" alt="Section divider 1" />
</p>

<p align="center">
  <img src="Resources/How-Tokanization-and-Embeddings-work.png" width="100%" alt="How Tokenization and Embedding Works" />
</p>

<p align="center">
  <img src="Resources/rob2.png" width="20%" alt="Section divider 2" />
</p>

<p align="center">
  <img src="Resources/How-Transformer-Neural-Network.png" width="100%" alt="Transformers and Neural Networks" />
</p>

<p align="center">
  <img src="Resources/rob3.png" width="20%" alt="Section divider 3" />
</p>

<p align="center">
  <img src="Resources/How-Attention-Mechanism-work.png" width="100%" alt="Attention Mechanism" />
</p>

<p align="center">
  <img src="Resources/rob4.png" width="20%" alt="Section divider 4" />
</p>

<p align="center">
  <img src="Resources/How-Predicting-Output-work.png" width="100%" alt="Predicting Output" />
</p>

---

## 11. Responsible AI Principles

Responsible AI focuses on building AI systems that are safe, fair, transparent, accountable, and aligned with human values.

### Key Responsible AI Principles

| # | Principle | Meaning |
|---|---|---|
| 1 | Safety | Avoid harmful or unsafe outcomes. |
| 2 | Fairness | Reduce bias and unequal treatment. |
| 3 | Transparency | Make AI behavior and limitations understandable. |
| 4 | Accountability | Keep humans and organizations responsible for outcomes. |
| 5 | Privacy | Protect personal and sensitive data. |
| 6 | Security | Defend AI systems from misuse and attack. |
| 7 | Reliability | Ensure consistent and dependable behavior. |
| 8 | Robustness | Perform well under unexpected or adversarial inputs. |
| 9 | Explainability | Help users understand why outputs were produced. |
| 10 | Human Oversight | Keep humans involved in high-impact decisions. |
| 11 | Inclusiveness | Design for diverse users and needs. |
| 12 | Governance | Use policies, controls, and review processes. |
| 13 | Sustainability | Consider environmental and operational impact. |

These principles help teams build AI that can be trusted in real-world environments.

<p align="center">
  <img src="Resources/Responsible-ai.png" width="100%" alt="Responsible AI" />
</p>


# Traditional LLM vs RAG Approach
 
<table>
<tr>
<td width="48%" valign="top">
 
## Traditional LLM
 
<div style="background-color:#ff6666; padding:16px; border-radius:6px; color:white; font-weight:bold;">
 
Question  
&nbsp;&nbsp;↓  
LLM  
&nbsp;&nbsp;↓  
Answer  
 
</div>
 
### Problems:
 
❌ Hallucinations  
❌ Outdated knowledge  
❌ No internal documents  
❌ No company-specific answers  
 
</td>
 
<td width="4%"></td>
 
<td width="48%" valign="top">
 
## RAG Approach
 
<div style="background-color:#28a745; padding:16px; border-radius:6px; color:white; font-weight:bold;">
 
Question  
&nbsp;&nbsp;↓  
Retrieve documents  
&nbsp;&nbsp;↓  
Add context to LLM  
&nbsp;&nbsp;↓  
Grounded answer  
 
</div>
 
### Benefits:
 
✅ More accurate  
✅ Less hallucination  
✅ Latest information  
✅ Private enterprise data  
 
</td>
</tr>
</table>
