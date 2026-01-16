from mlops.logging.logger import get_logger

logger = get_logger("api")

from fastapi import FastAPI
import os
from ingestion.azure_blob_loader import download_pdfs
from ingestion.pdf_loader import extract_text_from_pdf
from processing.text_cleaner import clean_text
from ai.query import search
from pathlib import Path
import json

app = FastAPI(title="AI Document Intelligence")

@app.post("/ingest")
def ingest():
    download_pdfs(os.getenv("AZURE_STORAGE_CONNECTION_STRING"))

    raw_dir = Path("data/raw_pdfs")
    clean_dir = Path("data/clean_text")
    processed_dir = Path("data/processed_text")

    clean_dir.mkdir(exist_ok=True)
    processed_dir.mkdir(exist_ok=True)

    documents = []

    for pdf in raw_dir.glob("*.pdf"):
        text = extract_text_from_pdf(pdf)
        cleaned = clean_text(text)

        txt_path = clean_dir / (pdf.stem + ".txt")
        txt_path.write_text(cleaned)

        documents.append({
            "source": pdf.name,
            "text": cleaned
        })

    with open(processed_dir / "documents.json", "w") as f:
        json.dump(documents, f, indent=2)

    return {"status": "Ingestion completed", "documents": len(documents)}

@app.get("/ask")
def ask(question: str):
    results = search(question)
    return {
        "question": question,
        "answers": results
    }

@app.post("/ingest")
def ingest():
    logger.info("Starting ingestion pipeline")
    ...
    logger.info(f"Ingested {len(documents)} documents")

@app.get("/ask")
def ask(question: str):
    logger.info(f"Received query: {question}")
    results = search(question)
    return {"question": question, "answers": results}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.on_event("startup")
async def startup_event():
    logger.info("API started successfully")


@app.get("/health")
def health():
    logger.info("Health check hit")
    return {"status": "ok"}
