import os
import sqlite3
import time
import hotelManagement
import hotelWorker

if os.path.isfile('cronhoteldb.db'):
    dbcon = sqlite3.connect('cronhoteldb.db')
    with dbcon:
        cursor = dbcon.cursor()
        listTasks = cursor.execute("SELECT TaskName,Parameter FROM Tasks JOIN TaskTimes ON Tasks.TasksId=TasksTimes.TaskId WHERE NumTimes>0").fetchall()
        finish = False
        while len(listTasks) > 0:
            for task in listTasks:
                lastTime = hotelWorker.dohoteltask(task[0], task[1])
                lastTimeList





