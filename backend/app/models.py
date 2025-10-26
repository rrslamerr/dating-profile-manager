from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from backend.app.database import BaseModel


class Profile(BaseModel):
    __tablename__ = "profiles"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int] = mapped_column()
    description: Mapped[str] = mapped_column(String(1000), nullable=True)
    interests: Mapped[str] = mapped_column(String(300), nullable=True)
