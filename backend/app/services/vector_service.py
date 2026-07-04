from pathlib import Path

from app.rag.vectorstore import VectorStoreManager


class VectorService:

    @staticmethod
    def create_vector_store(chunks, session_path: Path):

        vector_db_path = session_path / "vector_db"

        vector_store = VectorStoreManager.create(
            chunks=chunks,
            persist_directory=vector_db_path
        )

        return {
            "vector_store": vector_store,
            "chunk_count": len(chunks)
        }