from pydantic import BaseModel, Field  # Библиотека для проверки данных


class ProfileBase(BaseModel):
    # Базовая схема профиля, описывает общие поля профиля
    name: str  # Имя пользователя
    # Возраст пользователя, должен быть от 18 до 100 лет
    age: int = Field(..., ge=18, le=100)
    # Краткое описание пользователя, необязательное, максимум 1000 символов
    description: str | None = Field(default=None, max_length=1000)
    # Интересы пользователя, необязательное поле, максимум 300 символов
    interests: str | None = Field(default=None, max_length=300)


class ProfileCreate(ProfileBase):
    # Схема для создания нового профиля
    pass


class Profile(ProfileBase):
    # Схема для получения профиля из базы данных
    id: int  # Уникальный идентификатор профиля

    class Config:
        # Позволяет автоматически заполнять поля схемы данными из объекта базы данных
        from_attributes = True
