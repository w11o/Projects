from fastapi import APIRouter, Depends
from users.dao import UserDAO
from users.rb import RBUser
from users.schemas import User
from typing import List
router = APIRouter(prefix='/Users', tags=['Работа с пользователями'])

@router.get("/", summary='Получить всех пользователей', response_model=List[User])
async def get_all_users(request_body: RBUser = Depends()) -> list[User]:
    return await UserDAO.find_all(**request_body.to_dict())


@router.get("/{id}", summary='Получить одного пользователя по id')
async def get_user_by_id(user_id: int) -> User | dict:
    res = await UserDAO.find_full_data(user_id)
    if res is None:
        return {'message': f'Пользователь с ID {user_id} не найден.'}
    return res


@router.get("/by_filter", summary="Получить одного пользователя по фильтру")
async def get_student_by_filter(request_body: RBUser = Depends()) -> User | dict:
    res = await UserDAO.find_one_or_none(**request_body.to_dict())
    if res is None:
        return {'message': f'Пользователь с указанными вами параметрами: {request_body.to_dict()} не найден!'}
    return res
