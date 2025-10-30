from sqlalchemy import select  # Импортируем функцию select для составления SQL-запросов

# Импортируем модель Profile — она описывает структуру таблицы в базе данных
from app.models import Profile

# Импортируем Pydantic-схему ProfileCreate — она используется для валидации данных при создании профиля
from app.schemas import ProfileCreate

# Импортируем зависимость для работы с асинхронной сессией базы данных
from app.dependencies import SessionDep


# Функция для создания нового профиля пользователя
# data — это объект с данными профиля (имя, возраст, описание, интересы)
# session — это активная асинхронная сессия базы данных (через Depends)
async def create_profile(data: ProfileCreate, session: SessionDep):
    # Создаём экземпляр модели Profile, заполняя его полями из схемы ProfileCreate
    new_profile = Profile(
        name=data.name,  # Имя пользователя
        age=data.age,  # Возраст
        description=data.description,  # Описание профиля
        interests=data.interests,  # Интересы пользователя
    )

    # Добавляем новый объект (профиль) в сессию, но пока не сохраняем его в базу
    session.add(new_profile)

    await session.commit()  # Добавляем новый объект (профиль) в сессию, но пока не сохраняем его в базу


# Функция для получения списка всех профилей из базы данных
async def get_profiles(session: SessionDep):
    # Формируем SQL-запрос на выборку всех записей из таблицы Profile
    query = select(Profile)
    result = await session.execute(query)  # Выполняем запрос через асинхронную сессию

    # Метод scalars() достаёт сами объекты Profile (без метаданных),
    # а all() возвращает их в виде списка
    return result.scalars().all()
