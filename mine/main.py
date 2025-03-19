from typing import Optional
import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get("/")
def home():
    return "Welcome to FastAPI world...!"


@api.get("/api/calculate")
def calculate():
    value = 3 * 4

    return {"value": value}


@api.get("/api/calculate2")
def calculate2(a: int, b: int, z: Optional[int] = None):

    if z == 0:
        return fastapi.Response(content="ERROR: query 'z' cannot be 0", status_code=400)

    value = a * b

    if z is not None:
        value /= z

    return {"a": a, "b": b, "z": z, "value": value}


uvicorn.run(api, host="127.0.0.1", port=9000)
