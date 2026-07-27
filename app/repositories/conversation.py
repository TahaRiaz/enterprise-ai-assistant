from app.repositories.base import BaseRepository
from app.database.models.coversation import Conversation
from app.database.models.message import Message
from app.schemas.chat import ChatRequest
from sqlalchemy.orm import Session
from sqlalchemy import select

class ConversationRepository(BaseRepository):

    def __init__(self, db:Session):
        super().__init__(db, Conversation)


    def create_conversation(self, chat:ChatRequest):

        return super().create(Conversation(
            title = chat.question,
            user_id= chat.user_id,
        ))

    def get_by_id_and_user(self, conversation_id:int, user_id:str):
        statement =  select(Conversation).where(
            Conversation.id == conversation_id
        ).where(
            Conversation.user_id == user_id
        )

        return self.db.scalar(statement=statement)