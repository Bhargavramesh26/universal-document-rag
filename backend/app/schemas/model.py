from pydantic import BaseModel


class ModelInfo(BaseModel):
    id: str
    name: str
    status: str


class ModelListResponse(BaseModel):
    models: list[ModelInfo]