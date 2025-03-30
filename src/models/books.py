from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from .base import BaseModel

if TYPE_CHECKING:
    from .seller import Seller  # Type hinting only to avoid runtime circular imports

class Book(BaseModel):
    __tablename__ = "books_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    author: Mapped[str] = mapped_column(String(100), nullable=False)
    year: Mapped[int]
    pages: Mapped[int]
    
    seller: Mapped["Seller"] = relationship(back_populates="books", uselist=False)
    seller_id: Mapped[int] = mapped_column(ForeignKey("sellers_table.id"), nullable=True)