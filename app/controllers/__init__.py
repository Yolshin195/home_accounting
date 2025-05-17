from litestar import Router

from .pages import pages_router

routers = Router(path="/v2", route_handlers=[pages_router])