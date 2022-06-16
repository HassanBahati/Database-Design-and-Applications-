import csv

movies = set()
with open("gross movies.csv", "r", encoding="UTF-8") as file:
    reader = csv.DictReader(file)

    for movie in reader:
        #print all values with key Film
        print(movie["Film"])

        #store the values under key Film in a set 
        movies.add(movie["Film"])





