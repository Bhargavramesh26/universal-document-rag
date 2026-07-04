from pathlib import Path

from langchain_chroma import Chroma

from app.rag.embeddings import EmbeddingModel


class Retriever:

    @staticmethod
    def load_vector_store(persist_directory: Path):

        embeddings = EmbeddingModel.get_embeddings()

        vector_store = Chroma(
            persist_directory=str(persist_directory),
            embedding_function=embeddings
        )

        return vector_store

    @staticmethod
    def get_retriever(persist_directory: Path):

        vector_store = Retriever.load_vector_store(
            persist_directory
        )

        return vector_store.as_retriever(
            search_kwargs={
                "k": 4
            }
        )