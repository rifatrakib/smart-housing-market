from functools import lru_cache
from importlib import import_module
from typing import Type

from decouple import config

from src.config.environments import BaseConfig


class SettingsFactory:
    def __init__(self, mode: str):
        self.mode = mode

    def __call__(self) -> Type[BaseConfig]:
        mode = self.mode.lower()
        module = import_module(BaseConfig.__module__)
        model = getattr(module, f"{mode.capitalize()}Config")
        return model()


@lru_cache()
def get_settings() -> BaseConfig:
    factory = SettingsFactory(mode=config("MODE", default="development"))
    return factory()


settings: BaseConfig = get_settings()
