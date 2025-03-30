from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from .base import BaseModel

if TYPE_CHECKING:
    from .book import Book  # Import only for type hints to avoid circular imports

class Seller(BaseModel):
    __tablename__ = "sellers_table"  # FIXED: Correct table name

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    #hash_password: Mapped[str] = mapped_column(String(300), nullable=False)

    books: Mapped[list["Book"]] = relationship("Book", back_populates="seller", cascade="all, delete-orphan")
