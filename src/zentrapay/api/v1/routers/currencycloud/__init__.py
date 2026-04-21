from .accounts import router as account_router
from .balances import router as balances_router
from .contacts import router as contacts_router
from .beneficiaries import router as beneficiaries_router
from .transactions import router as transactions_router
from .transfers import router as transfers_router
from .references import router as references_router
from .payments import router as payments_router
from .fx import router as fx_router
from .funding import router as funding_router
__all__ = [
    "account_router",
    "balances_router",
    "contacts_router",
    "beneficiaries_router",
    "transactions_router",
    "transfers_router",
    "references_router",
    "payments_router",
    "fx_router",
]
