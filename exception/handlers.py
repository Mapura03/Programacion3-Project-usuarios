from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from .custom_exceptions import (
    PersonNotFoundException,
    EmptyTreeException,
    LocationNotFoundException,
    TypeDocNotFoundException,
    InvalidCSVFormatException
)


def register_exception_handlers(app: FastAPI):
    @app.exception_handler(PersonNotFoundException)
    async def person_not_found_exception_handler(request: Request, exc: PersonNotFoundException):
        return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

    @app.exception_handler(EmptyTreeException)
    async def empty_tree_exception_handler(request: Request, exc: EmptyTreeException):
        return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

    @app.exception_handler(LocationNotFoundException)
    async def location_not_found_exception_handler(request: Request, exc: LocationNotFoundException):
        return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

    @app.exception_handler(TypeDocNotFoundException)
    async def typedoc_not_found_exception_handler(request: Request, exc: TypeDocNotFoundException):
        return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

    @app.exception_handler(InvalidCSVFormatException)
    async def invalid_csv_format_exception_handler(request: Request, exc: InvalidCSVFormatException):
        return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})