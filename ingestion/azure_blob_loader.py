from azure.storage.blob import BlobServiceClient
from pathlib import Path
import os

CONTAINER_NAME = "raw-pdfs"

def download_pdfs(connection_string, output_dir="data/raw_pdfs"):
    blob_service = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service.get_container_client(CONTAINER_NAME)

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    for blob in container_client.list_blobs():
        blob_client = container_client.get_blob_client(blob.name)
        file_path = Path(output_dir) / blob.name

        with open(file_path, "wb") as f:
            f.write(blob_client.download_blob().readall())

        print(f"Downloaded {blob.name}")
