import csv 

# import cs50 module
from cs50 import SQL

#create db 
open("flicks.db", "w").close()

#store flicks.db in variable db
db=SQL("sqlite:///flicks.db")

#create tables
db.execute("CREATE TABLE movies (id INTEGER, title)")

