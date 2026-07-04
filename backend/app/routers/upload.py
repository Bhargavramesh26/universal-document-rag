from typing import Optional

from fastapi import APIRouter, File, Form, UploadFile

from app.schemas.upload import UploadResponse
from app.services.upload_service import UploadService

router = APIRouter()


@router.post(
    "/upload",
    response_model=UploadResponse,
    summary="Upload a document",
)
async def upload_document(
    file: UploadFile = File(...),
    workspace: str = Form("default"),
    session_id: Optional[str] = Form(None),
):

    return UploadService.upload_document(
        file=file,
        workspace=workspace,
        session_id=session_id,
    )