from fastapi import APIRouter

router = APIRouter(prefix="/saves", tags=["Salvamentos"])

@router.get("/")
def route_get_saves():
    pass