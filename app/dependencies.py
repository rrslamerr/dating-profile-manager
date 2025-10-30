# Импортируем класс AsyncSession — асинхронная версия сессии SQLAlchemy
# Она используется для выполнения запросов к базе данных в асинхронном режиме
from sqlalchemy.ext.asyncio import AsyncSession

# Импортируем Depends — механизм FastAPI для внедрения зависимостей
from fastapi import Depends

# Annotated используется для объединения типов и зависимостей в одной аннотации
from typing import Annotated

# Импортируем функцию get_session, которая создаёт и возвращает сессию БД
from app.database import get_session


# Определяем тип зависимости SessionDep
# При вызове функции FastAPI автоматически передаёт активную сессию БД.
SessionDep = Annotated[AsyncSession, Depends(get_session)]
