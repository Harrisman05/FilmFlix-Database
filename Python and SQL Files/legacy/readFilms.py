from dbConnectFilmflix import *
import time

def readFilms():
    time.sleep(2)
    cursor.execute('SELECT * from tblFilms')
    row = cursor.fetchall()
    for record in row:
        print(record)

#readFilms