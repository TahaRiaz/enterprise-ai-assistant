from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

class TimestampMixin:

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    update_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )


class IDMixin:
    id:Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )