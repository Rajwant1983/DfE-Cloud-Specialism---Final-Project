from dbconnect import * 

def read():
    # read data from table songs in Dfemusic.db
    cursor.execute("SELECT * FROM songs")# select all songs
    row = cursor.fetchall() # use to  fetch all data from the songs table and pass it to variable "row"
    for record in row:
        print(record)
        
# readSongs() #call/invoke the function  
