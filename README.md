# LLM-Powered RAG QA System

A production-style Retrieval-Augmented Generation (RAG) system that combines semantic search with LLM reasoning to answer questions based on custom data.

---

## Features

*  Semantic retrieval using FAISS vector database
*  Context-aware answers using OpenAI LLM
*  Redis caching to reduce latency and API calls
*  FastAPI backend with clean REST APIs
*  Text chunking and embedding pipeline

---

##  Tech Stack

* Python
* FastAPI
* FAISS
* OpenAI API
* Redis

---

##  Architecture

User Query → FastAPI → Redis Cache → Embedding → FAISS → Context → LLM → Response

---

##  Setup

1. Install dependencies
2. Add OpenAI API key in `.env`
3. Run FastAPI server

---

##  Run

```bash
uvicorn app.main:app --reload
```

---

##  API Endpoints

### Ingest Data

POST `/ingest`

### Query

POST `/query`

---

##  Future Improvements

* Async processing
* Streaming responses
* Reranking models
* Deployment with Docker

---

##  Resume Highlights

* Built an end-to-end RAG pipeline with semantic retrieval and LLM reasoning
* Developed scalable FastAPI APIs with caching for performance optimization
* Integrated FAISS and Redis to enable low-latency intelligent search
