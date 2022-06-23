## transforming sqlite to sql
.mode csv
.import "file"
# get design of table 
.schema

# for sql commands a termination is required
eg SELECT * FROM <table>;

## insert a movie into table
INSERT INTO table (<"column", "column") VALUES ("value", "value");