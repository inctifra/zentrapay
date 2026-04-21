from .base import _BaseSetting
import enum


class ENVEnum(str, enum.Enum):
    LOCAL = "local"
    DEVELOPMENT = "development"
    PRODUCTION = "production"


class ProductionSettings(_BaseSetting):
    CURRENCY_CLOUD_BASE_URL: str
    CURRENCY_CLOUD_LOGIN_ID: str
    CURRENCY_CLOUD_API_KEY: str

    ### The news related information
    NEWS_BASE_URL: str
    NEWS_API_KEY: str

    ENV: ENVEnum = ENVEnum.LOCAL


settings = ProductionSettings()
