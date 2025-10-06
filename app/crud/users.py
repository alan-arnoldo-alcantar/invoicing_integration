from app.schemas.users import UserSignup

async def userCreate(user: UserSignup) -> dict:
    # Guardar en la base de datos (simulado aquí)
    return {"id": 1, "operation":True}