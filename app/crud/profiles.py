from sqlalchemy import select
from app.models import Profile
from app.schemas import ProfileCreate
from app.dependencies import SessionDep


# Функция для создания нового профиля
async def create_profile(data: ProfileCreate, session: SessionDep):
    # Создаём новый объект профиля на основе введённых данных
    new_profile = Profile(
        name=data.name,
        age=data.age,
        description=data.description,
        interests=data.interests,
    )

    # Добавляем профиль в хранилище данных
    session.add(new_profile)

    # Подтверждаем сохранение
    await session.commit()

    # Обновляем данные, чтобы получить актуальную информацию
    await session.refresh(new_profile)

    # Возвращаем созданный профиль
    return new_profile


# Функция для получения списка всех профилей
async def get_profiles(session: SessionDep):
    # Готовим запрос, который запрашивает все профили
    query = select(Profile)

    # Выполняем запрос
    result = await session.execute(query)

    # Возвращаем список всех найденных профилей
    return result.scalars().all()


# Функция для получения одного профиля по его номеру
async def get_profile(profile_id: int, session: SessionDep):
    # Ищем профиль с нужным номером
    query = select(Profile).where(Profile.id == profile_id)

    # Выполняем запрос
    result = await session.execute(query)

    # Возвращаем найденный профиль или ничего, если его нет
    return result.scalar_one_or_none()


# Функция для изменения существующего профиля
async def update_profile(profile_id: int, data: ProfileCreate, session: SessionDep):
    # Сначала ищем профиль, который нужно изменить
    query = select(Profile).where(Profile.id == profile_id)
    result = await session.execute(query)
    profile = result.scalar_one_or_none()

    # Если такого профиля нет — сообщаем об этом
    if profile is None:
        return False

    # Обновляем данные профиля новыми значениями
    profile.name = data.name
    profile.age = data.age
    profile.description = data.description
    profile.interests = data.interests

    # Сохраняем изменения
    await session.commit()

    # Обновляем информацию профиля
    await session.refresh(profile)

    # Возвращаем обновлённый профиль
    return profile


# Функция для удаления профиля
async def delete_profile(profile_id: int, session: SessionDep):
    # Ищем профиль, который нужно удалить
    query = select(Profile).where(Profile.id == profile_id)
    result = await session.execute(query)
    profile = result.scalar_one_or_none()

    # Если профиль не найден — прекращаем выполнение
    if profile is None:
        return False

    # Удаляем профиль из базы
    await session.delete(profile)

    # Подтверждаем удаление
    await session.commit()

    # Сообщаем, что удаление прошло успешно
    return True
