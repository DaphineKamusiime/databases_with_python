#import csv libraryu for reading and opening from a csv file
import csv
from tkinter.tix import INTEGER
#using this file ton execute SQL queries
from cs50 import SQL
open ("tuesday.db","w").close()
db=SQL"sqlite:///tuesday.db"
db.execute("CREATE TABLE movies(id INTEGER, title TEXT, PRIMARY KEY(id))")
db.execute("CREATE TABLE genre(movie_id INTEGER, genre TEXT, FOREIGN KEY(movie_id) REFERENCES movies(id))")
with open("gross movies.csv","r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        title=row["Film"].strip().capitalize()
        
        db.execute("INSERT INTO movies(title) VALUES(?)", title)
        
        for genre in row["Genre"].split(","):
            db.execute("INSERT INTO genre(movie_id,genre)fcdfd" VALUES(?,?), movieId, genre)



