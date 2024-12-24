## list
- Able to store multiple pieces of values, but only in memory so once the program terminates it is gine
## open
- Allows you to open a file programmatically, similar to as if you would open a file yourself on your desktop
```
name = input("What's your name? ")

# Save value of name to a file, each time you run the program though you overwrite the file
file = open("names.txt", "w")
file.write(name)
file.close()
```

```
name = input("What's your name? ")

# 'a' allows you to append to the file each time on a new line
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
```
## with
- Allows you to specify in this context you want the program to automatically open and then close the file
```
name = input("What's your name? ")

with open("names.txt", "a") as file:
	file.write(f"{name}\n")
```
- How to read the file: 
```
with open("names.txt", "r") as file:
	for line in file:
		print(line.rstrip())
```
## sorted
```
names = []

# Store names from names.txt into list variable
with open("names.txt") as file:
	for line in file:
		names.append(line.rstrip())

# Print all names in order
for name in sorted(names):
	print(f"hello, {name}")
```
## Comma-Separated Values
- Allows you to store multiple types of data, sorted via commas. The different values act as columns.
students.csv
```
Hermione,Gryffindor
Harry,Gryffindor
Ron,Gryffindor
Draco,Slytherin
```
students.py
```
with open("students.csv") as file:
	for line in file:
		row = line.rstrip().split(",")
		print(f"{row[0]} is in {row[1]}")
```
- In order to sort in alphabetic order:
students.py
```
students = []

with open("students.csv") as file:
	for line in file:
		name, house = line.rstrip().split(",")
		students.append(f"{name} is in {house}")

for student in sorted(students):
	print(student)
```
- Better technique to sort by actual students name and not just the entire sentence beginning with the students name. 
```
students = []

with open("students.csv") as file:
	for line in file:
		name, house = line.rstrip().split(",")
		student = {}
		student["name"] = name
		student["house"] = house
		students.append(student)

for student in students:
	print(f"{student['name']} is in {student['house']}")
```
cleaner version and with sorting
```
students = []

with open("students.csv") as file:
	for line in file:
		name, house = line.rstrip().split(",")
		student = {"name": name, "house": house}

def get_name(student):
	return student["name"]
	
for student in sorted(students, key=get_name):
	print(f"{student['name']} is in {student['house']}")
```
## Lambda Functions
- Allows you to write a function as a variable in line. An anonymous function
```
students = []

with open("students.csv") as file:
	for line in file:
		name, house = line.rstrip().split(",")
		student = {"name": name, "house": house}

	
for student in sorted(students, key=lambda student: student["name"]):
	print(f"{student['name']} is in {student['house']}")
```
- `lambda student: student["name"]` equivalent to defining your own function above. You do not need to explicitly return a value for lambda functions
## csv Library
students.csv
```
Harry, Number Four, Privet Dr.
Ron, The Burrow
Draco, Malfoy Manor
```
students.py
```
students = []

with open("students.csv") as file:
	for line in file:
		name, home = line.rstrip().split(",")
		student = {"name": name, "home": home}

	
for student in sorted(students, key=lambda student: student["name"]):
	print(f"{student['name']} is from {student['home']}")
```
- Above you get a ValueError because the first line in students.csv has a comma in the address. The program does not differentiate between grammatic commas or commas separating values
- The `csv` library for python alleviates most of the pain points that come with reading/writing to csv files
## csv.reader
students.csv
```
Harry,"Number Four, Privet Dr."
Ron, The Burrow
Draco, Malfoy Manor
```
students.py
```
import csv

students = []

with open("students.csv") as file:
	reader = csv.reader(file)
	for name, home in reader:
		students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
	print(f"{student['name']} is from {student['home']}")
```
## csv.DictReader
- csv's usually have the first row delineate the names of the columns
students.csv
```
name,home
Harry,"Number Four, Privet Dr."
Ron, The Burrow
Draco, Malfoy Manor
```
- Now instead of using `csv.reader` you use `csv.DictReader` which returns a dictionary
students.py
```
import csv

students = []

with open("students.csv") as file:
	reader = csv.DictReader(file)
	for row in reader:
		students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
	print(f"{student['name']} is from {student['home']}")
```
## csv.Writer
students.py
```
import csv

name = input("What's your name? " )
home = input("Where's your home? ")

with open("students.csv", "a") as file:
	writer = csv.writer(file)
	writer.writerow([name, home])
```

```
$ python students.py
What's your name? Harry
Where's your home? Number Four, Privet Dr.
```

students.csv
```
name,home
Harry,"Number Four, Privet Dr."
```
## csv.DictWriter
students.py
```
import csv

name = input("What's your name? " )
home = input("Where's your home? ")

with open("students.csv", "a") as file:
	writer = csv.DictWriter(file, fieldnames=["name", "home"])
	writer.writerow({"name": name, "home": home})
```
## Images, PIL Library
- PIL - `pillow`, allows you to navigate and preform operations on image files
- Create an animated gif from two or more image files provided as args:
costumes.py
```
import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
	image = Image.open(arg)
	images.append(image)

images[0].save(
	"costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
```
