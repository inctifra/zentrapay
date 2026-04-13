from zentrapay.api.v1.providers.auth import CurrencyCloudClient
from zentrapay.config.settings.production import settings
from fastapi.exceptions import HTTPException


async def get_currencycloud_client() -> CurrencyCloudClient:
    """
    Provides an authenticated CurrencyCloudClient instance.
    """
    client = CurrencyCloudClient(
        login_id=settings.CURRENCY_CLOUD_LOGIN_ID,
        api_key=settings.CURRENCY_CLOUD_API_KEY,
        base_url=settings.CURRENCY_CLOUD_BASE_URL,
    )
    try:
        await client.authenticate()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Currency Cloud auth failed: {e}")
    return client
