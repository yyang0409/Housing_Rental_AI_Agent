import numpy as np
from agents.gemini_agent import GeminiAgent
from services.embedding_service import EmbeddingService
from services.chroma_service import ChromaService

class RentalAgent:
    def __init__(self, template: str):
        self.template = template
        self.embedding_service = EmbeddingService()
        self.chroma = ChromaService()
        self.llm = GeminiAgent()

    def analyze_contract(self, contract_text: str) -> str:
        prompt = f"""
請根據以下住宅租賃契約內容，對照範本進行分析。

合約內容：
{contract_text}

範本：
{self.template}

請指出缺失與違規，僅輸出純文字。
"""
        return self.llm.generate(prompt)

    def answer_question(self, question: str, category: str) -> str:
        query_emb = self.embedding_service.encode(question)
        results = self.chroma.query(query_emb)

        context = []
        for doc, meta in zip(
            results["documents"][0],
            results["metadatas"][0]
        ):
            if meta.get("category") == category:
                context.append(doc)

        prompt = f"""
使用者問題：{question}
相關資料：
{chr(10).join(context[:3])}

請給專業建議，純文字輸出。
"""
        return self.llm.generate(prompt)
