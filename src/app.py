from litestar import Litestar, get
from litestar.plugins.sqlalchemy import SQLAlchemyInitPlugin

from config.settings import settings


@get('/')
async def hello_world() -> str:
    """Hello world handle."""
    return 'Hello, world!'


app = Litestar(
    route_handlers=[hello_world],
    plugins=[SQLAlchemyInitPlugin(settings.db_config)],
)
