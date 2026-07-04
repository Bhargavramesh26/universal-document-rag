from pathlib import Path

from app.rag.loader import DocumentLoader
from app.rag.splitter import DocumentSplitter


class DocumentService:

    @staticmethod
    def process_document(file_path: Path):

        documents = DocumentLoader.load(file_path)

        chunks = DocumentSplitter.split(documents)

        return {
            "pages": len(documents),
            "chunks": chunks,
            "chunk_count": len(chunks),
            "characters": sum(
                len(doc.page_content)
                for doc in documents
            )
        }