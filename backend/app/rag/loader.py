from pathlib import Path

from langchain_community.document_loaders import (
    PyMuPDFLoader,
    TextLoader,
    Docx2txtLoader,
)


class DocumentLoader:

    @staticmethod
    def load(file_path: Path):

        extension = file_path.suffix.lower()

        if extension == ".pdf":
            loader = PyMuPDFLoader(str(file_path))

        elif extension == ".txt":
            loader = TextLoader(str(file_path), encoding="utf-8")

        elif extension == ".docx":
            loader = Docx2txtLoader(str(file_path))

        else:
            raise ValueError(f"Unsupported file type: {extension}")

        return loader.load()