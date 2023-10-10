import sqlite3

def save_user(Records):


    con = sqlite3.connect(r"C:\Users\User\Desktop\web123\regular\Users.db")
    cur = con.cursor()

    # Проверяем, существует ли таблица, и создаем ее, если нет
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Users';")
    if cur.fetchone() is None:
        cur.execute("""CREATE TABLE Users (Id INTEGER PRIMARY KEY, Username TEXT, Password TEXT);""")

    # Вставляем данные в таблицу
    insert_query = """INSERT INTO Users (Username, Password) VALUES (?, ?);"""
    cur.execute(insert_query, Records)

    con.commit()

    # После вставки данных, проверяем базу данных
    check_database()


def check_database():
    con = sqlite3.connect(r"C:\Users\User\Desktop\web123\regular\Users.db")
    cur = con.cursor()

    # Выбираем все записи из таблицы Users
    cur.execute("SELECT * FROM Users;")
    rows = cur.fetchall()

    # Выводим результат
    for row in rows:
        print(row)

    con.close()
