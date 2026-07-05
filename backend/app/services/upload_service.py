from typing import Optional

from fastapi import UploadFile

from app.schemas.upload import UploadResponse, UploadedFileInfo
from app.utils.file_utils import StorageManager
from app.exceptions.custom_exceptions import SessionNotFoundError
from app.services.document_service import DocumentService
from app.services.vector_service import VectorService
import logging
class UploadService:

    @staticmethod
    def upload_document(
        file: UploadFile,
        workspace: str = "default",
        session_id: Optional[str] = None
    ) -> UploadResponse:

        # Create a new session if one is not provided
        if session_id is None:

            session_id, session_path = StorageManager.create_session(
                workspace
            )

        else:

            workspace_path = StorageManager.create_workspace(
                workspace
            )

            session_path = (
                workspace_path
                / "sessions"
                / session_id
            )

            if not session_path.exists():
                raise SessionNotFoundError(session_id)

        file_info = StorageManager.save_document(
            file=file,
            session_path=session_path
        )
        document_path = (
             session_path
             / "documents"
             / file_info["saved_as"]
        )
        document_info = DocumentService.process_document(
             document_path
        )
        vector_info = VectorService.create_vector_store(
             chunks=document_info["chunks"],
             session_path=session_path
        )
        logger = logging.getLogger(__name__)
        logger.info(
            "Vector store created with %s chunks.",
            vector_info["chunk_count"]
        )
            
        logger.info(
            "Document processed. Pages=%s Chunks=%s Characters=%s",
            document_info["pages"],
            document_info["chunk_count"],
            document_info["characters"],
        )
        return UploadResponse(
            success=True,
            message="Document uploaded successfully.",
            workspace=workspace,
            session_id=session_id,
            uploaded_file=UploadedFileInfo(**file_info)
        )