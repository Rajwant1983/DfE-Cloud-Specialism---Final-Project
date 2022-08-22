from dbconnect import *
import time

#create a subroutine to add songs to the songs table in the dfemusic.db
def addSongs():
    # create an empty list
    songs=[]

    # songID field is autoIncrement

    #capture data inputted from the user

    title = input("Enter song title: ")
    artist = input("Enter artist name: ")
    genre = input("Enter song genre: ")
   # append the data captured from the user
   # songs.songID is the auto increment and would be added automatically
    songs.append(title)
    songs.append(artist)
    songs.append(genre)
    
    # insert data into the database that is songs table in the dfemusic.db
    cursor.execute("INSERT INTO songs VALUES(NULL,?,?,?)", songs)
    conn.commit() #commit the changes
    print(f"{title} added to Songs Table") #print out the song added
    time.sleep(3) # delay for 3 seconds before executing the select statement below

    # read data from table songs in Dfemusic.db
    cursor.execute("SELECT * FROM songs")# select all songs
    row = cursor.fetchall() # use to  fetch all data from the songs table and pass it to variable "row"
    for record in row:
        print(record)
        
addSongs() #call/invoke the function        