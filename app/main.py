from fastapi import FastAPI
from app.routers import profiles
from app.database import setup_database
from .models import BaseModel

app = FastAPI(title="Dating Profile Manager")
app.include_router(profiles.router)


@app.on_event("startup")
async def on_startup():
    await setup_database(BaseModel)
