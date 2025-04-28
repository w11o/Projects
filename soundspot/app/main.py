from fastapi import FastAPI, HTTPException
import pydantic
from users.router import router as router_users
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Можно указать конкретные домены вместо "*", чтобы разрешить только для них
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все HTTP-методы
    allow_headers=["*"],  # Разрешить все заголовки
)

@app.get("/")
def home_page():
    return {'message': 'Hello World!'}

app.include_router(router_users)

posts = [
    {'post_1': 'ищу группу'},
    {'post_2': 'ищу барабанщика срочно москва!!!'},
    {'post_3': 'ищу басиста'},
    {'post_4': 'Вот пример большого поста о поиске музыкальной группы, который можно использовать на форуме SoundSpot. Этот пост включает в себя заголовок, описание, информацию о музыканте, а также контактные данные. Вы можете использовать этот текст для демонстрации на вашей странице.'}
]
@app.get("/posts")
def home_page():
    return posts

app.include_router(router_users)


# @app.post("/register/")
# async def register_user(user: UserRegistration):
#     # Логика регистрации пользователя
#     return {"message": "User registered successfully", "user": user}


# @app.get("/user")   
# async def get_user(username: str) -> UserRegistration:
#     # Логика получения пользователя
#     for user in users:
#         if user.username == username:
#             return user
#     raise HTTPException(status_code=409, detail='No such users')
