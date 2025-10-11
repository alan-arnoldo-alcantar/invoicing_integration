from collections.abc import AsyncGenerator
from app.core.db import AsyncSessionMekerLocal
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from typing import Annotated


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionMekerLocal() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_db)]
