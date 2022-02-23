from dbConnect import * 

def readSong():
    cursor.execute('SELECT * FROM songs') #  select all data from songs table
    row = cursor.fetchall() # use fetchall to get all data from the songs table
    for record in row:
        print(record)
    # conn.close()
# readSong()