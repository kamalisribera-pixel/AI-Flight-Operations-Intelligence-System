# Engineering Decisions

AI_FOIS was designed as an engineering system rather than a simple LLM application. Each major architectural decision was made by considering the problem being solved, available alternatives, engineering trade-offs, maintainability, and future scalability.

## 1. Modular Architecture

**Decision:**
The system is divided into independent modules for document ingestion, processing, embeddings, vector storage, retrieval, generation, agents, tools, results, testing, and the application layer.

**Why:**
FOIS evolved beyond a simple chatbot into an aerospace intelligence system with multiple responsibilities. Separating these responsibilities makes the system easier to maintain, debug, test, and extend.

**Alternative considered:**
A single Python application containing the complete pipeline.

**Why rejected:**
A monolithic implementation would tightly couple the UI, retrieval, generation, and engineering logic, making future changes increasingly difficult.

**Future direction:**
The architecture can evolve toward:

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

## 2. Retrieval-Augmented Generation (RAG)

**Decision:**
FOIS uses Retrieval-Augmented Generation rather than relying solely on the language model's internal knowledge.

**Why:**
Aerospace maintenance documentation is large and continuously updated. Retrieving relevant information at query time allows the system to work with current technical documentation without retraining the language model.

**Benefits:**

* Grounded responses
* Improved factual consistency
* Reduced hallucination risk
* Documentation updates without model retraining

**Alternative considered:**
Fine-tuning a language model on aerospace manuals.

**Why rejected:**
Fine-tuning introduces additional computational requirements and would require retraining when documentation changes.

**Future direction:**
Introduce hybrid retrieval combining semantic search with keyword-based retrieval.

---

## 3. Local Language Model

**Decision:**
FOIS uses a locally hosted language model for inference.

**Why:**
Local inference provides greater control over the inference pipeline while supporting offline operation, privacy, and reduced dependence on external services.

**Alternative considered:**
Cloud-hosted proprietary LLM APIs.

**Why rejected:**

* Internet dependency
* Recurring operational costs
* Privacy considerations
* Less control over inference infrastructure

**Future direction:**
Create a unified LLM interface allowing multiple interchangeable model backends.

---

## 4. ChromaDB for Vector Storage

**Decision:**
ChromaDB was selected as the vector database.

**Why:**
FOIS requires persistent storage and similarity retrieval of document embeddings. ChromaDB provides a Python-friendly solution with persistent vector storage, metadata filtering, and similarity search.

**Alternatives considered:**

* FAISS
* Pinecone
* Weaviate
* Milvus

**Why ChromaDB:**
For the project's local and educational deployment requirements, ChromaDB provides the required functionality without introducing additional distributed infrastructure.

**Future direction:**
Evaluate distributed vector databases for larger-scale deployments.

---

## 5. Semantic Document Chunking

**Decision:**
Documents are divided into overlapping text chunks before embedding.

**Why:**
Embedding an entire technical manual as a single vector would reduce retrieval precision. Smaller semantic chunks allow the retrieval system to identify relevant sections more accurately.

Overlap is used to preserve contextual continuity between adjacent sections.

**Alternative considered:**
Embedding complete documents as individual vectors.

**Why rejected:**
Large documents can exceed embedding constraints and make retrieval less precise.

**Engineering principle:**

> Divide documents into semantically meaningful units while preserving enough surrounding context for accurate retrieval.

---

## 6. Sentence Transformer Embeddings

**Decision:**
Sentence Transformer models are used to generate document embeddings.

**Why:**
The system requires semantic retrieval rather than simple keyword matching. Dense embeddings allow related engineering concepts to be matched even when the exact words differ.

**Alternatives considered:**

* TF-IDF
* Bag-of-Words
* Keyword indexing

**Why rejected:**
Traditional lexical approaches have limited ability to capture semantic relationships between technical concepts.

---

## 7. Grounded Generation

**Decision:**
The language model is instructed to generate responses using retrieved aerospace documentation as supporting context.

**Why:**
LLMs can generate plausible but incorrect information when operating without supporting evidence. Grounding constrains the generation process around retrieved technical information.

**Benefits:**

* Better factual consistency
* Improved engineering reliability
* Greater transparency
* Increased user trust

**Alternative considered:**
Unrestricted LLM generation.

**Why rejected:**
For an aerospace-oriented system, unrestricted generation could produce unsupported maintenance or troubleshooting information.

---

## 8. Tool-Calling Architecture

**Decision:**
Specialized engineering tasks are delegated to dedicated tools rather than requiring the LLM to perform every task internally.

**Why:**
Language models are effective at language understanding and generation, while deterministic or specialized engineering operations benefit from explicit task boundaries.

**Implemented capabilities include:**

* Failure Classification
* Risk Assessment
* Maintenance Recommendation
* Root Cause Analysis
* System Dependency Analysis
* Flight Impact Analysis
* Procedure Recommendation
* Troubleshooting
* Engineering Report Generation

**Alternative considered:**
One general-purpose LLM performing all engineering reasoning.

**Why rejected:**
Separating responsibilities improves modularity, maintainability, and explainability.

**Engineering principle:**

> Each engineering task should have one clearly defined responsibility.

---

## 9. Multi-Agent Architecture

**Decision:**
FOIS uses specialized AI agents for different stages of aerospace engineering analysis.

**Why:**
Aircraft maintenance problems can involve multiple reasoning stages. Dividing these responsibilities allows each agent to focus on a specific task.

**Example workflow:**

```text
User Problem
     ↓
Failure Classifier
     ↓
Root Cause Analyzer
     ↓
Risk Assessor
     ↓
System Dependency Analyzer
     ↓
Flight Impact Analyzer
     ↓
Procedure Advisor
     ↓
Report Generator
```

**Alternative considered:**
A single conversational agent handling the complete workflow.

**Why rejected:**
A monolithic agent becomes increasingly difficult to reason about, test, maintain, and extend as system complexity grows.

**Future direction:**
Dynamic agent orchestration for more complex collaborative workflows.

---

## 10. Streamlit Interface

**Decision:**
Streamlit was selected for the initial application interface.

**Why:**
The primary engineering objective was to demonstrate the AI system rather than spend the majority of development effort on frontend infrastructure.

Streamlit provides:

* Rapid Python-based development
* Interactive interfaces
* Visualization support
* Direct integration with the AI pipeline

**Alternative considered:**
React + FastAPI.

**Why rejected:**
A separate frontend would increase implementation complexity without directly improving the core AI engineering capabilities being demonstrated.

**Future direction:**
The interface can be replaced with a production frontend while keeping the AI backend modular.

---

## 11. Separation of Retrieval and Generation

**Decision:**
Retrieval and language generation are implemented as independent components.

**Why:**
This creates clear boundaries between knowledge retrieval and language generation.

It also allows individual components to be replaced independently.

For example:

```text
Embedding Model
      ↓
Vector Database
      ↓
Retrieval
      ↓
Context
      ↓
LLM
      ↓
Generation
```

The embedding model, vector database, or language model can therefore be changed without redesigning the entire system.

**Engineering principle:**

> Retrieval locates knowledge; generation explains it.

---

## 12. Persistent Storage

**Decision:**
FOIS stores generated engineering reports and user interactions in a local database.

**Why:**
Persistence enables:

* Report history
* Auditing
* Future analytics
* Engineering documentation

**Alternative considered:**
Displaying responses without storing them.

**Why rejected:**
Generated engineering reports would be lost when the application shuts down.

---

## 13. Structured Engineering Reports

**Decision:**
FOIS generates structured engineering reports instead of returning only conversational responses.

**Why:**
Engineering workflows require organized, traceable, and reusable technical documentation.

Structured reports improve:

* Readability
* Traceability
* Documentation quality
* Workflow integration

**Output formats include:**

```text
Engineering Analysis
├── PDF
├── Markdown
└── JSON
```

**Alternative considered:**
Returning conversational responses only.

**Why rejected:**
Conversational responses are harder to archive, reference, audit, and integrate into engineering workflows.

---

# Engineering Philosophy

The central engineering philosophy behind AI_FOIS is:

> **Build an intelligent aerospace assistant that is modular, explainable, maintainable, and grounded in reliable technical knowledge rather than relying solely on the reasoning capabilities of a language model.**

The architecture balances:

* AI engineering
* Aerospace domain requirements
* Software modularity
* Maintainability
* Scalability
* Factual reliability
* Explainability
* Future extensibility

The result is an end-to-end system that transforms aerospace documentation into a retrieval-grounded AI workflow capable of supporting specialized engineering analysis and structured reporting.
