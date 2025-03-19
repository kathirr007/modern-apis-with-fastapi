"""
Api endpoints related to the weather report
"""

import fastapi


router = fastapi.APIRouter()


@router.get("/api/weather/{city}")
def weather():
    """Returns the weather data"""
    return "Some report"
