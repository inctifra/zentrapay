from zentrapay.api.v1.dependencies.main import NewsHttpClientAuthorizedProviderDep
from zentrapay.api.v1.models.news import TopNewsFilterModel, NewsFilterModel


async def everything(
    client: NewsHttpClientAuthorizedProviderDep, payload: NewsFilterModel
):
    query = payload.model_dump(exclude_none=True, mode="json")
    return await client.get("/everything", params=query)


async def headlines(
    client: NewsHttpClientAuthorizedProviderDep, payload: TopNewsFilterModel
):
    query = payload.model_dump(exclude_none=True, mode="json")
    return await client.get("/top-headlines", params=query)
