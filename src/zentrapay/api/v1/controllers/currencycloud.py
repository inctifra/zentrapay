from uuid import UUID

from zentrapay.api.v1.dependencies.main import CurrencyClientAuthorizedDep
from zentrapay.api.v1.models.currencycloud import (
    AccountCreateModel,
    AccountFilterModel,
    AccountUpdateModel,
    BeneficiaryCreationModel,
    BeneficiaryDeleteModel,
    BeneficiaryPaymentRequirementModel,
    BeneficiaryRetrievalModel,
    CompanyComplianceAccountModel,
    ContactCreateModel,
    ContactUpdateModel,
    FEchangeQueryModal,
    PaymentCreateModel,
    PaymentRetrievalModel,
    TransactionQueryModel,
    TransferCreationModel,
)
from zentrapay.api.v1.providers.auth import CurrencyCloudClient


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


async def retrieve_current_user_main_account(client: CurrencyClientAuthorizedDep):
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


async def retrieve_currencycloud_accounts(client: CurrencyCloudClient):
    return await client.post("contacts/find")


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


async def retrieve_currencycloud_account_transaction(
    id: UUID, params: TransactionQueryModel, client: CurrencyCloudClient
):
    query_params = params.model_dump(exclude_none=True, mode="json")
    return await client.get(f"transactions/{id}", params=query_params)


### =================================
# Beneficiaries controllers
### =================================


async def create_currencycloud_beneficiary(
    payload: BeneficiaryCreationModel, client: CurrencyCloudClient
):
    data = payload.model_dump(exclude_none=True, mode="json")
    return await client.post("beneficiaries/create", data)


async def retrieve_currencycloud_beneficiaries(
    payload: BeneficiaryRetrievalModel, client: CurrencyCloudClient
):
    data = payload.model_dump(exclude_none=True, mode="json")
    return await client.post("beneficiaries/find", data)


async def retrieve_currencycloud_beneficiary_account(
    id: str, client: CurrencyCloudClient
):
    return await client.get(f"beneficiaries/{id}")


async def delete_currencycloud_beneficiary_account(
    id: str, payload: BeneficiaryDeleteModel, client: CurrencyCloudClient
):
    data = payload.model_dump(exclude_none=True, mode="json")
    return await client.post(f"beneficiaries/{id}/delete", data)


### =================================
# Payment controllers
### =================================


async def create_currencycloud_payment(
    payload: PaymentCreateModel, client: CurrencyCloudClient
):
    """
    create payment
    """
    data = payload.model_dump(mode="json")
    return await client.post("payments/create", data=data)


async def retrieve_currencycloud_payments(client: CurrencyCloudClient):
    return await client.get("payments/find")


async def retrieve_currencycloud_payment(
    id: str, client: CurrencyCloudClient, params: PaymentRetrievalModel | None = None
):
    param = params.model_dump(exclude_none=True, mode="json")
    return await client.get(f"payments/{id}", params=param)


async def confirm_currencycloud_payment(id: str, client: CurrencyCloudClient):
    return await client.get(f"payments/{id}/confirmation")


async def payment_currencycloud_submission_info(id: str, client: CurrencyCloudClient):
    return await client.get(f"payments/{id}/submission_info")


async def authorize_currencycloud_payment(params: dict, client: CurrencyCloudClient):
    return await client.post("payments/authorise", params)


async def transfer_currencycloud_creation(
    payload: TransferCreationModel, client: CurrencyCloudClient
):
    """_summary_

    Args:
        payload (TransferCreationModel): {
            sender_account_id: id
            receiver_id: id
        }
        client (CurrencyCloudClient): _description_
    """
    data = payload.model_dump(exclude_none=True, mode="json")
    return await client.post("transfers/create", data)


async def retrieve_currencycloud_transfer(id: str, client: CurrencyCloudClient):
    """id: b54c933a-360c-43bb-8069-b52c0b82fecb"""
    return await client.get(f"transfers/{id}")


async def cancel_currencycloud_transfer(id: str, client: CurrencyCloudClient):
    """id: b54c933a-360c-43bb-8069-b52c0b82fecb"""
    return await client.post(f"transfers/{id}/cancel")


async def retrieve_currencycloud_transfers(client: CurrencyCloudClient):
    """All the transfers created by the user"""
    return await client.get("transfers/find")


### =================================
# References controllers
### =================================


async def reference_currencycloud_settlement_account(client: CurrencyCloudClient):
    return await client.get("reference/settlement_accounts")


async def reference_currencycloud_currencies(client: CurrencyCloudClient):
    return await client.get("reference/currencies")


async def reference_currencycloud_beneficiary_required_details(
    params: BeneficiaryPaymentRequirementModel, client: CurrencyCloudClient
):
    params = params.model_dump(exclude_none=True, mode="json")
    return await client.get("reference/beneficiary_required_details", params)


### =================================
# Foreign exchange rates controllers
### =================================
async def fx_realtime_exchange_rate_basic_information(
    base_currency: str,
    quote_currency: str,
    client: CurrencyCloudClient,
):
    pair = f"{base_currency.upper()}{quote_currency.upper()}"
    return await client.get("rates/find", params={"currency_pair": pair})


async def fx_realtime_exchange_rate_detailed_information(
    params: FEchangeQueryModal,
    client: CurrencyCloudClient,
):
    _params = params.model_dump(exclude_none=True, mode="json")
    return await client.get("rates/detailed", params=_params)
