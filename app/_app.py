from typing import Optional

from pydantic import SecretStr
from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    """Basic app configuration"""

    telegram_bot_token: Optional[SecretStr] = None

    class Config:
        env_file = "a/.env"
        env_file_encoding = "utf-8"
        extra = "ignore"


class App:
    name = "Mini Botspot Template"

    def __init__(self, **kwargs):
        self.config = AppConfig(**kwargs)
