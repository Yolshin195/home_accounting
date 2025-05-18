from uuid import UUID

from litestar import Controller, get, post, delete
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
    async def category_v3_index(self, service: CategoryReferenceService) -> Template:
        categories = await service.get_categories()
        return Template(template_name="references/category_v3.html.jinja2", context={
            "categories": categories
        })

    @delete(status_code=302)
    async def delete(self, category_id: UUID, service: CategoryReferenceService) -> Redirect:
        await service.delete_category(category_id)
        return Redirect("/v2/reference/category")

    @get('/old')
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

