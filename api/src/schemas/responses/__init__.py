from pydantic import ConfigDict

from src.schemas import BaseSchema


class BaseResponseSchema(BaseSchema):
    pass


class HealthResponse(BaseResponseSchema):
    status: str

    model_config = ConfigDict(
        json_schema_extra={"example": {"status": "ok"}},
    )
