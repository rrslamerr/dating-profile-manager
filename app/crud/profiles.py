from sqlalchemy import select
from app.models import Profile
from app.schemas import ProfileCreate
from app.dependencies import SessionDep


async def create_profile(data: ProfileCreate, session: SessionDep):
    new_profile = Profile(
        name=data.name,
        age=data.age,
        description=data.description,
        interests=data.interests,
    )
    session.add(new_profile)
    await session.commit()
    await session.refresh(new_profile)
    return new_profile


async def get_profile(profile_id: int, session: SessionDep):
    query = select(Profile).where(Profile.id == profile_id)
    result = await session.execute(query)
    return result.scalar_one_or_none()


async def get_profiles(session: SessionDep):
    query = select(Profile)
    result = await session.execute(query)
    return result.scalars().all()


async def delete_profile(profile_id: int, session: SessionDep):
    query = select(Profile).where(Profile.id == profile_id)
    result = await session.execute(query)
    profile = result.scalar_one_or_none()
    if profile is None:
        return False
    await session.delete(profile)
    await session.commit()
    return True
