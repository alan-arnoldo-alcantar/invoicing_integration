from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
import logging
from sqlalchemy.exc import (
    IntegrityError,
    DataError,
    OperationalError,
    NoResultFound
)

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def integrity_error_handler(request: Request, exc: IntegrityError):
    logger.error(f"IntegrityError: {exc.orig}")
    return JSONResponse(
        status_code=409,
        content={"detail": "Database integrity error occurred."},
    )


async def operational_error_handler(request:Request, exc:OperationalError):
    logger.error(f"OperationalError: {exc.orig}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Database operational error occurred."}
    )


async def data_error_handler(request: Request, exc:DataError):
    logger.error(f"DataError: {exc.orig}")
    return JSONResponse(
        status_code=400,
        content={"detail": "Invalid data provided."}
    )


async def no_result_found_handler(request: Request, exc: NoResultFound):
    logger.error("NoResultError")
    return JSONResponse(
        status_code=404,
        content={"detail": "Requested resource not found."}
    )


def register_db_exception_handlers(app: FastAPI):
    app.add_exception_handler(IntegrityError, integrity_error_handler)
    app.add_exception_handler(OperationalError, operational_error_handler)
    app.add_exception_handler(DataError, data_error_handler)
    app.add_exception_handler(NoResultFound, no_result_found_handler)
