from fastapi import APIRouter, Depends, Query
from zentrapay.api.v1.models.currencycloud import FEchangeQueryModal
from zentrapay.api.v1.dependencies.main import CurrencyClientDep
from zentrapay.api.v1.controllers.currencycloud import (
    fx_realtime_exchange_rate_basic_information,
    fx_realtime_exchange_rate_detailed_information,
)

# Depends(get_authorized_currency_client)
router = APIRouter(prefix="/fx", dependencies=[])


@router.get("/basic")
async def realtime_exchange_rate_basic(
    client: CurrencyClientDep,
    base_currency: str = Query(..., min_length=3, max_length=3),
    quote_currency: str = Query(..., min_length=3, max_length=3),
):

    return await fx_realtime_exchange_rate_basic_information(
        base_currency, quote_currency, client
    )


@router.get("/detailed")
async def realtime_exchange_rate_detailed(
    client: CurrencyClientDep, params: FEchangeQueryModal = Depends()
):

    return await fx_realtime_exchange_rate_detailed_information(params, client)
