from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(tags=["Profiles"])
templates = Jinja2Templates(directory="app/templates")


@router.get("/")
async def home(request: Request):
    """Главная страница"""
    return templates.TemplateResponse(request=request, name="home.html")
