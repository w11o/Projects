from dao.base import BaseDAO
from users.user_models import User, Specializes
from database import async_session_maker
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

class UserDAO(BaseDAO):
    model = User

    @classmethod
    async def find_full_data(cls, user_id: int):
        async with async_session_maker() as session:
            # Первый запрос для получения информации о студенте
            query_user = select(cls.model).options(joinedload(cls.model.spec)).filter_by(id=user_id)
            result_user = await session.execute(query_user)
            user_info = result_user.scalar_one_or_none()

            # Если студент не найден, возвращаем None
            if not user_info:
                return None

            user_data = user_info.to_dict()
            user_data['specialize'] = user_info.spec.speciality_name
            return user_data
        #создать foreign_key для spec и user

