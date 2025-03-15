import sqlite3
import datetime
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
    
    

def sql_add_task(username,usertable,id,task_name):
    result_table = username+"sresults"
    date = datetime.date.today().strftime("%Y/%m/%d")
    search_query = f"""SELECT * FROM {result_table} where day = '{date}' and taskid = {id}"""
    con = sqlite3.connect(DATABASE)
    task_id = con.execute(search_query).fetchall()[0][0]
    #check_empty = con.execute(search_query).fetchall()[0][5]
    print(task_id)
    con.close()
    con = sqlite3.connect(DATABASE)
    sql_add_quety = f"""UPDATE {usertable} SET taskname=(?) WHERE taskid=(?)"""
    sql_update_query = f"""UPDATE {result_table} SET checkempty=1 where id=(?)"""
    con.execute(sql_add_quety,(task_name,id))
    con.execute(sql_update_query,(task_id,))
    con.commit()
    con.close() 
    con = sqlite3.connect(DATABASE)

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
    #print(len(db_tasks))
    tasks = []
    for task in db_tasks:
        tasks.append(task)
    return tasks

def create_task_results(username):
    tableName = username + "sresults"
    con = sqlite3.connect(DATABASE)
    query = f"""
        CREATE TABLE IF NOT EXISTS {tableName} (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        taskid INTEGER NOT NULL,
        taskname VARCHAR(255) NOT NULL,
        result INTEGER NOT NULL,
        day VARCHAR(255) NOT NULL,
        checkempty INTEGER NOT NULL
    )
    """
    con.execute(query)
    con.close()

def task_insert_day_change(username):
    #taskidごと(0~7)のtask名取得
    tasktable = username+"Task"
    tasks = get_users_task(tasktable)
    #insertするresulttable名
    tableName = username + "sresults"
    con = sqlite3.connect(DATABASE)
    insert_query = f"""
        INSERT INTO {tableName} (taskid,taskname,result,day,checkempty) values(?,?,?,?,?)
    """
    check_empty = 0
    day = datetime.date.today().strftime("%Y/%m/%d")
    print(tableName)
    for i in range(7):
        check_empty = 0
        taskname = tasks[i][1]
        if(taskname != ""):
            check_empty = 1
        print(type(taskname))
        taskid = i
        result = 0
        con.execute(insert_query,(i,taskname,0,day,check_empty))  #resultは0でやってない,checkemptyは0で空
    con.commit()
    con.close()

    con = sqlite3.connect(DATABASE)
    get_query  = f"""SELECT * FROM {tableName}"""
    db_results = con.execute(get_query).fetchall()
    print(len(db_results))
    print("CHECK")
    con.close()

#更新(やったか)
def update_doing(username,number):
    table = username + "sresults"
    date = datetime.date.today().strftime("%Y/%m/%d")
    search_query = f"""SELECT * FROM {table} where day = '{date}' and taskid = {number}"""
    con = sqlite3.connect(DATABASE)
    task_id = con.execute(search_query).fetchall()[0][0]
    print(task_id)
    check_empty = con.execute(search_query).fetchall()[0][5]
    con.close()
    if(check_empty == 0):
        update_query = f""" 
        UPDATE {table} SET result = 0 WHERE id = {task_id}
        
        """
    else:
        update_query = f""" 
        UPDATE {table} SET result = 1 WHERE id = {task_id}
        
        """
    con = sqlite3.connect(DATABASE)
    con.execute(update_query)
    con.commit()
    con.close()
    check_query = f"""SELECT * FROM {table} where day = '{date}' and taskid = {number}"""
    con = sqlite3.connect(DATABASE)
    check = con.execute(check_query).fetchall()
    con.close()
    print(check)



#確認
def get_result_size(username):
    tableName = username + "sresults"
    con = sqlite3.connect(DATABASE)
    query  = f"""SELECT * FROM {tableName}"""
    db_results = con.execute(query).fetchall()
    con.close()
    results = []
    for result in db_results:
        results.append(result)
    size = len(results)
    return size
    
def get_result_days(username):
    tableName = username + "sresults"
    con = sqlite3.connect(DATABASE)
    query  = f"""SELECT * FROM {tableName}"""
    db_results = con.execute(query).fetchall()
    con.close()
    results = []
    for result in db_results:
        results.append(result[4])
        print(result[4])
    
    return results
    
def get_result_taskname(username):
    tableName = username + "sresults"
    con = sqlite3.connect(DATABASE)
    query  = f"""SELECT * FROM {tableName}"""
    db_results = con.execute(query).fetchall()
    con.close()
    results = []
    for result in db_results:
        results.append(result[2])
    
    return results

def get_all_result(username):
    tableName = username + "sresults"
    con = sqlite3.connect(DATABASE)
    query  = f"""SELECT * FROM {tableName}"""
    db_results = con.execute(query).fetchall()
    con.close()
    results = []
    for result in db_results:
        results.append(result)
    
    return results

def get_check_empty(username):
    tableName = username + "sresults"
    con = sqlite3.connect(DATABASE)
    query  = f"""SELECT * FROM {tableName}"""
    db_results = con.execute(query).fetchall()
    con.close()
    results = []
    for result in db_results:
        results.append(result[5])
    
    return results

def get_todays_result(username):
    tableName = username + "sresults"
    con = sqlite3.connect(DATABASE)
    query  = f"""SELECT * FROM {tableName}"""
    db_results = con.execute(query).fetchall()
    con.close()
    print(db_results)
    results = []
    for result in db_results:
        results.append(result[3])
    
    
    return results