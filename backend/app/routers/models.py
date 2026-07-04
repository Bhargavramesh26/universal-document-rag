from fastapi import APIRouter

from app.schemas.model import ModelListResponse
from app.services.model_service import ModelService

router = APIRouter()


@router.get(
    "/models",
    response_model=ModelListResponse
)
def get_models():

    models = ModelService.get_available_models()

    return ModelListResponse(models=models)