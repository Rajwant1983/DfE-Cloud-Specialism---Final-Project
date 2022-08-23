from readSongs import *
from addSongs import *
from searchSongs import *
from updateSongs import *
from delete import *

# create a function for the menu
def menuOptions():
    options= 0 #flag variables options=0
    
    # check the variables options which has a value set to zero "0"
    while options not in["1","2","3","4","5","6"]:
        print("Menu Options\n1. Print Songs.\n2. Add Songs.\n3. Update Songs.\n4. Search Songs.\n5. Delete Song.\n6. Exit")
    # reset the value for the options variable and assign it a new value
        options = input("\nEnter one of the options above ")
        if options not in ["1", "2", "3", "4", "5", "6"]:
            print(f"{options} is not in a valid option")
    return options


# create a boolean variable and set it value to True
mainProgram = True

while mainProgram == True:
    # pass menuOptions() function to the variable mainMenu
    mainmenu = menuOptions()

    if mainmenu == "1":
        read()
    elif mainmenu == "2":
        add()
    elif mainmenu == "3":
        updateSongs()
    elif mainmenu == "4":
        search()
    elif mainmenu == "5":
        deleteSongs()
    else:
        mainProgram = False
input("Press enter to exit")





menuOptions()
