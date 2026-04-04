from fastapi import FastAPI
from config.settings.production import settings
from app.main import init_app
from api.v1.routers import currencycloud_router
from core.middleware import PrepopulateUserSessionMiddleware
from api.v1.routers.news import news_router

app = init_app(FastAPI)
app.add_middleware(PrepopulateUserSessionMiddleware)


app.include_router(
    currencycloud_router,
    prefix=f"/api/{settings.VERSION}",
)

app.include_router(
    news_router,
    prefix=f"/api/{settings.VERSION}",
)
