from langchain_huggingface import HuggingFaceEmbeddings


class EmbeddingModel:

    _embedding_model = None

    @classmethod
    def get_embeddings(cls):

        if cls._embedding_model is None:

            cls._embedding_model = HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2",
                model_kwargs={
                    "device": "cpu"
                },
                encode_kwargs={
                    "normalize_embeddings": True
                }
            )

        return cls._embedding_model