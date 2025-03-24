import sqlite3
import db
import os
import time

os.environ["TZ"] = "Asia/Tokyo"
time.tzset()

DATABASE = "database.db"


def get_user():
    con = sqlite3.connect(DATABASE)
    db_users = con.execute("SELECT * FROM users").fetchall()
    con.close()
    print(len(db_users))
    return db_users

print(db.get_all_result("mufc"))