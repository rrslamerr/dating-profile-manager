from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String


class BaseModel(DeclarativeBase):
    pass


class Profile(BaseModel):
    __tablename__ = "profiles"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int] = mapped_column()
    description: Mapped[str] = mapped_column()
    interests: Mapped[str] = mapped_column(String(255))
