# Drug Discovery & Drug Information Copilot

> A GenAI-powered Life Sciences research and drug-information assistant
> that combines public scientific databases, Large Language Models
> (LLMs), and Retrieval-Augmented Generation (RAG) to help users explore
> drugs, targets, diseases, biological activity, and research
> literature.

------------------------------------------------------------------------

## 1. Project Overview

**Drug Discovery & Drug Information Copilot** is a modular GenAI
application designed to connect **Life Sciences knowledge** with
**Generative AI**.

The system will retrieve scientific information from trusted public
sources such as:

-   **PubChem** -- chemical compounds, molecular properties,
    identifiers, and related information
-   **ChEMBL** -- drug/compound information, biological activity,
    targets, and bioassay data
-   **PubMed** -- biomedical research literature and publications

The retrieved information can then be explained, compared, summarized,
and queried using an LLM.

The project is designed as a **research and information assistant**, not
as a medical diagnosis or treatment recommendation system.

------------------------------------------------------------------------

## 2. Main Goals

The project has two major learning goals:

### Life Sciences

Learn and work with concepts such as:

-   Drug
-   Chemical compound
-   Disease
-   Gene
-   Protein
-   Biological target
-   Drug-target interaction
-   Mechanism of action
-   Indication
-   Biological activity
-   Research paper
-   Clinical/research evidence

### Generative AI

Learn and implement:

-   LLM integration
-   Prompt engineering
-   Structured LLM responses
-   RAG
-   Embeddings
-   Vector databases
-   Document chunking
-   Semantic search
-   Source-aware answers
-   Citation/evidence handling
-   LLM provider abstraction
-   Multi-model support
-   AI evaluation and hallucination control

------------------------------------------------------------------------

## 3. Planned Features

### Phase 1 -- Drug Search

User enters a drug or compound name.

Example:

``` text
Aspirin
```

The application retrieves available information from scientific
databases.

Possible information:

-   Drug/compound name
-   Molecular formula
-   Molecular weight
-   Chemical identifiers
-   Synonyms
-   Chemical properties
-   Related targets
-   Biological activity
-   Source links

------------------------------------------------------------------------

### Phase 2 -- Drug Information Assistant

Users can ask questions about a drug.

Example:

``` text
What is aspirin?
```

``` text
What is the mechanism of action of aspirin?
```

``` text
What are the known biological targets of aspirin?
```

The application retrieves relevant information and uses an LLM to
generate a clear explanation.

------------------------------------------------------------------------

### Phase 3 -- Drug Comparison

Compare two or more drugs/compounds.

Example:

``` text
Compare Aspirin and Ibuprofen.
```

The system can organize information such as:

  Category               Drug A   Drug B
  ---------------------- -------- --------
  Name                            
  Compound information            
  Targets                         
  Mechanism                       
  Biological activity             
  Research evidence               

The comparison should distinguish between database facts, research
findings, and AI-generated interpretation.

------------------------------------------------------------------------

### Phase 4 -- Disease → Target → Drug Exploration

The application will eventually support exploration of relationships
such as:

``` text
Disease
   ↓
Biological Target
   ↓
Drug / Compound
   ↓
Mechanism / Activity
   ↓
Research Evidence
```

Example conceptual query:

``` text
What drug compounds are associated with a particular biological target?
```

This feature will help connect Life Sciences concepts instead of
treating the application as a simple chatbot.

------------------------------------------------------------------------

### Phase 5 -- Research Paper Analysis

Users can provide a research paper/PDF.

The system will:

1.  Read the document
2.  Extract text
3.  Split the text into chunks
4.  Generate embeddings
5.  Store embeddings in a vector database
6.  Retrieve relevant sections for a question
7.  Send the relevant context to an LLM
8.  Generate an answer
9.  Provide evidence/citations where possible

Example:

``` text
Summarize this research paper.
```

``` text
What was the main target studied in this paper?
```

``` text
What methodology was used?
```

``` text
What were the main findings?
```

------------------------------------------------------------------------

## 4. RAG Architecture

The planned Retrieval-Augmented Generation pipeline is:

``` text
Research Papers / Scientific Documents
                 ↓
             Text Extraction
                 ↓
              Chunking
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
          Generated Answer
                 ↓
       Sources / Evidence
```

RAG is important because the LLM should not be expected to know every
detail in a user's uploaded research document.

Instead, relevant information is retrieved first and then provided to
the LLM as context.

------------------------------------------------------------------------

## 5. High-Level System Architecture

``` text
                         ┌──────────────────────┐
                         │      User            │
                         │ Streamlit Frontend   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      FastAPI         │
                         │    API Layer         │
                         └──────────┬───────────┘
                                    │
              ┌─────────────────────┼─────────────────────┐
              │                     │                     │
              ▼                     ▼                     ▼
       ┌─────────────┐       ┌─────────────┐       ┌─────────────┐
       │ Drug Service│       │ Paper/RAG   │       │ Chat Service│
       └──────┬──────┘       └──────┬──────┘       └──────┬──────┘
              │                     │                     │
       ┌──────┼──────┐              │                     │
       ▼      ▼      ▼              ▼                     ▼
   PubChem  ChEMBL PubMed       Vector DB                LLM
                                  FAISS/Chroma          Provider
                                                           │
                                      ┌────────────────────┼──────────────┐
                                      ▼                    ▼              ▼
                                    OpenAI              Claude          Gemini
```

------------------------------------------------------------------------

## 6. Technology Stack

### Backend

-   Python
-   FastAPI
-   Uvicorn

### Frontend

-   Streamlit

### Generative AI

-   OpenAI GPT models
-   Anthropic Claude models
-   Google Gemini models

The exact model names should be configured rather than hard-coded
throughout the application.

### RAG

-   LangChain
-   Embeddings
-   FAISS or Chroma
-   PyMuPDF for PDF processing

### Scientific Data Sources

-   PubChem
-   ChEMBL
-   PubMed

### Database

Initial:

-   SQLite

Future:

-   PostgreSQL

### Development Tools

-   Git
-   GitHub
-   VS Code
-   Python virtual environment
-   Jupyter Notebook where useful

------------------------------------------------------------------------

## 7. Project Structure

``` text
drug-discovery-copilot/
│
├── app/
│   ├── main.py
│   │
│   ├── api/
│   │   ├── drugs.py
│   │   ├── chat.py
│   │   └── papers.py
│   │
│   ├── services/
│   │   ├── drug_service.py
│   │   ├── pubchem_service.py
│   │   ├── chembl_service.py
│   │   ├── pubmed_service.py
│   │   │
│   │   └── llm/
│   │       ├── base.py
│   │       ├── openai.py
│   │       ├── anthropic.py
│   │       └── gemini.py
│   │
│   ├── models/
│   │   ├── drug.py
│   │   └── paper.py
│   │
│   └── rag/
│       ├── embeddings.py
│       ├── retriever.py
│       └── pipeline.py
│
├── frontend/
│   └── streamlit_app.py
│
├── data/
├── vectorstore/
├── tests/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

------------------------------------------------------------------------

## 8. Folder and File Responsibilities

### `app/`

Contains the core backend application.

### `app/main.py`

FastAPI application entry point.

Responsibilities:

-   Create FastAPI application
-   Register API routes
-   Configure application startup
-   Add middleware/configuration when required

------------------------------------------------------------------------

### `app/api/`

Contains API endpoints.

#### `drugs.py`

Drug-related endpoints.

Example planned endpoint:

``` text
GET /drugs/{drug_name}
```

Example:

``` text
GET /drugs/aspirin
```

#### `chat.py`

AI question-answering endpoints.

#### `papers.py`

Research paper/PDF-related endpoints.

------------------------------------------------------------------------

### `app/services/`

Contains the application's business logic.

The API layer should not contain all the data retrieval and AI logic.

Instead:

``` text
API Route
    ↓
Service
    ↓
External API / Database / LLM
```

------------------------------------------------------------------------

### `drug_service.py`

Coordinates drug information from multiple sources.

Example:

``` text
User → Drug Service
          ├── PubChem
          ├── ChEMBL
          └── PubMed
```

------------------------------------------------------------------------

### `pubchem_service.py`

Responsible for communication with PubChem.

Potential responsibilities:

-   Search compound
-   Retrieve compound properties
-   Retrieve identifiers
-   Retrieve synonyms
-   Normalize PubChem response

------------------------------------------------------------------------

### `chembl_service.py`

Responsible for ChEMBL information.

Potential responsibilities:

-   Drug/compound lookup
-   Target information
-   Biological activity
-   Bioassay information
-   Drug-target relationships

------------------------------------------------------------------------

### `pubmed_service.py`

Responsible for biomedical literature retrieval.

Potential responsibilities:

-   Search papers
-   Retrieve metadata
-   Retrieve abstracts when available
-   Extract paper information
-   Store source metadata for citations

------------------------------------------------------------------------

## 9. LLM Provider Architecture

One of the most important design decisions is to avoid tightly coupling
the whole application to a single LLM provider.

The application should use a common interface:

``` text
                LLMProvider
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
    OpenAI       Anthropic      Gemini
```

Conceptual interface:

``` python
class LLMProvider:

    def generate(self, prompt: str) -> str:
        pass
```

Then each provider implements the same interface.

Example:

``` text
llm/base.py
       │
       ├── openai.py
       ├── anthropic.py
       └── gemini.py
```

This means application code can work with:

``` text
LLMProvider
```

instead of directly depending on:

``` text
OpenAI
```

### Why this architecture?

If the project initially uses GPT and later needs Claude or Gemini, the
main application logic should require minimal changes.

For example:

``` text
LLM_PROVIDER=openai
```

could later become:

``` text
LLM_PROVIDER=anthropic
```

or:

``` text
LLM_PROVIDER=gemini
```

The exact SDK/API implementation remains inside the corresponding
provider module.

------------------------------------------------------------------------

## 10. Configuration

A future `.env` file may contain configuration such as:

``` env
LLM_PROVIDER=openai

OPENAI_API_KEY=your_key_here

ANTHROPIC_API_KEY=your_key_here

GOOGLE_API_KEY=your_key_here
```

Do not commit real API keys to GitHub.

The `.env` file should be included in `.gitignore`.

------------------------------------------------------------------------

## 11. Initial Development Setup

Create the project:

``` bash
mkdir drug-discovery-copilot
cd drug-discovery-copilot
```

Create a virtual environment:

``` bash
python -m venv venv
```

Activate it on Windows:

``` bash
venv\Scripts\activate
```

Install the initial packages:

``` bash
pip install fastapi uvicorn streamlit python-dotenv requests
```

Later, install RAG, PDF, database, and LLM dependencies when those
phases are implemented.

This avoids installing the entire stack before it is needed.

------------------------------------------------------------------------

## 12. First Backend Test

Initial `app/main.py` should be a minimal FastAPI application.

Conceptually:

``` python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Drug Discovery Copilot API is running"}
```

Run:

``` bash
uvicorn app.main:app --reload
```

The first goal is simply to confirm that the backend works.

------------------------------------------------------------------------

## 13. Development Roadmap

### Phase 1 -- Foundation

-   [ ] Create project structure
-   [ ] Create virtual environment
-   [ ] Configure Git
-   [ ] Create FastAPI application
-   [ ] Create Streamlit application
-   [ ] Add configuration management
-   [ ] Add `.env`
-   [ ] Add `.gitignore`

### Phase 2 -- Life Sciences Data

-   [ ] Learn basic Life Sciences terminology
-   [ ] Integrate PubChem
-   [ ] Integrate ChEMBL
-   [ ] Integrate PubMed
-   [ ] Create normalized drug model
-   [ ] Create paper model
-   [ ] Handle API errors
-   [ ] Store source URLs/identifiers

### Phase 3 -- Drug Intelligence

-   [ ] Drug search
-   [ ] Drug details
-   [ ] Compound information
-   [ ] Target information
-   [ ] Biological activity
-   [ ] Drug comparison
-   [ ] Disease → target → drug exploration

### Phase 4 -- Generative AI

-   [ ] Integrate first LLM provider
-   [ ] Learn prompt engineering
-   [ ] Generate drug explanations
-   [ ] Generate structured answers
-   [ ] Add context-aware questions
-   [ ] Implement LLM provider interface

### Phase 5 -- RAG

-   [ ] Upload research paper
-   [ ] Extract PDF text
-   [ ] Clean extracted text
-   [ ] Chunk documents
-   [ ] Generate embeddings
-   [ ] Store vectors
-   [ ] Implement retrieval
-   [ ] Connect retrieved context to LLM
-   [ ] Add source references

### Phase 6 -- Advanced Research Features

-   [ ] Research paper summarization
-   [ ] Paper Q&A
-   [ ] Evidence extraction
-   [ ] Drug comparison using retrieved evidence
-   [ ] Disease-target-drug analysis
-   [ ] Hallucination reduction
-   [ ] Evaluation framework
-   [ ] Response quality testing

### Phase 7 -- Multi-Model Support

-   [ ] OpenAI provider
-   [ ] Anthropic provider
-   [ ] Gemini provider
-   [ ] Provider configuration
-   [ ] Model selection
-   [ ] Compare model responses
-   [ ] Standardize provider outputs

### Phase 8 -- Production/Portfolio Version

-   [ ] Authentication if required
-   [ ] Logging
-   [ ] Error handling
-   [ ] Automated tests
-   [ ] API documentation
-   [ ] Docker support
-   [ ] Deployment
-   [ ] Performance improvements
-   [ ] Security review
-   [ ] Complete GitHub documentation
-   [ ] Resume/project description

------------------------------------------------------------------------

## 14. Recommended Development Order

Do **not** build the entire system at once.

The recommended sequence is:

``` text
Project Setup
     ↓
FastAPI
     ↓
PubChem
     ↓
Drug Search
     ↓
Streamlit UI
     ↓
ChEMBL
     ↓
PubMed
     ↓
LLM Integration
     ↓
RAG
     ↓
Research Paper Q&A
     ↓
Drug Comparison
     ↓
Multi-Model Support
     ↓
Production Improvements
```

This order allows each concept to be learned and tested before adding
another layer.

------------------------------------------------------------------------

## 15. Example End-to-End Flow

### Drug Search

User:

``` text
Aspirin
```

Flow:

``` text
Streamlit
   ↓
FastAPI
   ↓
Drug API
   ↓
Drug Service
   ↓
PubChem / ChEMBL
   ↓
Normalized Drug Data
   ↓
Streamlit
```

------------------------------------------------------------------------

### AI Drug Question

User:

``` text
Explain the mechanism of action of aspirin.
```

Flow:

``` text
User Question
      ↓
FastAPI
      ↓
Drug / Scientific Data Retrieval
      ↓
Relevant Context
      ↓
LLM Provider
      ↓
AI Explanation
      ↓
Sources / Evidence
```

------------------------------------------------------------------------

### Research Paper Question

User uploads a PDF and asks:

``` text
What was the main biological target studied in this paper?
```

Flow:

``` text
PDF
 ↓
Text Extraction
 ↓
Chunking
 ↓
Embeddings
 ↓
Vector Database
 ↓
Retriever
 ↓
Relevant Chunks
 ↓
LLM
 ↓
Answer + Evidence
```

------------------------------------------------------------------------

## 16. Data Flow Principles

The application should follow these principles:

### Retrieve before generating

Whenever reliable external information is available:

``` text
Retrieve → Validate/organize → Generate
```

rather than:

``` text
Generate from model memory
```

### Keep source information

Each important piece of information should retain its source where
practical.

Example:

``` text
Source:
PubChem

Identifier:
CID ...

URL:
...

Retrieved information:
...
```

### Separate facts from interpretation

Responses should distinguish between:

1.  Established/database information
2.  Published research findings
3.  AI-generated interpretation

This is especially important for scientific information.

------------------------------------------------------------------------

## 17. Error Handling

The application should eventually handle:

-   Invalid drug names
-   Drug not found
-   PubChem API failure
-   ChEMBL API failure
-   PubMed search failure
-   Invalid PDF
-   Empty document
-   Unsupported document
-   LLM API failure
-   API rate limits
-   Missing API keys
-   Vector database errors
-   Network failures

The frontend should display useful messages rather than raw Python
exceptions.

------------------------------------------------------------------------

## 18. Security Considerations

The project should:

-   Never expose API keys in source code
-   Keep secrets in environment variables
-   Add `.env` to `.gitignore`
-   Validate uploaded files
-   Limit file size
-   Validate user inputs
-   Avoid executing uploaded content
-   Handle external API responses safely
-   Log errors without exposing secrets
-   Use HTTPS in production
-   Apply authentication/authorization if required

------------------------------------------------------------------------

## 19. Scientific Reliability

This project is intended for **research and educational information
retrieval**.

It should not be presented as:

-   A medical diagnosis system
-   A treatment recommendation engine
-   A replacement for doctors or scientists
-   A system that guarantees scientific correctness

The application should clearly communicate uncertainty when evidence is
incomplete.

For important scientific claims, provide the relevant source whenever
possible.

------------------------------------------------------------------------

## 20. Hallucination Control Strategy

A major objective of the project is reducing unsupported LLM responses.

Planned approach:

``` text
User Question
      ↓
Retrieve scientific information
      ↓
Select relevant evidence
      ↓
Give evidence to LLM
      ↓
Generate answer
      ↓
Attach sources
```

The prompt can instruct the model to:

-   Use supplied context
-   Avoid inventing facts
-   State when information is unavailable
-   Distinguish evidence from interpretation
-   Reference supporting sources

Later, the project can include automated evaluation for factuality and
retrieval quality.

------------------------------------------------------------------------

## 21. Testing Strategy

Testing should be introduced throughout development.

### Unit Tests

Test individual components:

``` text
PubChem service
ChEMBL service
PubMed service
Drug service
LLM provider
RAG retriever
```

### API Tests

Test endpoints such as:

``` text
GET /drugs/{drug_name}
```

### RAG Tests

Test whether the correct document chunks are retrieved.

### LLM Tests

Test:

-   Response structure
-   Missing context behavior
-   Unsupported-question behavior
-   Citation/source handling

### Integration Tests

Test complete flows:

``` text
Frontend → FastAPI → Service → External Source → LLM
```

------------------------------------------------------------------------

## 22. Future Improvements

Possible future features include:

-   Knowledge graph
-   Drug-target network visualization
-   Protein/gene exploration
-   Molecular structure visualization
-   Similar compound search
-   Drug repurposing research exploration
-   Advanced scientific literature search
-   Multiple document collections
-   Citation management
-   Conversation history
-   User workspaces
-   Experiment/evaluation dashboard
-   Model comparison dashboard
-   PostgreSQL
-   Cloud deployment
-   Docker
-   CI/CD

These should be added only after the core system is stable.

------------------------------------------------------------------------

## 23. Important Architecture Principle

The project should remain modular.

The goal is:

``` text
User Interface
      ↓
API Layer
      ↓
Business Services
      ↓
Data Sources / RAG
      ↓
LLM Interface
      ↓
Specific LLM Provider
```

Avoid putting everything inside:

``` text
main.py
```

and avoid putting provider-specific code throughout the application.

The most important abstraction is:

``` text
Application
    ↓
LLMProvider
    ↓
OpenAI / Anthropic / Gemini
```

This makes the project easier to maintain, test, and extend.

------------------------------------------------------------------------

## 24. Learning Plan

This project should be used as a practical learning path.

### Life Sciences

Learn:

``` text
Drug
 ↓
Compound
 ↓
Protein
 ↓
Gene
 ↓
Target
 ↓
Drug-Target Interaction
 ↓
Mechanism of Action
 ↓
Disease
 ↓
Research Evidence
```

### GenAI

Learn:

``` text
LLM
 ↓
Prompt Engineering
 ↓
Embeddings
 ↓
Vector Database
 ↓
Retrieval
 ↓
RAG
 ↓
Agents/advanced workflows
 ↓
Evaluation
```

### Software Engineering

Learn:

``` text
Python
 ↓
FastAPI
 ↓
REST APIs
 ↓
Service Architecture
 ↓
Database
 ↓
Testing
 ↓
Git/GitHub
 ↓
Docker
 ↓
Deployment
```

------------------------------------------------------------------------

## 25. Resume-Level Project Description

### Drug Discovery & Drug Information Copilot

Developing a GenAI-powered Life Sciences research assistant using
**Python, FastAPI, Streamlit, LangChain, RAG, vector databases, and
scientific data sources such as PubChem, ChEMBL, and PubMed**. The
system is designed to retrieve drug, target, biological activity, and
research-literature information and use LLMs to provide source-aware
explanations, comparisons, and research-paper question answering. The
architecture uses an **LLM provider abstraction** to support OpenAI,
Anthropic Claude, and Google Gemini with minimal application-level
changes.

------------------------------------------------------------------------

## 26. Current MVP Target

The first working version should be intentionally small:

``` text
User
 ↓
Streamlit
 ↓
FastAPI
 ↓
PubChem
 ↓
Drug Information
```

After this works reliably:

``` text
PubChem
   +
ChEMBL
   +
PubMed
```

Then:

``` text
Scientific Data
      ↓
     LLM
      ↓
AI Explanation
```

Then:

``` text
Research PDF
      ↓
     RAG
      ↓
LLM
      ↓
Evidence-based Answer
```

The final system can then add comparison, disease-target exploration,
multi-model support, testing, and deployment.

------------------------------------------------------------------------

## 27. Project Status

**Status:** Planning / Initial Development

### Current priority

1.  Project structure
2.  Python environment
3.  FastAPI setup
4.  Streamlit setup
5.  PubChem integration
6.  First drug-search API
7.  Connect frontend to backend

### Later priorities

-   ChEMBL
-   PubMed
-   LLM integration
-   RAG
-   Research paper analysis
-   Drug comparison
-   Multi-model support
-   Production deployment

------------------------------------------------------------------------

## 28. Long-Term Vision

The long-term goal is to build a **scientific research copilot** that
connects structured Life Sciences data with unstructured scientific
literature and Generative AI.

The intended architecture is:

``` text
                LIFE SCIENCES DATA
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
     PubChem         ChEMBL         PubMed
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                 Data / RAG Layer
                       │
                       ▼
                 LLM Abstraction
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
        GPT          Claude       Gemini
          │            │            │
          └────────────┼────────────┘
                       ▼
                Research Copilot
                       │
                       ▼
             Streamlit User Interface
```

The project should evolve gradually from a simple drug-information
application into a modular **GenAI + Life Sciences research platform**.

------------------------------------------------------------------------

## 29. Quick Reference

### Backend

``` text
FastAPI
```

### Frontend

``` text
Streamlit
```

### Programming Language

``` text
Python
```

### Scientific Sources

``` text
PubChem
ChEMBL
PubMed
```

### RAG

``` text
LangChain
Embeddings
FAISS / Chroma
PyMuPDF
```

### LLM Providers

``` text
OpenAI
Anthropic Claude
Google Gemini
```

### Initial Database

``` text
SQLite
```

### Future Database

``` text
PostgreSQL
```

### Core Architecture

``` text
API → Services → Data/RAG → LLM Provider
```

------------------------------------------------------------------------

## 30. Final Development Rule

Build and understand each layer before moving to the next.

Do not start with the complete RAG + multi-model + database system.

Start with:

``` text
FastAPI
  ↓
PubChem
  ↓
Drug Search
```

Then progressively add:

``` text
ChEMBL
  ↓
PubMed
  ↓
LLM
  ↓
RAG
  ↓
Comparison
  ↓
Multi-model
  ↓
Production
```

This keeps the project understandable, testable, and useful as a
long-term GenAI + Life Sciences learning project.




## 🚀 Uvicorn

**Uvicorn** is a lightweight, high-performance **ASGI web server** used to run the FastAPI application.

FastAPI is responsible for defining the API endpoints and application logic, while Uvicorn runs the application and listens for incoming HTTP requests.

### FastAPI vs Uvicorn

| Component     | Responsibility                                           |
| ------------- | -------------------------------------------------------- |
| **FastAPI**   | Framework used to build and define the REST API          |
| **Uvicorn**   | Web server used to run and serve the FastAPI application |
| **HTTP**      | Communication protocol used between clients and the API  |
| **Streamlit** | Frontend/user interface                                  |
| **LLM**       | Generates AI responses                                   |

### How Uvicorn Runs FastAPI

Our FastAPI application is located at:

```text
app/
└── main.py
```

Inside `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()
```

We start the application using:

```bash
uvicorn app.main:app --reload
```

The command can be understood as:

```text
uvicorn app.main:app --reload
        │   │    │
        │   │    └── FastAPI application object
        │   └─────── main.py
        └─────────── app directory
```

Therefore, `app.main:app` means:

> Load the `app` object from `app/main.py`.

### 🔄 Request Flow

When Uvicorn is running, the application becomes available at:

```text
http://127.0.0.1:8000
```

A request flows through the application as follows:

```text
Browser / Streamlit
        │
        │ HTTP Request
        ▼
    Uvicorn
        │
        ▼
    FastAPI
        │
        ▼
   API Endpoint
        │
        ▼
    Python Logic
        │
        ▼
     Response
        │
        ▼
Browser / Streamlit
```

### 🔁 What Does `--reload` Do?

The `--reload` option automatically restarts the development server whenever changes are detected in the Python source code.

```bash
uvicorn app.main:app --reload
```

This is useful during development because we don't need to manually stop and restart the server after every code change.

### 🧬 Uvicorn in This Project

In the **Drug Discovery & Drug Information Copilot**, Uvicorn will run the FastAPI backend.

The overall communication will eventually look like:

```text
                         USER
                           │
                           ▼
                    ┌─────────────┐
                    │  Streamlit  │
                    │     UI      │
                    └──────┬──────┘
                           │
                           │ HTTP
                           ▼
                    ┌─────────────┐
                    │   Uvicorn   │
                    │ Web Server  │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   FastAPI   │
                    │  REST API   │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   Services  │
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
           PubChem       ChEMBL       PubMed
                           │
                           ▼
                         RAG
                           │
                           ▼
                          LLM
                           │
                           ▼
                        Answer
                           │
                           ▼
                       Streamlit
```

**In simple terms:**

> **FastAPI defines what our backend can do, while Uvicorn runs that FastAPI backend and receives HTTP requests from clients such as Streamlit.**
