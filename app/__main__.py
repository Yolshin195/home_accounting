from pathlib import Path

from advanced_alchemy.extensions.litestar import SQLAlchemyInitPlugin
from litestar import Litestar, get
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.response import Template
from litestar.template.config import TemplateConfig

from app.controllers import routers
from app.db import sqlalchemy_config
from app.security import litestar_users


@get("/")
async def transaction_index() -> Template:
    return Template(template_name="transaction.html.jinja2")

@get("/reference/category")
async def category_index() -> Template:
    return Template(template_name="references/category.html.jinja2")

@get("/auth")
async def auth_index() -> Template:
    return Template(template_name="auth.html.jinja2")


@get("/books/{book_id:int}")
async def get_book(book_id: int) -> dict[str, int]:
    return {"book_id": book_id}

@get(
    "/v2/auth",
    exclude_from_auth=True,
)
async def auth_v2_index() -> Template:
    return Template(template_name="auth_v2.html.jinja2")

@get("/v2/calendar")
async def calendar_v2_index() -> Template:
    return Template(template_name="calendar.html.jinja2")


app = Litestar(
    [routers, calendar_v2_index, auth_index, transaction_index, category_index, get_book, auth_v2_index],
    template_config=TemplateConfig(
        directory=Path("app/templates"),
        engine=JinjaTemplateEngine,
    ),
    plugins=[SQLAlchemyInitPlugin(config=sqlalchemy_config), litestar_users],
)
