from fastapi import FastAPI
from zentrapay.config.settings.production import settings


def get_servers():
    if settings.ENV == "local":
        return [{"url": "http://localhost:8080", "description": "Local"}]

    elif settings.ENV == "development":
        return [{"url": "https://zentrapay.ipvs.cloud", "description": "Development"}]

    elif settings.ENV == "production":
        return [{"url": "https://api.zentrapay.com", "description": "Production"}]

    return []


def init_app(_app: FastAPI) -> FastAPI:
    """Initialize the app for reusability

    Args:
        _app (FastAPI): This will be the wrapper

    Returns:
        FastAPI: typing and all the object utility retained
    """
    return _app(
        title="Zentrapay API layer",
        description="",
        docs_url="/" if settings.ENV != "production" else None,
        redoc_url=None if settings.ENV == "production" else "/redoc",
        version=settings.VERSION,
        prefix="api",
        servers=get_servers(),
        openapi_url=None if settings.ENV == "production" else "/openapi.json",
    )
