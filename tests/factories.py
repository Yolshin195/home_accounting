from polyfactory.factories.sqlalchemy_factory import SQLAlchemyFactory

from models import UserProfile, Category, Transaction


class UserProfileFactory(SQLAlchemyFactory[UserProfile]):
    pass

class CategoryFactory(SQLAlchemyFactory[Category]):
    pass

class TransactionFactory(SQLAlchemyFactory[Transaction]):
    pass