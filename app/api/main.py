from fastapi import APIRouter
from app.api.routers import root
from app.api.routers import users
from app.api.routers import login

api_router = APIRouter()

api_router.include_router(root.router)
api_router.include_router(users.router)
api_router.include_router(login.router)
