from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "sqlite+aiosqlite:///database.db"

engine = create_async_engine(DATABASE_URL)
new_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_session():
    async with new_session() as session:
        yield session


async def setup_database(BaseModel):
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)


class BaseModel(DeclarativeBase):
    pass
