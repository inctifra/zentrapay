from api.v1.controllers.currencycloud import (
    create_currencycloud_account,
    get_payment_charges_settings,
    retrieve_all_accounts,
    retrieve_currencycloud_account,
    update_currencycloud_account,
    retrieve_currencycloud_account_compliance_information,
    update_currencycloud_account_compliance_information,
    retrieve_current_user_main_account,
)
from api.v1.dependencies.main import (
    CurrencyClientAuthorizedDep,
    CurrencyClientDep,
)
from api.v1.models.currencycloud import (
    AccountCreateModel,
    AccountFilterModel,
    AccountUpdateModel,
    CompanyComplianceAccountModel,
)
from fastapi import APIRouter


router = APIRouter(prefix="/accounts")

## ------------------------------------------------------
### ACCOUNT RELATED PATHS
## ------------------------------------------------------


@router.post("/")
async def create_account(
    payload: AccountCreateModel,
    client: CurrencyClientDep,
):
    """
    Example endpoint for creating an account on Currency Cloud.
    Injects the authenticated client automatically.
    id: 02bd782e-76a5-4996-911a-ffc766641c29
    """
    return await create_currencycloud_account(payload=payload, client=client)


@router.get("/{id}")
async def retrieve_account(
    id: str,
    client: CurrencyClientDep,
):
    """
    Retrieve a currencycloud account based on the provided id.
    id: 02bd782e-76a5-4996-911a-ffc766641c29
    """
    return await retrieve_currencycloud_account(id, client)


@router.post("/{id}")
async def update_account(
    id: str,
    payload: AccountUpdateModel,
    client: CurrencyClientDep,
):
    """
    update a currencycloud account based on the provided id.
    id: 02bd782e-76a5-4996-911a-ffc766641c29
    """
    return await update_currencycloud_account(id, payload, client)


@router.get("/{id}/compliance-settings")
async def retrieve_account_compliance_information(
    id: str,
    client: CurrencyClientDep,
):
    """
    id: 02bd782e-76a5-4996-911a-ffc766641c29
    """
    return await retrieve_currencycloud_account_compliance_information(id, client)


@router.post("/{id}/compliance-settings")
async def update_account_compliance_information(
    id: str,
    payload: CompanyComplianceAccountModel,
    client: CurrencyClientDep,
):
    """
    id: 02bd782e-76a5-4996-911a-ffc766641c29
    """
    return await update_currencycloud_account_compliance_information(
        id, payload, client
    )


@router.get("/current")
async def retrieve_main_account(
    client: CurrencyClientDep,
    user=CurrencyClientAuthorizedDep,
):
    print("Hello people,", user)
    return await retrieve_current_user_main_account(client)


@router.post("/find")
async def retrieve_accounts(
    payload: AccountFilterModel,
    client: CurrencyClientAuthorizedDep,
):
    return await retrieve_all_accounts(payload, client)


@router.get("/{id}/payment-charges-settings")
async def retrieve_payment_charges_settings(id: str, client: CurrencyClientDep):
    """
    account_id: 02bd782e-76a5-4996-911a-ffc766641c29
    payment_settings_id: {
        shared: 1b8e8716-b177-49a2-9f5a-a04e32d35c2c,
        ours: 894308da-e217-4d9e-bd34-3bdfb1c56081
    }
    """
    return await get_payment_charges_settings(id, client)


