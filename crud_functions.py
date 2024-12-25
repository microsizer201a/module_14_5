import sqlite3

def initiate_db():
    connection = sqlite3.connect("test_telegram.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    """)

    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect("test_telegram.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()

    connection.commit()
    connection.close()

    return products

def is_included(username):
    connection = sqlite3.connect("test_telegram.db")
    cursor = connection.cursor()

    cursor.execute("SELECT username FROM Users")
    users = cursor.fetchall()

    is_included_ = False
    for user in users:
        if user[0] == username:
            is_included_ = True
            break
        else:
            continue

    connection.commit()
    connection.close()
    return is_included_

def add_user(username, email, age):
    connection = sqlite3.connect("test_telegram.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)", (username, email, age, 1000))

    connection.commit()
    connection.close()

# initiate_db()
# connection = sqlite3.connect("test_telegram.db")
# cursor = connection.cursor()
#
# for number in range(1, 5):
#     cursor.execute("INSERT INTO Products(title, description, price) VALUES (?, ?, ?)", (f"Продукт {number}", f"Описание {number}", number * 100))
#
# connection.commit()
# connection.close()

