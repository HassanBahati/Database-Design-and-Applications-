## set environment
.mode csv

## import data file
.import "file" table_name

# get design of table 
.schema

# for sql commands a termination is required
eg SELECT * FROM "table";

## insert a movie into table
INSERT INTO table ("column", "column") VALUES ("value", "value");

## select a particular value from the table
SELECT "column_field" FROM "table" WHERE "Film" LIKE "%see%"

## delete a movie from the table 
DELETE FROM movies WHERE FILM LIKE "%Waitress%"

## update a field
UPDATE movies SET film = "Dear Collins" WHERE Film LIKE "%Dear%";

## save database 
.save moviesList 

## open database
.open moviesList.db

## delte table
DELETE FROM table

## Concatenation of queries - get movies whose id is in the list of ids with genre Romance
SELECT Film FROM movies WHERE id IN (SELECT movie_id FROM genre WHERE genre LIKE "%Romance%")

SELECT genre FROM genre WHERE movie_id = (SELECT id FROM movies WHERE title LIKE "%Zack%");

.txt and .db
get a lst of movies and their genres 

## count through a table
SELECT COUNT(column) FROM table;

## get the time taken by a query
.timer ON

## 
CREATE INDEX title_index ON shows (title);

CREATE INDEX name_index ON people (name)

SELECT title FROM shows WHERE id IN (SELECT person_id FROM stars WHERE person_id IN (SELECT id FROM people WHERE name LIKE "%Thomas%"));

SELECT name FROM people WHERE person_id IN (SELECT person_id FROM stars show_id IN (SELECT id FROM shows WHERE title LIKE "%The Office%"));