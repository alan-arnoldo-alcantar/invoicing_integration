from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
import logging
from jwt.exceptions import (
    InvalidTokenError,
    ExpiredSignatureError,
    DecodeError,
    InvalidSignatureError
)


logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

async def invalid_token_handler(request: Request, exc: InvalidTokenError):
    logger.error(f"Invalid token: {exc}")
    return JSONResponse(
        status_code=401,
        content={"detail": "Could not validate token"},
    )



async def expired_signature_handler(request: Request, exc: ExpiredSignatureError):
        logger.error(f"Expired token: {exc}")
        return JSONResponse(
            status_code=401,
            content={"detail": "Token has expired"},
        )


async def decode_token_handler(resuqest: Request, exc: DecodeError):
    logger.error(f"Decode error: {exc}")
    return JSONResponse(
        status_code=401,
        content={"detail": "Error decoding token"},
    )


async def invalid_signature_handler(request: Request, exc: InvalidSignatureError):
        logger.rror(f"Invalid signature: {exc}")
        return JSONResponse(
            status_code=401,
            content={"detail": "Invalid token signature"},
        )


def register_token_exception_handlers(app: FastAPI):
    app.add_exception_handler(InvalidTokenError, invalid_token_handler)
    app.add_exception_handler(ExpiredSignatureError, expired_signature_handler)
    app.add_exception_handler(DecodeError, decode_token_handler)
    app.add_exception_handler(InvalidSignatureError, invalid_signature_handler)
