import json
from math import fabs
from typing import Optional
from xmlrpc.client import Boolean
from fastapi import HTTPException
import httpx
import requests

api_key: Optional[str] = None

httpxAsyncClient = httpx.AsyncClient(verify=False)


async def get_report(
    city: str, state: Optional[str], country: str, units: Optional[str]
) -> dict:
    if state:
        q = f"{city}, {state}, {country}"
    else:
        q = f"{city}, {country}"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}&units={units}"
    # url = "https://jsonplaceholder.typicode.com/posts/1"

    print(url)

    try:
        async with httpx.AsyncClient(verify=False) as client:
            resp = await client.get(url)
            resp.raise_for_status()

        data = resp.json()
        return data

    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
    except httpx.RequestError as e:
        raise HTTPException(
            status_code=500, detail=f"Error connecting to JSONPlaceholder: {e}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {e}"
        )
