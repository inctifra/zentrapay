from api.v1.controllers.currencycloud import (
    create_account_contact,
    create_currencycloud_account,
    get_payment_charges_settings,
    retrieve_account_balance,
    retrieve_all_accounts,
    retrieve_currencycloud_account,
    retrieve_currencycloud_account_transactions,
    retrieve_individual_contact,
    update_currencycloud_account,
    retrieve_currencycloud_account_compliance_information,
    update_currencycloud_account_compliance_information,
    retrieve_current_user_main_account,
    updated_currencycloud_contact,
)
from api.v1.models.currencycloud import (
    AccountCreateModel,
    AccountFilterModel,
    AccountUpdateModel,
    CompanyComplianceAccountModel,
    ContactCreateModel,
    ContactUpdateModel,
    TransactionQueryModel,
)
from api.v1.providers.auth import CurrencyCloudClient
from api.v1.routers.common.utils import get_currencycloud_client
from fastapi import APIRouter, Depends


router = APIRouter(tags=["CurrencyCloud"], prefix="/currencycloud")

## ------------------------------------------------------
### ACCOUNT RELATED PATHS
## ------------------------------------------------------


@router.post("/accounts")
async def create_account(
    payload: AccountCreateModel,
    client: CurrencyCloudClient = Depends(get_currencycloud_client),
):
    """
    Example endpoint for creating an account on Currency Cloud.
    Injects the authenticated client automatically.
    id: 02bd782e-76a5-4996-911a-ffc766641c29
    """
    return await create_currencycloud_account(payload=payload, client=client)


@router.get("/accounts/{id}")
async def retrieve_account(
    id: str,
    client: CurrencyCloudClient = Depends(get_currencycloud_client),
):
    """
    Retrieve a currencycloud account based on the provided id.
    id: 02bd782e-76a5-4996-911a-ffc766641c29
    """
    return await retrieve_currencycloud_account(id, client)


@router.post("/accounts/{id}")
async def update_account(
    id: str,
    payload: AccountUpdateModel,
    client: CurrencyCloudClient = Depends(get_currencycloud_client),
):
    """
    update a currencycloud account based on the provided id.
    id: 02bd782e-76a5-4996-911a-ffc766641c29
    """
    return await update_currencycloud_account(id, payload, client)


@router.get("/accounts/{id}/compliance-settings")
async def retrieve_account_compliance_information(
    id: str,
    client: CurrencyCloudClient = Depends(get_currencycloud_client),
):
    """
    id: 02bd782e-76a5-4996-911a-ffc766641c29
    """
    return await retrieve_currencycloud_account_compliance_information(id, client)


@router.post("/accounts/{id}/compliance-settings")
async def update_account_compliance_information(
    id: str,
    payload: CompanyComplianceAccountModel,
    client: CurrencyCloudClient = Depends(get_currencycloud_client),
):
    """
    id: 02bd782e-76a5-4996-911a-ffc766641c29
    """
    return await update_currencycloud_account_compliance_information(
        id, payload, client
    )


@router.get("/accounts/current")
async def retrieve_main_account(
    client: CurrencyCloudClient = Depends(get_currencycloud_client),
):
    return await retrieve_current_user_main_account(client)


@router.post("/accounts/find")
async def retrieve_accounts(
    payload: AccountFilterModel,
    client: CurrencyCloudClient = Depends(get_currencycloud_client),
):
    return await retrieve_all_accounts(payload, client)


@router.get("/accounts/{id}/payment-charges-settings")
async def retrieve_payment_charges_settings(
    id: str, client: CurrencyCloudClient = Depends(get_currencycloud_client)
):
    """
    account_id: 02bd782e-76a5-4996-911a-ffc766641c29
    payment_settings_id: {
        shared: 1b8e8716-b177-49a2-9f5a-a04e32d35c2c,
        ours: 894308da-e217-4d9e-bd34-3bdfb1c56081
    }
    """
    return await get_payment_charges_settings(id, client)


## ------------------------------------------------------
### BALANCE RELATED PATHS
## ------------------------------------------------------


@router.get("/balances/{currency}")
async def account_balance(
    currency: str, client: CurrencyCloudClient = Depends(get_currencycloud_client)
):
    """
    Find the account id for the on_behalf_of:
    I will capture this from the user in my django db later
    """
    return await retrieve_account_balance(currency, client)


## ------------------------------------------------------
### CONTACT MANAGEMENT PATHS
## ------------------------------------------------------


@router.post("/contacts/create")
async def create_contact(
    payload: ContactCreateModel,
    client: CurrencyCloudClient = Depends(get_currencycloud_client),
):
    """
    on_behalf_off: (contact id: d2c17a8b-8a30-47b8-b39d-63039e144473)
    """
    return await create_account_contact(payload, client)


@router.get("/contacts/{id}")
async def retrieve_contact(
    id: str, client: CurrencyCloudClient = Depends(get_currencycloud_client)
):
    """
    The {id} will be users id saved on the proxy server
    """
    return await retrieve_individual_contact(id, client)


@router.post("/contacts/{id}")
async def update_contact(
    id: str,
    payload: ContactUpdateModel,
    client: CurrencyCloudClient = Depends(get_currencycloud_client),
):
    """
    The {id} will be users id saved on the proxy server
    """
    return await updated_currencycloud_contact(id, payload, client)




## ------------------------------------------------------
### TRANSACTION MANAGEMENT PATHS
## ------------------------------------------------------

@router.get("/transactions/find")
async def retrieve_transactions(
    params: TransactionQueryModel= Depends(),
    client: CurrencyCloudClient = Depends(get_currencycloud_client)
):
    return await retrieve_currencycloud_account_transactions(params, client)

