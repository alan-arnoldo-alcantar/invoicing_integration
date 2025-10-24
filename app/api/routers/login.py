from fastapi import APIRouter, HTTPException
from app.core.deps import SessionDep
from app.schemas.login import LoginIn, Token
from app.crud.users import get_user_by_email
from app.core.security import create_access_token, verify_passwrod

router = APIRouter(prefix="/login", tags=["login"])

@router.post("/access-token", response_model=Token)
async def login_accesss_token(*, session: SessionDep, data: LoginIn):
    user = await get_user_by_email(session=session, email=data.username)
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    elif not await verify_passwrod(plain_password=data.password, hashed_password=user.password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    return Token(
        access_token= await create_access_token(subject=str(user.id))
    )