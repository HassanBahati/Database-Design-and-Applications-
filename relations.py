import csv
from cs50 import SQL

# open database 
open("gross_movies_db.db", "w").close()

db=SQL("sqlite:///gross_movies_db.db")

# create table movies
db.execute("CREATE TABLE movies (id INTEGER, title TEXT, PRIMARY KEY(id))")

#create table genre
db.execute("CREATE TABLE genre (movie_id INTEGER, genre TEXT, FOREIGN KEY(movie_id) REFERENCES movies(id))" )

# inserting data into table
with open("gross movies.csv", "r") as file:
    #store in file called reader
    reader = csv.DictReader(file)