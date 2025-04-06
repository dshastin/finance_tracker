from typing import List

from litestar import Router

from api.v1.routes import v1_router


def register_routes() -> List[Router]:
    """Register all API routes."""
    return [
        v1_router,
    ] 