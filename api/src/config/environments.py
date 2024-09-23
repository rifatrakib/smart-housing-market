from pydantic import ConfigDict
from pydantic_settings import BaseSettings

from src.utils.enums import Modes


class BaseConfig(BaseSettings):
    APP_NAME: str
    MODE: Modes
    DEBUG: bool

    model_config = ConfigDict(env_file=".env", env_file_encoding="utf-8", extra="forbid")


class DevelopmentConfig(BaseConfig):
    MODE: Modes = Modes.DEVELOPMENT
    DEBUG: bool = True


class StagingConfig(BaseConfig):
    MODE: Modes = Modes.STAGING
    DEBUG: bool = False


class ProductionConfig(BaseConfig):
    MODE: Modes = Modes.PRODUCTION
    DEBUG: bool = False
