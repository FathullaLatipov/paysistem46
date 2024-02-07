from fastapi import APIRouter
from database.userservice import registration_user_db, edit_user_db, delete_user_db, get_exact_user_db, \
    get_all_users_db, check_user_email_db

from datetime import datetime

from users import UserRegistrationValidator, EditUserValidator

user_router = APIRouter(prefix='/user', tags=['Работа с пользователями БРАТ'])


# Регистрация
@user_router.post('/register')
async def register_new_user(data: UserRegistrationValidator):
    new_user_data = data.model_dump()

    checker = check_user_email_db(data.email)

    if checker:
        return {"message": 'Пользователь с таким эмейлом уже есть в БД'}
    else:
        result = registration_user_db(reg_date=datetime.now(), **new_user_data)

        return result


# Получения информации о пользователе
@user_router.get('/info')
async def get_user(user_id: int):
    result = get_exact_user_db(3)

    if result:
        return {'message': result}
    else:
        return {'message': 'Такого пользователя нету(('}


# Изменить данные пользователя
@user_router.put('/edit')
async def edit_user(data: EditUserValidator):
    change_data = data.model_dump()

    result = edit_user_db(**change_data)

    return result

# Получить всех пользователей -> def get_all_users
# Удалить пользователей -> def delete_user
# 18:45 - 18:55 спрошу

