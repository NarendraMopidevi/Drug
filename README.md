# Drug Discovery & Drug Information Copilot

### Project Overview

**Drug Discovery & Drug Information Copilot** is a **GenAI-powered Life Sciences research assistant**. It helps users search and understand information about **drugs, compounds, biological targets, diseases, and research papers**.

The system combines **Python, FastAPI, Streamlit, LLMs, and RAG** to retrieve scientific information and generate easy-to-understand answers.

It is designed for **research and educational purposes**, not for medical diagnosis or treatment recommendations.

### Main Features

* Search for drug/compound information
* Retrieve molecular and chemical properties
* Find drug targets and biological activity
* Search research papers
* Ask questions about drugs using an LLM
* Compare drugs or compounds
* Upload research papers/PDFs and ask questions
* Summarize scientific documents
* Use RAG to provide answers based on retrieved information
* Provide source/evidence information with answers

### System Architecture

```text
User
  ↓
Streamlit UI
  ↓
FastAPI REST API
  ↓
Services
  ├── Drug Service
  ├── Research/Paper Service
  └── Chat/LLM Service
        ↓
Scientific Data / RAG
  ├── PubChem
  ├── ChEMBL
  ├── PubMed
  └── Vector Database
        ↓
LLM
  ├── OpenAI
  ├── Anthropic Claude
  └── Google Gemini
        ↓
AI Answer + Sources
```

The overall architecture follows:

**UI → API → Services → Data/RAG → LLM → Response**

### RAG Pipeline

For research papers and other documents:

```text
PDF / Document
      ↓
Text Extraction
      ↓
Text Chunking
      ↓
Embeddings
      ↓
Vector Database
      ↓
Retriever
      ↓
Relevant Context
      ↓
LLM
      ↓
Answer + Evidence
```

RAG helps the LLM answer questions using the relevant information retrieved from the documents instead of relying only on its pretrained knowledge.

### Technologies Used

| Area                 | Technology                    |
| -------------------- | ----------------------------- |
| Programming Language | **Python**                    |
| Backend              | **FastAPI**                   |
| API Server           | **Uvicorn**                   |
| Frontend             | **Streamlit**                 |
| LLM                  | **OpenAI / Claude / Gemini**  |
| RAG Framework        | **LangChain**                 |
| Vector Database      | **FAISS / Chroma**            |
| PDF Processing       | **PyMuPDF**                   |
| Database             | **SQLite**                    |
| Future Database      | **PostgreSQL**                |
| Scientific Sources   | **PubChem, ChEMBL, PubMed**   |
| Version Control      | **Git / GitHub**              |
| Development          | **VS Code, Jupyter Notebook** |

These technologies and data sources are listed in the project's planned technology stack.

### Important Python Packages

The main packages used/planned for the project are:

```text
fastapi
uvicorn
streamlit
python-dotenv
requests

langchain
faiss-cpu / chromadb
pymupdf

openai
anthropic
google-generativeai

pydantic
```

**Purpose of the main packages:**

* **FastAPI** → Build REST APIs
* **Uvicorn** → Run the FastAPI backend
* **Streamlit** → Create the user interface
* **Requests** → Communicate with external APIs
* **python-dotenv** → Load API keys/configuration from `.env`
* **LangChain** → Build RAG and LLM workflows
* **FAISS / Chroma** → Store and search document embeddings
* **PyMuPDF** → Extract text from PDF research papers
* **OpenAI / Anthropic / Gemini SDKs** → Connect to different LLM providers
* **Pydantic** → Validate and structure API/data models

The initial project setup specifically starts with `fastapi`, `uvicorn`, `streamlit`, `python-dotenv`, and `requests`, with the RAG/PDF/LLM dependencies added as those features are implemented.

### Example Workflow

**User:**
`Explain the mechanism of action of Aspirin.`

```text
Streamlit
   ↓
FastAPI
   ↓
Drug Service
   ↓
Scientific Data
   ↓
Relevant Context
   ↓
LLM
   ↓
AI Explanation
   ↓
Sources / Evidence
```

For a research paper:

```text
Upload PDF
   ↓
Extract Text
   ↓
Create Chunks
   ↓
Generate Embeddings
   ↓
Store in FAISS/Chroma
   ↓
Retrieve Relevant Chunks
   ↓
LLM
   ↓
Answer + Evidence
```

### Current MVP

The first version should remain simple:

```text
Streamlit
    ↓
FastAPI
    ↓
Drug Service
    ↓
Scientific Data
    ↓
Drug Information
```

After the basic system works, **LLM → RAG → research-paper Q&A → drug comparison → multi-model support** can be added gradually.

### Short Resume Description

**Drug Discovery & Drug Information Copilot** — Developed a GenAI-powered Life Sciences research assistant using **Python, FastAPI, Streamlit, LangChain, RAG, vector databases, and scientific data sources**. The system retrieves drug, target, biological activity, and research information and uses LLMs to generate source-aware explanations and research-paper Q&A.
