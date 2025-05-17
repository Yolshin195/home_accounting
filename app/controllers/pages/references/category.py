from litestar import Controller, get, post
from litestar.di import Provide
from litestar.enums import RequestEncodingType
from litestar.params import Body
from litestar.response import Template, Redirect
from typing_extensions import Annotated

from app.providers import get_category_reference_service
from schema import CategoryCreate
from services.reference.category import CategoryReferenceService


class CategoryReferenceController(Controller):
    path = "/category"
    dependencies = {
        "service": Provide(get_category_reference_service)
    }

    @get()
    async def category_v2_index(self, service: CategoryReferenceService) -> Template:
        categories = await service.get_categories()
        return Template(template_name="references/category_v2.html.jinja2", context={
            "categories": categories
        })

    @post()
    async def create(
            self,
            data: Annotated[CategoryCreate, Body(media_type=RequestEncodingType.URL_ENCODED)],
            service: CategoryReferenceService
    ) -> Redirect:
        await service.create_category(data)
        return Redirect("/v2/reference/category")

