from litestar import Router

from .category import CategoryReferenceController

references_router = Router(path="/reference", tags=["reference"], route_handlers=[
    CategoryReferenceController
])