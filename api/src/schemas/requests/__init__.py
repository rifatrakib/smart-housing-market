from pydantic import ConfigDict

from api.src.schemas import BaseSchema


class BaseRequestSchema(BaseSchema):
    model_config = ConfigDict(
        extra="forbid",
    )
