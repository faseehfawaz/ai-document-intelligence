import pdfplumber
from pathlib import Path

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

if __name__ == "__main__":
    input_pdf = Path("data/raw_pdfs/sample.pdf")
    output_txt = Path("data/extracted_text/sample.txt")

    extracted_text = extract_text_from_pdf(input_pdf)

    output_txt.write_text(extracted_text)
    print("Text extraction completed.")
