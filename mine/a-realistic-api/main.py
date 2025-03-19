"""
Modern weather api using FastAPI and python
"""

import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get("/")
def index():
    """
    Index function just returns the welcome message
    """
    return {"message": "Welcome to awesome weather API...!"}


if __name__ == "__main__":
    uvicorn.run(api, port=8000, host="127.0.0.1")
