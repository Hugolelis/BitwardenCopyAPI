from fastapi import FastAPI

# API instancia
app = FastAPI(
    title="BitwardenCopy API",
    description="API desenvolvida para praticar conceitos de FastAPI, simulando algumas " 
    "funcionalidades do Bitwarden. Permite o gerenciamento seguro de senhas."
)

# routers
from src.routers import user_router
app.include_router(user_router.router)