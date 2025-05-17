from enum import Enum

from advanced_alchemy.base import UUIDAuditBase
from litestar_users.adapter.sqlalchemy.mixins import SQLAlchemyUserMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum as SQLEnum, ForeignKey
from sqlalchemy.orm import relationship


class TransactionType(str, Enum):
    EXPENSE = "expense"
    INCOME = "income"
    TRANSFER = "transfer"


class UserProfile(UUIDAuditBase, SQLAlchemyUserMixin):
    pass

class BaseEntity(UUIDAuditBase):
    __abstract__ = True


class Category(BaseEntity):
    name: Mapped[str]
    type: Mapped[TransactionType] = mapped_column(
        SQLEnum(TransactionType, native_enum=False),
        nullable=False,
        default=TransactionType.EXPENSE
    )
    author_id: Mapped[int] = mapped_column(ForeignKey("user_profile.id"))
    author: Mapped[UserProfile] = relationship(foreign_keys=[author_id])


class Transaction(BaseEntity):
    type: Mapped[TransactionType] = mapped_column(
        SQLEnum(TransactionType, native_enum=False),
        nullable=False,
        default=TransactionType.EXPENSE
    )
    amount: Mapped[float]
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    category: Mapped[Category] = relationship(foreign_keys=[category_id])
    author_id: Mapped[int] = mapped_column(ForeignKey("user_profile.id"))
    author: Mapped[UserProfile] = relationship(foreign_keys=[author_id])