from litestar import Controller, get
from litestar.response import Template


class CalendarController(Controller):
    path = "/calendar"

    @get()
    async def index(self) -> Template:
        return Template(template_name="calendar_v3.html.jinja2")

    @get('/old')
    async def old_index(self) -> Template:
        return Template(template_name="calendar.html.jinja2")
