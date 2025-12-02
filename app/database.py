from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "sqlite+aiosqlite:///database.db"

# Создаём соединение с базой данных
engine = create_async_engine(DATABASE_URL)
# Настраиваем инструмент, который будет создавать новые сеансы работы с базой
new_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_session():
    # Открываем новый сеанс работы с данными
    async with new_session() as session:
        # Передаём его тем частям программы, которым нужно работать с базой
        yield session


async def setup_database(BaseModel):
    # Открываем соединение для подготовки базы данных
    async with engine.begin() as conn:
        # Создаём все таблицы, которые описаны в моделях
        await conn.run_sync(BaseModel.metadata.create_all)


class BaseModel(DeclarativeBase):
    # Общий родительский класс для всех моделей базы данных
    pass
