import json
from pathlib import Path

INPUT_DIR = Path("data/clean_text")
OUTPUT_FILE = Path("data/processed_text/documents.json")

documents = []

for txt_file in INPUT_DIR.glob("*.txt"):
    with open(txt_file, "r", encoding="utf-8") as f:
        text = f.read().strip()
        if text:
            documents.append({
                "source": txt_file.name,
                "text": text
            })

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(documents, f, indent=2)

print(f"Saved {len(documents)} documents to {OUTPUT_FILE}")
