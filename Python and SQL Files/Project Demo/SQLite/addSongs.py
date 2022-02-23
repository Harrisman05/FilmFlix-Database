from dbConnect import * 
import time

# create a subroutine to add songs to the song table in the c6music db 
def addSong():
    # create an empty list 
    songs = []
    #SongID field is auto increment 
    "lastrowid from the cursor object. check the lastrowd id and start the next id a number above "
    # songID = cursor.lastrowid # auto generated 

    # capture data inputted form the user
    title = input("Enter song Title: ")
    artist = input("Enter song Artist: ")
    Genre = input("Enter song Genre: ")

    #append data captured from user input
    # songs.append(songID)
    songs.append(title)
    songs.append(artist)
    songs.append(Genre)

    # try: # insert data into songs table
    cursor.execute('INSERT INTO songs VALUES(NULL,?,?,?)', songs)
    conn.commit() # commiting the changes/the insert statement
    print(f"{title} added to Songs Table" )
    time.sleep(3)
    cursor.execute('SELECT * FROM songs') #  select all data from songs table
    row = cursor.fetchall() # use fetchall to get all data from the songs table
    for record in row:
        print(record)
    # except:
    #     print(f"{title} not added ! ")
    # finally:
    #     conn.close()

# addSong()





