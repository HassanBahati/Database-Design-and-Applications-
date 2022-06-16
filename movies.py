import csv

with open("gross movies.csv", "r", encoding="UTF-8") as file:
    reader = csv.DictReader(file)

    for movie in reader:
        print(movie["Film"])