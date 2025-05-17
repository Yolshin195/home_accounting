from litestar.dto import DTOData
from litestar.enums import RequestEncodingType
from litestar.exceptions import NotAuthorizedException
from litestar.params import Body
from litestar.response import Redirect
from litestar_users.schema import AuthenticationSchema
from litestar_users.service import UserServiceType
from typing import cast, Annotated
from litestar import Request, post, Controller
from litestar.di import Provide
from litestar_users.dependencies import provide_user_service
from app.security import UserRegistrationDTO, UserReadDTO, UserRegistrationSchema

class AuthPageController(Controller):
    @post(
        f'/register/form',
        dto=UserRegistrationDTO,
        return_dto=UserReadDTO,
        dependencies={"service": Provide(provide_user_service, sync_to_thread=False)},
        exclude_from_auth=True,
    )
    async def register_form(
            self,
            data: Annotated[DTOData[UserRegistrationSchema], Body(media_type=RequestEncodingType.URL_ENCODED)],
            service: UserServiceType,
            request: Request
    ) -> Redirect:
        """Register a new user."""
        await service.register(data.as_builtins(), request)
        return Redirect("/v2/auth")

    @post(
        'login/form',
        return_dto=UserReadDTO,
        dependencies={"service": Provide(provide_user_service, sync_to_thread=False)},
        exclude_from_auth=True,
    )
    async def login_session(
            self,
            data: Annotated[AuthenticationSchema, Body(media_type=RequestEncodingType.URL_ENCODED)],  # pyright: ignore
            service: UserServiceType,
            request: Request,
    ) -> Redirect:
        """Authenticate a user."""
        user = await service.authenticate(data, request)
        if user is None:
            request.clear_session()
            raise NotAuthorizedException(detail="login failed, invalid input")

        request.set_session({**request.session, "user_id": user.id})
        return Redirect("/v2")
