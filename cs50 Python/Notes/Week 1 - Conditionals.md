## Conditionals
- Allow you to ask questions and answer those questions in order to decide which lines of code you would like to execute
	-  Comparison Symbols:
		- '>' - greater than
		- '>=' - greater than or equal to
		- '<' - less than
		- '<=' - less than or equal to
		- '=/=' - equal to
		- '!=' - not equal to
- Expressions called `booleans`
## if statement
- If something is true, execute the line of code
```
x = int(input("What's x? ))
y = int(input("What's y? ))

if x < y:
	print("x is less than y")
if x > y:
	print("x is greater than y")
if x == y:
	print("x is equal to y")
```
Output:
```
What's x? 5
What's y? 6
$ x is less than y
```
## elif statements
- Way to group multiple if statements
```
x = int(input("What's x? ))
y = int(input("What's y? ))

if x < y:
	print("x is less than y")
elif x > y:
	print("x is greater than y")
elif x == y:
	print("x is equal to y")
```
Output:
```
What's x? 4
What's y? 1
$ x is greater than y
```
## else statement
- If something is not true execute the following line, else execute the line after the else statement
```
x = int(input("What's x? ))
y = int(input("What's y? ))

if x < y:
	print("x is less than y")
elif x > y:
	print("x is greater than y")
else:
	print("x is equal to y")
```
Output:
```
What's x? 4
What's y? 4
$ x equal to y
```
## or
```
x = int(input("What's x? ))
y = int(input("What's y? ))

if x < y or x > y:
	print("x not equal to y")
else:
	print("x is equal to y")
```
## not equal
```
x = int(input("What's x? ))
y = int(input("What's y? ))

if x != y:
	print("x not equal to y")
else:
	print("x is equal to y")
```
## and
```
score = int(input("Score: " ))

if score >= 90 and score <= 100:
	print("Grade: A")
elif score >= 80 and score < 90:
	print("Grade: B")
elif score >= 70 and score < 80:
	print("Grade: C")
elif score >= 60 and score < 70:
	print("Grade: D")
else:
	print("Grade: F")
```
## Chaining Comparisons and Operators
```
score = int(input("Score: " ))

if 90 < socre <= 100:
	print("Grade: A")
elif 80 <= socre < 90:
	print("Grade: B")
elif 70 <= socre < 80:
	print("Grade: C")
elif 60 <= socre < 70:
	print("Grade: D")
else:
	print("Grade: F")
```
Cleaner way:
```
score = int(input("Score: " ))

if score >= 90:
	print("Grade: A")
elif score >= 80:
	print("Grade: B")
elif score >= 70:
	print("Grade: C")
elif score >= 60:
	print("Grade: D")
else:
	print("Grade: F")
```
## Modulo (%)
- Returns the remainder of division
```
x = int(input("Number: "))

if x % 2 == 0:
	print("Even")
else:
	print("Odd")
```
## Boolean
- Represented as either `True` or `False`
```
def main():
	x = int(input("Number: "))
	
	if is_even(x):
		print("Even")
	else:
		print("Odd")

def is_even(n):
	if n % 2 == 0:
		return True
	else:
		return False

main()
```
## Pythonic Expressions
- The way you do things in python. Best practices using features only python has
```
def is_even(n):
	return True if n % 2 == 0 else False
```
Even better because the expression already returns a boolean
```
def is_even(n):
	return n % 2 == 0
```
## Match
- Switch statement
```
name = input("What's your name? ")

if name == "Harry":
	print("Gryffindor")
elif name == "Hermione":
	print("Gryffindor")
elif name == "Ron":
	print("Gryffindor")
elif name == "Draco":
	print("Slytherin")
else:
	print("Who?")
```
A little better:
```
if name == "Harry" or name == "Hermione" or name == "Ron":
	print("Gryffindor")
elif name == "Draco":
	print("Slytherin")
else:
	print("Who?")
```
Better with `match`
```
name = input("What's your name? ")

match name:
	case "Harry":
		print("Gryffindor")
	case "Hermione":
		print("Gryffindor")
	case "Ron":
		print("Gryffindor")
	case "Draco":
		print("Slytherin")
	case _:
		print("Who?")
```

`case _:` - handles any other case not handled above

```
name = input("What's your name? ")

match name:
	case "Harry" | "Hermione" | "Ron":
		print("Gryffindor")
	case "Draco":
		print("Slytherin")
	case _:
		print("Who?")
```

`|` - denotes `or` in the match statement