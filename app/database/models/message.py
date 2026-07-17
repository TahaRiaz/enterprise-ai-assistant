from sqlalchemy import (
    ForeignKey,String,Text,
)

from sqlalchemy.orm import(
    Mapped, mapped_column, relationship
)

from app.database.base import Base
from app.database.mixins import (
    IDMixin,TimestampMixin
)

class Message(
    Base,IDMixin,TimestampMixin
):
    __tablename__ = "messages"

    role: Mapped[str] = mapped_column[
        String(28)
    ]

    content: Mapped[str] = mapped_column[
        Text
    ]

    conversation_id: Mapped[int] = mapped_column(ForeignKey("conversation.id"),)

    conversation= relationship(
        "Conversation",
        back_populates="message",
    )