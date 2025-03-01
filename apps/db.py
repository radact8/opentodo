import sqlite3


import models

DATABASE = "database.db"

def create_user_table():
    con = sqlite3.connect(DATABASE)
    con.execute(
        """
                CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                username VARCHAR(255) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL
                )
        """
    )
    con.close()

def add_user(username,password):
    con = sqlite3.connect(DATABASE)
    con.execute("INSERT INTO users (username,password) values(?,?)",(username,password))
    con.commit()
    con.close()

def get_user():
    con = sqlite3.connect(DATABASE)
    db_users = con.execute("SELECT * FROM users").fetchall()
    con.close()
    return db_users

def users():
    con = sqlite3.connect(DATABASE)
    db_users = con.execute("SELECT * FROM users").fetchall()
    con.close()
    users_num = len(db_users)
    users = {}
    for i in range(users_num):
        users[db_users[i][0]] = models.User(id=db_users[i][0],username=db_users[i][1],password=db_users[i][2])
    return users

def create_tasks_table(name):
    con = sqlite3.connect(DATABASE)
    create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {name}(
            taskid integer,
            taskname VARCHAR(255)
        )
        """
    con.execute(create_table_query)
    con.close()
    con = sqlite3.connect(DATABASE)
    size_query = f"""SELECT * FROM {name}"""
    db_size = con.execute(size_query).fetchall()
    size = len(db_size)
    con.close()
    if(size == 0):
        con = sqlite3.connect(DATABASE)
        column_query = f"""INSERT INTO {name} (taskid,taskname) values(?,?)"""
        for i in range(7):
            taskname = ""
            con.execute(column_query,(i,taskname))
            con.commit()
            print("s")
        con.close()
        print("sss")
    
    

def sql_add_task(usertable,id,task_name):
    con = sqlite3.connect(DATABASE)
    sql_add_quety = f"""UPDATE {usertable} SET taskname=(?) WHERE taskid=(?)"""
    con.execute(sql_add_quety,(task_name,id))
    con.commit()
    con.close() 

def size_check(name):
    con = sqlite3.connect(DATABASE)
    size_query = f"""SELECT COUNT(*) FROM {name}"""
    size = con.execute(size_query)
    con.close()

    return size

def get_users_task(tasktable):
    con = sqlite3.connect(DATABASE)
    db_tasks_query = f"""SELECT * FROM {tasktable}"""
    db_tasks = con.execute(db_tasks_query).fetchall()
    print(len(db_tasks))
    tasks = []
    for task in db_tasks:
        tasks.append(task)
    return tasks

