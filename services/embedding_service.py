import torch
import numpy as np
from sklearn.preprocessing import normalize
from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL_NAME

class EmbeddingService:
    def __init__(self):
        device = "mps" if torch.backends.mps.is_available() else "cpu"
        self.model = SentenceTransformer(EMBEDDING_MODEL_NAME, device=device)

    def encode(self, text: str) -> np.ndarray:
        emb = self.model.encode(text, convert_to_tensor=True)
        emb = emb.cpu().numpy()
        emb = normalize([emb])[0]
        return emb
