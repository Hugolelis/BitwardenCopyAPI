from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context

from db.conn import Base
import os
from dotenv import load_dotenv

# Carrega .env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Models
from db.models import users_models

# Metadata para autogenerate
target_metadata = Base.metadata

# Configura logging
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    # Usa a URL do .env diretamente
    connectable = create_engine(
        DATABASE_URL,
        poolclass=pool.NullPool,
        echo=True
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
