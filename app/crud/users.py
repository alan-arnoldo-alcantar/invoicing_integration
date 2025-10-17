from app.schemas.users import UserSignup, UserPublic
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import EmailStr
from app.models.users import User
from sqlalchemy import select
from app.core.security import hash_password

async def get_user_by_email(*, session: AsyncSession, email: EmailStr):
    result = await session.scalar(select(User).where(User.email == email))
    result = result.first()
    return result


async def create_user(*, session: AsyncSession, user: UserSignup) -> User:
    user.password = hash_password(user.password)
    user_validated = UserSignup.model_validate(user)
    db_obj = User(**user_validated.model_dump())
    session.add(db_obj)
    await session.commit()
    await session.refresh(db_obj)
    return db_obj
