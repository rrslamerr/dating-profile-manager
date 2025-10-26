from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from typing import Annotated
from backend.app.database import get_session

SessionDep = Annotated[AsyncSession, Depends(get_session)]
