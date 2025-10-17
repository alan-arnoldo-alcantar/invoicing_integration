from fastapi import APIRouter
from app.schemas.users import UserSignup, UserPublic
from app.crud.users import create_user
from app.core.deps import SessionDep

router = APIRouter(tags=["users"], prefix="/users")


@router.get("/")
async def get_users():
    return {"message": "List of users"}


@router.post("/signup", response_model=UserPublic)
async def signup_user(session: SessionDep, user_signup: UserSignup):
    new_user = await create_user(session=session, user=user_signup)
    return new_user
