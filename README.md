# ✈️ AI Flight Operations Intelligence System (AI_FOIS)

> An Agentic AI-powered aerospace engineering platform that combines **Retrieval-Augmented Generation (RAG), Semantic Search, Large Language Models, Vector Databases, and Intelligent Tool-Based Reasoning** to assist with aircraft maintenance, failure analysis, troubleshooting, and engineering decision support.

---

# 📖 Overview

The **AI Flight Operations Intelligence System (AI_FOIS)** is a production-style Artificial Intelligence project that demonstrates the complete lifecycle of an **Agentic AI application**, from aerospace document ingestion to intelligent engineering assistance.

Aircraft maintenance manuals contain thousands of pages of highly technical information. Engineers often spend significant time locating relevant procedures, understanding interconnected aircraft systems, and interpreting engineering documentation before making operational or maintenance decisions.

AI_FOIS was developed to demonstrate how modern Artificial Intelligence techniques—including **Retrieval-Augmented Generation (RAG), Semantic Search, Vector Databases, Large Language Models, and Agentic AI**—can transform static aerospace documentation into an intelligent engineering assistant.

Rather than functioning as a traditional chatbot, AI_FOIS retrieves relevant aerospace knowledge, reasons over technical documentation, invokes specialized engineering tools, and generates structured engineering reports to support maintenance and flight operations.

---

# ✨ Features

## 📚 Knowledge Engineering

* Aerospace document ingestion
* PDF parsing and processing
* Intelligent document chunking
* Metadata extraction
* Semantic embedding generation
* Vector database indexing

---

## 🤖 Generative AI

* Retrieval-Augmented Generation (RAG)
* Context-aware response generation
* Grounded engineering responses
* Large Language Model integration

---

## 🧠 Agentic AI

* Aerospace AI Agent
* Intelligent tool orchestration
* Multi-stage reasoning pipeline
* Tool-based engineering analysis

---

## 🔧 Engineering Decision Support

* Failure Classification
* Failure Analysis
* Root Cause Analysis
* Risk Assessment
* Maintenance Recommendations
* Troubleshooting Assistance
* Flight Impact Analysis
* System Dependency Analysis
* Procedure Advisory
* Engineering Report Generation

---

# 🏗️ System Architecture

```text
Aircraft Technical Documents
           │
           ▼
    Document Ingestion
           │
           ▼
    Chunking and Embeddings
           │
           ▼
     Chroma Vector Database
           │
           ▼
      Semantic Retrieval
           │
           ▼
     Context Construction
           │
           ▼
      Local LLM (Ollama: llama3 by default)
           │
           ▼
  Aerospace Agent for failures
           │
           ▼
 Specialized Python tools
           │
           ▼
 Structured Engineering Report
```

---

# 📸 Application Screenshots

The current Streamlit interface includes the following workflows:

![AI-FOIS home dashboard](docs/images/home.png)

![AI-FOIS Ask AI page](docs/images/Ask_AI_FOIS.png)

![AI-FOIS failure analysis page](docs/images/failure_analysis.png)

![AI-FOIS maintenance advisor](docs/images/maintenance_advisor.png)

![AI-FOIS engineering reports](docs/images/engineering_reports.png)

![AI-FOIS history page](docs/images/history.png)

![AI-FOIS about page](docs/images/about.png)

---

# ⚙️ AI Pipeline

## 1. Document Ingestion

* PDF loading
* Multi-document processing
* Metadata extraction

---

## 2. Knowledge Processing

* Intelligent document chunking
* Chunk metadata generation
* JSON serialization

---

## 3. Embedding Generation

* SentenceTransformer embeddings
* Batch embedding generation
* NumPy embedding storage

---

## 4. Knowledge Indexing

* ChromaDB vector database
* Semantic indexing
* Metadata storage

---

## 5. Semantic Retrieval

* Similarity search
* Top-K retrieval
* Context construction

---

## 6. Large Language Model

* Retrieval-Augmented Generation
* Ollama model configured through `LLM_MODEL` (`llama3` by default)
* Grounded response generation

---

## 7. Aerospace AI Agent

The Aerospace Agent orchestrates multiple engineering tools to perform intelligent aerospace reasoning.

### Agent Workflow

```text
User Question
      │
      ▼
Intent Analysis
      │
      ▼
Knowledge Retrieval
      │
      ▼
LLM Reasoning
      │
      ▼
Engineering Tool Selection
      │
      ▼
Engineering Analysis
      │
      ▼
Engineering Report
```

---

# 🔧 Engineering Tools

## Failure Classification

Identifies the aircraft system involved in a reported failure scenario.

---

## Failure Analysis

Analyzes failure conditions using retrieved aerospace documentation.

---

## Root Cause Analysis

Determines possible causes contributing to aircraft system failures.

---

## Risk Assessment

Evaluates operational severity and potential safety impact.

---

## Maintenance Advisor

Generates maintenance recommendations based on engineering evidence.

---

## Troubleshooting Advisor

Suggests diagnostic procedures to isolate faults efficiently.

---

## Flight Impact Analyzer

Evaluates how component failures affect aircraft performance and flight operations.

---

## System Dependency Analyzer

Identifies interconnected aircraft systems that may be affected by component failures.

---

## Procedure Advisor

Recommends engineering procedures and operational actions.

---

## Engineering Report Generator

Produces structured aerospace engineering reports by combining AI-generated reasoning with deterministic engineering analysis.

---

# 🧠 Artificial Intelligence Technologies

## Retrieval-Augmented Generation (RAG)

Retrieves relevant aerospace documentation before generating responses, reducing hallucinations and improving factual accuracy.

---

## Semantic Search

Uses dense vector embeddings to locate conceptually similar engineering information rather than relying on keyword matching.

---

## Agentic AI

Coordinates multiple engineering tools through an intelligent Aerospace Agent capable of selecting appropriate analysis workflows.

---

## Tool Calling

Delegates specialized engineering tasks to dedicated tools such as failure analysis, risk assessment, and maintenance recommendation modules.

---

## Large Language Models

Uses the Ollama model configured through `LLM_MODEL` to generate grounded engineering explanations. The current default is `llama3`; Gemma is not configured in this repository.

---

## Vector Database

Stores semantic document embeddings using ChromaDB for efficient similarity search and retrieval.

---

# 📂 Aerospace Knowledge Base

The system processes aerospace references covering topics including:

* Aircraft Systems
* Flight Operations
* Aerodynamics
* Aircraft Performance
* Flight Controls
* Hydraulic Systems
* Fuel Systems
* Aircraft Stability
* Aircraft Maintenance

Technical documents are transformed into semantic chunks and indexed for efficient retrieval.

---

# 🛠️ Technology Stack

## Programming Language

* Python

---

## Artificial Intelligence

* Agentic AI
* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Tool Calling
* Prompt Engineering

---

## Large Language Models

* Ollama
* Ollama model configured through `LLM_MODEL` (default: `llama3`)

---

## Embedding Models

* SentenceTransformers

---

## Vector Database

* ChromaDB

---

## Document Processing

* PyMuPDF

---

## Scientific Computing

* NumPy

---

## Web Application

* Streamlit

---

# 📁 Project Structure

```text
AI_FOIS/

├── app/
│   ├── assets/
│   ├── components/
│   └── runtime.py

├── pages/
│   ├── 1_Home.py
│   ├── 2_Upload_Documents.py
│   ├── 3_Ask_AI.py
│   ├── 4_Failure_Analysis.py
│   ├── 5_Maintenance_Advisor.py
│   ├── 6_Engineering_Reports.py
│   ├── 7_History.py
│   └── 8_About.py

├── data/
│   ├── documents/
│   └── processed/

├── docs/

├── scripts/

├── src/
│   ├── agents/
│   ├── database/
│   ├── embeddings/
│   ├── generation/
│   ├── ingestion/
│   ├── retrieval/
│   ├── services/
│   └── tools/

├── database/
│   └── schema.sql

├── vector_db/

├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/AI_FOIS.git
```

---

## Navigate to Project

```bash
cd AI_FOIS
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Build the Knowledge Base

## Ingest Documents

```bash
python -m scripts.ingest_documents
```

## Build Document Chunks

```bash
python -m scripts.build_chunks
```

## Build Vector Database

```bash
python -m scripts.build_vector_db
```

---

# 🤖 Run the Streamlit application

```bash
streamlit run streamlit_app.py
```

For the optional console assistant:

```bash
python -m scripts.ask_ai_fois
```

---

# 📊 Evaluation

Evaluate retrieval performance.

```bash
python -m scripts.evaluate_retrieval
```

Test semantic retrieval.

```bash
python -m scripts.test_retrieval
```

---

# 🛠️ Engineering Challenges Solved

* Processed thousands of pages of aerospace documentation into semantic knowledge chunks.
* Built an end-to-end Retrieval-Augmented Generation pipeline for aerospace engineering.
* Implemented batched vector indexing to overcome ChromaDB insertion limits.
* Designed a modular Agentic AI architecture with specialized engineering tools.
* Reduced hallucinations by grounding responses in retrieved aerospace documentation.
* Combined deterministic engineering analysis with LLM reasoning to generate structured engineering reports.

---

# 🎯 Future Improvements

* Multi-agent collaboration
* Hybrid semantic and keyword retrieval
* Cross-document reasoning
* FAA maintenance manual integration
* Interactive engineering dashboard
* FastAPI REST API
* Docker containerization
* Cloud deployment
* Aircraft Digital Twin integration
* Vision-based document understanding
* Fine-tuned aerospace language model

---

# 👨‍💻 Author

**Kamalisri Bera**

AI Engineering • Software Engineering • Aerospace Engineering

---

# 📜 License

This project is released under the **MIT License**.

---

# ⭐ Acknowledgements

* FAA Pilot's Handbook of Aeronautical Knowledge
* Introduction to Flight
* Fundamentals of Aerodynamics
* Aircraft Systems by Ian Moir & Allan Seabridge
* Hugging Face SentenceTransformers
* ChromaDB
* Ollama
* Ollama model configured through `LLM_MODEL` (default: `llama3`)
* Streamlit
