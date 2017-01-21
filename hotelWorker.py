import os
import sqlite3

def dohoteltask(taskname,parameter)
    if os.path.isfile('cronhoteldb.db'):
        dbcon = sqlite3.connect('cronhoteldb.db')
        with dbcon:
            cursor = dbcon.cursor()
            if taskname=="breakfast":
                fullName=cursor.execute("SELECT FirstName,LastName FROM Residents WHERE RoomNumber =

