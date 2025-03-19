"""
Modern weather api using FastAPI and python
"""

import fastapi
from starlette.staticfiles import StaticFiles
import uvicorn

from api import weather_api
from views import home

api = fastapi.FastAPI()


def configure():
    """
    App level configurations for different features
    """
    configure_router()


def configure_router():
    """
    Configure routers
    """
    api.mount("/static", StaticFiles(directory="static"), name="static")
    api.include_router(home.router)
    api.include_router(weather_api.router)


if __name__ == "__main__":
    configure()
    uvicorn.run(api, port=8000, host="127.0.0.1")
else:
    configure()
