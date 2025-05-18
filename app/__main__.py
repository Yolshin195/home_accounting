from pathlib import Path

from advanced_alchemy.extensions.litestar import SQLAlchemyInitPlugin
from litestar import Litestar
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.template.config import TemplateConfig

from app.controllers import routers
from app.db import sqlalchemy_config
from app.middleware import redirect_unauthorized_users_middleware_factory
from app.security import litestar_users
from litestar.plugins.htmx import HTMXPlugin


app = Litestar(
    [routers],
    template_config=TemplateConfig(
        directory=Path("app/templates"),
        engine=JinjaTemplateEngine,
    ),
    plugins=[SQLAlchemyInitPlugin(config=sqlalchemy_config), litestar_users],
    middleware=[redirect_unauthorized_users_middleware_factory]
)
