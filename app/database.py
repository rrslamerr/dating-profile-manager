# Импортируем инструменты для работы с асинхронной базой данных
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

# Импортируем базовый класс для объявления моделей ORM
from sqlalchemy.orm import DeclarativeBase


# Адрес подключения к базе данных (используется SQLite с асинхронным драйвером aiosqlite)
DATABASE_URL = "sqlite+aiosqlite:///database.db"


# Создаём асинхронный движок (engine), который управляет соединением с базой данных
engine = create_async_engine(DATABASE_URL)

# Создаём фабрику сессий — объект, через который будем работать с БД
new_session = async_sessionmaker(engine, expire_on_commit=False)


# Асинхронная зависимость для получения сессии БД
# Используется в Depends() внутри маршрутов FastAPI
async def get_session():
    # Создаём новую сессию и автоматически закрываем её после использования
    async with new_session() as session:
        yield session


# Функция для первоначального создания таблиц в базе данных
# Вызывается при старте приложения, чтобы убедиться, что все таблицы созданы
async def setup_database(BaseModel):
    # engine.begin() открывает асинхронное подключение
    async with engine.begin() as conn:
        # run_sync позволяет вызвать синхронную команду (create_all) в асинхронном контексте
        await conn.run_sync(BaseModel.metadata.create_all)


# Базовый класс для всех моделей приложения
# От него будут наследоваться все модели (например, Profile)
class BaseModel(DeclarativeBase):
    pass
