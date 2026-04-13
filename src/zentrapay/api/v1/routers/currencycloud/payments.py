from zentrapay.api.v1.controllers.currencycloud import (
    authorize_currencycloud_payment,
    confirm_currencycloud_payment,
    create_currencycloud_payment,
    payment_currencycloud_submission_info,
    retrieve_currencycloud_payment,
    retrieve_currencycloud_payments,
)
from zentrapay.api.v1.dependencies.main import CurrencyClientDep
from zentrapay.api.v1.models.currencycloud import (
    PaymentCreateModel,
    PaymentRetrievalModel,
)
from fastapi import APIRouter, Depends, Query


router = APIRouter(prefix="/payments")


@router.post("/create")
async def payment_create(
    payload: PaymentCreateModel,
    client: CurrencyClientDep,
):
    """7a184979-31b8-409e-af21-fdbf06e90790"""
    return await create_currencycloud_payment(payload, client)


@router.get("/find")
async def retrieve_payments(
    client: CurrencyClientDep,
):
    return await retrieve_currencycloud_payments(client)


@router.get("/{id}")
async def retrieve_payment(
    id: str,
    client: CurrencyClientDep,
    params: PaymentRetrievalModel = Depends(),
):
    return await retrieve_currencycloud_payment(id, client, params)


@router.get("{id}/confirmation")
async def confirm_payment(id: str, client: CurrencyClientDep):
    """
    Check the status of payment id: eca84f98-0a67-44d6-a152-9c62349a69b9
    """
    return await confirm_currencycloud_payment(id, client)


@router.get("{id}/submission-info")
async def payment_submission_info(id: str, client: CurrencyClientDep):
    """
    Check the status of payment id: eca84f98-0a67-44d6-a152-9c62349a69b9
    """
    return await payment_currencycloud_submission_info(id, client)


@router.post("/authorize")
async def authorize_payment(
    client: CurrencyClientDep,
    payment_ids: list[str] = Query(...),
):
    """
    Pass an array of payment_ids for payments you what to authorize
    """
    params = {"payment_ids": payment_ids}
    return await authorize_currencycloud_payment(params, client)
