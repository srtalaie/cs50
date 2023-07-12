## SQL
- **Structured Query Language** (SQL) - language for querying databases

## Flat-file Databases
- **Flat-file Database** - a database stored in a file called a **flat file**. Records follow a uniform format, and there are no structures for indexing or recognizing relationships between record. ex./ .csv files
- Open a .csv in python and parse it. In this scenario you have to remember what columns are what because you are trusting "1" is the data you want.

```
import csv

with open("favorites.csv", "r") as file:
	reader = csv.reader(file)
	for row in reader:
		favorite = row[1]
		print(favorite)
```

- Using **DictReader** returns a dictionary rather than a list. This allows you to target the column by name so you do not have to remember what order the columns are.

```
import csv

with open("favorites.csv", "r") as file:
	reader = csv.DictReader(file)
	for row in reader:
		favorite = row["language"]
		print(favorite)
```

- Count the favorite languages from the .csv file

```
import csv

with open("favorites.csv", "r") as file:
	reader = csv.DictReader(file)
	scratch, c, python = 0, 0, 0
	for row in reader:
		favorite = row["language"]
		if favorite == "Scratch":
			scratch += 1
		elif favorite == "C":
			c += 1
		elif favorite == "Python":
			python += 1

print(f"Scratch: {scratch}")
print(f"C: {c}")
print(f"Python: {python}")
```

- Instead of using individual variables you can use a dictionary containing the keys of each language and incrementing from there. If the key already exists than increment, if not initialize it with 1. This way the program can scale as more languages are added to favorites.csv. **Sorted** will automatically sort by alphabetical order, can take arguments such as `reverse =True` to change to reverse alphabetical order.

```
import csv

with open("favorites.csv", "r") as file:
	reader = csv.DictReader(file)
	counts = {}
	for row in reader:
		favorite = row["language"]
		if favorite in counts:
			counts[favorite] += 1
		else:
			counts[favorite] = 1

# Define func that returns the counts value
def get_valule(language):
	return counts[language]

# Adding the func to sorted allows you to sort by top values
for favorite in sorted(counts, key=get_value):
	print(f"{favorite}: {counts[favorite]}")
```

- Using a **lambda** function (anonymous function) you can achieve the same as above, but without having to create function you will only use once. Using the lambda function you pass it the argument that you want the anonymous function to use, followed by a colon (":") and what you want the return value to be (`lambda {argument}: {return value}`)

```
import csv

with open("favorites.csv", "r") as file:
	reader = csv.DictReader(file)
	counts = {}
	for row in reader:
		favorite = row["language"]
		if favorite in counts:
			counts[favorite] += 1
		else:
			counts[favorite] = 1

for favorite in sorted(counts, key=lambda language: counts[language]):
	print(f"{favorite}: {counts[favorite]}")
```

- Same program using user input to print out counts of their favorite language

```
import csv

with open("favorites.csv", "r") as file:
	reader = csv.DictReader(file)
	counts = {}
	for row in reader:
		favorite = row["language"]
		if favorite in counts:
			counts[favorite] += 1
		else:
			counts[favorite] = 1

favorite = input("Favorite: ")
if favorite in counts:
	print(f"{favorite}: {counts[favorite]}")
```

## Relational Databases
- **Relational Database** - stores data in rows and columns still but in tables. Allow you to have data items with pre-defined relationships between them
  - These db's support CRUD:
    - **C**reate data
    - **R**eading data
    - **U**pdating data
    - **D**eleting data
  - In SQL these commands are:
    - CREATE, INSERT
    - SELECT
    - UPDATE
    - DELETE, DROP
- Creating a table in SQL
```
CREATE TABLE table (column type, ...);
```
- Create a database file in command line. This opens the sqlite program in terminal. Here you can set the mode to csv and import a separate csv file into a new table that you name. Using the `.schema` command you will see the actual SQL command to create the table.
```
$ sqlite3 favorites.db
sqlite> .mode csv
sqlite> .import favorites.csv favorites
sqlite> .schema
CREATE TABLE IF NOT EXISTS "favorites"("Timestamp" TEXT, "language" TEXT, "problem" TEXT);
```
- Exiting out of sqlite3 and rerunning it you will exit out of csv mode so you can run the following commands to output the data in an easier to read format
- Use the below command to get all of the data from the db
```
sqlite> SELECT * FROM favorites;
```
- To select just the languages:
```
sqlite> SELECT language FROM favorites;
```
- SQL functions:
  - AVG
  - COUNT
  - DISTINCT
  - LOWER
  - MAX
  - MIN
  - UPPER
- To get how many rows in db
```
sqlite> SELECT COUNT(*) FROM favorites;
```
- To get the distinct languages
```
sqlite> SELECT DISTINCT(language) FROM favorites;
```
- You can alias the output column name using `AS` so it is something more distinct than just the SQL query
```
sqlite> SELECT COUNT(DISTINCT(language)) AS num_of_languages FROM favorites;
```
- SQL keywords to filter selections even more:
  - WHERE
  - LIKE
  - ORDER BY
  - LIMIT
  - GROUP BY
- Select specifically how many people like a certain language
```
sqlite> SELECT COUNT(*) FROM favorites WHERE language = 'C';
```
- Select how many people liked a certain language and project
```
sqlite> SELECT COUNT(*) FROM favorites WHERE language = 'C' AND problem = 'Mario';
```
- Only show different languages but show the amount of people who liked the specific languages and order by ascending or descending (i.e. what we did above in python)
```
sqlite> SELECT language, COUNT(*) FROM favorites GROUP BY language ORDER BY COUNT(*) DESC;
```
- You can limit the answer to 1 to get the most popular language
```
sqlite> SELECT language, COUNT(*) FROM favorites GROUP BY language ORDER BY COUNT(*) DESC LIMIT 1;
```
- To add new data in the table
```
sqlite> INSERT INTO favorites (language, problem) VALUES ('SQL', 'Fiftyville')
```
- To change data for all rows matching a condition
```
sqlite> UPDATE favorites SET language = 'C++' WHERE language = 'C'
```
- To remove data matching a condition
```
sqlite> DELETE FROM favorites WHERE problem = 'Tideman';
```

## Schemas
- **Schema** - a collection of database objects associated with a database
- Plan of how the data will be displayed in the db

## Types
- Data types in SQLite:
  - **BLOB** - binary large object
  - **INTEGER** - integer
  - **NUMERIC** - catch all for numbers formatted specially, like date/time
  - **REAL** - float, decimal point
  - **TEXT** - strings

## Constraints
- Constraints on the data types:
  - **NOT NULL** - have a column that cannot be null
  - **UNIQUE** - data can only be one of a kind

## Primary Key, Foreign Key, Relationships
- **PRIMARY KEY** - database will use this column as a unique identifier, i.e. id's
- **FOREIGN KEY** - in SQL, this is a key that references an outside **PRIMARY KEY** in another table, i.e. a genre's "show_id" is just a reference to the "id" column in the show table
- Using the combination of **PRIMARY KEYS** and **FOREIGN KEYS** allow you to build relationships between separate tables and link them together
- Nesting queries allows you to get all the show titles that are comedies
```
sqlite> SELECT title FROM shows WHERE id IN (SELECT show_id FROM generes WHERE genre = 'Comedy');
```
- To get all of the shows a specific actor has been in
```
//First get actor id
sqlite> SELECT * FROM people WHERE name = 'Steve Carell';
//Get all the shows from stars table with his id
sqlite> SELECT * FROM stars WHERE person_id = 136797;
```

```
//Get the show titles of all the shows he is in by combining the above queries
sqlite> SELECT title FROM shows WHERE id IN (SELECT show_id FROM stars WHERE person_id = (SELECT id FROM people WHERE name = 'Steve Carrell')
```
- query = <font style="color:red">SELECT title FROM shows WHERE id IN</font><font style="color:green">(SELECT show_id FROM stars WHERE person_id = </font><font style="color:orange">(SELECT id FROM people WHERE name = 'Steve Carrell')</font><font style="color:green">)</font>
- You can accomplish the same as above using explicit JOIN
```
sqlite> SELECT title FROM people
   ...> JOIN stars ON people.id = stars.person_id
   ...> JOIN shows ON stars.show_id = shows.id
   ...> WHERE name = 'Steve Carell';
```
- OR using an implicit JOIN
```
sqlite> SELECT title FROM people, stars, shows
   ...> WHERE people.id = stars.person_id
   ...> AND stars.show_id = shows.id
   ...> AND name = 'Steve Carell';
```
- To **JOIN** separate tables into one on a related key. In this case a show with all of its genres. Join the tables where the show id equal the genre show_id 
```
sqlite> SELECT * FROM shows JOIN genres ON shows.id = genres.show_id
```
- You can use ```%``` as a wild card in quotes if you don't know exactly what you are looking for
```
sqlie> SELECT * FROM people WHERE name LIKE 'Steve C%';
```

## Indexes
- **Indexing** allows you search columns faster. ```CREATE INDEX name ON table (column, ...)```
- To create an index on show titles to make searching them faster. This creates a **B-tree** (not a binary tree)
```
sqlite> CREATE INDEX title_index ON shows (title);
```
- Do not want to create indexes on every column in every table because it will take a lot of storage to store each B-tree. You only want to index certain columns/tables.

## Python & SQL
- Get how many people liked a certain problem. The  ```
execute()``` function returns a list of dictionaries when using SELECT. Also in SQL ```?``` are used as placeholders
```
from cs50 import SQL

db = SQL("sqlite:///favorites.db")

favorite = input("Favorite: ")
rows = db.execute("SELECT COUNT(*) AS n FROM favorites WHERE problem = ?", favorite)

row = rows[0]
print(row["n"])
```

## Race Conditions
- **Race conditions** - when you have multiple independent lines of code that get interspersed when multiple people execute those lines at the same time. I.e. you make a decision on the state of the world while the state of the world was in the middle of being updated
```
rows = db.execute("SELECT likes FROM posts WHERE id = ?", id)
likes = rows[0]["likes"]
db.execute("UPDATE posts SET likes = ? WHERE id = ?", likes + 1, id)
```
- In SQL you can use statements that make your queries **Atomic** meaning that the queries are either execute together or not at all
```
db.execute("BEGIN TRANSACTION")
rows = db.execute("SELECT likes FROM posts WHERE id = ?", id)
likes = rows[0]["likes"]
db.execute("UPDATE posts SET likes = ? WHERE id = ?", likes + 1, id)
db.execute("COMMIT")
```

## SQL Injection Attacks
- When a user injects a SQL query in a form where they use SQL under the hood to check the info passed to the form
- In SQL ```--``` means everything to the right of the query is ignored
- ```test@harvard.edu'--``` using this combo if the code looks like:
```
rows = db.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")

if rows:
	...
```
- It will look like this in code when the query executes:
```
rows = db.execute(f"SELECT * FROM users WHERE username = 'test@harvard.edu'--' AND password = '{password}'")

if rows:
	...
```
- Thus the password is never even checked because of the ```--```
- DO NOT USE f-strings or % symbols. Use ? because it automatically escapes any dangerous characters in the argument, i.e. sanitizes the data