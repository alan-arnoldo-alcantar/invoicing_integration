from fastapi import FastAPI
from fastapi.routing import APIRoute
from app.api.main import api_router
from app.core.config import settings
from sqlalchemy.exc import (
    IntegrityError,
    DataError,
    OperationalError,
    NoResultFound
)
from app.exceptions.handlers import (
    integrity_error_handler,
    operational_error_handler,
    data_error_handler,
    no_result_found_handler,
)


def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_VERSION}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
)

app.include_router(api_router, prefix=settings.API_VERSION)
app.add_exception_handler(IntegrityError,integrity_error_handler)
app.add_exception_handler(OperationalError, operational_error_handler)
app.add_exception_handler(DataError, data_error_handler)
app.add_exception_handler(NoResultFound, no_result_found_handler)
