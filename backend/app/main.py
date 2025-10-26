from fastapi import FastAPI
from backend.app.routers import profiles
from backend.app.database import setup_database
from backend.app.models import BaseModel

app = FastAPI(title="Dating Profile Manager")
app.include_router(profiles.router)


@app.on_event("startup")
async def on_startup():
    await setup_database(BaseModel)
