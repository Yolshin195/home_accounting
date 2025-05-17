from litestar import Controller, get
from litestar.response import Template


class BudgetController(Controller):
    path = "/budget"

    @get()
    async def index(self) -> Template:
        return Template(template_name="budget.html.jinja2")