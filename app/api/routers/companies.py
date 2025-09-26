from fastapi import APIRouter
from app.crud import companies as crud

router = APIRouter(prefix="/companies", tags=["companies"])

router.get("/")
def read_companies():
    """
    List of companies
    """
    pass