from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from app.database import BaseModel


class Profile(BaseModel):
    # Эта таблица хранит данные профиля пользователя
    __tablename__ = "profiles"  # Имя таблицы в базе данных
    # Уникальный идентификатор каждого профиля, автоматически увеличивается
    id: Mapped[int] = mapped_column(primary_key=True)
    # Имя пользователя, максимум 50 символов
    name: Mapped[str] = mapped_column(String(50))
    # Возраст пользователя
    age: Mapped[int] = mapped_column()
    # Краткое описание пользователя, можно не заполнять
    description: Mapped[str] = mapped_column(String(1000), nullable=True)
    # Интересы пользователя, можно не заполнять
    interests: Mapped[str] = mapped_column(String(300), nullable=True)
