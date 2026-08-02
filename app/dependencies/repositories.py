from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.repositories.user import UserRepository
from app.repositories.document import DocumentRepository
from app.repositories.conversation import ConversationRepository
from app.repositories.message import MessageRepository
from app.repositories.chunk import ChunkRepository

def get_user_repository(db:Session = Depends(get_db),) -> UserRepository:
    return UserRepository(db=db)


def get_document_repository(db:Session = Depends(get_db),) -> DocumentRepository:
    return DocumentRepository(db=db)


def get_conversation_repository( db:Session = Depends (get_db)) -> ConversationRepository:
    return ConversationRepository(db=db)

def get_message_repository(db:Session = Depends(get_db),) -> MessageRepository:
    return MessageRepository(db=db)

def get_chunk_repository(db:Session = Depends(get_db),) -> ChunkRepository:
    return ChunkRepository(db=db)