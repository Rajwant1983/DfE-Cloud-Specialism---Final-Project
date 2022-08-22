import sqlite3 #import sqlite3 module/library

"create a variable 'conn' and pass sqlite3.connect method to it"
# pass in folderpath dbname.db as parameter,which will create the db
# it it does not exist/otherwise use if it exists
conn = sqlite3.connect("Part1 DB Operations\SQLite\Dfemusic.db")
cursor = conn.cursor() # cursor method iterates through database/tables