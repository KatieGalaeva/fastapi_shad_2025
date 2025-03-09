from pydantic import BaseModel, Field, field_validator
from pydantic_core import PydanticCustomError

__all__ = ["IncomingBook", "ReturnedBook", "ReturnedAllbooks"]


# Базовый класс "Книги", содержащий поля, которые есть во всех классах-наследниках.
class BaseBook(BaseModel):
    title: str
    author: str
    year: int
    seller_id: int | None



# Класс для валидации входящих данных. Не содержит id так как его присваивает БД.
class IncomingBook(BaseBook):
    pages: int = Field(
        default=150
    ) 

    @field_validator("year")  
    @staticmethod
    def validate_year(val: int):
        if val < 1950:
            raise PydanticCustomError("Validation error", "Year is too old!")

        return val


# Класс, валидирующий исходящие данные. Он уже содержит id
class ReturnedBook(BaseBook):
    id: int
    pages: int


# Класс для возврата массива объектов "Книга"
class ReturnedAllbooks(BaseModel):
    books: list[ReturnedBook]
