import os
import sqlite3

def dohoteltask(taskname,parameter):
    if os.path.isfile('cronhoteldb.db'):
        dbcon = sqlite3.connect('cronhoteldb.db')
        with dbcon:
            cursor = dbcon.cursor()
            if taskname=="breakfast":
                cursor.execute("SELECT FirstName,LastName FROM Residents WHERE RoomNumber = (?)", (parameter,))
                fullName=cursor.fetchone()

