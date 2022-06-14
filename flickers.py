#import csv library
import csv 

# import cs50 module from library cs50
from cs50 import SQL

#create db 
open("flicks.db", "w").close()

#store flicks.db in variable db
db=SQL("sqlite:///flicks.db")

#create movies table with priary keym
db.execute("CREATE TABLE movies (id INTEGER, title TEXT, PRIMARY KEY(id))")

#create genre table with foreign key 
db.execute("CREATE TABLE genres (movie_id INTEGER, genre TEXT, FOREIGN KEY(movie_id) REFERENCES movies(id))")

#open gross movies
with open("gross movies.csv", "r") as file:
    #store the file in variable reader
    reader = csv.DictReader(file)

    for row in reader:
        title = row["Film"].strip().capitalize()

        db.execute("INSERT INTO movies VALUES(?)", title)




# check if db has been created in terminal
# .open flicks.db
# .schema

