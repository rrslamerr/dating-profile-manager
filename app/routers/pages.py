from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, HTMLResponse
from app.dependencies import SessionDep
from app import crud


# Создаём объект, который отвечает за адреса нашего сайта
router = APIRouter(tags=["Profiles"])
# Подключаем папку, где лежат HTML-шаблоны для отображения страниц
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def home(request: Request, session: SessionDep):
    """Главная страница"""
    profiles = await crud.get_profiles(session)
    # Открываем страницу и передаём туда список профилей, чтобы показать их на экране
    return templates.TemplateResponse(
        request=request, context={"profiles": profiles}, name="index.html"
    )


@router.get("/edit/{profile_id}", response_class=HTMLResponse)
async def edit_page(request: Request, profile_id: int, session: SessionDep):
    """Страница редактирования профиля"""
    profile = await crud.get_profile(profile_id, session)
    # Если такого профиля нет — возвращаемся на главную страницу
    if not profile:
        return RedirectResponse(url="/", status_code=303)
    # Показываем страницу редактирования и передаём данные выбранного профиля
    return templates.TemplateResponse(
        "edit.html", {"request": request, "profile": profile}
    )


@router.get("/create", response_class=HTMLResponse)
async def create_page(request: Request):
    """Страница создания профиля"""
    return templates.TemplateResponse("create.html", {"request": request})


@router.post("/create")
async def create_profile_form(
    request: Request,
    session: SessionDep,
    name: str = Form(...),
    age: int = Form(...),
    description: str = Form(None),
    interests: str = Form(None),
):
    """Обработка формы создания профиля"""
    from app.schemas import ProfileCreate
    # Формируем данные профиля на основе того, что ввёл пользователь
    profile_data = ProfileCreate(
        name=name, age=age, description=description, interests=interests
    )
    # Сохраняем профиль
    await crud.create_profile(profile_data, session)
    # После сохранения отправляем пользователя на главную
    return RedirectResponse(url="/", status_code=303)


@router.post("/edit/{profile_id}")
async def edit_profile_form(
    request: Request,
    profile_id: int,
    session: SessionDep,
    name: str = Form(...),
    age: int = Form(...),
    description: str = Form(None),
    interests: str = Form(None),
):
    """Обработка формы редактирования профиля"""
    from app.schemas import ProfileCreate
    # Снова формируем объект с обновлёнными данными профиля
    profile_data = ProfileCreate(
        name=name, age=age, description=description, interests=interests
    )
    # Сохраняем изменения
    await crud.update_profile(profile_id, profile_data, session)
    # Возвращаем пользователя на главную страницу
    return RedirectResponse(url="/", status_code=303)


@router.post("/delete/{profile_id}")
async def delete_profile_form(profile_id: int, session: SessionDep):
    """Удаление профиля"""
    await crud.delete_profile(profile_id, session)
    return RedirectResponse(url="/", status_code=303)
