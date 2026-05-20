# AI-Security
This is the repository for the OWASP Top 10 LLM, Hand on Experience and Mitigations

![platform](https://img.shields.io/badge/AI-Security-violet)
![platform](https://img.shields.io/badge/LLM-Security-blueviolet)
![platform](https://img.shields.io/badge/Artificial-Intelligence-purple)
![platform](https://img.shields.io/badge/AIDataLeakage-Prevention-yellowgreen)
![platform](https://img.shields.io/badge/AISupplyChaine-Security-green)
![platform](https://img.shields.io/badge/SecurePrompt-Design-purple)
![platform](https://img.shields.io/badge/RetrievalAugmentedGeneration-RAG-yellow)

<img align="center" height="500" width="500" src="https://github.com/madhucnghubphilips/AI-Security/blob/main/Resources/Logo.png" />

<h1 align="center"><font face="Arial">Introduction to OWASP Top 10 for LLM Applications </font></h1>

The rapid adoption of Artificial Intelligence and Large Language Models (LLMs) is transforming how organizations build applications, automate operations, and interact with users. From AI chatbots and copilots to autonomous agents and enterprise automation platforms, LLMs are becoming a core part of modern digital ecosystems.

However, alongside innovation comes a new generation of security risks. Traditional application security controls alone are no longer sufficient to protect AI-driven systems. LLMs introduce unique attack surfaces such as Prompt Injection, Sensitive Information Disclosure, Model Poisoning, Excessive Agency, System Prompt Leakage, and Vector Database attacks.

To address these emerging threats, the OWASP Foundation introduced the OWASP Top 10 for LLM Applications — a globally recognized awareness and risk management framework focused on securing AI and Generative AI ecosystems.

## <h3 align="left"><font face="Arial"><span style="color:green">The OWASP Top 10 for LLMs helps organizations:</span></font></h3>

Understand the most critical AI security risks
Secure AI-powered applications and workflows
Implement Secure-by-Design AI architectures
Build governance and compliance controls for GenAI adoption
Enable secure AI innovation across the SDLC

## <h3 align="left"><font face="Arial"><span style="color:green">The framework highlights the most impactful vulnerabilities affecting LLM-based systems, including:</span></font></h3>

1.  LLM01 - Prompt Injection 
2.  LLM02 - Sensitive Information Disclosure
3.  LLM03 - Supply Chain Vulnerabilities
4.  LLM04 - Data and Model Poisoning 
5.  LLM05 - Improper Output Handling 
6.  LLM06 - Excessive Agency 
7.  LLM07 - System Prompt Leakage
8.  LLM08 - Vector and Embedding Weaknesses
9.  LLM09 - Misinformation 
10. LLM10 - Unbounded Consumption

<h1 align="center"><font face="Arial">How LLM Works</font></h1>


# 🚀 How a Large Language Model (LLM) Works Internally

<p align="center">
  <img src="https://github.com/madhucnghubphilips/AI-Security/blob/main/Resources/How%20LLM%20Works%20-%201.png" width="100%" alt="LLM Architecture Overview"/>
  </p>

---

# 📌 Introduction

Large Language Models (LLMs) such as GPT, Gemini, Claude, and Llama process human language using advanced neural network architectures called **Transformers**.

An LLM performs the following major steps internally:

```text
Input Text
   ↓
Tokenization
   ↓
Embeddings
   ↓
Transformer Layers
   ↓
Attention Mechanism
   ↓
Next Token Prediction
   ↓
Final Human-like Response
```

---

# 🧠 End-to-End LLM Workflow

<p align="center">
  <img src="https://github.com/madhucnghubphilips/AI-Security/blob/main/Resources/How%20LLM%20Works%20-%202.png" width="100%" alt="LLM End to End Workflow"/>
</p>

---

# 1️⃣ Tokenization & Embeddings

## 🔹 What is Tokenization?

The input sentence is broken into smaller units called **tokens**.

### Example

```text
Input:
"What is cloud security?"

Tokens:
["What", "is", "cloud", "security", "?"]
```

Each token is converted into a numeric ID.

| Token | Token ID |
|------|------|
| What | 1011 |
| is | 2053 |
| cloud | 5024 |
| security | 9617 |
| ? | 102 |

---

## 🔹 What are Embeddings?

Tokens are transformed into vectors (numerical representations).

These vectors capture:

- Semantic meaning
- Relationships
- Context
- Similarity

### Example Embedding

```text
cloud → [0.21, 0.87, 0.45, 0.12 ...]
```

Words with similar meaning have embeddings closer together in vector space.

---

# 2️⃣ Transformer Neural Network

<p align="center">
  <img src="https://github.com/madhucnghubphilips/AI-Security/blob/main/Resources/How%20LLM%20Works%20-%203.png" width="100%" alt="Transformer Neural Network"/>
</p>

---

## 🔹 What is a Transformer?

The Transformer is the core neural architecture behind modern LLMs.

It processes all tokens in parallel and understands relationships between words.

---

## 🔹 Main Components Inside Transformer

### ✅ Multi-Head Self-Attention

Allows the model to focus on different parts of the sentence simultaneously.

### ✅ Feed Forward Network (FFN)

Applies nonlinear transformations to improve understanding.

### ✅ Add & Norm

Helps stabilize training and preserve information.

### ✅ Positional Encoding

Adds word position information because transformers process tokens in parallel.

---

## 🔹 Transformer Block Flow

```text
Input Embedding
      ↓
Multi-Head Attention
      ↓
Add & Norm
      ↓
Feed Forward Network
      ↓
Add & Norm
      ↓
Output Representation
```

This process repeats across multiple layers.

---

# 3️⃣ Attention Mechanism

<p align="center">
  <img src="https://github.com/madhucnghubphilips/AI-Security/blob/main/Resources/How%20LLM%20Works%20-%204%20ATTENTION%20MECHANISM.png" width="100%" alt="Attention Mechanism"/>
</p>

---

## 🔹 What is Attention?

Attention helps the model determine:

> Which words are most important for understanding the current word.

---

## 🔹 Example

Sentence:

```text
"What is cloud security?"
```

When understanding the word:

```text
security
```

The model may focus more on:

- cloud
- security

and less on:

- what
- is

---

## 🔹 Query, Key, and Value (QKV)

Each token creates 3 vectors:

| Component | Purpose |
|---|---|
| Query (Q) | What am I searching for? |
| Key (K) | What information do I contain? |
| Value (V) | What information should I provide? |

---

## 🔹 Attention Formula

```math
Attention(Q,K,V) = Softmax(QKᵀ / √dₖ)V
```

Where:

- `QKᵀ` → similarity score
- `Softmax` → converts scores into probabilities
- `√dₖ` → scaling factor
- `V` → actual information passed forward

---

## 🔹 Why Attention is Powerful

Attention allows LLMs to:

- Understand long-range relationships
- Maintain context
- Focus dynamically on important words
- Improve reasoning capability

---

# 4️⃣ Predicting Output

<p align="center">
  <img src="https://github.com/madhucnghubphilips/AI-Security/blob/main/Resources/How%20LLM%20Works%20-%205.png" width="100%" alt="Predicting Output"/>
</p>

---

## 🔹 Next Token Prediction

LLMs generate responses one token at a time.

Example:

Input:

```text
"What is cloud security?"
```

The model predicts probabilities for the next token:

| Token | Probability |
|---|---|
| protect | 0.31 |
| data | 0.25 |
| secure | 0.15 |
| manage | 0.07 |

The highest probability token is selected.

---

## 🔹 Iterative Generation

The selected token becomes part of the next input.

Example:

```text
What is cloud security ?
→ protect
→ data
→ is
→ stored
→ securely
```

Generation continues until:

```text
<eos> (End of Sequence)
```

---

# 5️⃣ Final Output

The generated tokens are combined into a human-readable response.

### Example Final Response

```text
Cloud security protects data, applications,
and infrastructure from unauthorized access,
threats, and breaches.
```

---

# 🔥 Key Concepts Summary

| Component | Purpose |
|---|---|
| Tokenization | Break text into tokens |
| Embeddings | Convert tokens into vectors |
| Transformer | Process relationships |
| Attention | Focus on important context |
| FFN | Learn deeper representations |
| Prediction | Generate next token |
| Decoding | Produce final response |

---

# 🎯 Why Transformers Changed AI

Transformers revolutionized AI because they:

- Process tokens in parallel
- Handle long-range dependencies
- Scale efficiently
- Learn contextual understanding
- Generate human-like responses

---

# 🛡️ Real-World Applications of LLMs

- AI Chatbots
- Code Generation
- Security Automation
- Threat Modeling
- Medical AI
- Search Engines
- Document Summarization
- AI Assistants
- Translation Systems
- Autonomous Agents

---

# ⚠️ Security Considerations in LLMs

Modern LLMs also introduce security risks such as:

- Prompt Injection
- Jailbreak Attacks
- Hallucinations
- Data Leakage
- Model Poisoning
- System Prompt Leakage
- Unbounded Consumption
- Vector Database Attacks

---

# 📚 Additional Learning Topics

- Embeddings
- Vector Databases
- RAG (Retrieval-Augmented Generation)
- Fine-Tuning
- Prompt Engineering
- Multi-Head Attention
- Positional Encoding
- Decoder-only Transformers
- Mixture of Experts (MoE)
- AI Security & OWASP Top 10 for LLMs

---

# 🏆 Final Takeaway

LLMs work by:

1. Breaking text into tokens  
2. Converting tokens into embeddings  
3. Processing them through transformer layers  
4. Using attention to understand context  
5. Predicting one token at a time  
6. Generating coherent human-like responses  

---

# 📷 Architecture Visuals

## LLM Internal Workflow

<p align="center">
  <img src="https://github.com/madhucnghubphilips/AI-Security/blob/main/Resources/How%20LLM%20Works%20-%201.png" width="100%"/>
</p>

---

## Detailed Transformer Workflow

<p align="center">
  <img src="https://github.com/madhucnghubphilips/AI-Security/blob/main/Resources/How%20LLM%20Works%20-%202.png" width="100%"/>
</p>

---

## Transformer + Attention Architecture

<p align="center">
  <img src="https://github.com/madhucnghubphilips/AI-Security/blob/main/Resources/How%20LLM%20Works%20-%203.png" width="100%"/>
</p>

---

## Attention Mechanism Deep Dive

<p align="center">
  <img src="https://github.com/madhucnghubphilips/AI-Security/blob/main/Resources/How%20LLM%20Works%20-%204%20ATTENTION%20MECHANISM.png" width="100%"/>
</p>

---

## Predicting Output & Final Response

<p align="center">
  <img src="https://github.com/madhucnghubphilips/AI-Security/blob/main/Resources/How%20LLM%20Works%20-%205.png" width="100%"/>
</p>

---

# 👨‍💻 Author

**AI Security | Application Security | DevSecOps | LLM Security**

Focused on:
- Secure AI
- AI Security Automation
- OWASP Top 10 for LLM
- Cloud & Kubernetes Security
- Secure SDLC
- Responsible AI

---

# ⭐ If you found this useful

- Star ⭐ the repository
- Share with the AI & Security community
- Contribute improvements
- Explore more AI Security learning content



In today’s AI-driven world, securing LLM applications is no longer optional — it is a critical business, privacy, and operational requirement. Organizations that proactively adopt AI Security, governance, and secure AI engineering practices will be better positioned to innovate safely, protect sensitive data, and maintain customer trust.


