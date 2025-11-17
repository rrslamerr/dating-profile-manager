from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.dependencies import SessionDep
from app import crud

router = APIRouter(tags=["Profiles"])
templates = Jinja2Templates(directory="app/templates")


@router.get("/")
async def home(request: Request, session: SessionDep):
    """Главная страница"""
    profiles = await crud.get_profiles(session)
    return templates.TemplateResponse(
        request=request, context={"profiles": profiles}, name="index.html"
    )
