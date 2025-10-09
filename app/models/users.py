from .base import Base
import uuid as PyUUID
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy import func, UUID, text

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    uuid: Mapped[PyUUID.UUID] = mapped_column(
        UUID(as_uuid=True),
        unique=True,
        nullable=False,
        index=True,
        default=PyUUID.uuid4
    )
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False, index=True)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(nullable=False,server_default=text("true"))
    deleted: Mapped[bool] = mapped_column(nullable=False, server_default=text("false"))
    is_superuser: Mapped[bool] = mapped_column(nullable=False, server_default=text("false"))
    is_verified: Mapped[bool] = mapped_column(nullable=False, server_default=text("false"))
    created_at: Mapped[datetime] = mapped_column(nullable=False, server_default=func.now())