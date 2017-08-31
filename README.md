# SPHotel
version of cron that will help us in managing our hotel using Phyton and SQLite.

In order for our program to be sane and checkable in a reasonable time, we will assume 
that each task will be done ‘every t seconds’ for a specified integer t of that task.
Furthermore, in order for our program to be finite and terminate in a reasonable time
as well,we will assume that each task will be done ‘z’ times only, for a specified integer z of that task.

## Hotel Services
Our hotel will have the following services.These services are the ‘tasks’ to be done.

* Breakfast service: This service serves breakfast to the resident of a given room.

* Wakeup-call service: This service gives a wake-up call to the resident of a given room.

* Room-cleaning service: This service cleans all empty rooms (rooms with no resident).

## Method and technical description
We have an SQLlite database that holds our tasks tables, as well as our rooms tables.The database’s filename is cronhoteldb.db. 
Also,we have 3 Phyton modules.

## Configuration files
Each line in the config file either represents a room, a room with a resident, or a task.

Example config:
```
room,112,Harry,Potter
room,115,Darth,Vader
room,234
room,127
clean,10,2
breakfast,5,112,2
wakeup,10,115,2
breakfast,3,115,1
```

```
Rooms 127, 234 were cleaned at 1484899494.67
Harry Potter in room 112 has been served breakfast at 1484899494.67
Darth Vader in room 115 received a wakeup call at 1484899494.67
Darth Vader in room 115 has been served breakfast at 1484899494.67
Harry Potter in room 112 has been served breakfast at 1484899499.67
Rooms 127, 234 were cleaned at 1484899504.67
Darth Vader in room 115 received a wakeup call at 1484899504.67
```



