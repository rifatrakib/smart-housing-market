from fastapi import APIRouter

from src.routes.auth import v1
from src.utils.enums import Tags


async def create_router() -> APIRouter:
    router = APIRouter(prefix="/auth", tags=[Tags.AUTH])

    router.include_router(await v1.create_router())

    return router
