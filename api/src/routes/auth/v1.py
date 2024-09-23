from fastapi import APIRouter

from src.schemas.responses import HealthResponse


async def create_router() -> APIRouter:
    router = APIRouter(prefix="/v1")

    @router.get(
        "/check",
        response_model=HealthResponse,
    )
    async def check():
        return {"status": "ok"}

    return router
