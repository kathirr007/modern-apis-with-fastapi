"""
Modern weather api using FastAPI and python
"""

import json
from pathlib import Path
import fastapi
from starlette.staticfiles import StaticFiles
import uvicorn

from api import weather_api
from services import openweather_service
from views import home

app = fastapi.FastAPI()


def configure():
    """
    App level configurations for different features
    """
    configure_router()
    configure_apikeys()


def configure_apikeys():
    file = Path("settings.json").absolute()
    if not file.exists():
        print(
            f"WARNING: {file} not found, you cannot continue, please see the settings_template.json"
        )
        raise Exception(
            "settings.json not found, you cannot continue, please see the settings_template.json"
        )

    with open("settings.json") as fin:
        settings = json.load(fin)
        openweather_service.api_key = settings.get("api_key")


def configure_router():
    """
    Configure routers
    """
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.include_router(home.router)
    app.include_router(weather_api.router)


if __name__ == "__main__":
    configure()
    uvicorn.run(app, port=8000, host="127.0.0.1")
else:
    configure()
