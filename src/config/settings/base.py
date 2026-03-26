from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent


class _BaseSetting(BaseSettings):
    model_config = SettingsConfigDict(env_file=str(BASE_DIR.parent / ".env"))
    DEBUG: bool = True
    VERSION: str = "v1"

