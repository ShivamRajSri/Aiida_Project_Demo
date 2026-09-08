from rag.embedder import get_collection, model

def retrieve(query: str, top_k: int = 3) -> str:
    collection = get_collection()
    embedding  = model.encode([query]).tolist()
    results    = collection.query(query_embeddings=embedding, n_results=top_k)
    docs       = results["documents"][0]
    return "\n".join(f"- {d}" for d in docs)