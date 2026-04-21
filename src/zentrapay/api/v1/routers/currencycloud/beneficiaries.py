from uuid import UUID

from fastapi.params import Depends
from zentrapay.api.v1.controllers.currencycloud import (
    create_currencycloud_beneficiary,
    delete_currencycloud_beneficiary_account,
    retrieve_currencycloud_beneficiaries,
    retrieve_currencycloud_beneficiary_account,
)
from zentrapay.api.v1.dependencies.main import CurrencyClientDep
from zentrapay.api.v1.models.currencycloud import (
    BeneficiaryCreationModel,
    BeneficiaryDeleteModel,
    BeneficiaryRetrievalModel,
)
from fastapi import APIRouter

router = APIRouter(prefix="/beneficiaries")


@router.post("/create")
async def create_beneficiary(
    payload: BeneficiaryCreationModel,
    client: CurrencyClientDep,
):
    """
    contact id(on_behalf_of): d2c17a8b-8a30-47b8-b39d-63039e144473
    """
    return await create_currencycloud_beneficiary(payload, client)


@router.get("/find")
async def retrieve_beneficiaries(
    client: CurrencyClientDep,
    payload: BeneficiaryRetrievalModel = Depends(),
):
    """
    Beneficiary id[0]: bfe529f3-e822-4951-857c-0d2414bb519c
    """
    return await retrieve_currencycloud_beneficiaries(payload, client)


@router.get("/{id}")
async def retrieve_beneficiary_account(id: str, client: CurrencyClientDep):
    """
    Beneficiary id: bfe529f3-e822-4951-857c-0d2414bb519c
    """
    return await retrieve_currencycloud_beneficiary_account(id, client)


@router.delete("/{id}/delete")
async def delete_beneficiary_account(
    id: UUID,
    payload: BeneficiaryDeleteModel,
    client: CurrencyClientDep,
):
    """
    on_behalf_of: bfe529f3-e822-4951-857c-0d2414bb519c
    """
    return await delete_currencycloud_beneficiary_account(id, payload, client)
