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
