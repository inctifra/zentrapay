from zentrapay.api.v1.controllers.currencycloud import (
    retrieve_account_balance,
)
from zentrapay.api.v1.dependencies.main import CurrencyClientDep
from fastapi import APIRouter


router = APIRouter(prefix="/balances")


@router.get("/{currency}")
async def account_balance(currency: str, client: CurrencyClientDep):
    """
    Find the account id for the on_behalf_of:
    I will capture this from the user in my django db later
    """
    return await retrieve_account_balance(currency, client)
