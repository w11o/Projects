import  psycopg2
from config import  host, user, password, db_name


try:
    #connect to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    # the cursor for performing database operations
    #cursor = connection.cursor()

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version()"
        )

        print(f"Server version: {cursor.fetchone()}")

    # create a new table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE feedback(
    #         name VARCHAR(50) NOT NULL,
    #         message VARCHAR(500) NOT NULL );"""
    #     )
    #
    #     # connection.commit()
    #     print("[INFO] Table created successful")

    # insert data into a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """INSERT INTO feedback (name, message) VALUES
    #         ('Oleg', 'norm');"""
    #     )
    #     print("[INFO] Data was successfully inserted")

    # get data from a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT message FROM feedback WHERE name = 'Oleg';"""
    #     )
    #
    #     print(cursor.fetchone())

    # delete a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DROP TABLE feedback;"""
    #     )

    #     print("[INFO] Table was deleted")

    # delete row
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DELETE FROM feedback
    #          WHERE name = 'Oleg';"""
    #     )
    #     print("[INFO] Data was successfully deleted")

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        #cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")