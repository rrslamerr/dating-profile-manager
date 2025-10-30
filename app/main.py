# Импортируем FastAPI — основной класс для создания веб-приложения
from fastapi import FastAPI

# Импортируем роутер с маршрутами (эндпоинтами) для работы с профилями пользователей
from app.routers import profiles

# Импортируем функцию для инициализации базы данных
from app.database import setup_database

# Импортируем базовую модель, от которой наследуются все таблицы ORM
from app.models import BaseModel


# Создаём экземпляр приложения FastAPI
app = FastAPI(title="Dating Profile Manager")

# Подключаем маршруты из модуля profiles
# После этого все пути /profiles/... станут доступны в основном приложении
app.include_router(profiles.router)


# Обработчик события "startup" — выполняется один раз при запуске приложения
@app.on_event("startup")
async def on_startup():
    # При старте приложения создаются все таблицы, определённые в моделях (если их ещё нет)
    await setup_database(BaseModel)
