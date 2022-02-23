from dbConnect import * 
import readSongs
import time

def deleteSong():
    idField = input("Enter the ID for the reocrd to be deleted: ")

    cursor.execute("DELETE FROM songs WHERE SongID=" + idField)
    conn.commit()

    print(f"Record {idField} deleted")

    time.sleep(3)

    readSongs.readSong() 

# deleteSong()


