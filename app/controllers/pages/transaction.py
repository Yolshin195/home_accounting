from litestar import Controller, get
from litestar.response import Template


class TransactionController(Controller):
    path = "/"

    @get()
    async def transaction_v2_index(self) -> Template:
        return Template(template_name="transaction_v2.html.jinja2")