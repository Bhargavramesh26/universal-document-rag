from pathlib import Path

from app.rag.llm_factory import LLMFactory
from app.rag.prompt import RAG_PROMPT
from app.services.retrieval_service import RetrievalService
from app.utils.file_utils import StorageManager


class ChatService:

    @staticmethod
    def ask(
        workspace: str,
        session_id: str,
        question: str,
        model: str,
    ):

        workspace_path = StorageManager.create_workspace(
            workspace
        )

        session_path = (
            workspace_path
            / "sessions"
            / session_id
        )

        documents = RetrievalService.retrieve_context(
            question=question,
            session_path=session_path,
        )

        context = "\n\n".join(
            doc.page_content
            for doc in documents
        )

        llm = LLMFactory.get_llm(model)

        prompt = RAG_PROMPT.format(
            context=context,
            question=question,
        )

        response = llm.invoke(prompt)

        return response.content