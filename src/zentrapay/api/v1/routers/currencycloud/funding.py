from fastapi import APIRouter, Request
from fastapi.params import Depends
from zentrapay.api.v1.controllers.currencycloud import funding_accounts, inbound_fund_account
from zentrapay.api.v1.dependencies.main import CurrencyClientDep
from zentrapay.api.v1.models.currencycloud import InboundFundingRequest, SSIFundingAccountQueryParams


router = APIRouter(
    prefix="/funding",
    # dependencies=[Depends(get_authorized_currency_client)]
)

## ------------------------------------------------------
### Find Funding Accounts
## ------------------------------------------------------

@router.get("/retrieve")
async def find_funding_accounts(
    client: CurrencyClientDep,
    params: SSIFundingAccountQueryParams = Depends(),
):
    """
    Gets details of the Standard Settlement Instructions (SSIs) 
    that can be used to settle and collect funds in each available currency.
    """
    return await funding_accounts(params=params, client=client)

@router.post("/account-funding")
async def fund_inbound_account(
    client: CurrencyClientDep,
    payload: InboundFundingRequest
):
    
    """
    Emulate inbound funds
    Triggers a production-like flow for processing funds, topping up CM balance or
    rejecting the transaction without topping up CM balance. 
    """
    return await inbound_fund_account(payload, client)