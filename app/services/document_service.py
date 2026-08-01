from uuid import uuid4
from pathlib import Path

from fastapi import Depends,UploadFile
from app.database.enums import DocumentStatus
from app.database.models.documents import Document
from app.services.base_service import BaseService
from app.core.exceptions import AppException
from app.config.settings import Settings

class DocumentService(BaseService):

    def __init__(self, document_repository):
        self.document_repository = document_repository

    async def upload_document(
            self,
            file,
            current_user,
    ) -> Document:
        

        #validate file
        if not file.filename:
            raise AppException("Invalid filename")
        
        extension = Path(file.filename).suffix.lower()

        if extension not in Settings.ALLOWED_DOCUMENT_EXTENSIONS:
            raise AppException(
                f"Unsupported file type. Allowed types: {','.join(Settings.ALLOWED_DOCUMENT_EXTENSIONS)}"
            )
        
        content_type = file.content_type
        if content_type not in Settings.ALLOWED_TYPES:
            raise AppException(
                "Invalid FileType."
            )

        unique_filename = f"{uuid4()}{extension}"

        upload_dir = Path("storage/uploads")
        upload_dir.mkdir(parents=True, exist_ok=True)

        file_path = upload_dir / unique_filename

        size = 0

        with open(file_path, "wb") as buffer:
            while chunk := await file.read(1024 *1024):
                size += len(chunk)

                if size > Settings.MAX_FILE_SIZE:
                    buffer.close()
                    file_path.unlink(missing_ok=True)
                    raise AppException("File size exceeds 20 MB")
                
                buffer.write(chunk)

        document = Document(
            fielname=unique_filename,
            original_filename=file.filename,
            file_path=str(file_path),
            content_type=file.content_type,
            status= DocumentStatus.UPLOADED,
            user_id = current_user.id,
        )

        return self.document_repository.create(document)

