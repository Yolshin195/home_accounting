from litestar import Router

from .auth import AuthPageController
from .budget import BudgetController
from .calendar import CalendarController
from .dashboard import DashboardController
from .landing import LandingController
from .references import references_router
from .transaction import TransactionController

pages_router = Router(path="", route_handlers=[
    references_router,
    TransactionController,
    AuthPageController,
    DashboardController,
    CalendarController,
    LandingController,
    BudgetController
])