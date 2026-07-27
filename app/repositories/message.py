from sqlalchemy.orm import Session
from sqlalchemy import select
from app.database.models.message import Message
from app.repositories.base import BaseRepository

class MessageRepository(BaseRepository):

    def __init__(self, db:Session):
        super().__init__(db, Message)

    def add_message(self, message: Message):
        return super().create(message)

    def get_recent_messages(
            self, conversation_id: int,
    ) -> list[Message]:

        statement = select(Message).where(
            Message.conversation_id == conversation_id
        )

        return self.db.scalar(statement=statement).all()
        