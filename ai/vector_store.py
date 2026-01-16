import faiss
import json
import numpy as np
from ai.embedder import embed_text

def build_vector_store(json_path):
    with open(json_path) as f:
        docs = json.load(f)

    texts = [doc["text"] for doc in docs]
    embeddings = np.array([embed_text(t) for t in texts]).astype("float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    return index, texts
