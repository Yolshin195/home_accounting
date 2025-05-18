
from litestar.types import ASGIApp, Scope, Receive, Send


def redirect_unauthorized_users_middleware_factory(app: ASGIApp) -> ASGIApp:
    async def redirect_unauthorized_users_middleware(scope: Scope, receive: Receive, send: Send) -> None:
        await app(scope, receive, send)

    return redirect_unauthorized_users_middleware
