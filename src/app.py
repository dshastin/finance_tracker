from litestar import Litestar, get


@get('/')
async def hello_world() -> str:
    """Hello world handle."""
    return 'Hello, world!'


app = Litestar([hello_world])
