from fastapi import FastAPI

from src.events.startup import app_lifespan


def configure_app() -> FastAPI:
    app: FastAPI = FastAPI(lifespan=app_lifespan)
    return app


app: FastAPI = configure_app()
