from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions.custom_exceptions import (
    EmptyFileError,
    SessionNotFoundError,
    UnsupportedFileTypeError,
)


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(SessionNotFoundError)
    async def session_not_found_handler(
        request: Request,
        exc: SessionNotFoundError,
    ):
        return JSONResponse(
            status_code=404,
            content={
                "success": False,
                "message": str(exc),
            },
        )

    @app.exception_handler(UnsupportedFileTypeError)
    async def unsupported_file_handler(
        request: Request,
        exc: UnsupportedFileTypeError,
    ):
        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "message": str(exc),
            },
        )

    @app.exception_handler(EmptyFileError)
    async def empty_file_handler(
        request: Request,
        exc: EmptyFileError,
    ):
        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "message": str(exc),
            },
        )