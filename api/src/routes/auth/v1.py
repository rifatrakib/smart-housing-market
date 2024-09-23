from fastapi import APIRouter


async def create_router() -> APIRouter:
    router = APIRouter(prefix="/v1")

    @router.get("/check")
    async def check():
        return {"status": "ok"}

    return router
