import sqlite3 # import sqlite3 library/module
"create variable conn and pass the sqlite3.connect method to it"
 # pass in path/dbname as parameters, which will create the datbase
 # if it does not exist/ otherwsie use it  if it exists
conn  = sqlite3.connect('c6Music.db')
cursor = conn.cursor() # cursor iteraates through our database/tables
# 5. Programming Part11 DB operations\SQLite


