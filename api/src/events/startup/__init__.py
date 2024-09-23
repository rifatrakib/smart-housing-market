from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.events.startup.routes import register_routes


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    await register_routes(app)
    yield
