from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy_utils import database_exists, create_database

from dotenv import load_dotenv
import os

from rich import print

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Criar engine
engine = create_engine(DATABASE_URL, echo=True)

# Criar o banco caso nao exista
try:
    if not database_exists(engine.url):
        create_database(engine.url)
        print("[bold green]✔ Database created successfully![/bold green]")
    else:
        print("[bold yellow]⚠ Database already exists.[/bold yellow]")
except Exception as e:
    print(f"[bold red]❌ Failed to create database![/bold red] [red]{e}[/red]")

# Base para os models
Base = declarative_base()

# Criar sessão
SessionLocal = sessionmaker(bind=engine)

# Criação das tabelas no banco
Base.metadata.create_all(bind=engine)

