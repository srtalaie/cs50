
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
