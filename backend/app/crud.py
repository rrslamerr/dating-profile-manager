from sqlalchemy import select
from backend.app.models import Profile
from backend.app.schemas import ProfileCreate
from backend.app.dependencies import SessionDep


async def create_profile(data: ProfileCreate, session: SessionDep):
    new_profile = Profile(
        name=data.name,
        age=data.age,
        description=data.description,
        interests=data.interests,
    )
    session.add(new_profile)
    await session.commit()


async def get_profiles(session: SessionDep):
    query = select(Profile)
    result = await session.execute(query)
    return result.scalars().all()
