import sqlite3
import datetime
import db
import os
import time



names = db.get_user()
for name in names:
    db.task_insert_day_change(name[1])
