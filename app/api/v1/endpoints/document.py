from fastapi import APIRouter,BackgroundTasks
from app.core.constants import APITags
from app.schemas.document import DocumentResponse
from app.schemas.common import ApiResponse
from fastapi import UploadFile,File,Depends
from app.database.models.user import User
from app.dependencies.auth import get_current_user
from app.dependencies.services import get_document_service, get_document_processor_service
from app.services.document_service import DocumentService
from app.workers.document_processor import DocumentProcessor


router = APIRouter(
    prefix="/documents",
    tags= APITags.DOCUMENTS
)

@router.post("/upload", response_model=ApiResponse[DocumentResponse])
async def upload(
    background_tasks:BackgroundTasks,
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    service: DocumentService = Depends(get_document_service),
    processor: DocumentProcessor = Depends(get_document_processor_service)
):
    document = service.upload_document(
        file=file,
        current_user=current_user
    )

    background_tasks.add_task(processor.process_document, document_id=document.id)

    return ApiResponse(
        success=True,
        message="Uploaded successfully.",
        data=DocumentResponse.model_validate(document)
    )