from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship


from app.database.base import Base
from app.database.mixins import IDMixin,TimestampMixin


class Chunk(Base, IDMixin, TimestampMixin):

    __tablename__ = "chunks"

    document_id: Mapped[int] = mapped_column(
        ForeignKey("documents.id", ondelete="CASCADE")
    )

    chunk_index = Mapped[int] = mapped_column(
        nullable=False
    )

    page_number: Mapped[int |None] = mapped_column(
        nullable=True,
        )

    text:Mapped[str] = mapped_column(
        Text,nullable=False,
    )

    document = relationship(
        "Document",
        back_populates="chunks"
    )