from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from app.schemas import ProfileCreate
from app.models import Profile
from app.database import get_session

router = APIRouter(prefix="/profiles", tags=["Profiles"])

SessionDep = Annotated[AsyncSession, Depends(get_session)]


@router.post("/")
async def create_profile(data: ProfileCreate, session: SessionDep):
    new_profile = Profile(
        name=data.name,
        age=data.age,
        description=data.description,
        interests=data.interests,
    )
    session.add(new_profile)
    await session.commit()


@router.get("/")
async def get_profiles(session: SessionDep):
    query = select(Profile)
    result = await session.execute(query)
    return result.scalars().all()
