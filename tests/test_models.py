import pytest
from dependency_injector.wiring import inject, Provide

from containers import Container
from repositories import TransactionRepositoryService, UserProfileRepositoryService
from tests.factories import UserProfileFactory, CategoryFactory, TransactionFactory


@pytest.mark.asyncio
async def test_polyfactory(user_repo):
    mock_user = UserProfileFactory.build()

    user_bd = await user_repo.create(mock_user, auto_commit=True)

    print(user_bd.username)
    assert user_bd.username == mock_user.username


# @pytest.mark.asyncio
# @inject
# async def test_transaction(repo: TransactionRepositoryService = Provide[Container.transaction_repository]):
#     mock_user = UserProfileFactory.build()
#     mock_category = CategoryFactory.build(author=mock_user)
#     mock_transaction = TransactionFactory.build(category=mock_category, author=mock_user)
#     t1 = await repo.create(mock_transaction, auto_commit=True)
#
#     assert t1.id == mock_transaction.id
#     assert t1.amount == mock_transaction.amount
#     assert t1.category.name == mock_category.name
