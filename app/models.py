from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, String, Integer, Text


class BaseModel(DeclarativeBase):
    pass


class Profile(BaseModel):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    description = Column(Text)
    interests = Column(String(255))
