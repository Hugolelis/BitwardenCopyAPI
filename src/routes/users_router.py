from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Usuários"])

@router.get("/")
def route_get_users():
    pass
