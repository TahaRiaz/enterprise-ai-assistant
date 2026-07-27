from fastapi import Depends,APIRouter
from app.core.constants import APITags
from app.schemas.chat import ChatRequest,ChatResponse
from app.schemas.common import ApiResponse
from app.dependencies.services import get_rag_pipeline
from app.rag.pipeline import RAGPipeline
from app.core.exceptions import AppException
from fastapi.responses import StreamingResponse
from app.services.chat_service import ChatService

router = APIRouter(
    prefix="/conversation",
    tags= APITags.CHAT
)

@router.post("/{conversation_id}/messages", response_model=ApiResponse[ChatResponse])
async def chat(
    request: ChatRequest,
    pipeline: RAGPipeline = Depends(
        get_rag_pipeline
    ),
    service: 
):
    # answer = await pipeline.ask(
    #     request.question
    # )

    # if not answer:
    #     raise AppException(
    #         "No response found"
    #     )

    return StreamingResponse(
        pipeline.stream(request.question),
        media_type="text/event-stream",
    )