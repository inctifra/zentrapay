from fastapi import FastAPI
from config.settings.production import settings
from app.main import init_app
from api.v1.routers import currencycloud_router

app = init_app(FastAPI)


app.include_router(currencycloud_router, prefix=f"/api/{settings.VERSION}")