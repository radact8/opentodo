import sqlite3
import datetime
import db


names = db.get_user()
for name in names:
    #db.task_insert_day_change(name)[1]
    db.task_insert_day_change(name[1])

task_empty = db.get_check_empty("mufc")
for x in task_empty:
    if(x == 0):
        print("w")
    else:
        print("fewas")

get_all = db.get_all_result("mufc")
print(get_all[0][0])

