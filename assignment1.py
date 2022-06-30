import csv
from cs50 import SQL

# open database
open("assignment1.db", "w").close()

db = SQL("sqlite:///assignment1.db")

# create table movies
db.execute("CREATE TABLE movies (id INTEGER, title TEXT, PRIMARY KEY(id))")

# create table genre
db.execute("CREATE TABLE genre (id INTEGER, genre TEXT, PRIMARY KEY(id))")

# create table moviegenre
db.execute("CREATE TABLE moviegenre (movie_id INTEGER, genre TEXT, FOREIGN KEY(movie_id) REFERENCES movies(movie_id))")

with open("gross movies.csv", "r") as file:
    # store in file called reader
    reader = csv.DictReader(file)

    # remove duplicates from reader
    noDuplicates = set()

    for row in reader:
        # get title and store in a variable title
        title = row["Film"].strip().capitalize()


        # insert data into movies table
        id = db.execute("INSERT INTO movies (title) VALUES(?)", title)

        for genre in row["Genre"].split(","):
            # insert data into genre table
            db.execute(
                "INSERT INTO moviegenre (movie_id, genre) VALUES(?,?)", id, genre)

  