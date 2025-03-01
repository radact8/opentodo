import sqlite3
DATABASE = "database.db"


def get_user():
    con = sqlite3.connect(DATABASE)
    db_users = con.execute("SELECT * FROM users").fetchall()
    con.close()
    print(len(db_users))
    return db_users

get_user()