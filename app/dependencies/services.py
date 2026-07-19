from app.services.health_service import HealthService
from app.dependencies.repositories import get_user_repository
from app.repositories.user import UserRepository
from app.services.auth_service import AuthService
from app.services.document_service import DocumentService
from app.repositories.document import DocumentRepository
from app.dependencies.repositories import get_document_repository
from app.workers.document_processor import DocumentProcessor
from fastapi import Depends

def get_health_services() -> HealthService:
    return HealthService()

def get_auth_service(repository: UserRepository = Depends(get_user_repository,)):
    return AuthService(repository)


def get_document_service(repository: DocumentRepository = Depends(get_document_repository)):
    return DocumentService(repository)

def get_document_processor_service() -> DocumentProcessor:
    return DocumentProcessor()