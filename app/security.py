from dataclasses import dataclass
from os import urandom

from advanced_alchemy.extensions.litestar import SQLAlchemyDTO, SQLAlchemyDTOConfig
from litestar.dto import DataclassDTO
from litestar.middleware.session.client_side import CookieBackendConfig
from litestar_users import LitestarUsersPlugin, LitestarUsersConfig
from litestar_users.config import AuthHandlerConfig, RegisterHandlerConfig, VerificationHandlerConfig
from litestar_users.service import BaseUserService

from typing import Any

from litestar import Request
from litestar.security.session_auth.auth import SessionAuth

from models import UserProfile


ENCODING_SECRET = "1234567890abcdef"


@dataclass
class UserRegistrationSchema:
    email: str
    password: str


class UserRegistrationDTO(DataclassDTO[UserRegistrationSchema]):
    """User registration DTO."""


class UserReadDTO(SQLAlchemyDTO[UserProfile]):
    config = SQLAlchemyDTOConfig(exclude={"password_hash"})


class UserUpdateDTO(SQLAlchemyDTO[UserProfile]):
    config = SQLAlchemyDTOConfig(exclude={"password_hash"}, partial=True)


class UserService(BaseUserService[UserProfile, Any, Any]):  # type: ignore[type-var]
    async def post_registration_hook(self, user: UserProfile, request: Request | None = None) -> None:
        print(f"User <{user.email}> has registered!")
        user.is_verified = True
        self.user_repository.session.add(user)
        await self.user_repository.session.commit()



session_config = CookieBackendConfig(secret=urandom(16))
litestar_users = LitestarUsersPlugin(
    config=LitestarUsersConfig(
        auth_backend_class=SessionAuth,
        secret=ENCODING_SECRET,
        user_model=UserProfile,  # pyright: ignore
        user_read_dto=UserReadDTO,
        user_registration_dto=UserRegistrationDTO,
        user_update_dto=UserUpdateDTO,
        user_service_class=UserService,  # pyright: ignore
        auth_handler_config=AuthHandlerConfig(),
        register_handler_config=RegisterHandlerConfig(),
        verification_handler_config=VerificationHandlerConfig(),
        session_backend_config=session_config,
        auth_exclude_paths=['/v2/auth', '/register/form', '/v2/calendar'],
    )
)
