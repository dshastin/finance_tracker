from litestar import Litestar
from litestar.plugins.sqlalchemy import SQLAlchemyInitPlugin

from config.settings import settings
from api.routes import register_routes
from db.base import Base


def create_app() -> Litestar:
    """Create and configure the Litestar application."""
    app = Litestar(
        route_handlers=register_routes(),
        plugins=[
            SQLAlchemyInitPlugin(
                config=settings.db_config,
                metadata=Base.metadata,
            ),
        ],
    )
    return app


app = create_app()
