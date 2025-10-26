from fastapi import APIRouter
from backend.app.schemas import ProfileCreate
from backend.app.dependencies import SessionDep
from backend.app import crud

router = APIRouter(prefix="/profiles", tags=["Profiles"])


@router.post("/")
async def create_profile(data: ProfileCreate, session: SessionDep):
    return await crud.create_profile(data, session)


@router.get("/")
async def get_profiles(session: SessionDep):
    return await crud.get_profiles(session)
