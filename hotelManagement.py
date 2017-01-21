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
            if (not os.path.isfile(inputfilename)):  # check if file exists
                return
            with open(inputfilename) as inputfile:  # try-with-resources
                for line in inputfile:
                    words = line.split(',')
                    if words[0]=="room":
                        cursor.execute("INSERT INTO Rooms VALUES(?)", (words[1]))
                        if len(words)==4:
                            cursor.execute("INSERT INTO Residents VALUES(?,?,?)", (words[1]), ((words[2])),(words[3]))


