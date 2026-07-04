from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routers import health
from app.routers import models
from app.routers import upload
from app.core.exception_handlers import register_exception_handlers
from app.routers import chat

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

register_exception_handlers(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.ALLOWED_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    health.router,
    prefix=settings.API_PREFIX,
    tags=["Health"],
)

app.include_router(
    models.router,
    prefix=settings.API_PREFIX,
    tags=["Models"],
)

app.include_router(
    upload.router,
    prefix=settings.API_PREFIX,
    tags=["Upload"],
)

app.include_router(
    chat.router,
    prefix=settings.API_PREFIX,
    tags=["Chat"],
)

@app.get("/")
def root():
    return {
        "message": f"{settings.APP_NAME} Backend Running 🚀"
    }