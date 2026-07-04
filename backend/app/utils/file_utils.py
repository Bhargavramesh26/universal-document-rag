from pathlib import Path
from uuid import uuid4
import shutil

from fastapi import UploadFile

from app.core.constants import SUPPORTED_FILE_TYPES

from app.exceptions.custom_exceptions import (
    UnsupportedFileTypeError,
    EmptyFileError,
)

BASE_DIR = Path(__file__).resolve().parents[2]

STORAGE_DIR = BASE_DIR / "storage"
WORKSPACE_DIR = STORAGE_DIR / "workspaces"


class StorageManager:

    @staticmethod
    def create_workspace(workspace: str = "default") -> Path:

        workspace_path = WORKSPACE_DIR / workspace

        workspace_path.mkdir(
            parents=True,
            exist_ok=True
        )

        return workspace_path

    @staticmethod
    def create_session(workspace: str = "default"):

        workspace_path = StorageManager.create_workspace(workspace)

        session_id = f"session-{uuid4().hex[:8]}"

        session_path = workspace_path / "sessions" / session_id

        (session_path / "documents").mkdir(
            parents=True,
            exist_ok=True
        )

        (session_path / "vector_db").mkdir(exist_ok=True)
        
        (session_path / "metadata").mkdir(exist_ok=True)
        
        (session_path / "chat_history").mkdir(exist_ok=True)
        
        return session_id, session_path

    @staticmethod
    def validate_file(file: UploadFile):
        extension = Path(file.filename).suffix.lower()
        
        if extension not in SUPPORTED_FILE_TYPES:
            raise UnsupportedFileTypeError(extension)
        
        if not file.filename:
            raise EmptyFileError()

    @staticmethod
    def save_document(
        file: UploadFile,
        session_path: Path
    ):

        StorageManager.validate_file(file)

        unique_name = (
            f"{uuid4().hex[:8]}_{file.filename}"
        )

        destination = (
            session_path
            / "documents"
            / unique_name
        )

        with open(destination, "wb") as buffer:
            shutil.copyfileobj(
                file.file,
                buffer
            )

        return {
            "filename": file.filename,
            "saved_as": unique_name,
            "file_size": destination.stat().st_size,
            "file_type": destination.suffix
        }