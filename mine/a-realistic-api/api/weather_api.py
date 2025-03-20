"""
Api endpoints related to the weather report
"""

from typing import Optional
import fastapi
from fastapi import Depends
from pydantic import BaseModel
from services.openweather_service import get_report


router = fastapi.APIRouter()


class Location(BaseModel):
    city: str
    state: Optional[str]
    country: str = "IN"


@router.get("/api/weather/{city}")
async def weather(loc: Location = Depends(), units: Optional[str] = "metric"):
    """Returns the weather data"""
    data = await get_report(loc.city, loc.state, loc.country, units, True)
    return data
