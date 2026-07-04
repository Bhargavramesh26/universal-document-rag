from pydantic import BaseModel, Field


class UploadedFileInfo(BaseModel):
    filename: str = Field(..., description="Original filename")
    saved_as: str = Field(..., description="Filename stored on disk")
    file_size: int = Field(..., description="Size of file in bytes")
    file_type: str = Field(..., description="File extension")


class UploadResponse(BaseModel):
    success: bool
    message: str
    workspace: str
    session_id: str
    uploaded_file: UploadedFileInfo