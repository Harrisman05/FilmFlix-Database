from dbConnect import * 
import readSongs
import time

def update():
    # enter id of the record to be updated 
    idField = input("Enter the ID for the reocrd to be updated: ")
# enter the name of the field to be updated 
    fieldName = input("Which field would you like to update: (Title, Artist, Genre)? ").title()
#enter the value of the fieldName to be updated  
    newFieldValue = input(f"Enter the value for the {fieldName} ")
    print(f"User Value {newFieldValue}")

    newFieldValue = "'" + newFieldValue + "'" # adding single on the value entered by the user
    print(f"User Value with single quote added {newFieldValue}")


    cursor.execute("UPDATE songs SET " + fieldName + "=" + newFieldValue + "WHERE SongID = " + idField)
    conn.commit()
    print(f"Record {idField} Updated")

    time.sleep(3)

    readSongs.readSong() 



# update()