from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.repositories.user import UserRepository
from app.repositories.document import DocumentRepository

def get_user_repository(db:Session = Depends(get_db),) -> UserRepository:
    return UserRepository(db=db)


def get_document_repository(db:Session = Depends(get_db),) -> DocumentRepository:
    return DocumentRepository(db=db)