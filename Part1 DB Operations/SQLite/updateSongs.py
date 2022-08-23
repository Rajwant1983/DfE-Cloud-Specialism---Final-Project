from os import read
import readSongs
from dbconnect import * 
import time

def updateSongs():
    #songID to be deleted 
    idField = input("Enter the SongID of the song you want to update: ")
    # enter the name of the field to be updated
    fieldName=input("which field value would you like to update:(Title,Artist,Genre)?").title()
    #enter the value of the fieldName to be updated
    newFieldvalue=input(f"Enter the value for the {fieldName}")
    print(f"the field value enter by user is {newFieldvalue} ")

    newFieldvalue="'" + newFieldvalue + "'"
    print(f"the field value enter by user is {newFieldvalue} ")
    # update songs set the field to fieldName(user entry)  with value=newfieldvalue('my record') where songID(4)= idfield(4)
    cursor.execute("UPDATE songs SET "+ fieldName + "=" + newFieldvalue + "WHERE songID=" + idField )
 #UPDATE songs set the field to fieldName(user entry) with value = newFieldValue('my Record') where songID (4) = idField4)
    cursor.execute("UPDATE songs SET " + fieldName + "=" + newFieldvalue + "WHERE songID = " + idField )
    conn.commit()
    print(f"Record {idField} Updated")
    time.sleep(3)
    readSongs.readSongs()

#updateSongs()