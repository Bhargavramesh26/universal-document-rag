from pathlib import Path

from app.rag.retriever import Retriever


class RetrievalService:

    @staticmethod
    def retrieve_context(
        question: str,
        session_path: Path
    ):

        retriever = Retriever.get_retriever(
            session_path / "vector_db"
        )

        documents = retriever.invoke(question)

        return documents