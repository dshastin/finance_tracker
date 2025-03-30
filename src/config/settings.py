from pathlib import Path

from litestar.plugins.sqlalchemy import SQLAlchemyAsyncConfig
from pydantic_settings import BaseSettings

from db.base import Base

BASE_DIR = Path(__file__).parent.parent

class Settings(BaseSettings):
    """APP Settings."""

    @property
    def db_config(self) -> SQLAlchemyAsyncConfig:
        """DB Connection parameters."""
        return SQLAlchemyAsyncConfig(
            connection_string='sqlite+aiosqlite:///db.sqlite',
            create_all=True,
            metadata=Base.metadata,
)


settings = Settings()
