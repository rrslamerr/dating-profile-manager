# FastAPI приложение (профили пользователей)

## Описание проекта
Проект представляет собой REST API для управления профилями пользователей.  
Реализованы функции создания, получения, обновления и удаления профилей.  
API построено с использованием **FastAPI**, **SQLAlchemy (Async)** и **SQLite**.  

---

## Основные возможности
- Добавление нового профиля  
- Получение списка всех профилей  
- Получение профиля по ID  
- Обновление данных профиля  
- Удаление профиля  

---

## Технологии
- **Python 3.11+**
- **FastAPI**
- **SQLAlchemy (async)**
- **Pydantic**
- **SQLite (через aiosqlite)**
- **Uvicorn** — сервер для запуска приложения

---

## Структура проекта
```
dating_profile_manager/
├── app/
│ ├── init.py
│ ├── main.py # Точка входа в приложение
│ ├── database.py # Настройка подключения к базе данных
│ ├── dependencies.py # Зависимости и сессия БД
│ ├── models.py # SQLAlchemy модели
│ ├── schemas.py # Pydantic-схемы (валидация)
│ │
│ ├── crud/ # Логика CRUD-операций
│ │ ├── init.py
│ │ └── profiles.py
│ │
│ └── routers/ # Роутеры FastAPI
│ ├── init.py
│ └── profiles.py
│
├── database.db # Файл базы данных SQLite
├── requirements.txt # Список зависимостей проекта
└── README.md # Документация проекта
```

---

## Установка и запуск

### Клонировать репозиторий
```
git clone https://github.com/rrslamerr/dating-profile-manager
cd dating-profile-manager
```
### Создать виртуальное окружение
```
python -m venv venv
venv\Scripts\activate        # Для Windows
```
### Установить зависимости
```
pip install -r requirements.txt
```
### Запустить приложение
```
uvicorn app.main:app --reload
```
### Перейти по адресу
```
http://127.0.0.1:8000/docs
```
Там доступна Swagger-документация API.

---

## Пример работы API

```
{
  "name": "Иван",
  "age": 22,
  "description": "Студент ИБ",
  "interests": "Кибербезопасность"
}
```
Ответ:
```
{
  "id": 1,
  "name": "Иван",
  "age": 22,
  "description": "Студент ИБ",
  "interests": "Кибербезопасность"
}
```