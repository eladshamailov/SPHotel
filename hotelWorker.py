import os
import sqlite3
import time

def dohoteltask(taskname,parameter):
    if os.path.isfile('cronhoteldb.db'):
        dbcon = sqlite3.connect('cronhoteldb.db')
        with dbcon:
            cursor = dbcon.cursor()
            if taskname=="breakfast":
                cursor.execute("SELECT FirstName,LastName FROM Residents WHERE RoomNumber = (?)", (parameter,))
                fullName=cursor.fetchone()
                print (fullName[0]+" "+fullName[1]+" in room "+parameter+" has been served breakfast at "+str(time.time()))
                ans=time.time()
                cursor.execute("UPDATE TaskTimes SET NumTimes=(?) WHERE TasksTimes.TaskId=(SELECT TaskId FROM Tasks WHERE Tasks.parameter=(?) AND Tasks.TaskName=(?))", [NumTimes-1, parameter, 'breakfast'])
                return ans
            else:
                if taskname=="wakeup":
                    cursor.execute("SELECT FirstName,LastName FROM Residents WHERE RoomNumber = (?)", (parameter,))
                    fullName = cursor.fetchone()
                    print (fullName[0]+" "+fullName[1]+" in room "+parameter+" has been served breakfast at "+str(time.time()))
                    ans = time.time()
                    cursor.execute("UPDATE TaskTimes SET NumTimes=(?) WHERE TasksTimes.TaskId=(SELECT TaskId FROM Tasks WHERE Tasks.parameter=(?) AND Tasks.TaskName=(?))", [NumTimes-1, parameter, 'wakeup'])
                    return ans
                else:
                    if taskname=="clean":
                        cursor.execute("SELECT * FROM Rooms")
                        allRooms = cursor.fetchall()
                        cursor.execute("SELECT TaskId FROM Tasks WHERE TaskName=(?) AND Parameter=(?)", (taskname, parameter,))
                        taskId = cursor.fecthone()
                        string_rooms = ""
                        for room in allRooms:
                            Strooms = Strooms + room
                        print("Rooms ", Strooms, " cleaned at ", str(time.time()))
                        ans = time.time()
                        cursor.execute("UPDATE TaskTimes SET NumTimes = NumTimes -1 WHERE TaskId = (?)", (taskId,))
                        return ans
