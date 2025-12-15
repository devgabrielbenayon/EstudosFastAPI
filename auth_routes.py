from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def auth():
    """
    Essa é a rota padrão de autorização do sistema.
    """
    return {"mensagem": "Você acessou a rota de autorização!"}