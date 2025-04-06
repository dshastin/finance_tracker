from litestar import Router, get


@get('/health')
async def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {'status': 'ok'}


health_router = Router(
    path='/health',
    route_handlers=[health_check],
)
