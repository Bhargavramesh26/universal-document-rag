from pathlib import Path

from langchain_chroma import Chroma

from app.rag.embeddings import EmbeddingModel


class VectorStoreManager:

    @staticmethod
    def create(chunks, persist_directory: Path):

        embeddings = EmbeddingModel.get_embeddings()

        vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory=str(persist_directory)
        )

        return vector_store