from sqlalchemy import ( ForeignKey, String)
from sqlalchemy.orm import (Mapped, mapped_column, relationship)

from app.database.base import Base
from app.database.mixins import IDMixin,TimestampMixin

class Conversation(
    Base,
    IDMixin,TimestampMixin
):
    __tablename__ = "conversations"

    title: Mapped[str] = mapped_column(
        String(255)
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
    )
    
    user = relationship(
        "User",
        back_populates="converstations"
    )

    messages = relationship(
        "Message",
        back_populates="conversation",
        cascade="all, delete-orphan"
    )
