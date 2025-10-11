from fastapi import APIRouter
from app.schemas.users import UserSignup
from app.crud.users import userCreate

router = APIRouter(tags=["users"], prefix="/users")


@router.get("/")
async def get_users():
    return {"message": "List of users"}


@router.post("/signup")
async def signup_user(user: UserSignup):
    new_user = await userCreate(user=user)
    return new_user
