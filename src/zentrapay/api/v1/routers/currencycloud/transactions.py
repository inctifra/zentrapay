from uuid import UUID

from zentrapay.api.v1.controllers.currencycloud import (
    retrieve_currencycloud_account_transaction,
    retrieve_currencycloud_account_transactions,
)
from zentrapay.api.v1.dependencies.main import CurrencyClientDep
from zentrapay.api.v1.models.currencycloud import TransactionQueryModel
from fastapi import APIRouter, Depends


router = APIRouter(prefix="/transactions")


@router.get("/find")
async def retrieve_transactions(
    client: CurrencyClientDep,
    params: TransactionQueryModel = Depends(),
):
    return await retrieve_currencycloud_account_transactions(params, client)


@router.get("/{id}")
async def retrieve_transaction(
    id: UUID,
    client: CurrencyClientDep,
    params: TransactionQueryModel = Depends(),
):
    return await retrieve_currencycloud_account_transaction(id, params, client)
