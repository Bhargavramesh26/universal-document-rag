from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.core.constants import (
    DEFAULT_CHUNK_SIZE,
    DEFAULT_CHUNK_OVERLAP,
)


class DocumentSplitter:

    @staticmethod
    def split(documents):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=DEFAULT_CHUNK_SIZE,
            chunk_overlap=DEFAULT_CHUNK_OVERLAP,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

        return splitter.split_documents(documents)