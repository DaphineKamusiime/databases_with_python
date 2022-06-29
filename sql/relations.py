import csv
from turtle import title
from cs50 import SQL
open("gross movies.db","w").close()
bdb=SQL("ite:///grass_movies_db.db")
db.execute("CREATE TABLE movies(id INTEGER, title TEXT. PRIMARY KEY(id))")
db.execute("CREATE TABLE genre(movie_id INTEGER, genre TEXT, FOREIGN KEY(movie_id) REFERENCES movies(id))")
with open("gross movies.csv", "r") as file:
    reader=csv.DictReader(title)
    for row in reader:
        titlerow["Film"].strip().capitalize()
        db.execute("INSERT INTO movies (title) VALUES(?)", title)
        for genre in row[" Genre"].split(","):
            db.execute("INSERT INTO genre (movie_id, genre) VALUES(?,?)",id,genre)
        
    



