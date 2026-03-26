from typing import Any

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


async def create_currencycloud_account(
    payload: AccountCreateModel, client: CurrencyCloudClient
):
    data = payload.model_dump(mode="json")
    return await client.post("accounts/create", data=data)


async def retrieve_currencycloud_account(id: str, client: CurrencyCloudClient):
    return await client.get(f"accounts/{id}")


async def update_currencycloud_account(
    id: str, payload: AccountUpdateModel, client: CurrencyCloudClient
):
    data = payload.model_dump(mode="json")
    return await client.post(f"accounts/{id}", data=data)


async def retrieve_currencycloud_account_compliance_information(
    id: str, client: CurrencyCloudClient
):
    return await client.get(f"accounts/{id}/compliance_settings")


async def update_currencycloud_account_compliance_information(
    id: str, payload: CompanyComplianceAccountModel, client: CurrencyCloudClient
):
    data = payload.model_dump(mode="json")
    return await client.post(f"accounts/{id}", data=data)


async def retrieve_current_user_main_account(client: CurrencyCloudClient):
    return await client.get("accounts/current")


async def retrieve_all_accounts(
    payload: AccountFilterModel, client: CurrencyCloudClient
):
    data = payload.model_dump(mode="json")
    return await client.post("accounts/find", data=data)


async def get_payment_charges_settings(id: str, client: CurrencyCloudClient):
    return await client.get(f"accounts/{id}/payment_charges_settings")


async def retrieve_account_balance(currency: str, client: CurrencyCloudClient):
    """
    Find the account id for the on_behalf_of:
    I will capture this from the user in my django db later

    """
    return await client.get(f"balances/{currency}")


### =================================
# Contact creation
### =================================


async def create_account_contact(
    payload: ContactCreateModel, client: CurrencyCloudClient
):
    data = payload.model_dump(mode="json")
    return await client.post("/contacts/create", data=data)


async def retrieve_individual_contact(id: str, client: CurrencyCloudClient):
    return await client.get(f"contacts/{id}")


async def updated_currencycloud_contact(
    id: str, payload: ContactUpdateModel, client: CurrencyCloudClient
):
    data = payload.model_dump(mode="json")
    return await client.post(f"contacts/{id}", data=data)


async def retrieve_currencycloud_account_transactions(
    params: TransactionQueryModel, client: CurrencyCloudClient
):
    query_params = params.model_dump(exclude_none=True, mode="json")
    return await client.get("transactions/find", params=query_params)
