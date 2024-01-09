
from sqlite3 import Error
from connect import create_connection, database


def create_db():
    # читаємо файл зі скриптом для створення БД
    with open('create_table.sql', 'r') as f:
        sql = f.read()

    # створюємо з'єднання з БД 
    with create_connection('hw6.db') as con:
        cur = con.cursor()
        cur.executescript(sql)


if __name__ == "__main__":
    create_db()
    