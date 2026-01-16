# AI Document Intelligence Platform

An end-to-end AI system that ingests documents from Azure Blob Storage, processes them at scale using Apache Spark, and enables semantic search using AI embeddings.

## Features
- Azure Blob Storage ingestion
- OCR + PDF text extraction
- Text cleaning & normalization
- Apache Spark analytics
- AI semantic search (Sentence Transformers + FAISS)
- REST API using FastAPI

## Architecture
1. PDFs stored in Azure Blob Storage
2. Secure ingestion via Azure SDK
3. Text extraction with OCR fallback
4. Spark-based processing for scalability
5. AI embeddings for semantic understanding
6. FastAPI service for querying documents

## Tech Stack
- Python
- Apache Spark (PySpark)
- Azure Blob Storage
- Sentence Transformers
- FAISS
- FastAPI

## How to Run
```bash
uvicorn api.main:app --reload
