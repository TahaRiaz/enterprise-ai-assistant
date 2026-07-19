from app.database.models.document import Document
from app.repositories.base import BaseRepository
from sqlalchemy.orm import Session
from sqlalchemy import select

class DocumentRepository(BaseRepository):

    def __init__(self, db:Session,):
        super().__init__(db, Document)

    def get_by_id(self, doc_id:int):
        statement = select(Document).where(
            Document.id == doc_id
        )

        return self.db.scalar(statement=statement)

    def get_by_user(self, user_id:int):
        statement = select(Document).where(
            Document.user_id == user_id
        
        )

        return self.db.scalar(statement=statement).all()
    
    def get_current_status(self,doc_id:int):
        statement = select(Document).where(
            Document.id ==doc_id
        )

        return self.db.scalar(statement=statement).status