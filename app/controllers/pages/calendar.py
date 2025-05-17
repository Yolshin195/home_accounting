from litestar import Controller, get
from litestar.response import Template


class CalendarController(Controller):
    path = "/"

    @get()
    async def calendar_v2_index(self) -> Template:
        return Template(template_name="transaction_v2.html.jinja2")