from zentrapay.api.v1.controllers.currencycloud import (
    cancel_currencycloud_transfer,
    retrieve_currencycloud_transfer,
    retrieve_currencycloud_transfers,
    transfer_currencycloud_creation,
)
from zentrapay.api.v1.dependencies.main import CurrencyClientDep
from zentrapay.api.v1.models.currencycloud import TransferCreationModel
from fastapi import APIRouter


router = APIRouter(prefix="/transfers")


@router.post("/create")
async def create_transfer(
    payload: TransferCreationModel,
    client: CurrencyClientDep,
):
    """
    Pass an array of payment_ids for payments you what to authorize

    destination: 63ed9945-2026-4c56-9e24-b09be21cd7db
    source: 02bd782e-76a5-4996-911a-ffc766641c29
    source:
    """
    return await transfer_currencycloud_creation(payload, client)


@router.get("/{id}")
async def retrieve_transfer(id: str, client: CurrencyClientDep):
    return await retrieve_currencycloud_transfer(id, client)


@router.post("/{id}/cancel")
async def cancel_transfer(id: str, client: CurrencyClientDep):
    return await cancel_currencycloud_transfer(id, client)


@router.get("/find")
async def retrieve_transfers(client: CurrencyClientDep):
    return await retrieve_currencycloud_transfers(client)
