
## Compilation & Interpretation
- Python does not require compilation, where you convert the language to 0's and 1's
- Python uses an interpreter, which is a program installed on the computer and interprets the code for you

## Import
- Use ```import``` to bring in other libraries
```
//Imports the cs50 library
import cs50

//Imports just the get_string function from cs50
from cs50 import get_string
```

## Dynamically Typed
- Do not need to declare the variable type, python infers the variable type via context

## Types
- Data types:
	- **bool** - True/False
	- **float** - decimal
	- **int** - integer
	- **str** - string, text
	- **range** - immutable sequence of numbers
	- **list** - an array
	- **tuple** - an immutable list
	- **dict** - key value pairs
	- **set** - collection of values with no duplicates

## Speller (python)
```
words = set()

def check(word):
	if word.lower() in words:
		return True
	else:
		return False

def load(dictionary):
	file = open(dictionary, "r")
	for line in file:
		# Removes the trailing '\n'
		word = line.rstrip()
		words.add(word)
	close(file)
	return True
	
def size():
	return len(words)
	
def unload():
	# You do not need to manage memory in python
	return True
```

## Conditionals
- **If statement**
```
if x < y:
	print("x is less than y")
```
- **If Else statement**
```
if x < y:
	print("x is less than y")
else:
	print("x is greater than y")
```
- **Else If statement**
```
if x < y:
	print("x is less than y")
elif x > y:
	print("x is greater than y")
else:
	print("x is equal to y")
```

## Variables
- Only need to name the variable and include the assignment operator. No need for type
```
counter = 0

# Increment it
counter = counter + 1
counter += 1
```

## Loops
- **While Loop**
```
i = 0
while i < 3:
	print("meow")
	i+=1

```
- **For Loop**
	- You use a list of numbers
```
for i in [0, 1, 2]:
	print(hello, world")

# Better implementation
for i in range(3):
	print("hello, world")
```
- **Infinite Loop**
```
while True:
	print("meow")
```

## Calculator (python)
```
from cs50 import get_int

x = get_int("x: ")
y = get_int("y: ")

print(x + y)

#Output
$ python calculator.py
$ x: 1
$ y: 2
3

# Without cs50 lib
x = input("x: ")
y = input("y: ")

print(x + y)

#Output
$ python calculator.py
$ x: 1
$ y: 2
12
```
- Without ```get_int``` from the cs50 library python treats the user input as strings, so the output is a concatenation of strings. In order to fix this you need to type cast the user's input.
```
x = int(input("x: "))
y = int(input("y: "))

print(x + y)

#Output
$ python calculator.py
$ x: 1
$ y: 2
3
```

```
# With division
x = int(input("x: "))
y = int(input("y: "))
z = x / y

print(z)

#Output
$ python calculator.py
$ x: 1
$ y: 3
0.33333333333333
```
- In python the int is automatically converted to a float. Using fstring (format string) you can fine tune how many digits you want to see:
```
# With division
x = int(input("x: "))
y = int(input("y: "))
z = x / y

print(f"{z:.50f}")

#Output
$ python calculator.py
$ x: 1
$ y: 3
0.33333333333333435568769
```
- Python still has **floating-point imprecision**
- Python does not have **integer overflow** though so you can count as high as you want

## Compare (python)
```
from cs50 import get_int

x = get_int("x: ")
y = get_int("y: ")

if x < y:
	print("x is less than y")
elif x > y:
	print("x is greater than y")
else:
	print("x is equal to y")
```

## Object Oriented Programing (OOP)
- Certain types of values have properties and functions built into them as well
	- **str** has **.lower()** which converts the string to all lowercase

## Meow (python)
```
def main():
	meow(3)

def meow(n):
	for i in range(n):
		print("meow")

main()
```
- Still correct procedure to include a main function in python, allows you to modularize your code in functions. To do so you need to call main at the bottom of your function.

## Mario (python)
```
from cs50 import get_int

# Get user input and check it
while True:
	n = get_int("Height: ")
	if n > 0:
		break

for i in range(n):
	print("#")
```

```
from cs50 import get_int

def main():
	height = get_height()
	for i in range(height):
		print("#")


def get_height():
	while True:
		n = get_int("Height: ")
		if n > 0:
			break
	return n


main()
```
- Declaring n in the while loop, you are still able to use the variable outside of the while loop, hence returning n outside of the while loop. Could also be written like:
```
def get_height():
	while True:
		n = get_int("Height: ")
		if n > 0:
			return n
```
- Without the cs50 library use **Try/Except** to validate user input
```
def main():
	height = get_height()
	for i in range(height):
		print("#")


def get_height():
	while True:
		try: 
			n = int(input("Height: "))
			if n > 0:
				return n
		except ValueError:
			print("Not an integer")


main()
```
- To print all on the same line you can add arguments that will override the default behavior. Here you override the end line to be empty ("") rather than the default of "\\n"
```
for i in range(4):
	print("?", end="")
print()

# Output
????
```
- An easier way to implement this is:
```
print("?" * 4)

# Output
????
```
- Print 2D blocks
```
for i in range(3):
	for j in range(3):
		print("#", end="")
	print()

# Output
###
###
###

# Or
for i in range(3):
	print("#"" * 3)
```

## Scores (python)
```
scores = [72, 73, 33]

average = sum(scores) / len(scores)

print(f"Avg: {average}")
```

```
from cs50 import get_int

//Get scores from user input
scores = []

for i in range(3):
	score = get_int("Score: ")
	scores.append(score)

average = sum(scores) / len(scores)
print(f"Average: {average}")
```

## Uppercase (python)
```
before = input("Before: ")
print("After: ", end="")
for c in before
	print(c.upper(), end="")
print()


//Output
Before: david
After: DAVID
```

```
before = input("Before: ")
after = before.upper()
print(f"After: {after}")


//Output
Before: david
After: DAVID
```

## Greet (python)
```
from sys import argv

if len(argv) == 2:
	print(f"hello, {argv[1]}")
else:
	print("hello, world")

//Console
$ python greet.py
hello, world
$ python greet.py David
hello, David
```

## Exit Status
```
import sys

if len(sys.argv) !=2:
	print("Missing command-line argument")
	sys.exit(1)
else
	print(f"hello, {sys.argv[1]}")
sys.exit(0)


//Console
$ python exit.py
Missing command-line argument
$ echo $?
1
$ python exit.py David
hello, David
$ echo $?
0
```

## Search (python)
```
import sys

names = ["Bill", "Charlie", "Ginny", "Fred", "George", "Percy", "Ron"]

name = input("Name: ")

for n in names:
	if name == n:
		print("Found")
		sys.exit(0)
print("Not Found")
sys.exit(1)

//Console
$ python names.py
Name: Ron
Found
$ python names.py
Name: Hermione
Not Found
```

```
import sys

names = ["Bill", "Charlie", "Ginny", "Fred", "George", "Percy", "Ron"]

name = input("Name: ")

for name in names:
	print("Found")
	sys.exit(0)
print("Not Found")
sys.exit(1)

//Console
$ python names.py
Name: Ron
Found
$ python names.py
Name: Hermione
Not Found
```

## Phonebook (python)
```
//Create a dictionary for people
people = {
	"Carter": "+1-617-495-1000",
	"David": "+1-949-468-2750"
}

name = input("Name: ")

if name in people:
	number = people[name]
	print(f"Number: {number}")



//Console
$ python phonebook.py
Name: Carter
Number: +1-617-495-1000
```

## Compare String (python)
```
input("s: ")
input("t: ")

if s == t:
	print("Same")
else:
	print("Different")


//Console
$ python compare.py
s: cat
t: cat
Same
$ python compare.py
s: cat
t: dog
Different
```
- 2 same strings in C were different because they were in different locations of memory. In python this taken care of behind the scenes so the strings are compared character by character

## Swap (python)
```
x = 1
y = 2

print(f"x is {x}, y is {y}")
x, y = y, x
print(f"x is {x}, y is {y}")

//Console
$ python swap.py
x is 1, y is 2
x is 2, y is 1
```

## CSV (python)
phonebook.csv
```
name,number
```

phonebook.py
```
import csv

//Open file in append mode, and close after operations
with open("phonebook.csv", "a") as file:

	name = input("Name: ")
	number = input("Number: ")
	
	//Will format for writing to csv file
	writer = csv.DictWriter(file, fieldnames=["name", "number"])
	writer.writerow(["name": name, "number": number])


//Console
$ python phonebook.py
Name: David
Number: +1-949-468-2750

//phonebook.csv
name,number
David,+1-949-468-2750
```

## Speech (python)
```
import pyttsx3

engine = pyttsx3.init()
name = input("Name: ")
engine.say(f"hello, {name}")
engine.runAndWait()
```

## QR Code (python)
```
import os
import qrcode

image = qrcode.make("https://youtu.be/xvFZjo5PgG0")

image.save("qr.png", "PNG")

os.system("open qr.png")
```