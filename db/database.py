import sqlite3


def get_connection():
    return sqlite3.connect("qa_test.db")


def setup_database():
    connection = get_connection()

    with open("sql/setup.sql", "r") as file:
        sql_script = file.read()

    connection.executescript("DROP TABLE IF EXISTS users;")
    connection.executescript(sql_script)

    connection.commit()
    connection.close()