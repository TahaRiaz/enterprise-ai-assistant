from app.services.health_service import HealthService
from app.dependencies.repositories import get_user_repository
from app.repositories.user import UserRepository
from app.services.auth_service import AuthService
from app.services.document_service import DocumentService
from app.repositories.document import DocumentRepository
from app.repositories.message import MessageRepository
from app.repositories.conversation import ConversationRepository
from app.dependencies.repositories import get_document_repository, get_conversation_repository, get_message_repository, get_chunk_repository
from app.workers.document_processor import DocumentProcessor
from app.services.chat_service import ChatService
from app.rag.pipeline import RAGPipeline
from app.repositories.chunk import ChunkRepository
from app.services.chunk_service import ChunkService
from fastapi import Depends

def get_health_services() -> HealthService:
    return HealthService()

def get_auth_service(repository: UserRepository = Depends(get_user_repository,)):
    return AuthService(repository)


def get_document_service(repository: DocumentRepository = Depends(get_document_repository)):
    return DocumentService(repository)

def get_chunk_service(repository: ChunkRepository = Depends(get_chunk_repository)):
    return ChunkService(repository)

def get_document_processor_service(chunk_service: ChunkService = Depends(get_chunk_service)) -> DocumentProcessor:
    return DocumentProcessor(chunk_service=chunk_service)

def get_rag_pipeline() ->RAGPipeline:
    return RAGPipeline()

def get_chat_services(conversation_repository: ConversationRepository = Depends(get_conversation_repository),
                      message_repository:MessageRepository = Depends(get_message_repository),
                      pipeline: RAGPipeline = Depends(get_rag_pipeline)) -> ChatService:
    return ChatService(
        conversation_repository,
        message_repository,
        pipeline,
    )