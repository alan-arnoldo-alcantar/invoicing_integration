from fastapi import FastAPI
from .db import register_db_exception_handlers
from .token import register_token_exception_handlers

def register_all_exception_handlers(app: FastAPI):
    register_db_exception_handlers(app)
    register_token_exception_handlers(app)