from fastapi import APIRouter
from app.api.routers import root

api_router = APIRouter()

api_router.include_router(root.router)
