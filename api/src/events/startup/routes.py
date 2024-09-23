import importlib
from pathlib import Path

from fastapi import FastAPI

from src import routes


async def register_routes(app: FastAPI):
    app.include_router(await routes.create_router())

    modules = Path(routes.__path__[0]).iterdir()
    for module in modules:
        if module.is_file() or module.name == "__pycache__":
            continue

        router = importlib.import_module(f"{routes.__name__}.{module.name}")
        app.include_router(await router.create_router())
