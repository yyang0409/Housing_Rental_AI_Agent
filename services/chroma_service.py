import os
import chromadb
from config import CHROMA_DB_PATH, COLLECTION_NAME

class ChromaService:
    def __init__(self):
        os.makedirs(CHROMA_DB_PATH, exist_ok=True)
        self.client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME
        )

    def add(self, doc_id, embedding, document, metadata):
        self.collection.add(
            ids=[str(doc_id)],
            embeddings=[embedding],
            documents=[document],
            metadatas=[metadata]
        )

    def query(self, embedding, n_results=500):
        return self.collection.query(
            query_embeddings=[embedding],
            n_results=n_results,
            include=["documents", "metadatas", "embeddings"]
        )
