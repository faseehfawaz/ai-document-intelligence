import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import numpy as np
from ai.embedder import embed_text
from ai.vector_store import build_vector_store

index, texts = build_vector_store("data/processed_text/documents.json")

def search(query, top_k=3):
    q_embedding = np.array([embed_text(query)]).astype("float32")
    distances, indices = index.search(q_embedding, top_k)

    results = []
    for i in indices[0]:
        results.append(texts[i])

    return results

if __name__ == "__main__":
    question = input("Ask a question: ")
    answers = search(question)

    for i, ans in enumerate(answers, 1):
        print(f"\nResult {i}:\n{ans[:500]}...")
