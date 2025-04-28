from pydantic import EmailStr
from database import async_session_maker
class RBUser:
    def __init__(self, id: int | None = None,
                 username: str | None = None,
                 email: EmailStr | None = None):
        self.id = id
        self.username = username
        self.email = email


        
    def to_dict(self) -> dict:
        data = {'id': self.id, 'username': self.username, 'email':self.email}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data
    
    
