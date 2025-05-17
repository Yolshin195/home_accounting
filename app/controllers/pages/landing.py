from litestar import Controller, get
from litestar.response import Template


class LandingController(Controller):
    path = "/landing"

    @get()
    async def index(self) -> Template:
        return Template(template_name="landing.html.jinja2")