from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from typing import Annotated
from app.database import get_session

# Автоматически передаёт сеанс работы с базой данных в нужные функции
SessionDep = Annotated[AsyncSession, Depends(get_session)]
