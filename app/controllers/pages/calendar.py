from litestar import Controller, get
from litestar.response import Template


class CalendarController(Controller):
    path = "/calendar"

    @get()
    async def index(self) -> Template:
        return Template(template_name="calendar.html.jinja2")