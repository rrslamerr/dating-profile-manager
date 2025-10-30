# Импортируем типы Mapped и mapped_column — они используются для описания полей таблицы
from sqlalchemy.orm import Mapped, mapped_column

# Импортируем тип данных String для текстовых полей
from sqlalchemy import String

# Импортируем базовую модель, от которой наследуются все ORM-модели приложения
from app.database import BaseModel


# Класс Profile представляет таблицу "profiles" в базе данных
# Каждый экземпляр этого класса соответствует одной записи (строке) в таблице
class Profile(BaseModel):
    # Указываем имя таблицы в базе данных
    __tablename__ = "profiles"

    # Первичный ключ (уникальный идентификатор профиля)
    id: Mapped[int] = mapped_column(primary_key=True)

    # Имя пользователя (строка длиной до 50 символов)
    name: Mapped[str] = mapped_column(String(50))

    # Возраст пользователя (целое число)
    age: Mapped[int] = mapped_column()

    # Описание профиля (необязательное поле, до 1000 символов)
    description: Mapped[str] = mapped_column(String(1000), nullable=True)

    # Интересы пользователя (необязательное поле, до 300 символов)
    interests: Mapped[str] = mapped_column(String(300), nullable=True)
