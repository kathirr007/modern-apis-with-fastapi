"""
Api endpoints related to the static home view "/"
"""

import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates

templates = Jinja2Templates("templates")

router = fastapi.APIRouter()


@router.get("/")
def index(request: Request):
    """
    Returns the home page html content compiled from templates folder
    """
    # return {"message": "Welcome to awesome weather API...!"}
    return templates.TemplateResponse("home/index.html", {"request": request})


@router.get("/favicon.ico")
def favicon():
    """Redirects the favicon request to the static file path"""
    return fastapi.responses.RedirectResponse(url="/static/img/favicon.ico")
