from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.orm import (Mapped, mapped_column,relationship)
from app.database.mixins import (
    IDMixin,
    TimestampMixin
)
from app.database.base import Base

class User(Base,IDMixin,TimestampMixin):
    __tablename__ = "users"
    
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
    )

    username: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        index=True,
    )

    hash_password: Mapped[str] = mapped_column(
        String(255)
    )

    is_active:Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    is_superuser: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    conversation = relationship(
        "Conversation",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    

