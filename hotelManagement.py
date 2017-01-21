import os
import sqlite3

databaseexisted = os.path.isfile('cronhoteldb.db')
dbcon = sqlite3.connect('cronhoteldb.db')
with dbcon:
    cursor = dbcon.cursor()
    if not databaseexisted:  # First time creating the database. Create the tables
        cursor.execute("CREATE TABLE TaskTimes(TaskId INTEGER PRIMARY KEY NOT NULL,DoEvery INTEGER NOT NULL, NumTimes INTEGER NOT NULL)")  # create table TaskTimes
        cursor.execute("CREATE TABLE Tasks(TaskId INTEGER REFERENCES TaskTimes(TaskId),TaskName TEXT NOT NULL, Parameter INTEGER)")  # create table students
        cursor.execute("CREATE TABLE Rooms(RoomNumber INTEGER PRIMARY KEY NOT NULL)")  # create table students
        cursor.execute("CREATE TABLE Residents(RoomNumber INTEGER NOT NULL REFERENCES Rooms(RoomNumber),FirstName TEXT NOT NULL, LastName TEXT NOT NULL)")  # create table students
        cursor.execute("INSERT INTO Students VALUES(?,?)",
                       (1, 'Morad',))  # add entry 'id = 1, name = Morad' into the table.
        cursor.execute("INSERT INTO Students VALUES(?,?)", (2, 'Harry Potter',))

