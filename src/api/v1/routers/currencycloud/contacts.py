
from api.v1.controllers.currencycloud import (
    create_account_contact,
    retrieve_currencycloud_accounts,
    retrieve_individual_contact,
    updated_currencycloud_contact,
)
from api.v1.dependencies.main import CurrencyClientDep
from api.v1.models.currencycloud import (
    ContactCreateModel,
    ContactUpdateModel,
)
from fastapi import APIRouter


router = APIRouter(prefix="/contacts")




@router.post("/create")
async def create_contact(
    payload: ContactCreateModel,
    client: CurrencyClientDep,
):
    """
    on_behalf_off: (contact id: d2c17a8b-8a30-47b8-b39d-63039e144473)
    """
    return await create_account_contact(payload, client)


@router.get("/{id}")
async def retrieve_contact(id: str, client: CurrencyClientDep):
    """
    The {id} will be users id saved on the proxy server
    """
    return await retrieve_individual_contact(id, client)


@router.post("/find")
async def retrieve_contacts(
    client: CurrencyClientDep,
):
    """
    Find all the contacts
    """
    return await retrieve_currencycloud_accounts(client)


@router.post("/{id}")
async def update_contact(
    id: str,
    payload: ContactUpdateModel,
    client: CurrencyClientDep,
):
    """
    The {id} will be users id saved on the proxy server
    """
    return await updated_currencycloud_contact(id, payload, client)

