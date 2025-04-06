from litestar import Router

from api.v1.health.router import health_router

v1_router = Router(
    path="/api/v1",
    route_handlers=[
        health_router,
    ],
) 