from typing import AsyncGenerator

import pytest_asyncio
from advanced_alchemy.config import AsyncSessionConfig, SQLAlchemyAsyncConfig
from sqlalchemy.ext.asyncio import AsyncSession

from containers import Container
from models import BaseEntity
from services import UserProfileService

@pytest_asyncio.fixture
async def container() -> Container:
    """Фикстура для настройки и доступа к контейнеру в тестах."""
    # Создаем инстанс вашего контейнера
    container = Container()

    # Настраиваем контейнер для тестовой среды через провайдер Configuration
    container.config.db.connection_string.override("sqlite+aiosqlite:///:memory:")
    container.config.db.create_all.override(True)

    await container.init_resources()
    container.wire(modules=[__name__])

    # Возвращаем настроенный контейнер
    return container

@pytest_asyncio.fixture
async def user_repo(container):
    return container.user_profile_repository()


@pytest_asyncio.fixture
async def transaction_repo(container):
    return container.transaction_repository()


