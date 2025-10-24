from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
from pytz import UTC
from app.core.config import settings


pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

async def hash_password(password: str) -> str:
    return pwd_context.hash(password)


async def verify_passwrod(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


async def create_access_token(
        subject: str,
        expires_delta: timedelta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    ) -> str:
    expire = datetime.now(tz=UTC) + expires_delta
    to_encode = {"exp": expire, "sub": subject}
    encoded_jwt = jwt.encode(
        payload=to_encode,
        key= settings.TOKEN_SECRET_KEY, algorithm=settings.TOKEN_ALGORITHM
    )
    return encoded_jwt
