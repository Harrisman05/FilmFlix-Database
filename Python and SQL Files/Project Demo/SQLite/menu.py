from readSongs import * # import from the respective files
from addSongs import *
from updateSongs import *
from deleteSongs import *

def menuOptions(): # create a function
    options = 0  # created a flag variable and assign it an integer variable datatype

    # check for the value 0
    while options not in ["1","2","3","4","5"]:
        print(f"\nMenu Options\n1. Print Songs.\n2. Add Songs.\n3. Update Songs.\n4. Delete Songs.\n5. Exit")
    #reset/reassign value in the options variable 
        options = input("\nEnter one of the options above: ")
    # if the option the user enter is not found, then print("Not in the list of options")
        if options not in ["1","2","3","4","5"]: 
            # if found return the option 
            print("Not in the list of options")
    return  options

# create a flag variable with a boolean value set to True 
mainProgram = True 

while mainProgram == True:
    # pass the menuOptions function into a variable called mainMenu
    mainMenu = menuOptions() # invoke the function menuOptions

    if mainMenu == "1":
        readSong()  # invoke/call the readSong subroutine
    
    elif mainMenu == "2":
        addSong()
          
    elif mainMenu =="3":
        update()
    
    elif mainMenu =="4":
        deleteSong()

    else:
        mainProgram = False
input("Press Enter to exit: ")

