from fastapi import APIRouter, HTTPException
from app.schemas import ProfileCreate
from app.dependencies import SessionDep
from app import crud

router = APIRouter(prefix="/profiles", tags=["Profiles"])


@router.post("/")
async def create_profile(data: ProfileCreate, session: SessionDep):
    return await crud.create_profile(data, session)


@router.get("/")
async def get_profiles(session: SessionDep):
    return await crud.get_profiles(session)


@router.delete("/{profile_id}")
async def delete_profile(profile_id: int, session: SessionDep):
    deleted = await crud.delete_profile(profile_id, session)
    if not deleted:
        raise HTTPException(status_code=404, detail="Profile not found")
    return {"message": "Profile deleted successfully"}
