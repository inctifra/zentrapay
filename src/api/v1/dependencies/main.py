from typing import Annotated

from .auth import authorize_user
from api.v1.providers.auth import CurrencyCloudClient
from api.v1.routers.common.utils import get_currencycloud_client
from fastapi import Depends


async def get_authorized_currency_client(
    user=Depends(authorize_user),
    client: CurrencyCloudClient = Depends(get_currencycloud_client),
) -> CurrencyCloudClient:
    print("Hello people")
    client.user_id = user["user_id"]
    return client

## Without the auth service
CurrencyClientDep = Annotated[CurrencyCloudClient, Depends(get_currencycloud_client)]
## With the auth service imposed
CurrencyClientAuthorizedDep = Annotated[
    CurrencyCloudClient, Depends(get_authorized_currency_client)
]
