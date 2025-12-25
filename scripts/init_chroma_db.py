import pandas as pd
import numpy as np

from services.embedding_service import EmbeddingService
from services.chroma_service import ChromaService

CSV_PATH = "data/LawBot_Data.csv"

def init_chroma_db():
    embedder = EmbeddingService()
    chroma = ChromaService()

    df = pd.read_csv(CSV_PATH)

    for idx, row in df.iterrows():
        text = row.get("text", "")

        if not isinstance(text, str) or not text.strip():
            print(f"⚠️ 跳過空文本：{idx}")
            continue

        emb = embedder.encode(text)

        if np.isnan(emb).any() or np.isinf(emb).any():
            print(f"⚠️ 向量異常：{row['id']}")
            continue

        chroma.add(
            doc_id=row["id"],
            embedding=emb,
            document=text,
            metadata={
                "category": row["category"],
                "dataset_name": row["dataset_name"]
            }
        )

        print(f"✅ 已加入 ID {row['id']}")

    print("🎉 ChromaDB 初始化完成")

if __name__ == "__main__":
    init_chroma_db()
