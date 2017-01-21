import os
import sqlite3

databaseexisted = os.path.isfile('cronhoteldb.db')
dbcon = sqlite3.connect('cronhoteldb.db')
with dbcon:
    cursor = dbcon.cursor()
    if not databaseexisted:  # First time creating the database. Create the tables
        cursor.execute("CREATE TABLE TaskTimes(TaskId INTEGER PRIMARY KEY NOT NULL,DoEvery INTEGER NOT NULL, NumTimes INTEGER NOT NULL)")  # create table TaskTimes
        cursor.execute("CREATE TABLE Tasks(TaskId INTEGER REFERENCES TaskTimes(TaskId),TaskName TEXT NOT NULL, Parameter INTEGER)")  # create table Tasks
        cursor.execute("CREATE TABLE Rooms(RoomNumber INTEGER PRIMARY KEY NOT NULL)")  # create table Rooms
        cursor.execute("CREATE TABLE Residents(RoomNumber INTEGER NOT NULL REFERENCES Rooms(RoomNumber),FirstName TEXT NOT NULL, LastName TEXT NOT NULL)")  # create table Residents

        def main(args):
            inputfilename = args[1]
            counter = 0
            if (not os.path.isfile(inputfilename)):  # check if file exists
                return
            with open(inputfilename) as inputfile:  # try-with-resources
                for line in inputfile:
                    words = line.split(',')
                    if words[0]=="room":
                        cursor.execute("INSERT INTO Rooms VALUES(?)", (words[1]))
                        if len(words)==4:
                            cursor.execute("INSERT INTO Residents VALUES(?,?,?)", (words[1]), ((words[2])),(words[3]))
                    else:
                        if (len(words)==4 and ((words[0]=="clean") or (words[0]=="breakfast") or (words[0]=="wakeup"))):
                            cursor.execute("INSERT INTO TaskTimes VALUES (?,?,?)", (counter, words[1], words[3],))
                            cursor.execute("INSERT INTO Tasks VALUES (?,?,?)", (counter, words[0], words[2],))
                            counter = counter + 1
                        else:
                            if (len(words) == 3 and ((words[0] == "clean") or (words[0] == "breakfast") or (words[0] == "wakeup"))):
                                cursor.execute("INSERT INTO TaskTimes VALUES (?,?,?)", (counter, words[1], words[2],))
                                cursor.execute("INSERT INTO Tasks VALUES (?,?,?)", (counter, words[0], 0,))
                                counter = counter+1

