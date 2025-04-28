from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str



settings = Settings(
    DB_HOST='localhost',
    DB_PORT='5432',
    DB_NAME='fastapi',
    DB_USER='postgres',
    DB_PASSWORD=''
)


def get_db_url():
    return (f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@"
            f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}")
print(get_db_url())