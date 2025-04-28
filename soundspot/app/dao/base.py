from sqlalchemy.future import select
from database import async_session_maker


class BaseDAO:
    model = None
    
    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()
    

    @classmethod                                                #возвращать такая функция будет или None, 
    async def find_one_or_none_by_id(cls, data_id: int):        #что будет говорить про отсутствие записи
        async with async_session_maker() as session:            #с указанным id или саму запись.
            query = select(cls.model).filter_by(id=data_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()
    
    
    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()
    