import chromadb
from sentence_transformers import SentenceTransformer
from pathlib import Path

KB_DIR = Path(__file__).parent / "knowledge_base"
COLLECTION_NAME = "aiida_docs"

client = chromadb.Client()
model  = SentenceTransformer("all-MiniLM-L6-v2")

def build_index():
    collection = client.get_or_create_collection(COLLECTION_NAME)
    docs, ids = [], []
    for i, path in enumerate(KB_DIR.glob("*.txt")):
        for j, line in enumerate(path.read_text().strip().splitlines()):
            if line.strip():
                docs.append(line.strip())
                ids.append(f"{path.stem}_{j}")
    embeddings = model.encode(docs).tolist()
    collection.add(documents=docs, embeddings=embeddings, ids=ids)
    return collection

_collection = None
def get_collection():
    global _collection
    if _collection is None:
        _collection = build_index()
    return _collection