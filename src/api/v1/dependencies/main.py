from typing import Annotated
from pydantic import BaseModel
from .auth import authorize_user
from api.v1.providers.auth import CurrencyCloudClient
from api.v1.routers.common.utils import get_currencycloud_client
from fastapi import Depends


class User(BaseModel):
    user_id: str
    role: str


CurrencyClientDep = Annotated[CurrencyCloudClient, Depends(get_currencycloud_client)]


async def get_authorized_currency_client(
    client: CurrencyClientDep,
    user_data: dict = Depends(authorize_user),
) -> CurrencyCloudClient:
    user = User(**user_data)
    client.userObject = user.model_dump()
    return client


CurrencyClientAuthorizedDep = Annotated[
    CurrencyCloudClient, Depends(get_authorized_currency_client)
]
