# Импортируем класс APIRouter для создания группы маршрутов (эндпоинтов)
from fastapi import APIRouter

# Импортируем схему ProfileCreate для проверки и описания входных данных при создании профиля
from app.schemas import ProfileCreate

# Импортируем зависимость для получения асинхронной сессии базы данных
from app.dependencies import SessionDep

# Импортируем модуль crud, в котором описана логика работы с базой данных
from app import crud


# Создаём экземпляр роутера для работы с профилями пользователей
# prefix — общий путь для всех маршрутов этого роутера (/profiles)
# tags — используется для группировки маршрутов в документации Swagger
router = APIRouter(prefix="/profiles", tags=["Profiles"])


@router.post("/")
async def create_profile(data: ProfileCreate, session: SessionDep):
    """Создаёт новый профиль пользователя"""
    # Передаём данные в функцию crud.create_profile, которая сохраняет профиль в базе
    return await crud.create_profile(data, session)


@router.get("/")
async def get_profiles(session: SessionDep):
    """Возвращает список всех профилей пользователей"""
    # Вызываем crud.get_profiles, чтобы получить все записи из базы данных
    return await crud.get_profiles(session)
