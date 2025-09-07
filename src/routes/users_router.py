from fastapi import APIRouter
from sqlalchemy.orm import Session as SessionType
from fastapi import Depends
from db.schemas.users_schemas import UserCreate, UserResponse
from src.helpers.getDB import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register", response_model=UserResponse)
def route_get_users(user: UserCreate, db: SessionType = Depends(get_db)):
    pass
