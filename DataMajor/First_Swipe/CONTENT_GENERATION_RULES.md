# Content Generation Rules — First Swipe

## 1. Interaction Trigger
The user will request content using the following short-code format:
`<TOPIC_NAME> <TYPE> <DOC_NUMBER>`

*   **TOPIC_NAME**: The technology or concept (e.g., `FLINK`, `SPARK`).
*   **TYPE**: `A` (Concepts) or `B` (Interview Questions).
*   **DOC_NUMBER**: The sequential ID (e.g., `00015`).

**Example**: `<FLINK> <B> <00015>`

---

## 2. Type A: High-Level Concepts
*   **Filename**: `<DOC_NUMBER>.<TopicName>.md` (e.g., `00015.Flink.md`)
*   **Title**: `# <Topic Name>` followed by `### The English Version`.
*   **Tone**: "Plain English," conversational but professional. Focus on *why* it exists before *how* it works. Use Capital One (financial services) analogies where possible.

### Structure
1.  **What is it and Why Does it Exist?**
    *   Start with the problem it solves (e.g., "Manual scaling was impossible...").
    *   Explain the historical context if relevant (e.g., "Google Borg", "LinkedIn Kafka").
2.  **Core Concepts in Plain English**
    *   Define key terms (Nodes, Pods, Brokers, etc.) using simple analogies.
    *   **Formatting**: **Bold** terms, standard text definitions.
3.  **Architecture / Deep Dive**
    *   Explain the internal mechanics (Control Plane, Leader/Follower, etc.).
4.  **<Topic> at Capital One**
    *   Specific use cases (Fraud Detection, Transaction Processing, Regulatory Reporting).
    *   Mention specific AWS managed services if applicable (EKS, MSK, EMR).
5.  **Comparison Table**
    *   Contrast with the "Old Way" or alternative technologies.
    *   Use Markdown tables.

### Visuals
*   Use ASCII diagrams for architectural flows.
*   **Style**: Use box drawing characters (`╔`, `═`, `║`, `╚`) for clean, professional borders.
*   **Alignment**: Ensure lines match up perfectly.

---

## 3. Type B: Top Interview Questions
*   **Filename**: `<DOC_NUMBER>.<TopicName>.Q.md` (e.g., `00015.Flink.Q.md`)
*   **Title**: `# Mock Interview — <Topic Name>`

### Question Levels
Progress through these levels as appropriate for the topic:
1.  **Beginner Level** (Definitions, basic concepts)
2.  **Warming Up** (Why use it, basic architecture)
3.  **Getting Serious** (Trade-offs, specific scenarios)
4.  **Data Engineer Level** (Production patterns, failure handling)
5.  **Lead Data Engineer Level** (System design, multi-technology integration)
6.  **Final Boss** (Deep internals, obscure edge cases, optimization)

### Structure Per Question
Each question **MUST** follow this exact format:

#### 1. The Question
*   Header: `## Question X — <Level>`
*   Bold text of the question.

#### 2. Feedback First
*   Header: `# Feedback First`
*   **Subheader**: `## What You Nailed ✅`
    *   Bullet points highlighting good parts of a potential answer (simulated).
*   **Subheader**: `## What to Tighten Up 🔧`
    *   Bullet points highlighting missing depth, nuance, or specific keywords.
    *   Use *italicized text* to explain the missing concept.

#### 3. Model Answer
*   Header: `# Model Answer`
*   Use a separator `---`.
*   Provide a spoken-word, professional answer (Lead Engineer persona).
*   Include "Capital One" context/examples (e.g., "At Capital One, we would use...").

#### 4. Diagrams
*   Header: `# Diagrams`
*   ASCII art illustrating the specific concept discussed in the answer.
*   **Style**: Strict box-drawing characters for clean tables and flows.

---

## 4. General Formatting Guidelines
*   **Separators**: Use `---` between major sections.
*   **Diagrams**: meaningful ASCII diagrams.
    *   Example:
        ```text
        ╔════════════════════╗
        ║  Concept           ║
        ╚══════════╦═════════╝
                   ▼
        ```
*   **Tone**: Authoritative yet accessible. Mentor-like.
