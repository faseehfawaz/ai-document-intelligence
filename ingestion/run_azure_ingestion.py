import os
from ingestion.azure_blob_loader import download_pdfs

conn = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
download_pdfs(conn)
