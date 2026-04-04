import httpx
from config.settings.production import settings


class HttpClientProvider:
    """
    Provider to handle interactions with the Currency Cloud API.
    """

    def __init__(self):
        self.base_url = settings.CURRENCY_CLOUD_BASE_URL

    async def initialize(
        self, method: str, path: str, data: dict | None = None, timeout: int = 10
    ):
        """
        Generic method to make requests to Currency Cloud.
        """
        url = f"{self.base_url}/{path}"

        async with httpx.AsyncClient(timeout=timeout) as client:
            if method.upper() == "POST":
                res = await client.post(url, json=data)
            elif method.upper() == "GET":
                res = await client.get(url, params=data)
            else:
                raise NotImplementedError(f"Method {method} not implemented.")
            return res
