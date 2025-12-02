from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import profiles, pages
from app.database import setup_database
from app.models import BaseModel


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Здесь мы создаём все таблицы в базе данных, если их ещё нет
    await setup_database(BaseModel)
    yield


# Создаём экземпляр веб-приложения
app = FastAPI(
    title="Dating Profile Manager",
    description="REST API для управления профилями пользователей",
    version="1.0.0",
    lifespan=lifespan,  # Указываем функцию, которая будет выполняться при запуске и завершении работы
)

# Подключаем папку со статическими файлами, чтобы можно было показывать картинки, стили и скрипты
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Подключаем маршруты для страниц и профилей
app.include_router(pages.router)
app.include_router(profiles.router)
