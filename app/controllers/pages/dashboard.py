from litestar import Controller, get
from litestar.response import Template


class DashboardController(Controller):
    path = "/dashboard"

    @get()
    async def index(self) -> Template:
        return Template(template_name="dashboard.html.jinja2")