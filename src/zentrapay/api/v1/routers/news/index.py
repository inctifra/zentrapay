from zentrapay.api.v1.controllers.news import headlines, everything
from zentrapay.api.v1.dependencies.main import NewsHttpClientAuthorizedProviderDep
from zentrapay.api.v1.models.news import TopNewsFilterModel, NewsFilterModel
from fastapi import APIRouter, Depends


router = APIRouter(prefix="/news", tags=["News"])


@router.get("/")
async def get_all_news(
    client: NewsHttpClientAuthorizedProviderDep, payload: NewsFilterModel = Depends()
):
    return await everything(client, payload)


@router.get("/headlines")
async def get_headlines(
    client: NewsHttpClientAuthorizedProviderDep, payload: TopNewsFilterModel = Depends()
):
    return await headlines(client, payload)
