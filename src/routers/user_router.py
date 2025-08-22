from fastapi import APIRouter
from src.controllers.user_controller import UserController

router = APIRouter(prefix="/user", tags=["Usuários"])
controller = UserController()  # instancia da classe

@router.get("/")
def route_get_users():
    return controller.get_users()
