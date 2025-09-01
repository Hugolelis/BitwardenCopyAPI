from fastapi import FastAPI

from db.conn import engine  
from sqlalchemy import text

from rich import print

# API instancia
app = FastAPI(
    title="BitwardenCopy API",
    description="API desenvolvida para praticar conceitos de FastAPI, simulando algumas " 
    "funcionalidades do Bitwarden. Permite o gerenciamento seguro de senhas."
)

# teste conn db
try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print(f"[bold green]✅ Connection successful:[/] [yellow]{result.scalar()}[/]")
except Exception as e:
    print(f"[bold red]❌ Connection failed:[/] {e}")


# routers
from src.routers import users_router
app.include_router(users_router.router)