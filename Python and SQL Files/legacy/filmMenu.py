from readFilms import *
from addFilm import *
from updateFilms import *
from deleteFilms import *
from filterFilms import *

def menuOptions():

    options = 0 

    while options not in ["1","2","3","4","5"]:
        print(f"\nMenu Options\n1. View all Films.\n2. Add Films.\n3. Update Films.\n4. Delete Films.\n5. Filter Films.\n6. Exit")

        options = input("\nEnter one of the options above: ")

        if options not in ["1","2","3","4","5","6"]: 

            print("Not in the list of options")

    return  options

mainProgram = True

while mainProgram == True:

    mainMenu = menuOptions()

    if mainMenu == "1":
        readFilms.readFilms()  # invoke/call the readSong subroutine

    elif mainMenu == "2":
        addFilm()
          
    elif mainMenu =="3":
        updateFilms()
    
    elif mainMenu == "4":
        deleteFilms()
    
    elif mainMenu == "5":
        filterFilms()

    else:
        mainProgram = False

input("Press Enter to exit: ")


