import csv

movies = set()
with open("gross movies.csv", "r", encoding="UTF-8") as file:
    reader = csv.DictReader(file)

    for movie in reader:
        #print all values with key Film
        # print(movie["Film"])

        #store the values under key Film in a set 
        movies.add(movie["Film"])

    #loop through the movies set and sort the data
    for ka_movie in sorted(movies):
        print(ka_movie)





