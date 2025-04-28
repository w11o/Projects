from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from pydantic import ConfigDict

class User(BaseModel):
    model_config = ConfigDict(from_attributes=True) #Указывается она в начале описания модели и я советую вам ее всегда указывать, когда речь идет про взаимодействие с базой данных через алхимию. Тем самым Pydantic понимает явно, что работать он будет с аргументами базы данных.
    username: str = Field(..., description='Имя пользователя (Логин)')
    email: EmailStr = Field(..., description='Электронная почта пользователя')
    updated_at: datetime = Field(..., description='Послденее обновление')
    created_at: datetime = Field(..., description='Дата создания')
    id: int
    password: str = Field(..., description='Пароль пользователя')
    spec_id: int | None


class Specializes(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    speciality_id: int
    speciality_name: str = Field(..., description='Название специальности(Барабанщик|гитарист|...)')
