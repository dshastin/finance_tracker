from pathlib import Path
from typing import Any

from litestar.plugins.sqlalchemy import SQLAlchemyAsyncConfig
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""
    
    # Database settings
    DATABASE_URL: str = "sqlite+aiosqlite:///./app.db"
    
    @property
    def db_config(self) -> SQLAlchemyAsyncConfig:
        """Get database configuration."""
        return SQLAlchemyAsyncConfig(
            connection_string=self.DATABASE_URL,
            create_all=True,
        )
    
    class Config:
        """Pydantic config."""
        env_file = ".env"
        case_sensitive = True


settings = Settings()
