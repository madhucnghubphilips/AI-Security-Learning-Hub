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



# Embeddings + Positions and Transformer (Attention + FFN)

This document explains how input text is converted into vectors, enriched with positional information, and processed by a Transformer block using **Multi-Head Self-Attention**, **Feed-Forward Networks (FFN)**, **Residual Connections**, and **Layer Normalization**.

> Example question used across the visuals: **“What is cloud Security?”**

---

## 1. End-to-End View: Embeddings + Positions → Transformer

The full flow starts with input tokens, converts each token into a vector, adds positional encodings, and sends the result into the Transformer block.

<p align="center">
  <img src="[https://github.com/madhucnghubphilips/AI-Security/blob/main/Resources/1)Embedding%20Positions%20and%20Transformer%20(AttentionFFN).png]" alt="Embeddings, Positions and Transformer Attention FFN Overview" width="100%" />
</p>

### Key Points

- **Token embeddings** capture the meaning of each token.
- **Position encodings** capture the order of tokens in the sentence.
- **Embedding + position vectors** become the input to the Transformer.
- **Self-attention** helps each token understand other relevant tokens.
- **FFN** refines each token representation independently.
- **Residual connections + layer normalization** stabilize training and preserve information.

---

## 2. Token Embeddings

Token embeddings convert each word/token into a dense numerical vector. These vectors are learned during model training.

For example, the sentence:

```text
What is cloud Security?
```

is tokenized as:

```text
[What, is, cloud, Security, ?]
```

Each token is mapped to a vector of size `d_model = 6` in this simplified example.

<p align="center">
  <img src="https://github.com/madhucnghubphilips/AI-Security/blob/main/Resources/2) TOKEN EMBEDDINGS(1).png" alt="Token Embeddings Example" width="100%" />
</p>

### Interpretation

- Each row represents the learned vector for one token.
- Similar words usually have closer vector representations.
- Embeddings capture semantic meaning, but they do **not** capture token order by themselves.

---

## 3. Position Encodings

Position encodings add order information to the model. Without position encodings, the model may know the token meanings but not where each token appears in the sentence.

<p align="center">
  <img src="https://github.com/madhucnghubphilips/AI-Security/blob/main/Resources/3) POSITION ENCODINGS(1).png" alt="Position Encodings Heatmap and Explanation" width="100%" />
</p>

### Why Position Encoding Is Needed

For the sentence:

```text
What is cloud Security?
```

The model must know:

- `What` is at position 1
- `is` is at position 2
- `cloud` is at position 3
- `Security` is at position 4
- `?` is at position 5

Position encoding injects this order information into the input vector.

---

## 3.1 Sinusoidal Position Encoding

The original Transformer uses fixed sinusoidal functions for positional encoding.

<p align="center">
  <img src="https://github.com/madhucnghubphilips/AI-Security/blob/main/Resources/3.1) POSITION ENCODINGS(1).png" alt="Sinusoidal Position Encoding Formula and Matrix" width="100%" />
</p>

### Formula

For even dimensions:

```text
PE(pos, 2i) = sin(pos / 10000^(2i / d_model))
```

For odd dimensions:

```text
PE(pos, 2i + 1) = cos(pos / 10000^(2i / d_model))
```

Where:

- `pos` = token position
- `i` = dimension pair index
- `d_model` = embedding dimension

### Interpretation

- Even dimensions use `sin()`.
- Odd dimensions use `cos()`.
- Different dimensions use different frequencies.
- This helps the model learn both short-range and long-range token order relationships.

---

## 3.2 Step-by-Step Position Encoding Calculation

This visual explains the positional encoding calculation step by step using `d_model = 6`.

<p align="center">
  <img src="https://github.com/madhucnghubphilips/AI-Security/blob/main/Resources/3.2) POSITION ENCODINGS with Example(1).png" alt="Step-by-Step Sinusoidal Position Encoding Calculation" width="100%" />
</p>

### Calculation Flow

1. Set embedding dimension: `d_model = 6`.
2. Define dimension indexes: `0, 1, 2, 3, 4, 5`.
3. Compute frequency terms.
4. Compute angles using position and frequency.
5. Apply `sin()` for even dimensions.
6. Apply `cos()` for odd dimensions.
7. Build the final positional encoding matrix.

### Key Takeaway

Position encoding creates a unique vector for each position. This vector is added to the token embedding before sending the input to the Transformer.

---

## 4. Embedding + Position

The final input vector to the Transformer is created by adding the token embedding and the position encoding element by element.

```text
xᵢ = eᵢ + pᵢ
```

Where:

- `eᵢ` = learned token embedding
- `pᵢ` = positional encoding
- `xᵢ` = final input vector to the Transformer

<p align="center">
  <img src="https://github.com/madhucnghubphilips/AI-Security/blob/main/Resources/4) EMBEDDING + POSITION(1).png" alt="Embedding Plus Position Input to Transformer" width="100%" />
</p>

### Interpretation

- `eᵢ` tells the model what the token means.
- `pᵢ` tells the model where the token is located.
- `xᵢ` gives the model both meaning and order.

---

## 5. Transformer Block Summary

After embedding and position information are combined, the vectors are passed into the Transformer block.

### Multi-Head Self-Attention

Self-attention allows each token to look at all other tokens and decide which ones are most important for context.

Example:

For the token **cloud**, the model may pay more attention to:

- **Security** because it defines the context
- **is** because it helps sentence structure
- **What** because it indicates a question

### Feed-Forward Network

The FFN is applied independently to each token position. It refines the contextual representation created by attention.

### Residual Connection + Layer Normalization

These improve training stability and help preserve the original information while adding learned transformations.

---

## Final Summary

```text
Input Text
   ↓
Tokens
   ↓
Token Embeddings
   ↓
Position Encodings
   ↓
Embedding + Position
   ↓
Transformer Block
   ↓
Contextualized Output Vectors
```

The final output vectors understand both:

- the **meaning** of each token, and
- the **context** of the full sentence.

---

## Image Tags for GitHub Markdown

```html
<img src="https://github.com/madhucnghubphilips/AI-Security/blob/main/Resources/1) Embedding Positions and Transformer (Attention + FFN)(1).png" alt="Embeddings, Positions and Transformer Attention FFN Overview" width="100%" />
<img src="https://github.com/madhucnghubphilips/AI-Security/blob/main/Resources/2) TOKEN EMBEDDINGS(1).png" alt="Token Embeddings Example" width="100%" />
<img src="https://github.com/madhucnghubphilips/AI-Security/blob/main/Resources/3) POSITION ENCODINGS(1).png" alt="Position Encodings Heatmap and Explanation" width="100%" />
<img src="https://github.com/madhucnghubphilips/AI-Security/blob/main/Resources/3.1) POSITION ENCODINGS(1).png" alt="Sinusoidal Position Encoding Formula and Matrix" width="100%" />
<img src="https://github.com/madhucnghubphilips/AI-Security/blob/main/Resources/3.2) POSITION ENCODINGS with Example(1).png" alt="Step-by-Step Sinusoidal Position Encoding Calculation" width="100%" />
<img src="https://github.com/madhucnghubphilips/AI-Security/blob/main/Resources/4) EMBEDDING + POSITION(1).png" alt="Embedding Plus Position Input to Transformer" width="100%" />
```






In today’s AI-driven world, securing LLM applications is no longer optional — it is a critical business, privacy, and operational requirement. Organizations that proactively adopt AI Security, governance, and secure AI engineering practices will be better positioned to innovate safely, protect sensitive data, and maintain customer trust.


