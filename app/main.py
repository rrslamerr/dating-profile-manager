from fastapi import FastAPI
from app.routers import profiles

app = FastAPI()
app.include_router(profiles.router)
