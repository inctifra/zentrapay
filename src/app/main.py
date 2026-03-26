from fastapi import FastAPI
from config.settings.production import settings


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
        docs_url="/",
        version=settings.VERSION,
        prefix="api",
        servers=[
            {"url": "http://localhost:8000", "description": "Development"},
            {"url": "https://api.zentrapay.com", "description": "Production"},
        ],
    )
