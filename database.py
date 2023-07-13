import sqlite3



def add_data(data:tuple):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO users(Email, Password) VALUES (?, ?)", data)
    conn.commit()
    conn.close()

def get_data(email:str)->tuple:
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()

    result = cur.execute(f"SELECT * from users where Email = '{email}'").fetchone()

    return result

def create_users_table():
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()

    cur.execute("CREATE TABLE users(_id INTEGER PRIMARY KEY, Email TEXT, Password TEXT )")

    conn.commit()
    conn.close()


def create_plans_table():
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()

    cur.execute("CREATE TABLE plans(id INTEGER PRIMARY KEY,  Planes TEXT, Email TEXT )")

    conn.commit()
    conn.close()


def add_plan(email, plane):
    conn = sqlite3.connect('plans.db')
    cur = conn.cursor()
    cur.execute(f"INSERT INTO plans(Planes, Email) VALUES('{plane}', '{email}')")

    conn.commit()


def get_all_planes(email):
    conn = sqlite3.connect('plans.db')
    cur = conn.cursor()

    result = cur.execute(f"SELECT * from plans where Email = '{email}'").fetchall()

    return result







