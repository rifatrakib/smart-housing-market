from fastapi import APIRouter

from src.schemas.responses import HealthResponse
from src.utils.enums import Tags


async def create_router() -> APIRouter:
    router = APIRouter(prefix="/health")

    @router.get(
        "",
        tags=[Tags.HEALTH],
        response_model=HealthResponse,
    )
    async def health():
        return {"status": "ok"}

    return router
