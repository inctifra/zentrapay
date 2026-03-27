from api.v1.controllers.currencycloud import (
    reference_currencycloud_beneficiary_required_details,
    reference_currencycloud_currencies,
    reference_currencycloud_settlement_account,
)
from api.v1.dependencies.main import CurrencyClientDep
from api.v1.models.currencycloud import BeneficiaryPaymentRequirementModel
from fastapi import APIRouter, Depends


router = APIRouter(prefix="/references")


@router.get("/settlement-accounts")
async def retrieve_reference_settlement_account(client: CurrencyClientDep):
    return await reference_currencycloud_settlement_account(client)


@router.get("/currencies")
async def retrieve_reference_available_currencies(client: CurrencyClientDep):
    return await reference_currencycloud_currencies(client)


@router.get("/beneficiary-payment-requirements")
async def retrieve_reference_beneficiary_payment_requirements(
    client: CurrencyClientDep, params: BeneficiaryPaymentRequirementModel = Depends()
):
    return await reference_currencycloud_beneficiary_required_details(params, client)
