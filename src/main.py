from fastapi import FastAPI
from zentrapay.config.settings.production import settings
from zentrapay.app.main import init_app
from zentrapay.api.v1.routers import currencycloud_router
from zentrapay.core.middleware import PrepopulateUserSessionMiddleware
from zentrapay.api.v1.routers.news import news_router
import uvicorn

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


def run():
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    run()
