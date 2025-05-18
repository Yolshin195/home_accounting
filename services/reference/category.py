from uuid import UUID

from models import UserProfile, Category
from repositories import CategoryRepositoryService
from schema import CategoryCreate


class CategoryReferenceService:
    def __init__(self, repo: CategoryRepositoryService, author: UserProfile):
        self.repo = repo
        self.author = author

    async def get_categories(self):
        return await self.repo.list(author=self.author)

    async def create_category(self, new_category: CategoryCreate) -> None:
        await self.repo.create(Category(
            name=new_category.name,
            icon=new_category.icon,
            description=new_category.description,
            type=new_category.type,
            author=self.author,
        ), auto_commit=True)

    async def delete_category(self, category_id: UUID) -> None:
        category = await self.repo.get_one(author=self.author, id=category_id)
        if category:
            await self.repo.delete(item_id=category.id, auto_commit=True)