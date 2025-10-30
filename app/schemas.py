# Импортируем базовый класс Pydantic для описания схем данных
from pydantic import BaseModel, Field


class ProfileBase(BaseModel):
    """
    Базовая схема профиля пользователя.
    Используется для валидации входных данных и обмена информацией между клиентом и сервером.
    """

    name: str  # Имя пользователя
    age: int  # Возраст пользователя
    description: str | None = Field(default=None, max_length=1000)
    # Описание профиля (необязательное поле, макс. Длина 1000 символов)
    interests: str | None = Field(default=None, max_length=300)
    # Интересы пользователя (необязательное поле, макс. Длина 300 символов)


class ProfileCreate(ProfileBase):
    """
    Схема для создания нового профиля.
    Наследуется от ProfileBase, не добавляет новых полей.
    """

    pass


class Profile(ProfileBase):
    """
    Схема для отображения профиля с идентификатором.
    Используется при ответах API (например, GET-запросы).
    """

    id: int  # Уникальный идентификатор профиля в базе данных

    class Config:
        # Разрешает создавать Pydantic-модель из ORM-объекта SQLAlchemy
        from_attributes = True
