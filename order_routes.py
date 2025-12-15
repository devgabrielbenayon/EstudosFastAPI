from fastapi import APIRouter

order_router = APIRouter(prefix="/order", tags=["order"])

@order_router.get("/")
async def order():
    """
    Essa é a rota padrão de pedidos do sistema.
    """
    return {"mensagem": "Você acessou a rota de pedidos"}