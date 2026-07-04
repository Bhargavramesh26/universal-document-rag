from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter()


@router.post(
    "/chat",
    response_model=ChatResponse,
    summary="Ask a question",
)
async def chat(request: ChatRequest):

    answer = ChatService.ask(
        workspace="default",
        session_id=request.session_id,
        question=request.question,
        model=request.model,
    )

    return ChatResponse(
        success=True,
        answer=answer,
    )