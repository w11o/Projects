import psycopg2
from config import  host, user, password, db_name

def insert(feedback):

    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True


        with connection.cursor() as cursor:
            cursor.execute(
                """INSERT INTO feedback (name, message) VALUES (%s, %s)""", [feedback.name, feedback.message])
            print("[INFO] Data was successfully inserted")

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)

def get_product_by_id(id: int):

    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT * FROM products WHERE product_id = (%s)""", [id]
            )
            print(cursor.fetchone())

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)

    finally:
        print("[INFO] PostgreSQL connection closed")

get_product_by_id(101)
