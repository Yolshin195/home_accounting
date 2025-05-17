from typing import Any

from litestar import Request
from sqlalchemy.ext.asyncio import AsyncSession

from models import UserProfile
from repositories import CategoryRepositoryService
from services.reference.category import CategoryReferenceService


async def get_category_reference_service(
        session: AsyncSession, request: Request[UserProfile, Any, Any]
) -> CategoryReferenceService:
    return CategoryReferenceService(repo=CategoryRepositoryService(session=session), author=request.user)