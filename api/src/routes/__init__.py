from fastapi import APIRouter

from src.utils.enums import Tags


async def create_router() -> APIRouter:
    router = APIRouter(prefix="/health")

    @router.get(
        "",
        tags=[Tags.HEALTH],
    )
    async def health():
        return {"status": "ok"}

    return router
