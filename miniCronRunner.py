import os
import sqlite3

if os.path.isfile('cronhoteldb.db'):
    dbcon = sqlite3.connect('cronhoteldb.db')
    with dbcon:
        cursor = dbcon.cursor()
        tasks = cursor.execute("SELECT TaskName,Parameter FROM Tasks JOIN TaskTimes ON Tasks.TasksId=TasksTimes.TaskId WHERE NumTimes>0").fetchall()


