from sqlalchemy import (String,ForeignKey,Integer,Enum)
from sqlalchemy.orm import (
    Mapped, 
    mapped_column,
    relationship
)
from app.database.base import Base
from app.database.mixins import (
    IDMixin,
    TimestampMixin
)
from app.database.enums import DocumentStatus


class Documents(Base,TimestampMixin,IDMixin):
    __tablename__ = "documents"


    filename: Mapped[str] = mapped_column(
        String(255)
    )
    original_filename: Mapped[str] = mapped_column(
        String(255)
    )

    content_type: Mapped[str] = mapped_column(
        String(100)
    )

    storage_path: Mapped[str] = mapped_column(
        String(100)
    )

    file_size: Mapped[int] = mapped_column(
        Integer
    )

    status: Mapped[DocumentStatus] = mapped_column(
        Enum(DocumentStatus),
        default=DocumentStatus.UPLOADED,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    user = relationship(
        "User",
        back_populates="documents"
    )