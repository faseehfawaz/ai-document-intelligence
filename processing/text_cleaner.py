import re
from pathlib import Path

INPUT_DIR = Path("data/extracted_text")
OUTPUT_DIR = Path("data/clean_text")

OUTPUT_DIR.mkdir(exist_ok=True)

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-z0-9.,;:!?()\-\s]', '', text)
    return text.strip()

for txt_file in INPUT_DIR.glob("*.txt"):
    raw_text = txt_file.read_text(encoding="utf-8", errors="ignore")
    cleaned = clean_text(raw_text)

    output_path = OUTPUT_DIR / txt_file.name
    output_path.write_text(cleaned, encoding="utf-8")

print("Text cleaning completed.")
