# Engineering Decisions

## Flight Operations Intelligent System (FOIS)

This document explains the major technical and architectural decisions made during the development of the Flight Operations Intelligent System (FOIS).

The purpose of this document is to document the reasoning behind the system architecture, Retrieval-Augmented Generation (RAG) pipeline, AI agent design, tool-calling framework, vector database implementation, and software engineering decisions adopted throughout the project.

---

# 1. Project Architecture Decision

## Decision

The project was structured into independent modules:

```text
app/
src/
data/
database/
embeddings/
generation/
retrieval/
agents/
tools/
results/
tests/
docs/
```

---

## Reason

As the project evolved beyond a simple chatbot into an intelligent aerospace assistant, it became necessary to separate responsibilities into dedicated modules.

The application includes:

- document ingestion
- text processing
- embedding generation
- vector storage
- semantic retrieval
- language model inference
- AI agent orchestration
- engineering tool execution
- Streamlit interface

Separating these components improves:

- maintainability
- scalability
- readability
- debugging
- future extensibility

---

## Alternative Considered

Implementing the complete application inside a single Python script.

---

## Why It Was Not Selected

A monolithic implementation tightly couples retrieval, generation, user interface, and engineering logic, making the system difficult to maintain and extend.

---

## Future Improvement

The architecture can later evolve into:

```text
Frontend

↓

API Layer

↓

Agent Orchestrator

↓

RAG Service

↓

LLM Service

↓

Vector Database

↓

Monitoring & Logging
```

---

# 2. Decision: Choosing Retrieval-Augmented Generation (RAG)

## Decision

The system uses a Retrieval-Augmented Generation (RAG) architecture instead of relying solely on a language model.

---

## Reason

Aircraft maintenance documentation is extensive and continuously updated.

Retrieval allows the language model to access relevant information at query time instead of memorizing documents during training.

Benefits include:

- grounded responses
- improved factual accuracy
- reduced hallucinations
- support for updated documentation without retraining

---

## Alternative Considered

Fine-tuning a language model on aerospace manuals.

---

## Why It Was Not Selected

Fine-tuning requires significant computational resources and retraining whenever documentation changes.

RAG provides a more flexible and maintainable solution.

---

## Future Improvement

Hybrid retrieval combining semantic search and keyword search can further improve document retrieval quality.

---

# 3. Decision: Choosing a Local Language Model

## Decision

A locally hosted language model was selected for inference.

---

## Reason

Running inference locally provides:

- offline capability
- improved privacy
- lower operational cost
- greater control over the inference pipeline

This is particularly important when working with technical aerospace documentation.

---

## Alternative Considered

Cloud-hosted proprietary language models.

---

## Why It Was Not Selected

Cloud services introduce:

- recurring operational costs
- internet dependency
- privacy concerns
- limited control over inference behavior

---

## Future Improvement

Support multiple interchangeable LLM backends through a unified inference interface.

---

# 4. Decision: Choosing ChromaDB as the Vector Database

## Decision

ChromaDB was selected as the vector database.

---

## Reason

The system requires efficient storage and retrieval of document embeddings.

ChromaDB provides:

- persistent vector storage
- metadata filtering
- fast similarity search
- simple Python integration

---

## Alternative Considered

- FAISS
- Pinecone
- Weaviate
- Milvus

---

## Why It Was Not Selected

For a local educational project, ChromaDB provides sufficient performance without requiring additional infrastructure.

---

## Future Improvement

Migration to distributed vector databases for large-scale deployments.

---

# 5. Decision: Semantic Document Chunking

## Decision

Technical documents are divided into overlapping text chunks before embedding generation.

---

## Reason

Large language models have limited context windows.

Chunking enables:

- efficient retrieval
- improved semantic matching
- manageable embedding sizes

Overlapping chunks preserve contextual continuity between adjacent sections.

---

## Alternative Considered

Embedding complete PDF documents as a single vector.

---

## Why It Was Not Selected

Entire manuals exceed embedding model limitations and reduce retrieval precision.

---

## Engineering Principle

> Documents should be divided into semantically meaningful chunks to maximize retrieval accuracy while preserving contextual information.

---

# 6. Decision: Using Sentence Transformer Embeddings

## Decision

Sentence Transformer models were selected for embedding generation.

---

## Reason

Sentence Transformers generate dense semantic representations that capture contextual meaning rather than relying solely on keyword matching.

Benefits include:

- semantic similarity search
- robust retrieval
- efficient inference
- compatibility with vector databases

---

## Alternative Considered

- TF-IDF
- Bag-of-Words
- Keyword indexing

---

## Why It Was Not Selected

Traditional lexical methods cannot capture semantic relationships between engineering concepts.

---

# 7. Decision: Grounding Responses with Retrieved Context

## Decision

The language model is instructed to answer only using retrieved aerospace documentation.

---

## Reason

Large language models may generate plausible but incorrect information when operating without supporting context.

Grounding responses improves:

- factual consistency
- engineering reliability
- transparency
- user trust

---

## Alternative Considered

Allowing unrestricted language model generation.

---

## Why It Was Not Selected

Ungrounded generation increases the likelihood of hallucinated maintenance procedures and inaccurate technical guidance.

---

# 8. Decision: Tool Calling Architecture

## Decision

The language model delegates specialized engineering tasks to dedicated tools.

---

## Reason

Language models excel at natural language generation but complex engineering reasoning benefits from structured task decomposition.

Dedicated tools provide deterministic outputs for specific responsibilities.

Examples include:

- Failure Classifier
- Risk Assessor
- Maintenance Advisor
- Root Cause Analyzer
- System Dependency Analyzer
- Flight Impact Analyzer
- Procedure Advisor
- Troubleshooting Agent
- Report Generator

---

## Alternative Considered

Allowing the language model to perform all engineering reasoning internally.

---

## Why It Was Not Selected

Separating responsibilities improves modularity, explainability, and maintainability.

---

## Engineering Principle

> Each engineering task should have one clearly defined responsibility.

---

# 9. Decision: Multi-Agent Architecture

## Decision

FOIS adopts an agent-based architecture where specialized AI agents collaborate to solve complex aerospace maintenance tasks.

---

## Reason

Aircraft maintenance involves multiple reasoning stages that are easier to manage when divided among independent agents.

Examples include:

- Failure Classifier
- Root Cause Analyzer
- Risk Assessor
- System Dependency Analyzer
- Flight Impact Analyzer
- Procedure Advisor
- Troubleshooting Agent
- Report Generator

---

## Alternative Considered

Using a single general-purpose conversational agent.

---

## Why It Was Not Selected

A monolithic agent becomes increasingly difficult to maintain as engineering reasoning grows more complex.

---

## Future Improvement

Dynamic agent orchestration with collaborative multi-agent workflows.

---

# 10. Decision: Choosing Streamlit for the User Interface

## Decision

Streamlit was selected for application development.

---

## Reason

The primary objective was to demonstrate AI engineering rather than frontend development.

Streamlit enables:

- rapid prototyping
- seamless Python integration
- interactive dashboards
- visualization support

---

## Alternative Considered

React + FastAPI.

---

## Why It Was Not Selected

Developing a complete frontend would increase project complexity without contributing directly to the project's AI objectives.

---

## Future Improvement

The Streamlit interface can later be replaced with:

- React
- Angular
- Mobile applications

while keeping the AI backend unchanged.

---

# 11. Decision: Separating Retrieval and Generation

## Decision

The retrieval pipeline and language generation pipeline were implemented as independent components.

---

## Reason

Separating these stages allows individual components to be replaced without affecting the remainder of the system.

Examples include:

- replacing the embedding model
- changing the vector database
- switching to another language model

---

## Engineering Principle

> Retrieval should locate knowledge, while generation should explain it.

---

# 12. Decision: Persistent Conversation and Report Storage

## Decision

The system stores generated engineering reports and user interactions in a local database.

---

## Reason

Persistent storage enables:

- report history
- auditing
- future analytics
- engineering documentation

---

## Alternative Considered

Displaying responses without storing them.

---

## Why It Was Not Selected

Generated reports would be lost after application shutdown.

---

# 13. Decision: Structured Engineering Report Generation

## Decision

Instead of returning plain conversational responses, FOIS generates structured engineering reports.

---

## Reason

Maintenance engineers require organized technical documentation rather than conversational text.

Structured reports improve:

- readability
- traceability
- documentation quality
- maintenance workflow integration

---

## Alternative Considered

Returning conversational AI responses only.

---

## Why It Was Not Selected

Conversational responses are difficult to archive, reference, and integrate into engineering workflows.

---

# 14. Overall Engineering Philosophy

The primary engineering principle followed throughout the development of FOIS was:

> Build an intelligent aerospace assistant that is modular, explainable, maintainable, and grounded in reliable technical knowledge rather than relying solely on the reasoning capabilities of a language model.

Every architectural decision was guided by balancing:

- AI engineering principles
- aerospace domain requirements
- maintainability
- scalability
- modular software design
- factual reliability
- future extensibility

The final system demonstrates the complete journey from raw aerospace documentation to an intelligent Retrieval-Augmented Generation system capable of supporting aircraft maintenance engineers through grounded AI reasoning and specialized engineering agents.