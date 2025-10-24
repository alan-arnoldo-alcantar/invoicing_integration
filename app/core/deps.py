from collections.abc import AsyncGenerator
from app.core.db import AsyncSessionMakerLocal
from app.core.config import settings
from app.models import User
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException, Header, status
from fastapi.security import OAuth2PasswordBearer, HTTPBearer
from typing import Annotated
import logging
import jwt


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"                    
)
logger = logging.getLogger(__name__)


reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_VERSION}/login/access-token"
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionMakerLocal() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_db)]
TokenDep = Annotated[str, Depends(reusable_oauth2)]


async def get_current_active_user(session: SessionDep, token: TokenDep) -> User:
    payload = jwt.decode(
        jwt=token,
        key=settings.TOKEN_SECRET_KEY,
        algorithms=[settings.TOKEN_ALGORITHM]
    )
    user: User = await session.get(User, int(payload.get("sub")))
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return user


CurrentUser = Annotated[User, Depends(get_current_active_user)]


async def get_current_superuser(current_user: CurrentUser) -> User:
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user