from collections.abc import AsyncGenerator
from app.core.db import AsyncSessionMakerLocal
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from typing import Annotated


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionMakerLocal() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_db)]
