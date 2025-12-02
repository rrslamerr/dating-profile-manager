from fastapi import APIRouter, HTTPException
from app.schemas import ProfileCreate
from app.dependencies import SessionDep
from app import crud

# Создаём группу адресов для работы с профилями.
# Всё, что относится к профилям, будет начинаться с /profiles
router = APIRouter(prefix="/profiles", tags=["Profiles"])


@router.post("/")
async def create_profile(data: ProfileCreate, session: SessionDep):
    """Создаёт новый профиль пользователя"""
    # Передаём данные на сохранение в отдельную часть программы
    return await crud.create_profile(data, session)


@router.get("/{profile_id}")
async def get_profile(profile_id: int, session: SessionDep):
    """Возвращает профиль по id"""
    # Пытаемся найти профиль по его номеру
    profile = await crud.get_profile(profile_id, session)
    # Если ничего не найдено — сообщаем об этом
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    # Возвращаем найденный профиль
    return profile


@router.get("/")
async def get_profiles(session: SessionDep):
    """Возвращает список всех профилей пользователей"""
    # Получаем полный список всех созданных профилей
    return await crud.get_profiles(session)


@router.put("/{profile_id}")
async def update_profile(profile_id: int, data: ProfileCreate, session: SessionDep):
    """Обновляет профиль по id"""
    # Пытаемся обновить данные выбранного профиля
    updated = await crud.update_profile(profile_id, data, session)
    # Если профиль не найден — выводим сообщение об ошибке
    if not updated:
        raise HTTPException(status_code=404, detail="Profile not found")
    # Возвращаем обновлённые данные профиля
    return updated


@router.delete("/{profile_id}")
async def delete_profile(profile_id: int, session: SessionDep):
    """Удаляет профиль по id"""
    # Пытаемся удалить профиль
    deleted = await crud.delete_profile(profile_id, session)
    # Если удалять нечего — профиль не существует
    if not deleted:
        raise HTTPException(status_code=404, detail="Profile not found")
    # Сообщаем, что удаление прошло успешно
    return {"message": "Profile deleted successfully"}
