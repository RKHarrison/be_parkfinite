from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import SQLAlchemyError
from os import getenv

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    body = exc.body
    if getenv("ENV") == "development":
        print("Validation errors:", errors)
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": errors, "body": body}),
    )

async def attribute_error_handler(request: Request, exc: AttributeError):
    if getenv("ENV") == "development":
        print( f"An attribute error occurred: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"detail": "A server error occured"}
    )

async def http_exception_handler(request: Request, exc: HTTPException):
    if getenv("ENV") == "development":
        print(f"HTTP exception occurred: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
    if getenv("ENV") == "development":
        print(f"Database error occurred: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"detail": "A database error occurred"},
    )

