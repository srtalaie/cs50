## Loops
- Block of code that does something again and again cyclically 
## While Loop
- `While` is a construct that allows the user to ask a question again and again in the form of a boolean.
```
i = 3

while i != 0:
	print("meow")
	i = i - 1
```

```
i = 1

while i <= 3:
	print("meow")
	i = i + 1
```

```
# Most Pythonic
i = 0

while i < 0:
	print("meow")
	i += 1
```
## For Loop
- `For` loop especially good for working with `lists`
	- list - type of data that contains multiple values all under the same variable
```
for i in [0, 1, 2]:
	print("meow")
```
- Instead of hardcoding the list use `range` which will take an argument of how many times you want the loop to run starting from 0 up to but NOT including the number you pass it
- You also do not need to pass it an iterator if you are not going to use it
```
for _ in range(3):
	print("meow")
```

```
# Most Pythonic, less readable
print("meow\n" * 3, end="")

$ python cat.py
meow
meow
meow
```
## Validation Input
- You can ask user how many times you want a loop to run
- When you want to get user input that matches an expectation you have you induce an infinite loop and asking for your input in the loop as the break
```
# Ensure user provides a positive integer
while True:
	n= int(input("What's n? "))
	if n < 0:
		continue
	else:
		break
```
- `continue` used to continue asking the loop, and the `break` will end the most recently begun loop
```
# More efficient way
while True:
	n = int(input("What's n? "))
	if n > 0:
		break
for _ in range(n):
	print("meow")
```

```
def main():
	number = get_number()
	meow(number)

def meow(n):
	for _ in range(n):
		print("meow")

def get_number():
	while True:
		n = int(input("What's n? "))
		if n > 0:
			return n
		
main()
```
- Instead of using `break` to end loop, `return` will break the loop and return the needed value from the function
## Iteration with Lists
- Lists start at 0 and you can use `[]` to access the index of the user
```
students = ["Harry", "Hermione", "Ron"]

for student in students:
	print(students[student])
```
## Len
- If you want to use integers to control the loop instead you can use `len` which returns the length of a list
```
students = ["Harry", "Hermione", "Ron"]

for i in range(len(students)):
	print(i + 1, students[i])
```
## Dictionaries
- dict - are data structures that allow you to associate one value with another. Represented as `key value` pairs
- Dictionaries allow you to use words as your indicies
```
students = {
	"Hermione": "Gryffindor", 
	"Harry": "Gryffindor", 
	"Ron": "Gryffindor", 
	"Draco": "Slytherin"
}

print(students["Hermione"])

# Prints
Gryffindor

for student in students:
	print(student, students[student], sep=", ")

# Prints
Hermione, Gryffindor 
Harry, Gryffindor 
Ron, Gryffindor
Draco, Slytherin
```
## List of Dictionaries
- `None` keyword that represents the absence of a value
```
students = [
	{
		"name": "Hermione", 
		"house": "Gryffindor", 
		"patronus": "Otter"
	},
	{
		"name": "Harry", 
		"house": "Gryffindor", 
		"patronus": "Stag"
	},
	{
		"name": "Ron", 
		"house": "Gryffindor", 
		"patronus": "Jack Russell Terrier"
	},
	{
		"name": "Draco", 
		"house": "Slytherin", 
		"patronus": None
	}
]

for student in students:
	print(student["name"], student["house"], student["patronus"], sep=", ")

# Prints:
Hermione, Gryffindor, Otter 
Harry, Gryffindor, Stag
Ron, Gryffindor, Jack Russell Terrier
Draco, Slytherin, None
```
## Nested Loops
```
def main():
	print_square

def print_square(size):

	# For each row in square
	for i in range(size):
	
		# For each brick in row
		for j in range(size):
		
			# Print brick
			print("#", end="")
			
		print()

main()
```

```
def main():
	print_square

def print_square(size):
	for i in range(size):
		print("#" * size)

main()
```
Using abstraction to take the row printing out of the square and using it in its own function
```
def main():
	print_square

def print_square(size):
	for i in range(size):
		print_row(size)

def print_row(width):
	print("#" * width)

main()
```

