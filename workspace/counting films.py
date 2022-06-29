import csv
movies= dict {}
with open("gross movies.csv", "r", encoding ='UTF8') as file:
    reader =csv.DictReader(file)
for movie in movies:
    movie=row