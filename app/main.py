from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routers import profiles
from app.database import setup_database
from app.models import BaseModel


@asynccontextmanager
async def lifespan(app: FastAPI):
    await setup_database(BaseModel)
    yield


app = FastAPI(
    title="Dating Profile Manager",
    description="REST API для управления профилями пользователей",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(profiles.router)
