from .base import _BaseSetting

class ProductionSettings(_BaseSetting):
    CURRENCY_CLOUD_BASE_URL: str
    CURRENCY_CLOUD_LOGIN_ID: str
    CURRENCY_CLOUD_API_KEY: str
    
    ### The news related information
    NEWS_BASE_URL: str
    NEWS_API_KEY: str


settings = ProductionSettings()

