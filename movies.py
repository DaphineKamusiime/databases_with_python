import csv
from itertools import count
movies=set()
with open("gross movies.csv", "r", encoding ='UTF8') as file:
    reader =csv.DictReader(file)
   # next (reader)
    
    for movie in reader:
        movies.add(movie["Film"])

       # print(movie[1])

for kaMovies in count((movies)):
    print(kaMovies)

    