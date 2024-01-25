from fastapi.responses import FileResponse, JSONResponse
from db_feedback_products import insert, get_product_by_id
from fastapi import FastAPI
from models import FeedBack, UserCreate
import psycopg2
from config import  host, user, password, db_name
app = FastAPI()

# Пример пользовательских данных (для демонстрационных целей)


# Конечная точка для получения информации о пользователе по ID

@app.post("/feedback")
async def feedback(feedback: FeedBack):
    insert(feedback)
    return JSONResponse({"message": f"Feedback received. Thank you {feedback.name}"})

@app.post("/create_user")
async def subscribers(user: UserCreate):
    return user

@app.get("/product/{product_id}")
async def products(product_id:int):
    a = get_product_by_id(product_id)
    return print(get_product_by_id(product_id))


@app.get("/products/search")
async def search(keyword, category, limit):
    return {'keyword': keyword, 'category': category, 'limit': limit}

#uvicorn main:app --reload
#Документацию можете посмотреть по ссылкам http://127.0.0.1:8000/docs и http://127.0.0.1:8000/redoc (альтернативная).
#uvicorn main:app --host 127.0.0.1 --port 80
