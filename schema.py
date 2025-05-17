from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, UUID4


class TransactionType(str, Enum):
    EXPENSE = "expense"
    INCOME = "income"
    TRANSFER = "transfer"


# Базовая схема с общими полями
class CategoryBase(BaseModel):
    name: str
    type: TransactionType = TransactionType.EXPENSE


# Схема для создания новой категории
class CategoryCreate(CategoryBase):
    pass


# Схема для получения категории (при чтении)
class CategoryRead(CategoryBase):
    id: UUID4
    author_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Схема для обновления категории
class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[TransactionType] = None


# Схема для удаления категории - обычно здесь не требуется особых полей,
# но иногда используется для подтверждения удаления
class CategoryDelete(BaseModel):
    id: UUID4


# Схема для фильтрации/поиска категорий
class CategoryFilter(BaseModel):
    name: Optional[str] = None
    type: Optional[TransactionType] = None
    author_id: Optional[int] = None

