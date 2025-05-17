from advanced_alchemy.repository import SQLAlchemyAsyncRepository
from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService

from models import (
    UserProfile,
    Category,
    Transaction,
)


class UserProfileRepository(SQLAlchemyAsyncRepository[UserProfile]):
    model_type = UserProfile


class CategoryRepository(SQLAlchemyAsyncRepository[Category]):
    model_type = Category


class TransactionRepository(SQLAlchemyAsyncRepository[Transaction]):
    model_type = Transaction


class UserProfileRepositoryService(SQLAlchemyAsyncRepositoryService[UserProfile]):
    repository_type = UserProfileRepository


class CategoryRepositoryService(SQLAlchemyAsyncRepositoryService[Category]):
    repository_type = CategoryRepository


class TransactionRepositoryService(SQLAlchemyAsyncRepositoryService[Transaction]):
    repository_type = TransactionRepository
