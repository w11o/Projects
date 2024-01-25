from pydantic import BaseModel, EmailStr, PositiveInt, Field
from typing import Union
class FeedBack(BaseModel):
    name: str
    message: str


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: Union[PositiveInt, None] = Field(default=None, lt= 130)
    is_subscribed: Union[None, bool] = None

#description: Union[str, None] = None