import csv
#this is a dicttionary to take a list of movies
olivier={}
with open("gross movies.csv", "r", encoding='UTF8') as file:
   movies6read = csv.DictReader(file)
   for work in movies6:   
        movie=movies6["Film"].strip().lower()
        if movie not in olivier:
            olivier[movie]= 0
            olivier[movie]+= 1
            for movie in sorted(olivier):
                print(movie)
                print(work["lead studio"])


