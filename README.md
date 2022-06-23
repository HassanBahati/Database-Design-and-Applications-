## transforming sqlite to sql
.mode csv
.import "file"
# get design of table 
.schema

# for sql commands a termination is required
eg SELECT * FROM "table";

## insert a movie into table
INSERT INTO table (<"column", "column") VALUES ("value", "value");

## select a particular value from the table
SELECT Film FROM movies WHERE Film LIKE "%see%"

## delete a movie from the table 
DELETE FROM movies WHERE FILM LIKE "%Waitress%"

## update a field
UPDATE movies SET film = "Dear Collins" WHERE Film LIKE "%Dear%";

## save database 
.save moviesList 